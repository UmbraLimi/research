# Screen: Admin Enrollments

**Code:** AENR
**URL:** `/admin/enrollments` (route within Admin SPA)
**Access:** Authenticated (Admin role)
**Priority:** P0
**Status:** In Scope

---

## Purpose

CRUD interface for managing enrollments - view, create manual enrollments, cancel, issue refunds, and reassign Student-Teachers.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| ADMN | "Enrollments" nav item | Admin sidebar |
| AUSR | "View Enrollments" on user | Filtered to user |
| ACRS | "View Enrollments" on course | Filtered to course |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| AUSR | Student/ST name click | View user |
| ACRS | Course name click | View course |
| ASES | "View Sessions" | Filtered to enrollment |
| APAY | "View Transactions" | Related payments |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| enrollments | All fields | Enrollment records |
| users (students) | id, name, email | Student info |
| users (STs) | id, name | Assigned ST |
| courses | id, title, price_cents | Course info |
| transactions | enrollment_id, amount_cents, status | Payment info |
| sessions | enrollment_id, count | Session stats |
| module_progress | enrollment_id | Progress data |

---

## Sections

### Header
- Screen title: "Enrollment Management"
- "Create Enrollment" button
- Export button

### Search & Filters
- **Search:** Student name/email, course title
- **Course filter:** All / specific course
- **Status filter:** All / Active / Completed / Cancelled
- **ST filter:** All / Assigned / Unassigned
- **Date filter:** Enrollment date range

### Enrollments Table

| Column | Content |
|--------|---------|
| Student | Name + email |
| Course | Course title |
| ST | Assigned ST name (or "Unassigned") |
| Enrolled | Date |
| Progress | Progress bar |
| Sessions | Completed / Scheduled |
| Status | Active / Completed / Cancelled |
| Payment | Paid / Refunded |
| Actions | Edit, Cancel, Refund |

### Enrollment Detail Panel

**View Mode:**
- Full enrollment info
- Student info (link to AUSR)
- Course info (link to ACRS)
- Assigned ST (link to AUSR)
- Progress breakdown:
  - Modules completed
  - Sessions completed / scheduled
  - Time since last activity
- Payment details:
  - Transaction ID
  - Amount paid
  - Refund status
- Timeline:
  - Enrolled
  - First session
  - Last activity
  - Completed (if applicable)

**Edit Mode:**
- Reassign ST (dropdown of course STs)
- Status change (with reason)
- Admin notes

### Actions

| Action | Description |
|--------|-------------|
| Edit | Change ST, status, notes |
| Reassign ST | Change assigned Student-Teacher |
| Cancel | Cancel enrollment (with reason) |
| Full Refund | Process full refund |
| Partial Refund | Process partial refund |
| Force Complete | Mark as completed (override) |
| Extend Access | Extend enrollment period (if applicable) |

### Create Enrollment Modal
- Select student (search)
- Select course
- Assign ST (optional)
- Payment status (paid/comp/waived)
- Reason (comp enrollments)
- Send notification toggle

---

## CRUD Operations

| Operation | Endpoint | Notes |
|-----------|----------|-------|
| List | GET /api/admin/enrollments | Paginated, filterable |
| Read | GET /api/admin/enrollments/:id | Full enrollment data |
| Create | POST /api/admin/enrollments | Manual/comp enrollment |
| Update | PATCH /api/admin/enrollments/:id | Edit enrollment |
| Delete | DELETE /api/admin/enrollments/:id | Soft delete |

---

## States & Variations

| State | Description |
|-------|-------------|
| List | Default enrollment list |
| Filtered | By user, course, status |
| Detail | Enrollment panel open |
| Creating | New enrollment form |
| Refunding | Refund confirmation flow |

---

## Error Handling

| Error | Display |
|-------|---------|
| Load fails | "Unable to load enrollments. [Retry]" |
| Refund fails | "Refund failed. Check Stripe." |
| No STs available | "No Student-Teachers available for this course" |

---

## Notes

- Comp enrollments: Admin can enroll without payment
- Refunds go through Stripe
- ST reassignment should notify both old and new ST
