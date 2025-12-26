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

## Server Integration

### API Endpoints Called

| Endpoint | When | Purpose |
|----------|------|---------|
| `GET /api/instructors/:id/feed/access` | Page load | Verify user has access |
| `POST /api/stream/token` | After access verified | Get Stream token with instructor feed |
| `POST /api/posts` | Create post | Store + publish to instructor feed |
| `POST /api/posts/:id/promote` | Promote post | Use points to boost to main feed |

### Access Control (Server-Side Gating)

```typescript
// Page load flow:
1. GET /api/instructors/:handle/feed/access
2. Backend checks instructor_followers table:
   SELECT 1 FROM instructor_followers
   WHERE instructor_id = :instructor_id
     AND follower_id = :current_user_id

3. If no record → 403: "Enroll in a course to access"
4. If record exists → 200: { has_access: true, instructor: {...} }

// Access is granted when:
INSERT INTO instructor_followers (instructor_id, follower_id)
VALUES (:instructor_id, :user_id)
ON enrollment in any course where course.creator_id = :instructor_id

// Access persists even after:
- Course completion
- All courses refunded (?)
- Instructor creates new courses
```

### Stream Token with Instructor Feed

```typescript
// POST /api/stream/token (for IFED context)
{
  requested_feeds: ['instructor:456']
}

// Backend:
1. Verify user has access (instructor_followers check)
2. Generate token with instructor feed permission:

const token = streamClient.createUserToken(user.id, {
  extra_data: {
    allowed_feeds: ['instructor:456', 'user:*', 'townhall:main']
  }
});

// Response:
{
  token: "eyJ...",
  user_id: "user_123",
  api_key: "xxx...",
  feed_id: "instructor:456"
}
```

### Feed Connection Flow

```javascript
// Client connects to instructor-specific feed:
const client = stream.connect(api_key, token, app_id);
const instructorFeed = client.feed('instructor', instructor_id);

// Get activities:
const activities = await instructorFeed.get({
  limit: 25,
  reactions: { own: true, counts: true }
});

// Subscribe to real-time:
instructorFeed.subscribe((data) => {
  if (data.new) updateFeed(data.new);
});

// Optional: Filter by course
const filtered = await instructorFeed.get({
  limit: 25,
  filter: { course_id: 'course_123' }
});
```

### Post to Instructor Feed

```
Create Post in Instructor Feed:
  1. POST /api/posts {
       content: "...",
       feed_type: "instructor",
       feed_id: instructor_id,
       course_id: "optional_course_123"  // Tag with course
     }
  2. Backend validates:
     - User is instructor OR enrolled student
     - If course_id: user enrolled in that course
  3. Store in posts table
  4. Publish to Stream:
     instructorFeed.addActivity({
       actor: user_id,
       verb: 'post',
       object: `post:${post.id}`,
       course: course_id || null,
       foreign_id: `post:${post.id}`
     })
```

### Post Promotion Flow (Goodwill Points)

```
Promote Post to Main Feed:
  1. User clicks "Promote" on their post
  2. Show cost (e.g., 50 goodwill points)
  3. POST /api/posts/:id/promote {
       points_to_spend: 50
     }
  4. Backend:
     - Validates user owns post
     - Validates user has sufficient points
     - Deducts points from user.goodwill_points
     - Records in promoted_posts table
     - Copies activity to townhall feed:
       townhallFeed.addActivity({
         actor: user_id,
         verb: 'promoted',
         object: `post:${post.id}`,
         promoted_from: 'instructor',
         points_spent: 50
       })
  5. Post appears in main community feed (FEED)
```

### Data Flow Diagram

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   IFED      │      │  PeerLoop   │      │  Stream.io  │
│   (Client)  │      │  (Server)   │      │  (Service)  │
└──────┬──────┘      └──────┬──────┘      └──────┬──────┘
       │                    │                    │
       │ GET /instructors/  │                    │
       │   :id/feed/access  │                    │
       │───────────────────>│                    │
       │                    │ Check followers    │
       │ { has_access }     │                    │
       │<───────────────────│                    │
       │                    │                    │
       │ POST /stream/token │                    │
       │ { feeds: [inst:X] }│                    │
       │───────────────────>│                    │
       │                    │ Validate access    │
       │                    │ Generate token     │
       │ { token }          │                    │
       │<───────────────────│                    │
       │                    │                    │
       │ Connect to instructor:X feed            │
       │─────────────────────────────────────────>
       │                    │                    │
       │ Subscribe                               │
       │─────────────────────────────────────────>
       │ (WebSocket)                             │
       │<─────────────────────────────────────────
```

### Instructor Followers Table

```sql
-- Created on first enrollment with instructor's course
instructor_followers (
  instructor_id  -- references users(id) where role = 'creator'
  follower_id    -- references users(id)
  created_at
  PRIMARY KEY (instructor_id, follower_id)
)

-- Populated by:
CREATE TRIGGER on_enrollment_insert:
  IF NOT EXISTS follower record:
    INSERT INTO instructor_followers
    VALUES (course.creator_id, enrollment.user_id, NOW())
```

---

## Notes

- CD-024: Instructor feed access granted on first enrollment
- Access persists indefinitely (perpetual community access)
- Promotion uses goodwill points (Block 2+ feature)
- Consider notification settings for instructor feed
- Uses Stream.io `instructor` feed group
- Token permissions scoped to specific instructor feed
- Course filtering via Stream activity metadata
