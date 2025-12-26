# Page: Instructor Feed

**Code:** IFED
**URL:** `/@:handle/feed` or `/instructors/:handle/feed`
**Access:** Authenticated (users who have purchased any course from this instructor)
**Priority:** P1
**Status:** In Scope

---

## Purpose

Exclusive feed for current and former students of an instructor, showing posts across all of that instructor's courses and enabling deeper community engagement.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| CPRO | "View Feed" link | From creator profile |
| SDSH | Instructor feed link | Dashboard quick access |
| NOTF | Notification about instructor post | Direct to feed |
| CDET | "Instructor Feed" link | From course detail |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| CPRO | Instructor name/avatar click | View instructor profile |
| CDET | Course mention click | View course |
| PROF | Other student name click | View their profile |
| FEED | "Main Feed" nav | Return to main community feed |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| users (instructor) | id, name, avatar, handle | Instructor info |
| instructor_followers | instructor_id, follower_id | Access control |
| posts | id, author_id, course_id, content, created_at | Feed content |
| courses | id, title (where creator_id = instructor) | Course context |
| post_interactions | post_id, type, count | Engagement |
| promoted_posts | post_id, points_spent | Promoted content |

---

## Sections

### Header
- Instructor avatar + name
- "@[handle]'s Feed"
- Follower count (students in this feed)
- "Back to Profile" → CPRO

### Feed Content
- Posts from:
  - The instructor directly
  - Any course by this instructor
  - Students in instructor's courses (with course context)
- Each post shows:
  - Author avatar + name
  - Course tag (if course-specific)
  - Content
  - Timestamp
  - Engagement bar (like, reply, repost, bookmark)
  - Promoted badge (if promoted from course feed)

### Post Composer
- Only visible to authorized users
- Text input
- Course selector: "Post to [Course] or General"
- "Promote to Main Feed" option:
  - Uses goodwill points
  - Shows point cost
- Post button

### Sidebar (Desktop)
- **Instructor Info:**
  - Mini profile card
  - Courses list
  - "View Full Profile" → CPRO
- **Course Filter:**
  - Show posts from specific course
  - "All Courses" default
- **Active Students:**
  - Who's online in this community
- **Promote Feature:**
  - "Boost your post to main feed"
  - Points cost info

---

## User Stories Fulfilled

- US-S070: Access instructor-specific feed
- US-C037: Creator has dedicated feed for students
- US-C038: Creator posts reach their students
- US-P084: Track instructor followers for feed access
- US-P085: Support post promotion with points

---

## States & Variations

| State | Description |
|-------|-------------|
| Active | Posts flowing from instructor and students |
| Quiet | Few posts, "Be the first to post" prompt |
| Filtered | Viewing posts from specific course |
| Promoting | User is promoting a post |
| No Access | Not enrolled, "Enroll to access" |

---

## Mobile Considerations

- Feed is main view
- Sidebar becomes tabs or bottom sheet
- Instructor header is collapsible
- Promote option in post composer

---

## Error Handling

| Error | Display |
|-------|---------|
| No access | "Enroll in one of [Name]'s courses to access this feed." |
| Post fails | "Unable to post. Try again." |
| Promote fails | "Unable to promote. Try again." |
| Load fails | "Unable to load feed. [Retry]" |

---

## Analytics Events

| Event | Trigger | Data |
|-------|---------|------|
| `page_view` | Page load | instructor_id |
| `post_created` | Post submitted | instructor_id, course_id |
| `post_promoted` | Promoted to main feed | post_id, points_spent |
| `post_liked` | Like clicked | post_id |
| `course_filtered` | Filter applied | course_id |

---

## Access Control Logic

```
User can access IFED for instructor X if:
  EXISTS in instructor_followers
  WHERE instructor_id = X AND follower_id = current_user

instructor_followers created when:
  User enrolls in any course where course.creator_id = X

Access persists even after:
  - Course completion
  - Course refund (?)
  - Instructor creates new courses
```

---

## Notes

- CD-024: Instructor feed access granted on first enrollment
- Access persists indefinitely (perpetual community access)
- Promotion uses goodwill points (Block 2+ but feed access is P1)
- Consider notification settings for instructor feed
- May use Stream.io feed groups
