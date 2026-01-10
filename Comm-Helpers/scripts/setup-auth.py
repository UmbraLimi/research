#!/usr/bin/env python3
"""
Gmail API Authentication Setup

Run this once after placing your OAuth credentials.json file to
complete the authentication flow and store your refresh token.

Usage:
    ./setup-auth.py
"""

import sys
from pathlib import Path

# Configuration
CONFIG_DIR = Path.home() / ".config" / "gmail-thread"
CREDENTIALS_FILE = CONFIG_DIR / "credentials.json"
TOKEN_FILE = CONFIG_DIR / "token.json"
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def main():
    print("=" * 60)
    print("Gmail API Authentication Setup")
    print("=" * 60)
    print()

    # Check for Google libraries
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        print("Error: Required Google libraries not installed.")
        print()
        print("Install with:")
        print("  pip install google-auth google-auth-oauthlib google-api-python-client")
        sys.exit(1)

    # Check for credentials file
    if not CREDENTIALS_FILE.exists():
        print(f"Error: OAuth credentials not found.")
        print()
        print("To get credentials:")
        print()
        print("1. Go to https://console.cloud.google.com/")
        print()
        print("2. Create a new project (or select existing):")
        print("   - Click 'Select a project' dropdown at top")
        print("   - Click 'New Project'")
        print("   - Name it (e.g., 'Gmail Thread Exporter')")
        print()
        print("3. Enable the Gmail API:")
        print("   - Go to 'APIs & Services' > 'Library'")
        print("   - Search for 'Gmail API'")
        print("   - Click 'Enable'")
        print()
        print("4. Configure OAuth consent screen:")
        print("   - Go to 'APIs & Services' > 'OAuth consent screen'")
        print("   - Select 'External' (or 'Internal' if Workspace)")
        print("   - Fill in app name and your email")
        print("   - Add scope: 'Gmail API .../auth/gmail.readonly'")
        print("   - Add yourself as a test user")
        print()
        print("5. Create OAuth credentials:")
        print("   - Go to 'APIs & Services' > 'Credentials'")
        print("   - Click 'Create Credentials' > 'OAuth client ID'")
        print("   - Application type: 'Desktop app'")
        print("   - Name it (e.g., 'Gmail Thread CLI')")
        print("   - Click 'Create'")
        print()
        print("6. Download and save credentials:")
        print("   - Click the download icon next to your new credential")
        print("   - Save the JSON file to:")
        print(f"     {CREDENTIALS_FILE}")
        print()
        print("7. Run this script again:")
        print("   ./setup-auth.py")
        print()

        # Create config directory if it doesn't exist
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        print(f"(Config directory created at {CONFIG_DIR})")
        sys.exit(1)

    # Check if already authenticated
    if TOKEN_FILE.exists():
        try:
            creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
            if creds and creds.valid:
                print("Already authenticated!")
                print(f"Token stored at: {TOKEN_FILE}")
                print()
                print("To re-authenticate, delete the token file and run again:")
                print(f"  rm {TOKEN_FILE}")
                print("  ./setup-auth.py")
                return
            elif creds and creds.expired and creds.refresh_token:
                print("Token expired, refreshing...")
                creds.refresh(Request())
                with open(TOKEN_FILE, "w") as token:
                    token.write(creds.to_json())
                print("Token refreshed successfully!")
                return
        except Exception as e:
            print(f"Existing token invalid: {e}")
            print("Starting fresh authentication...")
            print()

    # Run OAuth flow
    print("Starting OAuth flow...")
    print()
    print("A browser window will open for you to authorize access.")
    print("(If it doesn't open, check your terminal for a URL to copy)")
    print()

    try:
        flow = InstalledAppFlow.from_client_secrets_file(
            str(CREDENTIALS_FILE), SCOPES
        )
        creds = flow.run_local_server(port=0)

        # Save the token
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

        print()
        print("=" * 60)
        print("Authentication successful!")
        print("=" * 60)
        print()
        print(f"Token stored at: {TOKEN_FILE}")
        print()
        print("You can now use gmail-thread.py:")
        print("  ./gmail-thread.py THREAD_ID")
        print()
        print("To get a thread ID, open any email in Gmail and copy")
        print("the ID from the URL after #inbox/ or #sent/")
        print()

    except Exception as e:
        print(f"Authentication failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
