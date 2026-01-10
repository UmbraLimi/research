# Gmail Thread Exporter

**Used by `/r-email` skill for complete thread metadata.**

Fetch Gmail threads via API with **full metadata** for all messages:
- Complete To/CC/BCC for every message in thread
- All attachment names and sizes
- Proper threading with prev/next links
- Obsidian-formatted output ready for Daily Notes

## Why This Exists

Gmail's copy-paste methods lose metadata:
- **Print view:** Only shows attachments/CC from most recent email
- **Forward:** Attachments not copyable as text
- **Show Original:** One message at a time

The Gmail API returns **everything** for the entire thread in one call.

## Quick Start

```bash
# 1. Install dependencies
pip3 install google-auth google-auth-oauthlib google-api-python-client

# 2. Set up Google Cloud credentials (see below)

# 3. Authenticate
./setup-auth.py

# 4. Export a thread
./gmail-thread.py THREAD_ID --copy
```

## Setup (One-Time)

### Step 1: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click **Select a project** → **New Project**
3. Name it (e.g., "Gmail Thread Exporter")
4. Click **Create**

### Step 2: Enable Gmail API

1. In your project, go to **APIs & Services** → **Library**
2. Search for "Gmail API"
3. Click **Enable**

### Step 3: Configure OAuth Consent Screen

1. Go to **APIs & Services** → **OAuth consent screen**
2. Select **External** (or Internal if using Google Workspace)
3. Fill in:
   - App name: "Gmail Thread Exporter"
   - User support email: your email
   - Developer contact: your email
4. Click **Save and Continue**
5. On Scopes page, click **Add or Remove Scopes**
6. Find and select: `https://www.googleapis.com/auth/gmail.readonly`
7. Click **Save and Continue**
8. On Test Users page, click **Add Users**
9. Add your Gmail address
10. Click **Save and Continue**

### Step 4: Create OAuth Credentials

1. Go to **APIs & Services** → **Credentials**
2. Click **Create Credentials** → **OAuth client ID**
3. Application type: **Desktop app**
4. Name: "Gmail Thread CLI"
5. Click **Create**
6. Click the **download icon** to download JSON
7. Save as: `~/.config/gmail-thread/credentials.json`

```bash
# Create directory and move credentials
mkdir -p ~/.config/gmail-thread
mv ~/Downloads/client_secret_*.json ~/.config/gmail-thread/credentials.json
```

### Step 5: Authenticate

```bash
cd /path/to/Comm-Helpers/scripts
chmod +x setup-auth.py gmail-thread.py
./setup-auth.py
```

A browser window opens. Sign in and authorize. Token is saved locally.

## Usage

### Get Thread ID

Open any email thread in Gmail. The URL looks like:
```
https://mail.google.com/mail/u/0/#inbox/18d5a2b3c4e5f6g7
                                       └───────────────┘
                                           Thread ID
```

Copy the ID after `#inbox/` (or `#sent/`, `#label/`, etc.)

### Export Thread

```bash
# Output to terminal (Obsidian format)
./gmail-thread.py 18d5a2b3c4e5f6g7

# Copy to clipboard
./gmail-thread.py 18d5a2b3c4e5f6g7 --copy

# JSON format
./gmail-thread.py 18d5a2b3c4e5f6g7 --format json

# Debug: raw API response
./gmail-thread.py 18d5a2b3c4e5f6g7 --raw
```

### Output

The script outputs Obsidian-formatted markdown:
- One block per calendar day
- `prev`/`next` links between days
- Full From/To/CC with wiki-links (from `email-reference.md`)
- All attachments with sizes
- Thread Summary placeholder on final day

## Files

```
~/.config/gmail-thread/
├── credentials.json    # OAuth client credentials (you create)
└── token.json          # Refresh token (auto-generated)

Comm-Helpers/scripts/
├── gmail-thread.py     # Main export script
├── setup-auth.py       # One-time auth helper
└── README.md           # This file

Comm-Helpers/.claude/commands/
└── email-reference.md  # Email → wiki-link mappings (used by script)
```

## Security

- **credentials.json**: OAuth client ID. Not secret, but don't share publicly.
- **token.json**: Contains refresh token. **Keep private.** Grants read access to your Gmail.
- Both files stay local in `~/.config/gmail-thread/`
- The script only requests `gmail.readonly` scope (cannot modify/delete)

## Troubleshooting

### "Credentials not found"
Run `./setup-auth.py` for instructions on getting credentials.

### "Token expired"
Run `./setup-auth.py` again to refresh.

### "Access blocked: App not verified"
During OAuth flow, click **Advanced** → **Go to [app name] (unsafe)**.
This is normal for personal-use apps that haven't gone through Google's review.

### "Rate limit exceeded"
Wait a few minutes. The Gmail API has usage quotas.

## Limitations

- Requires Python 3.8+
- macOS clipboard support (`pbcopy`). For Linux, modify `copy_to_clipboard()`.
- Thread ID must be copied manually from Gmail URL.
- Focus field uses first line of body (enhance by editing script).
- Thread Summary is a placeholder (add manually or enhance script).
