# Page: Session Booking

**Code:** SBOK
**URL:** `/book/:st_id` or `/courses/:course_id/book`
**Access:** Authenticated (enrolled students)
**Priority:** P0
**Status:** In Scope

---

## Purpose

Enable students to select a Student-Teacher and schedule a tutoring session for their enrolled course.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| CDET | "Book a Session" CTA | Course detail page |
| CDET | ST card "Book with [Name]" | Pre-selected ST |
| SDSH | "Book Session" on course card | From dashboard |
| STPR | "Book Session" button | Pre-selected ST |
| STDR | "Book Session" on ST card | Pre-selected ST |
| CCNT | "Schedule Session" | From course content |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| SDSH | After successful booking | Return to dashboard |
| STPR | ST name/avatar click | View ST profile |
| CDET | Back/cancel | Return to course |
| (Payment) | If session requires payment | Payment flow |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| student_teachers | user_id, course_id, is_active | Available STs |
| users (STs) | name, avatar, timezone | ST display |
| availability | day_of_week, start_time, end_time, timezone | Available slots |
| sessions | scheduled_start, teacher_id | Existing bookings (to exclude) |
| enrollments | student_id, course_id | Verify enrollment |
| courses | title, session_count | Course context |

---

## Sections

### Header
- Page title: "Book a Session"
- Course context: "for [Course Title]"
- Back link → CDET or previous page

### Step 1: Select Student-Teacher (if not pre-selected)
- **ST Cards:**
  - Avatar, name
  - Students taught count
  - Rating (if available)
  - "Select" button
- **Or:** "Schedule Later" option per CD-033
  - Skips ST selection
  - Platform assigns ST when student is ready
  - Goes to "Schedule Later" confirmation

### Step 2: Select Date
- **Calendar View:**
  - Month calendar navigation
  - Days with availability highlighted
  - Past dates disabled
  - Select a date to see times
- **Quick Options:**
  - "Next Available" shortcut
  - "This Week" filter

### Step 3: Select Time
- **Time Slots:**
  - Available slots for selected date
  - Shown in user's timezone
  - Duration indicated (e.g., "60 min")
  - "Select" to choose slot
- **Timezone Note:**
  - "Times shown in [Your Timezone]"
  - Link to change timezone in settings

### Step 4: Confirm Booking
- **Summary:**
  - Course: [Title]
  - Student-Teacher: [Name] + avatar
  - Date: [Full date]
  - Time: [Start] - [End] [Timezone]
  - Duration: [X minutes]
- **Reminders:** Checkbox to enable session reminders
- **Notes field:** Optional message to ST
- **Confirm button:** "Book Session"

### "Schedule Later" Flow (per CD-033)
- Instead of selecting ST/time:
  - Show confirmation: "We'll notify you when you're ready to schedule"
  - "You can schedule anytime from your dashboard"
  - CTA: "Continue to Dashboard"

### Confirmation Screen
- Success message: "Session Booked!"
- Session details
- "Add to Calendar" button (Google, Apple, Outlook)
- "Back to Dashboard" → SDSH
- "Book Another Session"

---

## User Stories Fulfilled

- US-S044: Book session with Student-Teacher
- US-S045: View available time slots
- US-S046: Receive booking confirmation
- US-P006: Platform enables session booking
- US-P020: Calendar-based scheduling
- US-P024: Session reminders
- US-S084: Access ST calendar during enrollment
- US-S085: "Schedule Later" option

---

## States & Variations

| State | Description |
|-------|-------------|
| ST Pre-selected | Skip step 1, show ST info |
| Choose ST | Multiple STs available, show selection |
| No STs Available | "No Student-Teachers available. Try later." |
| Date Selected | Show time slots for that date |
| Slot Selected | Show confirmation |
| Booking | Loading state during booking |
| Success | Confirmation screen |
| Schedule Later | Alternative flow, skips ST/time |

---

## Mobile Considerations

- Wizard-style flow (one step per screen)
- Calendar is swipeable
- Time slots are large touch targets
- Sticky "Confirm" button at bottom

---

## Error Handling

| Error | Display |
|-------|---------|
| Not enrolled | "You must be enrolled to book. [Enroll now]" |
| ST unavailable | "This time is no longer available. Select another." |
| Booking conflict | "You have another session at this time." |
| Booking fails | "Unable to book. Please try again." |

---

## Analytics Events

| Event | Trigger | Data |
|-------|---------|------|
| `page_view` | Page load | course_id, st_preselected |
| `st_selected` | ST chosen | st_id |
| `date_selected` | Date chosen | date |
| `time_selected` | Slot chosen | time, st_id |
| `booking_attempted` | Confirm clicked | course_id, st_id, datetime |
| `booking_success` | Booking confirmed | session_id |
| `booking_failed` | Booking failed | error_type |
| `schedule_later` | Schedule later chosen | course_id |

---

## Notes

- CD-033: "Schedule Later" is key option for flexible enrollment
- Consider buffer time between sessions
- Timezone handling is critical
- Integration with VideoProvider for room creation
- Email confirmation with calendar invite
