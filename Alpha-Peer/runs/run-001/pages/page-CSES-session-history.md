# Page: Session History (Creator)

**Code:** CSES
**URL:** `/studio/sessions`
**Access:** Authenticated (Creator role)
**Priority:** P0
**Status:** In Scope

---

## Purpose

Allow Creators to view all tutoring sessions across their courses, monitor ST performance, access recordings, and handle session-related issues.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| CDSH | "View Sessions" link | From dashboard |
| STUD | "Sessions" tab | From Creator Studio |
| CMST | "View Sessions" on student | Filtered to student |
| Nav | "Sessions" link | Creator navigation |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| PROF | Student/ST name click | View profile |
| SROM | "View Recording" | If recording exists |
| MSGS | "Message" button | Contact participant |
| CDET | Course name click | View course |
| CDSH | Back/breadcrumb | Return to dashboard |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| sessions | All fields | Session records |
| users (students) | id, name, avatar | Student info |
| users (STs) | id, name, avatar | ST info |
| courses | id, title (where creator_id = current user) | Course filter |
| enrollments | id, course_id, student_id | Enrollment context |
| session_assessments | rating, comment | Feedback data |

---

## Sections

### Header
- Page title: "Session History"
- Stats: "X total sessions, Y this week"
- Date range selector

### Filters
- **Course:** All / specific course
- **ST:** All / specific Student-Teacher
- **Student:** Search by name
- **Status:** All / Completed / Scheduled / Cancelled / No-show
- **Date range:** Preset (Today, This week, This month) or custom

### Sessions Table

| Column | Content |
|--------|---------|
| Date/Time | Session datetime |
| Course | Course title |
| Student | Avatar + name |
| ST | Avatar + name |
| Duration | Actual duration |
| Status | Completed / Cancelled / No-show |
| Rating | Stars (if rated) |
| Recording | Play icon (if available) |
| Actions | View, Message |

### Session Detail Panel
When clicking a session:
- Full session info
- Student feedback (rating + comment)
- ST feedback (rating + comment)
- Recording player (if available)
- Session notes
- Dispute resolution (if flagged)

### Upcoming Sessions Tab
- Calendar view of scheduled sessions
- Quick view: who, when, which course
- No direct intervention (STs manage their own)

### Session Metrics Summary
- Average session duration
- Completion rate
- Average rating
- No-show rate
- By ST breakdown

---

## User Stories Fulfilled

- US-C043: View session history
- US-C044: Access session recordings
- US-C045: Monitor ST performance via sessions
- US-C046: Handle session disputes

---

## States & Variations

| State | Description |
|-------|-------------|
| Default | Recent sessions, all courses |
| Filtered | By course, ST, student, or date |
| Detail Open | Session detail panel visible |
| Calendar View | Upcoming sessions in calendar |
| Empty | No sessions yet |

---

## Mobile Considerations

- Card list instead of table
- Swipe for actions
- Recording plays in modal
- Calendar view simplified

---

## Error Handling

| Error | Display |
|-------|---------|
| Load fails | "Unable to load sessions. [Retry]" |
| Recording unavailable | "Recording not available" |

---

## Analytics Events

| Event | Trigger | Data |
|-------|---------|------|
| `page_view` | Page load | session_count, filter_state |
| `session_viewed` | Detail opened | session_id |
| `recording_played` | Play clicked | session_id |
| `filter_applied` | Filter changed | filter_type, value |

---

## Notes

- Recordings stored in R2, streamed via signed URLs
- Creator cannot join live sessions (ST-student only)
- Consider flagging sessions with low ratings for review
