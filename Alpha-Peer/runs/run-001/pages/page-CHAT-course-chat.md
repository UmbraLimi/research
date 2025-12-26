# Page: Course Chat

**Code:** CHAT
**URL:** `/courses/:id/chat`
**Access:** Authenticated (enrolled students and certified STs)
**Priority:** P2 (Block 2+)
**Status:** In Scope (Goodwill Points Feature)

---

## Purpose

Course-specific community chat room where enrolled students can ask questions, get help from STs, and award goodwill points for helpful answers.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| CCNT | "Course Chat" link | From course content |
| CDET | "Join Discussion" | From course detail |
| NOTF | Chat notification | New message/mention |
| SDSH | Course chat icon | Quick access |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| CCNT | "Back to Course" | Return to content |
| STPR | ST name click | View helper's profile |
| PROF | User name click | View user's profile |
| HELP | "Need 1-on-1 Help?" | Escalate to Summon |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| posts | id, author_id, course_id, content, created_at | Chat messages |
| users | id, name, avatar, is_student_teacher | Participant info |
| student_teachers | course_id, user_id | ST badge display |
| user_goodwill | balance | Points available to award |
| goodwill_transactions | from_user_id, to_user_id, points, reason | Awards |
| courses | id, title | Course context |

---

## Sections

### Header
- Course title + "Chat"
- Participants count: "X online"
- "Back to Course" → CCNT
- Room settings (mute, etc.)

### Chat Messages (Main Area)
- Real-time message stream
- Each message shows:
  - Author avatar + name
  - ST badge (if certified for this course)
  - Timestamp
  - Message content
  - **Action buttons:**
    - "Mark as Question" (on own messages)
    - "This Helped!" (on others' answers)
- Question messages highlighted differently
- Answers to questions indented/grouped

### Help Queue Panel (Sidebar or Tab)
- **Pending Questions:**
  - Questions awaiting answers
  - Ordered by time asked
  - Quick link to question in chat
- **Available Helpers:**
  - STs currently online
  - "Available to Help" status
  - Avatar + name

### Message Composer
- Text input
- "Ask Question" toggle (marks as question)
- Send button
- Character limit indicator

### "This Helped!" Interaction
- On clicking "This Helped!":
  - Opens slider: 5 points (default)
  - Note: "Award points for helpful answer"
  - Confirm button
  - Points deducted from giver's balance
  - Points added to helper's total

### Goodwill Points Indicator
- User's available balance shown
- "X points to give"
- Link to earn more

---

## User Stories Fulfilled

- US-S065: Participate in course chat
- US-S066: Ask questions in chat
- US-T028: ST answers questions in chat
- US-S069: Award points for helpful answers (from CD-023)

---

## States & Variations

| State | Description |
|-------|-------------|
| Active | Messages flowing, users online |
| Quiet | No recent messages, "Start the conversation" prompt |
| Question Pending | User's question awaiting answer |
| Helping | ST actively answering questions |
| Low Balance | User has few points to award, subtle prompt to help others |

---

## Mobile Considerations

- Full-screen chat
- Help queue accessed via tab or swipe
- Composer sticky at bottom
- Quick point award via long-press

---

## Error Handling

| Error | Display |
|-------|---------|
| Not authorized | "You must be enrolled to access this chat." |
| Send fails | "Message not sent. [Retry]" |
| Award fails | "Unable to award points. Try again." |
| Connection lost | "Reconnecting..." with retry |

---

## Analytics Events

| Event | Trigger | Data |
|-------|---------|------|
| `page_view` | Page load | course_id, user_role |
| `message_sent` | Message sent | course_id, is_question |
| `question_asked` | Question marked | course_id |
| `points_awarded` | "This Helped" completed | points, recipient_id |
| `helper_online` | ST came online | st_id, course_id |

---

## Notes

- **Block 2+ feature:** Part of Goodwill Points system (CD-023)
- May use Stream Chat or similar real-time service
- Consider anti-spam: rate limits, moderation
- ST incentive: Earning points for helping
- Integration with MODQ for flagged content
