# Page: Course Content

**Code:** CCNT
**URL:** `/learn/:course_id`
**Access:** Authenticated (enrolled students only)
**Priority:** P0
**Status:** In Scope

---

## Purpose

Deliver course content to enrolled students, track module progress, enable self-paced learning, and provide access to resources and help features.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| SDSH | "Continue Learning" | From dashboard |
| CDET | "Start Learning" (enrolled) | From course detail |
| SROM | "Back to Course" | After session |
| NOTF | Course update notification | Content updates |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| SBOK | "Schedule Session" | Book tutoring session |
| SROM | "Join Session" (if imminent) | Active session |
| SDSH | "Dashboard" / back | Return to dashboard |
| CDET | "Course Info" | View course details |
| CHAT | "Course Chat" (Block 2+) | Course community chat |
| HELP | "Summon Help" button (Block 2+) | Request help from ST |
| STPR | ST name in "Your Teacher" | View assigned ST |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| courses | id, title, slug | Course context |
| course_curriculum | id, title, description, duration, video_url, document_url, module_order, session_number | Content display |
| module_progress | enrollment_id, module_id, is_complete | Progress tracking |
| enrollments | id, student_teacher_id | Enrollment status |
| sessions | scheduled_start | Upcoming session reminder |
| users (ST) | name, avatar | Assigned teacher |
| user_availability | is_available | Helpers online (Block 2+) |

---

## Sections

### Header Bar
- Course title
- Progress bar (% complete)
- "Dashboard" link → SDSH
- "Schedule Session" → SBOK

### Sidebar / Navigation Panel
- **Module List:**
  - All modules in order
  - Completion checkboxes
  - Current module highlighted
  - Session grouping (if applicable)
  - Progress indicators
- **Your Teacher:**
  - Assigned ST avatar + name
  - "Message" button → MSGS
  - Next session reminder (if scheduled)
- **Quick Actions:**
  - "Schedule Session" → SBOK
  - "Course Info" → CDET

### Content Area
- **Module Header:**
  - Module title
  - Duration
  - Session number (if grouped)
- **Learning Objectives:**
  - What you'll learn in this module
- **Video Player (if video_url):**
  - Embedded video (YouTube/Vimeo)
  - Playback controls
  - Speed adjustment
- **Document Link (if document_url):**
  - Link to external doc (Google Docs, Notion)
  - Opens in new tab
- **Module Content:**
  - Description text
  - Topics covered
  - Hands-on exercise description
- **Mark Complete:**
  - Checkbox: "I've completed this module"
  - Progress updates on check
- **Navigation:**
  - "Previous Module" / "Next Module" buttons

### Summon Help Button (Block 2+)
- Floating button: "Summon Help"
- Shows online helpers count: "3 available"
- Opens HELP modal when clicked
- Source: CD-023

### Progress Summary (Bottom/Footer)
- Overall progress: X of Y modules complete
- "Continue to Next Module" or "You've completed all modules!"
- Certificate prompt when done

---

## User Stories Fulfilled

- US-S052: Access enrolled course content
- US-S053: View course materials (videos, docs)
- US-S054: Track module progress
- US-S055: Mark modules complete
- US-S056: Navigate between modules
- US-S062: Access "Summon Help" feature (Block 2+)
- US-S063: See helpers available (Block 2+)

---

## States & Variations

| State | Description |
|-------|-------------|
| In Progress | Modules partially complete, current highlighted |
| Not Started | First visit, start at module 1 |
| Complete | All modules done, certificate prompt |
| Module View | Viewing specific module content |
| Video Playing | Video player active |
| Session Imminent | "Join Session" banner if within 15 min |

---

## Mobile Considerations

- Sidebar becomes bottom sheet or hamburger menu
- Video player full-width
- Mark complete is prominent
- Module navigation via swipe or buttons
- Floating Summon Help accessible

---

## Error Handling

| Error | Display |
|-------|---------|
| Not enrolled | "You must be enrolled. [Enroll now]" → CDET |
| Content load fails | "Unable to load content. [Retry]" |
| Video fails | "Video unavailable. Try external link." |
| Progress save fails | "Unable to save progress. Trying again..." |

---

## Analytics Events

| Event | Trigger | Data |
|-------|---------|------|
| `page_view` | Page load | course_id, module_id |
| `module_viewed` | Module accessed | module_id, time_spent |
| `module_completed` | Marked complete | module_id |
| `video_played` | Video started | module_id, video_url |
| `video_completed` | Video watched >90% | module_id |
| `summon_help_clicked` | Summon clicked | module_id, helpers_count |
| `session_scheduled` | Schedule clicked | course_id |

---

## API Calls

| Endpoint | When | Purpose |
|----------|------|---------|
| `GET /api/courses/:course_id` | Page load | Course info |
| `GET /api/courses/:course_id/curriculum` | Page load | All modules |
| `GET /api/enrollments?course_id=:course_id` | Page load | Enrollment + ST info |
| `GET /api/enrollments/:enrollment_id/progress` | Page load | Module progress |
| `POST /api/enrollments/:enrollment_id/progress` | Mark complete | Update module progress |
| `GET /api/sessions?course_id=:course_id&upcoming=true&limit=1` | Page load | Next session reminder |
| `GET /api/helpers/available?course_id=:course_id` | Page load (Block 2+) | Available helper count |

**Curriculum Response:**
```typescript
GET /api/courses/:course_id/curriculum
{
  modules: [{
    id, title, description, duration,
    video_url, document_url,
    module_order, session_number
  }]
}
```

**Progress Update:**
```typescript
POST /api/enrollments/:enrollment_id/progress
{
  module_id: string,
  is_complete: boolean
}
// Returns updated progress summary
```

**Progress Response:**
```typescript
GET /api/enrollments/:enrollment_id/progress
{
  modules: [{ module_id, is_complete }],
  summary: { completed: number, total: number, percent: number }
}
```

---

## Notes

- CD-019: External LMS content (videos/docs hosted externally)
- Progress is self-reported (checkbox model)
- Consider video progress tracking (pause/resume points)
- Certificate prompt when all modules complete
- Block 2+: Summon Help is goodwill-based feature
