#!/usr/bin/env python3
"""
Gmail Thread Exporter

Fetches a Gmail thread via API and outputs full metadata for all messages.
Supports JSON output or formatted Obsidian markdown.

Usage:
    ./gmail-thread.py INPUT [--format json|obsidian] [--copy]

Input can be:
    - Thread ID: 18d5a2b3c4e5f6g7
    - Gmail URL: https://mail.google.com/mail/u/0/#inbox/...
    - Popup URL: https://mail.google.com/mail/u/2/popout?...
    - Message-ID: <CAJ-oin...@mail.gmail.com> (from "Show Original")

Examples:
    ./gmail-thread.py 18d5a2b3c4e5f6g7
    ./gmail-thread.py 18d5a2b3c4e5f6g7 --format obsidian --copy
    ./gmail-thread.py "https://mail.google.com/mail/u/0/#inbox/18d5a2b3c4e5f6g7"
    ./gmail-thread.py "<CAJ-oinXYZ123@mail.gmail.com>"
"""

import argparse
import base64
import json
import os
import re
import subprocess
import sys
import warnings
from datetime import datetime
from email.utils import parseaddr, parsedate_to_datetime
from pathlib import Path
from typing import Optional
from urllib.parse import unquote, urlparse, parse_qs

# Suppress noisy warnings from urllib3 and google-api-core
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", message=".*NotOpenSSLWarning.*")
warnings.filterwarnings("ignore", message=".*urllib3.*")

# Google API imports - will fail gracefully if not installed
try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    GOOGLE_LIBS_AVAILABLE = True
except ImportError:
    GOOGLE_LIBS_AVAILABLE = False

# Configuration
CONFIG_DIR = Path.home() / ".config" / "gmail-thread"
CREDENTIALS_FILE = CONFIG_DIR / "credentials.json"  # OAuth client credentials
TOKEN_FILE = CONFIG_DIR / "token.json"  # Stored access/refresh token
REFERENCE_FILE = Path(__file__).parent.parent / ".claude" / "commands" / "email-reference.md"

# Gmail API scope - read-only access
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def is_message_id(input_str: str) -> bool:
    """Check if input looks like an RFC822 Message-ID."""
    # Message-IDs are typically in angle brackets: <...@...>
    # Or without brackets: ...@mail.gmail.com
    return "@" in input_str and ("mail.gmail.com" in input_str or input_str.startswith("<"))


def search_by_message_id(service, message_id: str) -> Optional[str]:
    """
    Search for a thread by RFC822 Message-ID and return its thread ID.

    See: https://support.cloudhq.net/find-email-messages-in-gmail-with-rfc822msgid/
    """
    # Clean up message ID - remove angle brackets if present
    clean_id = message_id.strip().strip("<>")

    query = f"rfc822msgid:{clean_id}"
    print(f"Searching for message: {query}", file=sys.stderr)

    try:
        results = service.users().messages().list(
            userId="me",
            q=query,
            maxResults=1
        ).execute()

        messages = results.get("messages", [])
        if messages:
            # Return the thread ID from the first matching message
            return messages[0].get("threadId")
        else:
            print(f"No message found with Message-ID: {clean_id}", file=sys.stderr)
            return None
    except Exception as e:
        print(f"Error searching for message: {e}", file=sys.stderr)
        return None


def extract_thread_id(input_str: str) -> str:
    """
    Extract thread ID from various Gmail URL formats or return as-is if already an ID.

    Supported formats:
    - Raw thread ID: 18d5a2b3c4e5f6g7
    - Standard URL: https://mail.google.com/mail/u/0/#inbox/18d5a2b3c4e5f6g7
    - Popup URL: https://mail.google.com/mail/u/2/popout?...&th=%23thread-f%3A1853045190304467755%7C...
    - Search URL: https://mail.google.com/mail/u/0/#search/.../.../18d5a2b3c4e5f6g7

    Note: For Message-IDs (from Show Original), use search_by_message_id() instead.
    """
    input_str = input_str.strip()

    # If it doesn't look like a URL, assume it's already a thread ID
    if not input_str.startswith("http"):
        return input_str

    # URL decode first
    decoded = unquote(input_str)

    # Try popup URL format: th=#thread-f:THREAD_ID|msg-a:...
    th_match = re.search(r'thread-f[:\s]*(\d+)', decoded)
    if th_match:
        return th_match.group(1)

    # Try standard URL format: #inbox/THREAD_ID or #sent/THREAD_ID or #label/name/THREAD_ID
    hash_match = re.search(r'#(?:inbox|sent|drafts|starred|snoozed|imp|trash|spam|all|label/[^/]+)/([a-zA-Z0-9]+)(?:\?|$)', decoded)
    if hash_match:
        return hash_match.group(1)

    # Try search URL format: #search/.../THREAD_ID
    search_match = re.search(r'#search/[^/]+/([a-zA-Z0-9]+)(?:\?|$)', decoded)
    if search_match:
        return search_match.group(1)

    # Last resort: find any long alphanumeric string that looks like a thread ID
    # Gmail thread IDs are typically 16+ hex characters or decimal digits
    id_match = re.search(r'[/=]([a-fA-F0-9]{16,}|\d{16,})(?:[&|?]|$)', decoded)
    if id_match:
        return id_match.group(1)

    # If nothing matches, return original (will fail at API call with clear error)
    return input_str


def check_dependencies():
    """Check if required Google libraries are installed."""
    if not GOOGLE_LIBS_AVAILABLE:
        print("Error: Required Google libraries not installed.")
        print("\nInstall with:")
        print("  pip install google-auth google-auth-oauthlib google-api-python-client")
        sys.exit(1)


def get_gmail_service():
    """Authenticate and return Gmail API service."""
    creds = None

    # Check for existing token
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    # If no valid credentials, run auth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDENTIALS_FILE.exists():
                print(f"Error: OAuth credentials not found at {CREDENTIALS_FILE}")
                print("\nTo set up authentication:")
                print("  1. Go to https://console.cloud.google.com/")
                print("  2. Create a project and enable Gmail API")
                print("  3. Create OAuth 2.0 credentials (Desktop app)")
                print("  4. Download JSON and save to:")
                print(f"     {CREDENTIALS_FILE}")
                print("  5. Run: ./setup-auth.py")
                sys.exit(1)

            flow = InstalledAppFlow.from_client_secrets_file(
                str(CREDENTIALS_FILE), SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save credentials for next run
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


def load_email_reference() -> dict:
    """Load email-reference.md and parse lookup tables."""
    reference = {
        "emails": {},      # email -> wiki-link
        "glossary": {},    # term -> wiki-link
        "accounts": [],    # list of user's gmail accounts
    }

    if not REFERENCE_FILE.exists():
        return reference

    content = REFERENCE_FILE.read_text()
    current_section = None

    for line in content.split("\n"):
        line = line.strip()

        # Detect section headers
        if "## Gmail Accounts" in line:
            current_section = "accounts"
        elif "## Email → Person Mapping" in line or "## Email -> Person Mapping" in line:
            current_section = "emails"
        elif "## Glossary" in line:
            current_section = "glossary"
        elif line.startswith("## "):
            current_section = None

        # Parse table rows
        if line.startswith("|") and not line.startswith("|-") and current_section:
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 2 and parts[0] and not parts[0].startswith("--"):
                # Skip header rows
                if parts[0].lower() in ["email", "term variations", "name variations"]:
                    continue

                if current_section == "emails":
                    email = parts[0].lower()
                    wikilink = parts[1]
                    reference["emails"][email] = wikilink
                elif current_section == "glossary":
                    terms = [t.strip() for t in parts[0].split(",")]
                    wikilink = parts[1]
                    for term in terms:
                        reference["glossary"][term.lower()] = wikilink
                elif current_section == "accounts":
                    if "@" in parts[0]:
                        reference["accounts"].append(parts[0].lower())

    return reference


def parse_email_address(raw: str) -> tuple[str, str]:
    """Parse 'Name <email>' format, return (name, email)."""
    name, email = parseaddr(raw)
    return name or email.split("@")[0], email.lower()


def get_header(headers: list, name: str) -> Optional[str]:
    """Get header value by name (case-insensitive)."""
    name_lower = name.lower()
    for header in headers:
        if header["name"].lower() == name_lower:
            return header["value"]
    return None


def parse_recipients(header_value: Optional[str]) -> list[dict]:
    """Parse To/CC header into list of {name, email}."""
    if not header_value:
        return []

    recipients = []
    # Handle comma-separated addresses
    # This is tricky because names can contain commas
    # Simple approach: split on >, then clean up
    parts = re.split(r">,\s*", header_value)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if not part.endswith(">"):
            part += ">"
        name, email = parse_email_address(part)
        if email:
            recipients.append({"name": name, "email": email})

    return recipients


def extract_attachments(payload: dict) -> list[dict]:
    """Recursively extract attachment metadata from message payload."""
    attachments = []

    def process_part(part: dict):
        filename = part.get("filename", "")
        if filename:
            body = part.get("body", {})
            attachments.append({
                "filename": filename,
                "mimeType": part.get("mimeType", ""),
                "size": body.get("size", 0),
                "attachmentId": body.get("attachmentId", ""),
            })

        # Process nested parts
        for subpart in part.get("parts", []):
            process_part(subpart)

    process_part(payload)
    return attachments


def format_size(size_bytes: int) -> str:
    """Format byte size as human-readable string."""
    if size_bytes < 1024:
        return f"{size_bytes}B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes // 1024}K"
    else:
        return f"{size_bytes // (1024 * 1024)}M"


def strip_quoted_text(body: str) -> str:
    """
    Remove quoted replies from email body.

    Strips:
    - Lines starting with > (quoted text)
    - "On [date] [person] wrote:" attribution lines
    - Signature blocks after "--"
    """
    if not body:
        return ""

    lines = body.split("\n")
    result_lines = []
    in_quote = False

    for line in lines:
        stripped = line.strip()

        # Skip empty lines at the start
        if not result_lines and not stripped:
            continue

        # Detect start of quoted section: "On ... wrote:"
        if re.match(r'^On .+wrote:$', stripped) or re.match(r'^On .+wrote:\s*$', stripped):
            in_quote = True
            continue

        # Skip quoted lines (starting with >)
        if stripped.startswith(">"):
            in_quote = True
            continue

        # Skip signature delimiter and everything after
        if stripped == "--":
            break

        # If we were in a quote and hit a non-quoted line, we might be out
        # But for safety, once we hit quoted content, stop
        if in_quote:
            continue

        result_lines.append(line)

    # Clean up trailing whitespace
    result = "\n".join(result_lines).strip()
    return result


def truncate_at_word(text: str, max_len: int = 80) -> str:
    """Truncate text at word boundary."""
    if len(text) <= max_len:
        return text

    # Find last space before max_len
    truncated = text[:max_len]
    last_space = truncated.rfind(" ")
    if last_space > max_len // 2:  # Only use if we keep at least half
        truncated = truncated[:last_space]

    return truncated.rstrip(".,;:") + "..."


def generate_focus(body: str, subject: str) -> str:
    """Generate a brief Focus summary from the email body."""
    # Strip quoted text first
    clean_body = strip_quoted_text(body)

    if not clean_body:
        return subject

    # Join lines into single string, collapse whitespace
    single_line = " ".join(clean_body.split())

    # Skip common salutations at the start
    single_line = re.sub(r'^(Hi|Hello|Hey|Dear|Good morning|Good afternoon|Good evening)[,\s]+\w+[,\s]*', '', single_line, flags=re.I)
    single_line = single_line.strip()

    if not single_line:
        return subject

    return truncate_at_word(single_line, 80)


def generate_thread_summary(messages: list[dict], reference: dict) -> str:
    """
    Generate a thread summary from the message list.

    Provides: who initiated, topic, participants, date range, attachments, outcome.
    """
    if not messages:
        return "(Empty thread)"

    # Get thread info
    first_msg = messages[0]
    last_msg = messages[-1]

    # Subject (remove Re: prefix for cleaner look)
    subject = first_msg["subject"]
    clean_subject = re.sub(r'^(Re:\s*|Fwd:\s*)+', '', subject, flags=re.I).strip()

    # Date range
    first_date = first_msg["datetime"].strftime("%b %d") if first_msg.get("datetime") else "?"
    last_date = last_msg["datetime"].strftime("%b %d, %Y") if last_msg.get("datetime") else "?"

    # Participants (unique, excluding self)
    participants = set()
    for msg in messages:
        sender_email = msg["from"]["email"]
        if not msg["from"].get("is_me"):
            sender_name = msg["from"]["name"]
            wikilink = email_to_wikilink(sender_email, sender_name, reference)
            if wikilink != "me":
                participants.add(wikilink)
        for recip in msg.get("to", []) + msg.get("cc", []):
            wikilink = email_to_wikilink(recip["email"], recip["name"], reference)
            if wikilink != "me":
                participants.add(wikilink)

    # Count attachments
    total_attachments = sum(len(msg.get("attachments", [])) for msg in messages)

    # Who started it
    initiator = email_to_wikilink(
        first_msg["from"]["email"],
        first_msg["from"]["name"],
        reference
    )

    # Final message summary
    final_focus = generate_focus(last_msg["body"], "")

    # Build summary
    parts = []

    # Opening: who started, topic
    if initiator == "me":
        parts.append(f"I initiated this thread about {clean_subject}.")
    else:
        parts.append(f"{initiator} initiated this thread about {clean_subject}.")

    # Participants
    other_participants = [p for p in participants if p != initiator]
    if other_participants:
        parts.append(f"Participants: {', '.join(sorted(other_participants))}.")

    # Message count and date range
    msg_count = len(messages)
    if msg_count > 1:
        parts.append(f"{msg_count} messages from {first_date} to {last_date}.")

    # Attachments
    if total_attachments > 0:
        parts.append(f"{total_attachments} attachment(s) shared.")

    # Final status (from last message) - truncate to keep summary readable
    if final_focus and final_focus != clean_subject:
        final_focus_short = truncate_at_word(final_focus, 60)
        last_sender = email_to_wikilink(
            last_msg["from"]["email"],
            last_msg["from"]["name"],
            reference
        )
        if last_sender == "me":
            parts.append(f"Final: \"{final_focus_short}\"")
        else:
            parts.append(f"Final ({last_sender}): \"{final_focus_short}\"")

    return " ".join(parts)


def parse_message(msg: dict, reference: dict) -> dict:
    """Parse a Gmail API message into structured data."""
    headers = msg.get("payload", {}).get("headers", [])

    # Parse date
    date_str = get_header(headers, "Date")
    try:
        dt = parsedate_to_datetime(date_str) if date_str else None
    except:
        dt = None

    # Parse sender
    from_raw = get_header(headers, "From") or ""
    from_name, from_email = parse_email_address(from_raw)

    # Parse recipients
    to_list = parse_recipients(get_header(headers, "To"))
    cc_list = parse_recipients(get_header(headers, "Cc"))
    bcc_list = parse_recipients(get_header(headers, "Bcc"))

    # Get subject
    subject = get_header(headers, "Subject") or "(no subject)"

    # Get message body (plain text preferred)
    body = extract_body(msg.get("payload", {}))

    # Get attachments
    attachments = extract_attachments(msg.get("payload", {}))

    # Determine if this is from the user
    is_from_me = from_email in reference.get("accounts", [])

    return {
        "id": msg.get("id"),
        "threadId": msg.get("threadId"),
        "date": dt.isoformat() if dt else None,
        "datetime": dt,
        "timestamp": int(msg.get("internalDate", 0)),
        "from": {
            "name": from_name,
            "email": from_email,
            "is_me": is_from_me,
        },
        "to": to_list,
        "cc": cc_list,
        "bcc": bcc_list,
        "subject": subject,
        "body": body,
        "attachments": attachments,
        "labels": msg.get("labelIds", []),
    }


def extract_body(payload: dict, prefer_plain: bool = True) -> str:
    """Extract message body from payload, preferring plain text."""

    def decode_body(data: str) -> str:
        """Decode base64url encoded body."""
        if not data:
            return ""
        # Add padding if needed
        padding = 4 - len(data) % 4
        if padding != 4:
            data += "=" * padding
        try:
            return base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")
        except:
            return ""

    def find_body(part: dict, mime_type: str) -> Optional[str]:
        """Recursively find body with specific MIME type."""
        if part.get("mimeType") == mime_type:
            data = part.get("body", {}).get("data", "")
            if data:
                return decode_body(data)

        for subpart in part.get("parts", []):
            result = find_body(subpart, mime_type)
            if result:
                return result
        return None

    # Try plain text first
    if prefer_plain:
        body = find_body(payload, "text/plain")
        if body:
            return body

    # Fall back to HTML (strip tags for now)
    body = find_body(payload, "text/html")
    if body:
        # Basic HTML tag stripping
        body = re.sub(r"<[^>]+>", "", body)
        body = body.replace("&nbsp;", " ")
        body = body.replace("&lt;", "<")
        body = body.replace("&gt;", ">")
        body = body.replace("&amp;", "&")
        body = body.replace("&#39;", "'")
        body = body.replace("&quot;", '"')
        return body

    # Check if body is directly in payload
    data = payload.get("body", {}).get("data", "")
    if data:
        return decode_body(data)

    return ""


def fetch_thread(service, thread_id: str) -> dict:
    """Fetch full thread from Gmail API."""
    try:
        thread = service.users().threads().get(
            userId="me",
            id=thread_id,
            format="full"
        ).execute()
        return thread
    except Exception as e:
        print(f"Error fetching thread: {e}")
        sys.exit(1)


def email_to_wikilink(email: str, name: str, reference: dict) -> str:
    """Convert email address to wiki-link using reference."""
    email_lower = email.lower()

    # Check reference file
    if email_lower in reference.get("emails", {}):
        return reference["emails"][email_lower]

    # Check if it's the user's email
    if email_lower in reference.get("accounts", []):
        return "me"

    # Default: use name without wiki-link
    return name or email


def apply_glossary(text: str, reference: dict) -> str:
    """Apply glossary wiki-links to text."""
    glossary = reference.get("glossary", {})

    for term, wikilink in glossary.items():
        # Case-insensitive whole word replacement
        pattern = rf"\b{re.escape(term)}\b"
        # Only replace if not already a wiki-link
        if f"[[{term}" not in text and f"|{term}]]" not in text:
            text = re.sub(pattern, wikilink, text, flags=re.IGNORECASE)

    return text


def get_day_of_week(dt: datetime) -> str:
    """Get 3-letter day of week."""
    return dt.strftime("%a")


def format_date_for_link(dt: datetime) -> str:
    """Format date as Mon-DD-YYYY Day for Obsidian links."""
    return dt.strftime("%b-%d-%Y") + " " + get_day_of_week(dt)


def format_time_for_anchor(dt: datetime, sender_name: str) -> str:
    """Format time for Obsidian anchor: 'from Name HH MM'."""
    time_str = dt.strftime("%H %M")
    return f"from {sender_name} {time_str}"


def format_obsidian(messages: list[dict], reference: dict) -> str:
    """Format parsed messages as Obsidian markdown."""

    # Group messages by calendar date
    by_date = {}
    for msg in messages:
        dt = msg.get("datetime")
        if not dt:
            continue
        date_key = dt.strftime("%Y-%m-%d")
        if date_key not in by_date:
            by_date[date_key] = []
        by_date[date_key].append(msg)

    # Sort dates
    sorted_dates = sorted(by_date.keys())

    output_blocks = []

    for i, date_key in enumerate(sorted_dates):
        day_messages = sorted(by_date[date_key], key=lambda m: m.get("timestamp", 0))
        first_msg = day_messages[0]
        last_msg = day_messages[-1]

        dt = first_msg["datetime"]

        # Determine header name (other person, not me)
        if first_msg["from"]["is_me"]:
            # I'm sender, use first recipient
            if first_msg["to"]:
                header_name = first_msg["to"][0]["name"]
            else:
                header_name = "Unknown"
        else:
            header_name = first_msg["from"]["name"]

        # Subject (truncate to 50 chars)
        subject = first_msg["subject"]
        if len(subject) > 50:
            subject = subject[:47] + "..."

        # Start time
        start_time = dt.strftime("%H:%M")

        # Build header
        lines = [f"### 📫 Email • {header_name} • {subject} • {start_time}"]

        # Prev link (if not first day)
        if i > 0:
            prev_date = sorted_dates[i - 1]
            prev_msgs = by_date[prev_date]
            prev_last = sorted(prev_msgs, key=lambda m: m.get("timestamp", 0))[-1]
            prev_dt = prev_last["datetime"]
            prev_sender = prev_last["from"]["name"]
            prev_link = f"[[{format_date_for_link(prev_dt)}#{format_time_for_anchor(prev_dt, prev_sender)}]]"
            lines.append(f"- `prev  `:: {prev_link}")

        # Next link (if not last day)
        if i < len(sorted_dates) - 1:
            next_date = sorted_dates[i + 1]
            next_msgs = by_date[next_date]
            next_first = sorted(next_msgs, key=lambda m: m.get("timestamp", 0))[0]
            next_dt = next_first["datetime"]
            next_sender = next_first["from"]["name"]
            next_link = f"[[{format_date_for_link(next_dt)}#{format_time_for_anchor(next_dt, next_sender)}]]"
            lines.append(f"- `next  `:: {next_link}")

        # From
        from_wikilink = email_to_wikilink(
            first_msg["from"]["email"],
            first_msg["from"]["name"],
            reference
        )
        lines.append(f"- `From  `:: {from_wikilink}")

        # To
        to_links = [
            email_to_wikilink(r["email"], r["name"], reference)
            for r in first_msg["to"]
        ]
        if to_links:
            lines.append(f"- `To    `:: {', '.join(to_links)}")

        # CC
        cc_links = [
            email_to_wikilink(r["email"], r["name"], reference)
            for r in first_msg["cc"]
        ]
        if cc_links:
            lines.append(f"- `CC    `:: {', '.join(cc_links)}")

        # Subject
        lines.append(f"- `Subj  `:: {first_msg['subject']}")

        # Focus (brief summary from body, skipping salutations and quotes)
        focus_text = generate_focus(first_msg["body"], first_msg["subject"])
        focus = apply_glossary(focus_text, reference)
        lines.append(f"- `Focus `:: {focus}")

        # Date
        lines.append(f"- `Date  `:: {dt.strftime('%Y-%m-%d')}")

        # Time
        lines.append(f"- `Time  `:: {start_time}")

        # Message bodies for this day
        for msg in day_messages:
            msg_dt = msg["datetime"]
            sender = msg["from"]["name"]
            time_str = msg_dt.strftime("%H:%M")

            lines.append(f"##### from: {sender} : {time_str}")

            # Quote the body (strip quoted replies to avoid duplication)
            clean_body = strip_quoted_text(msg["body"])
            if clean_body:
                body_lines = clean_body.split("\n")
                for body_line in body_lines:
                    lines.append(f"> {body_line}")
            else:
                lines.append("> (no new content - reply only)")

        # Attachments section (collect from all messages this day)
        all_attachments = []
        for msg in day_messages:
            for att in msg["attachments"]:
                all_attachments.append(att)

        if all_attachments:
            lines.append("#### Attachments")
            for att in all_attachments:
                size_str = format_size(att["size"])
                lines.append(f"- `{att['filename']}` — {size_str}")

        # Thread Summary (only on last day)
        if i == len(sorted_dates) - 1 and len(sorted_dates) > 1:
            lines.append("#### Thread Summary")
            # Generate summary from thread data
            summary = generate_thread_summary(messages, reference)
            lines.append(summary)

        # Tasks section
        lines.append("#### Tasks")
        lines.append("None")

        # Separator
        lines.append("---")

        output_blocks.append("\n".join(lines))

    return "\n\n".join(output_blocks)


def format_json(messages: list[dict]) -> str:
    """Format parsed messages as JSON."""
    # Convert datetime objects to strings for JSON serialization
    def serialize(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return obj

    output = []
    for msg in messages:
        clean_msg = {k: v for k, v in msg.items() if k != "datetime"}
        output.append(clean_msg)

    return json.dumps(output, indent=2, default=serialize)


def copy_to_clipboard(text: str):
    """Copy text to clipboard (macOS)."""
    try:
        process = subprocess.Popen(
            ["pbcopy"],
            stdin=subprocess.PIPE,
            env={**os.environ, "LANG": "en_US.UTF-8"}
        )
        process.communicate(text.encode("utf-8"))
        return True
    except:
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Fetch Gmail thread and export with full metadata"
    )
    parser.add_argument(
        "thread_id",
        help="Gmail thread ID or full URL (standard, popup, or search URL)"
    )
    parser.add_argument(
        "--format", "-f",
        choices=["json", "obsidian"],
        default="obsidian",
        help="Output format (default: obsidian)"
    )
    parser.add_argument(
        "--copy", "-c",
        action="store_true",
        help="Copy output to clipboard"
    )
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Output raw API response (for debugging)"
    )

    args = parser.parse_args()

    # Check dependencies
    check_dependencies()

    # Load reference file
    reference = load_email_reference()

    # Get Gmail service
    service = get_gmail_service()

    # Determine thread ID from input (URL, Message-ID, or raw ID)
    input_str = args.thread_id.strip()

    if is_message_id(input_str):
        # Input is a Message-ID from "Show Original" - search for it
        thread_id = search_by_message_id(service, input_str)
        if not thread_id:
            print("Could not find thread. Check that you're authenticated with the correct account.", file=sys.stderr)
            sys.exit(1)
        print(f"Found thread ID: {thread_id}", file=sys.stderr)
    else:
        # Input is a URL or raw thread ID
        thread_id = extract_thread_id(input_str)
        if thread_id != input_str:
            print(f"Extracted thread ID: {thread_id}", file=sys.stderr)

    # Fetch thread
    print(f"Fetching thread {thread_id}...", file=sys.stderr)
    thread = fetch_thread(service, thread_id)

    if args.raw:
        output = json.dumps(thread, indent=2)
    else:
        # Parse all messages
        messages = []
        for msg in thread.get("messages", []):
            parsed = parse_message(msg, reference)
            messages.append(parsed)

        # Sort by timestamp
        messages.sort(key=lambda m: m.get("timestamp", 0))

        # Format output
        if args.format == "json":
            output = format_json(messages)
        else:
            output = format_obsidian(messages, reference)

    # Output
    if args.copy:
        if copy_to_clipboard(output):
            print("Output copied to clipboard", file=sys.stderr)
        else:
            print("Failed to copy to clipboard", file=sys.stderr)
            print(output)
    else:
        print(output)


if __name__ == "__main__":
    main()
