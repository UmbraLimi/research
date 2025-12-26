# Page: Creator Dashboard

**Code:** CDSH
**URL:** `/dashboard` (role-aware, same URL as SDSH/TDSH)
**Access:** Authenticated (Creator role)
**Priority:** P0
**Status:** In Scope

---

## Purpose

Central hub for Creators to manage their courses, track earnings, approve Student-Teachers, monitor course performance, and handle creator-specific workflows.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| LGIN | Successful login (Creator role) | Default post-login |
| Nav | "Dashboard" link | Global navigation |
| STUD | "Dashboard" link | From Creator Studio |
| CPRO | "Dashboard" link | From own profile |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| STUD | "Creator Studio" / "Manage Courses" | Course management |
| CPRO | "View Public Profile" | See public creator profile |
| PROF | "Edit Profile" | Edit profile settings |
| CDET | Course card click | View course detail |
| (ST Approval) | "Review Application" | ST approval flow |
| (Cert Approval) | "Review Certification" | Certification approval |
| (Payout) | "Request Payout" | Initiate payout |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| courses | id, title, student_count, rating, is_active | Course list |
| enrollments | course_id, status | Enrollment counts |
| student_teachers | course_id, user_id, is_active | ST management |
| certificates | course_id, user_id, type, recommended_by | Pending certifications |
| payment_splits | amount_cents, status (where creator) | Earnings |
| payouts | amount_cents, status, paid_at | Payout history |
| users (students) | count | Total students |

---

## Sections

### Header Bar
- Greeting: "Welcome, Creator [Name]!"
- Quick stats: X courses, Y total students, Z STs

### Earnings Overview
- **Royalty Balance:** Pending creator royalties (15% per CD-020)
- **Total Earned:** Lifetime royalties
- **This Month:** Current month earnings
- "View Earnings Details" → breakdown by course
- "Request Payout" button

### Pending Approvals
- **Badge count** showing total pending items
- **ST Applications:**
  - Students requesting to become STs for your courses
  - Each shows: name, course, qualifications
  - "Approve" / "Decline" buttons
  - Source: US-P063
- **Certification Requests:**
  - ST recommendations awaiting creator approval
  - Each shows: student name, course, recommended by
  - "Issue Certificate" / "Decline" buttons
  - Source: US-P062
- Empty state: "No pending approvals"

### Course Performance
- Grid/list of creator's courses
- Each course shows:
  - Title + thumbnail
  - Active students count
  - Completion rate
  - Average rating
  - Revenue generated
  - "Manage" → STUD (course edit)
  - "View" → CDET
- Sort by: Students, Revenue, Rating

### Student-Teacher Overview
- List of STs certified for creator's courses
- Each shows:
  - Name, avatar
  - Course(s) certified for
  - Students taught
  - Performance rating
  - "View Profile" → STPR
- "View All STs" if many

### Recent Activity
- Timeline of recent events:
  - New enrollments
  - Course completions
  - ST certifications
  - Reviews received
- Last 10 items

### Quick Actions
- "Create New Course" → STUD
- "View All Courses" → STUD
- "Update Profile" → PROF

---

## User Stories Fulfilled

- US-P003: Creator dashboard for course management
- US-C033: View course analytics
- US-P062: Approve student certifications
- US-P063: Approve ST applications
- US-P064: Approve payouts (via request)
- US-C035: View earnings and royalties

---

## States & Variations

| State | Description |
|-------|-------------|
| New Creator | No courses yet, prominent "Create Course" CTA |
| Active Creator | Courses live, students enrolled |
| Pending Actions | Badge on Pending Approvals, highlight needed |
| Payout Available | Highlight royalty balance |
| Multi-Role | May also show learning sections |

---

## Mobile Considerations

- Earnings summary at top
- Pending approvals with swipe actions
- Course cards stack vertically
- Collapsible sections

---

## Error Handling

| Error | Display |
|-------|---------|
| Data load fails | "Unable to load dashboard. [Retry]" |
| Approval fails | "Unable to process. Please try again." |

---

## Analytics Events

| Event | Trigger | Data |
|-------|---------|------|
| `page_view` | Page load | courses_count, pending_count |
| `approve_st` | ST approved | st_id, course_id |
| `approve_cert` | Cert issued | student_id, course_id |
| `view_course` | Course clicked | course_id |
| `request_payout` | Payout clicked | amount |

---

## Notes

- CD-020: Creator gets 15% royalty
- Creators may also be Students/STs (multi-role dashboard)
- Consider email notifications for pending approvals
- Analytics could expand significantly (separate page?)
