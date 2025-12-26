# Page: Student-Teacher Dashboard

**Code:** TDSH
**URL:** `/dashboard` (role-aware, same URL as SDSH)
**Access:** Authenticated (Student-Teacher role)
**Priority:** P0
**Status:** In Scope

---

## Purpose

Central hub for Student-Teachers to manage their teaching schedule, track earnings, view their students, and handle teaching-related tasks.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| LGIN | Successful login (ST role) | Default post-login |
| Nav | "Dashboard" link | Global navigation |
| SROM | "Back to Dashboard" | After teaching session |
| PROF | "Dashboard" link | From profile |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| SROM | "Join Session" | Join teaching session |
| STPR | "View My Profile" | See public ST profile |
| PROF | "Edit Profile" | Edit profile settings |
| SETT | "Availability" | Manage teaching schedule |
| MSGS | "Message Student" | Contact a student |
| CDET | Course title click | View course info |
| (Payout) | "Request Payout" | Initiate payout (future) |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| sessions | id, scheduled_start, student_id, course_id, status | Teaching schedule |
| student_teachers | course_id, students_taught, is_active | Certification status |
| payment_splits | amount_cents, status | Earnings tracking |
| payouts | amount_cents, status, paid_at | Payout history |
| enrollments | student_id, course_id | My students list |
| users (students) | name, avatar | Student display |
| courses | id, title | Course info |
| certificates | user_id, course_id, type, recommended_by | Pending recommendations |

---

## Sections

### Header Bar
- Greeting: "Welcome, Teacher [Name]!"
- Availability toggle: "Available for Summon" (if goodwill enabled)
- Quick stats: X students, Y sessions this week

### Earnings Overview
- **Pending Balance:** Amount awaiting payout
- **Total Earned:** Lifetime earnings
- **This Month:** Current month earnings
- "View Earnings Details" → detailed breakdown
- "Request Payout" button (if eligible)

### Upcoming Teaching Sessions
- Next 5 scheduled sessions
- Each shows:
  - Date/time
  - Student name + avatar
  - Course title
  - "Join" button (active near start time) → SROM
  - "Reschedule" option
- Empty state: "No sessions scheduled"

### My Students
- List of students currently learning from this ST
- Each shows:
  - Avatar + name
  - Course enrolled in
  - Progress percentage
  - "Message" → MSGS
  - "View Progress" → detailed view
- Grouped by course if teaching multiple

### Pending Actions
- **Certification Recommendations:**
  - Students ready for completion certificate
  - "Recommend for Certification" button
- **Intro Session Requests** (per CD-029):
  - Pending free intro sessions
  - Accept/decline options
- Empty state: "No pending actions"

### Availability Quick View
- Weekly calendar showing available slots
- "Edit Availability" → SETT

### Teaching Stats
- Sessions completed this month
- Average session rating
- Students helped

---

## User Stories Fulfilled

- US-T013: Access ST-specific dashboard
- US-T023: View teaching earnings
- US-P061: Recommend students for certification

---

## States & Variations

| State | Description |
|-------|-------------|
| New ST | Just certified, no sessions yet, onboarding tips |
| Active ST | Sessions scheduled, students assigned |
| Session Starting | "Join Now" prominently displayed |
| Payout Available | Highlight pending balance, enable payout |
| Multi-Role | Combined with student sections (unified dashboard) |

---

## Mobile Considerations

- Earnings summary at top (primary concern for STs)
- Sessions list scrollable
- Sticky "Join Session" if imminent
- Quick toggle for availability

---

## Error Handling

| Error | Display |
|-------|---------|
| Data load fails | "Unable to load dashboard. [Retry]" |
| Payout request fails | "Unable to process. Please try again." |

---

## Analytics Events

| Event | Trigger | Data |
|-------|---------|------|
| `page_view` | Page load | sessions_count, earnings_pending |
| `join_session` | Join clicked | session_id |
| `recommend_cert` | Recommend clicked | student_id, course_id |
| `view_earnings` | Earnings detail clicked | - |
| `request_payout` | Payout clicked | amount |

---

## Notes

- Multi-role users: May see both learning + teaching sections
- CD-033: 85/15 split (ST gets 85%)
- Consider combining SDSH + TDSH into unified role-aware dashboard
- Real-time notification for new session bookings
