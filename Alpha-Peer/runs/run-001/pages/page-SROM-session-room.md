# Page: Session Room

**Code:** SROM
**URL:** `/session/:id`
**Access:** Authenticated (session participants only)
**Priority:** P0
**Status:** In Scope

---

## Purpose

Video conferencing interface for 1-on-1 tutoring sessions between students and Student-Teachers, powered by VideoProvider (BBB or PlugNmeet).

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| SDSH | "Join Session" button | Student joining |
| TDSH | "Join Session" button | ST joining |
| NOTF | Session reminder notification | Direct join |
| (Email) | Email reminder link | Direct join |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| SDSH | "Back to Dashboard" / session ends (Student) | Return to dashboard |
| TDSH | "Back to Dashboard" / session ends (ST) | Return to dashboard |
| CCNT | "Back to Course" | Return to course content |
| (Feedback) | Session ends | Post-session feedback modal |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| sessions | id, scheduled_start, scheduled_end, bbb_meeting_url, status | Session info |
| users (student) | name, avatar | Participant display |
| users (teacher) | name, avatar | Participant display |
| courses | title | Context display |
| enrollments | course_id | Course context |

---

## Sections

### Pre-Join Screen (Before Video Starts)
- **Session Info:**
  - Course title
  - Participant: [Other person's name + avatar]
  - Scheduled time
  - Duration
- **Device Check:**
  - Camera preview
  - Microphone indicator
  - Speaker test
- **Ready Actions:**
  - "Join Session" button → enters video room
  - "Test Audio/Video" link
- **Tips:**
  - "Ensure good lighting"
  - "Use headphones for best audio"

### Video Room (Main Session)
*Implemented via VideoProvider iframe/SDK*

- **Video Area:**
  - Main video feed (active speaker)
  - Self-view (small, corner)
  - Participant video
- **Controls Bar:**
  - Mute/unmute microphone
  - Enable/disable camera
  - Screen share
  - Chat toggle
  - Settings (audio/video devices)
  - Leave session button
- **Side Panel (Optional):**
  - Text chat
  - Session notes
  - Resource links
- **Session Timer:**
  - Time elapsed
  - Scheduled end time

### Session Header
- Course title
- Participant name
- Session status indicator

### Post-Session Screen
- "Session Ended"
- **Quick Feedback:**
  - Rating: 1-5 stars
  - Optional comment
  - Submit button
- **Actions:**
  - "Back to Dashboard" → SDSH/TDSH
  - "Book Next Session" → SBOK
  - "View Course Content" → CCNT
- **Recording Access (if enabled):**
  - "Recording will be available shortly"
  - Link when ready

---

## User Stories Fulfilled

- US-S042: Join scheduled session
- US-S043: Participate in video session
- US-V001: Access video conferencing
- US-V005: Access session recordings (if enabled)
- US-V006: Rate session after completion
- US-T007: ST conducts teaching session

---

## States & Variations

| State | Description |
|-------|-------------|
| Early | Session not yet joinable (>15 min before) |
| Joinable | Within join window, pre-join screen |
| In Progress | Active video session |
| Waiting | One participant waiting for other |
| Ended | Post-session feedback screen |
| No Show | Other participant didn't join |
| Technical Issues | Connection problems, retry options |

---

## Mobile Considerations

- Full-screen video by default
- Controls at bottom, auto-hide
- Portrait: stacked videos
- Landscape: side-by-side
- Minimize to picture-in-picture

---

## Error Handling

| Error | Display |
|-------|---------|
| Session not found | "Session not found. Check your dashboard." |
| Not authorized | "You're not part of this session." |
| Session expired | "This session has ended." |
| Connection failed | "Unable to connect. [Retry]" |
| Camera/mic denied | "Please allow camera/microphone access." |
| Video provider error | "Video service unavailable. Try again." |

---

## Analytics Events

| Event | Trigger | Data |
|-------|---------|------|
| `page_view` | Page load | session_id, user_role |
| `session_joined` | Entered video room | session_id, time_before_start |
| `session_started` | Both participants present | session_id |
| `session_ended` | Session concluded | session_id, duration |
| `feedback_submitted` | Rating submitted | session_id, rating |
| `tech_issue` | Connection problem | error_type |

---

## Notes

- **VideoProvider abstraction:** BBB or PlugNmeet (see API.md)
- CD-007: 1-on-1 optimized, P2P when possible
- Recording storage: R2 or video provider cloud
- Session reminders: 24h, 1h, 15min before
- Consider "reschedule" option from pre-join if issues
- Accessibility: Keyboard navigation, screen reader support for controls
