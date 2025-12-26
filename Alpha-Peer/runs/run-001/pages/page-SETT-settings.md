# Page: Settings

**Code:** SETT
**URL:** `/settings`
**Access:** Authenticated
**Priority:** P0
**Status:** In Scope

---

## Purpose

Central location for account management, notification preferences, payment settings, availability management, and security options.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| Nav | "Settings" link | Global navigation or user menu |
| PROF | "Settings" link | From profile page |
| SDSH/TDSH/CDSH | "Settings" in menu | From dashboards |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| PROF | "View Profile" link | Back to profile |
| (Stripe) | "Manage Payment" | External: Stripe portal |
| LGIN | After logout | Redirect to login |
| PWRS | "Change Password" → reset flow | Password change |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| users | email, name, handle, timezone | Account settings |
| (notification_preferences) | various flags | Notification settings |
| availability | day_of_week, start_time, end_time, timezone | ST availability |
| (stripe_customer) | customer_id, payment_method | Payment info |

---

## Sections

### Settings Navigation
- Sidebar or tab navigation:
  - Account
  - Notifications
  - Availability (STs/Creators)
  - Payment (STs/Creators)
  - Privacy
  - Security

### Account Settings
- **Email:** Display current, "Change" button
- **Name:** Editable field
- **Handle:** Display @handle, "Change" (with availability check)
- **Timezone:** Dropdown selector
- **Language:** (Future) Dropdown

### Notification Preferences
- **Email Notifications:**
  - Session reminders (toggle)
  - New message received (toggle)
  - Course updates (toggle)
  - Marketing/newsletter (toggle)
  - Certification notifications (toggle)
- **Push Notifications:** (if mobile app)
  - Same categories as email
- **Notification Frequency:**
  - Immediate / Daily digest / Weekly digest

### Availability Settings (STs/Creators Only)
- Weekly calendar grid
- Set available time slots:
  - Day of week
  - Start time
  - End time
- Timezone reminder/display
- "Copy to all days" helper
- Buffer time between sessions (optional)

### Payment Settings (STs/Creators Only)
- **Payout Method:**
  - Connected Stripe account status
  - "Connect Stripe" or "Update" button → Stripe Connect
- **Payout Threshold:**
  - Minimum balance for auto-payout
- **Payout History:**
  - Recent payouts list
  - "View All" link

### Privacy Settings
- **Profile Visibility:** Public/Private toggle
- **Show Online Status:** Toggle
- **Allow Messages From:** Everyone / Enrolled only / Following only
- **Data Export:** "Download My Data" button

### Security Settings
- **Password:**
  - "Change Password" → PWRS flow or inline
  - Last changed date
- **Two-Factor Authentication:** (Future)
  - Enable/disable 2FA
  - Recovery codes
- **Active Sessions:**
  - List of logged-in devices
  - "Log out" button per session
  - "Log out all devices"
- **Delete Account:**
  - "Delete My Account" (with confirmation)

### Logout
- "Log Out" button
- Confirms and redirects to HOME/LGIN

---

## User Stories Fulfilled

- US-P010: Manage account settings
- US-P018: Control notification preferences
- US-C006: Creator sets availability
- US-T001: ST sets availability
- US-P022: Set timezone preference

---

## States & Variations

| State | Description |
|-------|-------------|
| Student | Hides Availability, Payment sections |
| ST | Shows Availability, Payment sections |
| Creator | Shows Availability, Payment sections |
| Multi-Role | All sections visible |
| Stripe Connected | Shows account status, update option |
| Stripe Not Connected | Prominent "Connect Stripe" CTA |

---

## Mobile Considerations

- Settings nav becomes horizontal tabs or accordion
- Each section is a separate screen
- Large touch targets for toggles
- Confirmation dialogs for destructive actions

---

## Error Handling

| Error | Display |
|-------|---------|
| Save fails | "Unable to save settings. Please try again." |
| Email change fails | "Unable to update email. Try again." |
| Stripe connection fails | "Unable to connect payment. Try again." |
| Account deletion fails | "Unable to delete. Contact support." |

---

## Analytics Events

| Event | Trigger | Data |
|-------|---------|------|
| `page_view` | Page load | section |
| `setting_changed` | Any setting saved | setting_name, new_value |
| `availability_updated` | Availability changed | slots_count |
| `stripe_connected` | Stripe connected | - |
| `logout` | Logout clicked | - |
| `account_deleted` | Account deleted | - |

---

## Notes

- Security-sensitive changes should require password confirmation
- Email change should trigger verification email
- Consider in-app notification preview
- Stripe Connect for marketplace payouts (CD-020)
