# Page: Sign Up

**Code:** SGUP
**URL:** `/signup`
**Access:** Public (redirects if logged in)
**Priority:** P0
**Status:** In Scope

---

## Purpose

Register new users to the platform, collecting essential information and creating their account.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| HOME | "Get Started" / "Sign Up" CTA | Primary conversion |
| LGIN | "Create an account" link | From login page |
| CDET | "Sign up to enroll" | Enrollment prompt |
| SBOK | "Sign up to book" | Booking prompt |
| CPRO | "Follow" while logged out | To follow creator |
| (External) | Direct URL, marketing | `/signup` |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| SDSH | Successful signup (as Student) | Onboarding may intercept |
| CDSH | Successful signup (as Creator) | Onboarding may intercept |
| (Return URL) | Successful signup | If came from specific page |
| LGIN | "Already have an account? Log in" | Existing user |
| HOME | Logo click | Return to home |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| users | name, email, password_hash, role, email_verified, created_at | Account creation |

---

## Sections

### Header
- Logo (links to HOME)
- Minimal navigation

### Signup Form
- **Name input**
  - Label: "Full Name"
  - Validation: required, min 2 characters
  - Error: "Please enter your name"
- **Email input**
  - Label: "Email"
  - Type: email
  - Validation: email format, unique check
  - Error: "Please enter a valid email" / "Email already registered"
- **Password input**
  - Label: "Password"
  - Type: password
  - Show/hide toggle
  - Requirements indicator: min 8 chars, etc.
  - Error: "Password must be at least 8 characters"
- **Confirm Password** (optional, or match on submit)
- **Role selection** (optional for MVP)
  - "I want to learn" (Student - default)
  - "I want to create courses" (Creator)
- **Terms checkbox**
  - "I agree to the Terms of Service and Privacy Policy"
  - Links open in new tab
  - Required
- **Submit button:** "Create Account"

### Already Have Account Link
- "Already have an account? Log in" → LGIN
- Below form

### Social Signup (Future)
- "Or sign up with..."
- Google, GitHub
- Placeholder for MVP

---

## User Stories Fulfilled

- US-G011: Register for new account
- US-P007: Create account with email/password

---

## States & Variations

| State | Description |
|-------|-------------|
| Default | Empty form |
| With Return URL | "Sign up to continue" message |
| With Prefill | Email prefilled from marketing/invite |
| Validation Errors | Inline errors per field |
| Email Exists | "Email already registered. Log in instead?" |
| Loading | Submit shows spinner |
| Success | Redirect to dashboard or onboarding |
| Already Logged In | Redirect to dashboard |

---

## Mobile Considerations

- Full-width form
- Large touch targets
- Appropriate keyboard types
- Terms link opens modal or new tab (not navigate away)

---

## Error Handling

| Error | Display |
|-------|---------|
| Email exists | "This email is already registered. [Log in instead?]" |
| Weak password | "Password must be at least 8 characters" |
| Terms not accepted | "Please accept the terms to continue" |
| Network error | "Unable to create account. Please try again." |
| Server error | "Something went wrong. Please try again later." |

---

## Analytics Events

| Event | Trigger | Data |
|-------|---------|------|
| `page_view` | Page load | source, return_url |
| `signup_attempt` | Form submitted | role_selected |
| `signup_success` | Account created | user_id, role |
| `signup_failure` | Signup failed | error_type |
| `login_link_click` | Log in link clicked | - |
| `terms_view` | Terms link clicked | which_link |

---

## Notes

- **Invitation-only launch (GO-025):** May require invite code field for Genesis Cohort
- Consider progressive profiling: minimal signup, more info later
- Email verification flow should follow (US-P013)
- Security: Password strength indicator
- GDPR: Clear consent for terms/privacy
