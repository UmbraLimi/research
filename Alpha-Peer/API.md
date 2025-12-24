# PeerLoop - API Surface

**Version:** v1
**Last Updated:** 2025-12-23
**Status:** GATHER Phase - Accumulating from source documents
**Primary Source:** CD-021 (Database Schema Sample), User Stories

> This document defines the backend API operations needed to support the application. During RUN phase, scenarios may specify REST vs. GraphQL, specific frameworks, or third-party API integrations.

---

## API Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        PeerLoop API                             │
├─────────────────────────────────────────────────────────────────┤
│  Auth        Users       Courses      Sessions      Payments    │
│  ────        ─────       ───────      ────────      ────────    │
│  login       getUser     getCourses   book          checkout    │
│  signup      updateUser  getCourse    cancel        split       │
│  logout      follow      enroll       join          payout      │
│  refresh     unfollow    progress     record        refund      │
├─────────────────────────────────────────────────────────────────┤
│  Feed        Messages    Certs        Admin         Webhooks    │
│  ────        ────────    ─────        ─────         ────────    │
│  getPosts    getConvs    issue        users         stripe      │
│  createPost  sendMsg     verify       payouts       bbb         │
│  interact    markRead    download     analytics     stream      │
└─────────────────────────────────────────────────────────────────┘
```

---

## Authentication

### POST /auth/signup
Create new user account.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-G011, US-P007 |
| **Access** | Public |
| **Rate Limit** | 5/minute |

**Request:**
```json
{
  "name": "string",
  "email": "string",
  "password": "string",
  "role": "student | creator"
}
```

**Response:** `201 Created`
```json
{
  "user": { "id": "uuid", "name": "string", "email": "string", "role": "string" },
  "token": "jwt_token"
}
```

---

### POST /auth/login
Authenticate user.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-G012, US-P008 |
| **Access** | Public |
| **Rate Limit** | 10/minute |

**Request:**
```json
{
  "email": "string",
  "password": "string"
}
```

**Response:** `200 OK`
```json
{
  "user": { ... },
  "token": "jwt_token",
  "refreshToken": "refresh_token"
}
```

---

### POST /auth/logout
End user session.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-P010 |
| **Access** | Authenticated |

**Response:** `204 No Content`

---

### POST /auth/reset-password
Request password reset.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-G013, US-P009 |
| **Access** | Public |
| **Rate Limit** | 3/hour |

**Request:**
```json
{
  "email": "string"
}
```

**Response:** `200 OK` (always, for security)

---

### POST /auth/refresh
Refresh access token.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-P012 |
| **Access** | Public (with refresh token) |

---

## Users

### GET /users/:id
Get user profile.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-G008, US-G009, US-C008, US-T003 |
| **Access** | Public (respects privacy_public) |
| **Data Source** | users, user_qualifications, user_expertise, user_stats |

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "name": "string",
  "handle": "string",
  "title": "string",
  "avatar_url": "string",
  "bio": "string",
  "website": "string",
  "is_creator": "boolean",
  "is_student_teacher": "boolean",
  "qualifications": [
    { "id": "uuid", "sentence": "string" }
  ],
  "expertise": ["string"],
  "stats": {
    "students_taught": "number",
    "courses_created": "number",
    "average_rating": "number",
    "total_reviews": "number"
  },
  "follower_count": "number",
  "following_count": "number",
  "is_following": "boolean"
}
```

---

### PATCH /users/:id
Update own profile.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S008, US-C008, US-T003 |
| **Access** | Authenticated (own profile only) |

**Request:**
```json
{
  "name": "string",
  "title": "string",
  "bio": "string",
  "bio_short": "string",
  "website": "string",
  "avatar_url": "string",
  "privacy_public": "boolean",
  "is_student_teacher": "boolean"
}
```

---

### POST /users/:id/follow
Follow a user.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S048, US-S028 |
| **Access** | Authenticated |
| **Data Source** | follows |

**Response:** `201 Created`

---

### DELETE /users/:id/follow
Unfollow a user.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S048 |
| **Access** | Authenticated |

**Response:** `204 No Content`

---

### GET /users/:id/followers
Get user's followers.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S049 |
| **Access** | Authenticated |

**Response:** `200 OK`
```json
{
  "followers": [{ "id": "uuid", "name": "string", "avatar_url": "string" }],
  "total": "number",
  "page": "number"
}
```

---

### GET /users/:id/following
Get users this user follows.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S049 |
| **Access** | Authenticated |

---

### GET /student-teachers
List Student-Teachers.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S050, US-S051, US-P066 |
| **Access** | Public or Authenticated |
| **Data Source** | users, student_teachers |

**Query Params:**
- `course_id` - Filter by course (US-S061)
- `search` - Name/interest search
- `page`, `limit` - Pagination

**Response:** `200 OK`
```json
{
  "student_teachers": [
    {
      "user": { ... },
      "courses_certified": [{ "id": "uuid", "title": "string" }],
      "students_taught": "number",
      "certified_date": "date"
    }
  ],
  "total": "number"
}
```

---

### GET /creators
List creators.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S004 |
| **Access** | Public |
| **Data Source** | users (is_creator=true), user_expertise, user_stats |

**Query Params:**
- `search` - Name/expertise search
- `expertise` - Filter by expertise tag
- `page`, `limit`

---

## Courses

### GET /courses
List courses with filtering.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-G005, US-S001, US-S003, US-S057, US-S058 |
| **Access** | Public |
| **Data Source** | courses, categories |

**Query Params:**
- `search` - Title/description search
- `level` - beginner, intermediate, advanced (US-S057)
- `category_id` - Category filter (US-S058)
- `min_price`, `max_price` - Price range
- `creator_id` - Filter by creator
- `sort` - rating, students, price, newest
- `page`, `limit`

**Response:** `200 OK`
```json
{
  "courses": [
    {
      "id": "uuid",
      "title": "string",
      "description": "string",
      "thumbnail_url": "string",
      "level": "string",
      "price_cents": "number",
      "duration": "string",
      "rating": "number",
      "student_count": "number",
      "category": { "id": "uuid", "name": "string" },
      "creator": { "id": "uuid", "name": "string", "avatar_url": "string" }
    }
  ],
  "total": "number",
  "page": "number"
}
```

---

### GET /courses/:id
Get course details.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-G006, US-S005, US-S059, US-S060, US-S061 |
| **Access** | Public |
| **Data Source** | courses, course_curriculum, course_objectives, course_includes, student_teachers |

**Response:** `200 OK`
```json
{
  "id": "uuid",
  "title": "string",
  "description": "string",
  "thumbnail_url": "string",
  "level": "string",
  "price_cents": "number",
  "duration": "string",
  "rating": "number",
  "student_count": "number",
  "creator": { ... },
  "category": { ... },
  "tags": ["string"],
  "learning_objectives": ["string"],
  "includes": ["string"],
  "curriculum": [
    {
      "id": "uuid",
      "title": "string",
      "description": "string",
      "duration": "string",
      "video_count": "number",
      "reading_count": "number",
      "has_assessment": "boolean"
    }
  ],
  "peerloop_features": {
    "one_on_one_teaching": "boolean",
    "certified_teachers": "boolean",
    "earn_while_teaching": "boolean",
    "teacher_commission": "number"
  },
  "student_teachers": [
    {
      "user": { "id": "uuid", "name": "string", "avatar_url": "string" },
      "students_taught": "number",
      "certified_date": "date"
    }
  ],
  "is_enrolled": "boolean",
  "is_following": "boolean"
}
```

---

### POST /courses/:id/follow
Follow a course.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S006 |
| **Access** | Authenticated |
| **Data Source** | course_follows |

---

### DELETE /courses/:id/follow
Unfollow a course.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S006 |
| **Access** | Authenticated |

---

### GET /categories
List course categories.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S058 |
| **Access** | Public |
| **Data Source** | categories |

**Response:** `200 OK`
```json
{
  "categories": [
    { "id": "uuid", "name": "string", "slug": "string", "course_count": "number" }
  ]
}
```

---

## Enrollments

### POST /courses/:id/enroll
Enroll in a course (initiates payment).

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S002, US-S006, US-P026 |
| **Access** | Authenticated |
| **Data Source** | enrollments, transactions |

**Request:**
```json
{
  "student_teacher_id": "uuid (optional)"
}
```

**Response:** `200 OK`
```json
{
  "checkout_url": "stripe_checkout_url",
  "session_id": "stripe_session_id"
}
```

---

### GET /enrollments
Get user's enrollments.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S009, US-P060 |
| **Access** | Authenticated |
| **Data Source** | enrollments, courses, module_progress |

**Response:** `200 OK`
```json
{
  "enrollments": [
    {
      "id": "uuid",
      "course": { ... },
      "status": "string",
      "progress_percent": "number",
      "enrolled_at": "timestamp",
      "student_teacher": { ... },
      "next_session": { ... }
    }
  ]
}
```

---

### GET /enrollments/:id/content
Get course content (enrolled users only).

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S052, US-S053, US-S054 |
| **Access** | Authenticated (enrolled only) |
| **Data Source** | course_curriculum, module_progress |

**Response:** `200 OK`
```json
{
  "course": { ... },
  "modules": [
    {
      "id": "uuid",
      "title": "string",
      "description": "string",
      "video_url": "string",
      "document_url": "string",
      "is_complete": "boolean"
    }
  ]
}
```

---

### PATCH /enrollments/:id/modules/:moduleId
Update module progress.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S055 |
| **Access** | Authenticated (enrolled only) |
| **Data Source** | module_progress |

**Request:**
```json
{
  "is_complete": "boolean"
}
```

---

### DELETE /enrollments/:id
Cancel enrollment.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S015 |
| **Access** | Authenticated (own enrollment) |

**Request:**
```json
{
  "reason": "string"
}
```

---

## Sessions

### GET /availability/:userId
Get teacher availability.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-P020, US-S035 |
| **Access** | Authenticated |
| **Data Source** | availability |

**Query Params:**
- `date` - Specific date
- `start_date`, `end_date` - Date range

**Response:** `200 OK`
```json
{
  "slots": [
    {
      "date": "date",
      "start_time": "time",
      "end_time": "time",
      "is_available": "boolean"
    }
  ],
  "timezone": "string"
}
```

---

### POST /sessions
Book a session.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S044, US-S045, US-P021 |
| **Access** | Authenticated (enrolled students) |
| **Data Source** | sessions, availability |

**Request:**
```json
{
  "enrollment_id": "uuid",
  "teacher_id": "uuid",
  "scheduled_start": "timestamp"
}
```

**Response:** `201 Created`
```json
{
  "session": {
    "id": "uuid",
    "scheduled_start": "timestamp",
    "scheduled_end": "timestamp",
    "bbb_meeting_url": "string"
  }
}
```

**Side Effects:**
- Sends email notification (US-S046)
- Sends in-app notification
- Generates BBB link (US-P065)

---

### GET /sessions
Get user's sessions.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S009 |
| **Access** | Authenticated |
| **Data Source** | sessions |

**Query Params:**
- `status` - scheduled, completed, cancelled
- `role` - student, teacher
- `upcoming` - boolean

---

### PATCH /sessions/:id
Update session (reschedule, cancel).

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S013, US-S014, US-T002 |
| **Access** | Authenticated (participant) |

**Request:**
```json
{
  "scheduled_start": "timestamp (for reschedule)",
  "status": "cancelled",
  "cancel_reason": "string"
}
```

---

### POST /sessions/:id/join
Get join URL for session.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S042 |
| **Access** | Authenticated (participant) |

**Response:** `200 OK`
```json
{
  "join_url": "bbb_join_url"
}
```

---

### POST /sessions/:id/assessment
Submit post-session assessment.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-V006 |
| **Access** | Authenticated (participant) |
| **Data Source** | session_assessments |

**Request:**
```json
{
  "rating": "number (1-5)",
  "comment": "string (optional)"
}
```

---

## Payments

### POST /checkout/create
Create Stripe checkout session.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-P026 |
| **Access** | Authenticated |

**Request:**
```json
{
  "course_id": "uuid"
}
```

**Response:** `200 OK`
```json
{
  "checkout_url": "string",
  "session_id": "string"
}
```

---

### GET /earnings
Get user's earnings.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S012, US-T013, US-T023, US-C035 |
| **Access** | Authenticated (ST or Creator) |
| **Data Source** | payment_splits |

**Response:** `200 OK`
```json
{
  "pending_balance_cents": "number",
  "total_earned_cents": "number",
  "recent_transactions": [
    {
      "id": "uuid",
      "amount_cents": "number",
      "status": "string",
      "course_title": "string",
      "date": "timestamp"
    }
  ]
}
```

---

### GET /payouts
Get payout history.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-T023, US-C035 |
| **Access** | Authenticated (ST or Creator) |
| **Data Source** | payouts |

---

## Certificates

### POST /certificates/recommend
ST recommends student for certification.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-P061 |
| **Access** | Authenticated (Student-Teacher) |

**Request:**
```json
{
  "enrollment_id": "uuid",
  "type": "completion | mastery"
}
```

---

### POST /certificates/issue
Creator issues certificate.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-C014, US-P062 |
| **Access** | Authenticated (Creator) |
| **Data Source** | certificates |

**Request:**
```json
{
  "enrollment_id": "uuid",
  "type": "completion | mastery | teaching"
}
```

---

### GET /certificates
Get user's certificates.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S021, US-S022 |
| **Access** | Authenticated |
| **Data Source** | certificates |

---

## Community Feed

> **Note:** Most feed operations will use getstream.io SDK. These endpoints are for reference or custom functionality.

### GET /feed
Get personalized feed.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S025, US-P002 |
| **Access** | Authenticated |
| **Integration** | getstream.io |

---

### POST /posts
Create a post.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S036, US-T017, US-C031 |
| **Access** | Authenticated |
| **Data Source** | posts (or getstream.io) |

**Request:**
```json
{
  "content": "string",
  "post_type": "post | announcement | teaching_tip | availability",
  "course_id": "uuid (optional)"
}
```

---

### POST /posts/:id/like
Like a post.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S037 |
| **Access** | Authenticated |

---

### POST /posts/:id/bookmark
Bookmark a post.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S038 |
| **Access** | Authenticated |

---

### POST /posts/:id/reply
Reply to a post.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S039 |
| **Access** | Authenticated |

---

### POST /posts/:id/flag
Flag post for moderation.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S041 |
| **Access** | Authenticated |
| **Data Source** | content_flags |

---

### POST /posts/:id/promote
Promote a post to the main Peer Loop feed.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S071, US-P085 |
| **Access** | Authenticated (post author) |
| **Data Source** | promoted_posts, user_goodwill |
| **Source** | CD-024 |

**Request:**
```json
{
  "points_to_spend": "number"
}
```

**Validation:**
- User must have sufficient goodwill balance
- Post must be course-specific (not already in main feed)

**Response:** `201 Created`
```json
{
  "promotion": {
    "id": "uuid",
    "post_id": "uuid",
    "points_spent": "number",
    "expires_at": "timestamp"
  }
}
```

---

### GET /instructors/:id/feed
Get instructor-level feed (for students who have purchased any course from this instructor).

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S070, US-C037 |
| **Access** | Authenticated (users in instructor_followers) |
| **Data Source** | posts (filtered by instructor), instructor_followers |
| **Source** | CD-024 |

**Query Params:**
- `page`, `limit` - Pagination

**Access Control:**
- Checks if user has purchased any course from this instructor
- Returns 403 if not a follower

**Response:** `200 OK`
```json
{
  "instructor": { "id": "uuid", "name": "string", "avatar_url": "string" },
  "posts": [
    {
      "id": "uuid",
      "author": { ... },
      "content": "string",
      "course": { "id": "uuid", "title": "string" },
      "created_at": "timestamp"
    }
  ],
  "total": "number"
}
```

---

### GET /users/:id/instructor-followers
Get list of students who have access to instructor's feed.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-C038 |
| **Access** | Authenticated (instructor viewing own followers) |
| **Data Source** | instructor_followers |
| **Source** | CD-024 |

**Response:** `200 OK`
```json
{
  "followers": [
    {
      "user": { "id": "uuid", "name": "string", "avatar_url": "string" },
      "first_enrollment_at": "timestamp",
      "courses_enrolled": ["string"]
    }
  ],
  "total": "number"
}
```

---

### GET /feed/access
Get user's feed access levels.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S069, US-P083 |
| **Access** | Authenticated |
| **Data Source** | enrollments, instructor_followers |
| **Source** | CD-024 |

**Response:** `200 OK`
```json
{
  "course_feeds": [
    { "course_id": "uuid", "course_title": "string" }
  ],
  "instructor_feeds": [
    { "instructor_id": "uuid", "instructor_name": "string" }
  ],
  "main_feed": true
}
```

---

## Messages

### GET /conversations
Get user's conversations.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-P004, US-S019 |
| **Access** | Authenticated |
| **Data Source** | conversations, conversation_participants, messages |

---

### POST /conversations
Create new conversation.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S016, US-S018, US-T008 |
| **Access** | Authenticated |

**Request:**
```json
{
  "participant_ids": ["uuid"]
}
```

---

### GET /conversations/:id/messages
Get messages in conversation.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S019 |
| **Access** | Authenticated (participant) |
| **Data Source** | messages |

---

### POST /conversations/:id/messages
Send message.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S016, US-T008 |
| **Access** | Authenticated (participant) |

**Request:**
```json
{
  "content": "string"
}
```

---

## Admin

### GET /admin/pending-payouts
Get pending payouts.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-A026 |
| **Access** | Authenticated (Admin) |
| **Data Source** | payment_splits |

---

### POST /admin/payouts/:id/process
Process a payout.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-A027 |
| **Access** | Authenticated (Admin) |
| **Data Source** | payouts |

---

### POST /admin/payouts/batch
Process all pending payouts.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-A028 |
| **Access** | Authenticated (Admin) |

---

### GET /admin/analytics
Get platform analytics.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-A019-A025 |
| **Access** | Authenticated (Admin) |

**Response includes:**
- User retention (US-A019)
- Course stats (US-A020)
- Revenue tracking (US-A021)
- Session status (US-A022)
- Conversion rates (US-A023)
- Grade averages (US-A024)

---

## Webhooks (Incoming)

### POST /webhooks/stripe
Stripe payment webhooks.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-P026, US-P028 |
| **Sender** | Stripe |

**Events handled:**
- `checkout.session.completed` - Enrollment confirmed
- `payment_intent.succeeded` - Payment successful
- `charge.refunded` - Refund processed

---

### POST /webhooks/bbb
BigBlueButton session webhooks.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-A018, US-V005 |
| **Sender** | BBB/Blindside Networks |

**Events handled:**
- `meeting-ended` - Session completed
- `recording-ready` - Recording available

---

## Goodwill Points (Block 2+)

*Note: Not MVP - Goodwill points are a community currency replacing 5-star reviews.*

### POST /summons
Create a help summon request.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S062 |
| **Access** | Authenticated (enrolled students) |
| **Data Source** | help_summons |

**Request:**
```json
{
  "course_id": "uuid",
  "module_id": "uuid (optional)"
}
```

**Response:** `201 Created`
```json
{
  "summon": {
    "id": "uuid",
    "status": "pending",
    "available_helpers": 3
  }
}
```

---

### GET /summons/active
Get active summon requests for available S-Ts.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-T025 |
| **Access** | Authenticated (S-Ts with availability on) |
| **Data Source** | help_summons |

**Response:** `200 OK`
```json
{
  "summons": [
    {
      "id": "uuid",
      "student": { "id": "uuid", "name": "string", "avatar_url": "string" },
      "course": { "id": "uuid", "title": "string" },
      "module_title": "string",
      "created_at": "timestamp"
    }
  ]
}
```

---

### POST /summons/:id/respond
Respond to a summon request.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-T026 |
| **Access** | Authenticated (certified S-T for that course) |
| **Data Source** | help_summons |

**Response:** `200 OK`
```json
{
  "summon": {
    "id": "uuid",
    "status": "responded",
    "chat_url": "string"
  }
}
```

---

### POST /summons/:id/complete
Complete a summon and award points.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S064, US-T027 |
| **Access** | Authenticated (student who created summon) |
| **Data Source** | help_summons, goodwill_transactions |

**Request:**
```json
{
  "points": 15
}
```

**Validation:**
- Points must be 10-25
- Session must be 5+ minutes

**Response:** `200 OK`
```json
{
  "summon": { "status": "completed", "points_awarded": 15 },
  "helper_new_total": 862
}
```

---

### GET /goodwill/balance
Get own goodwill balance.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S067 |
| **Access** | Authenticated |
| **Data Source** | user_goodwill |

**Response:** `200 OK`
```json
{
  "total_earned": 847,
  "spent": 120,
  "balance": 727,
  "breakdown": {
    "summons_helped": 12,
    "questions_answered": 45,
    "referrals": 2
  }
}
```

---

### GET /goodwill/transactions
Get goodwill transaction history.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S067 |
| **Access** | Authenticated |
| **Data Source** | goodwill_transactions |

**Query Params:**
- `type` - earned, spent
- `page`, `limit`

**Response:** `200 OK`
```json
{
  "transactions": [
    {
      "id": "uuid",
      "type": "earned",
      "points": 15,
      "reason": "summon_help",
      "from_user": { "name": "string" },
      "course_title": "string",
      "created_at": "timestamp"
    }
  ]
}
```

---

### POST /goodwill/award
Award points to a user (for chat answers).

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S066 |
| **Access** | Authenticated |
| **Data Source** | goodwill_transactions, user_goodwill |

**Request:**
```json
{
  "to_user_id": "uuid",
  "points": 5,
  "reason": "question_answer",
  "message_id": "uuid"
}
```

**Validation:**
- Max 3 awards per day to same person
- Cooldown between awards

**Response:** `201 Created`

---

### PATCH /users/:id/availability
Update "Available to Help" status.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-T024 |
| **Access** | Authenticated (own profile, S-Ts only) |
| **Data Source** | user_availability |

**Request:**
```json
{
  "is_available": true
}
```

**Response:** `200 OK`

---

### GET /courses/:id/available-helpers
Get count of available helpers for a course.

| Attribute | Value |
|-----------|-------|
| **User Stories** | US-S063, US-P080 |
| **Access** | Authenticated (enrolled students) |
| **Data Source** | user_availability, student_teachers |

**Response:** `200 OK`
```json
{
  "available_count": 3,
  "helpers": [
    { "id": "uuid", "name": "string", "avatar_url": "string" }
  ]
}
```

---

## API Summary

| Category | Endpoints |
|----------|-----------|
| Authentication | 5 |
| Users | 9 |
| Courses | 5 |
| Enrollments | 5 |
| Sessions | 6 |
| Payments | 3 |
| Certificates | 3 |
| Feed | 10 |
| Messages | 4 |
| Admin | 4 |
| Webhooks | 2 |
| Goodwill | 9 |
| **Total** | **65** |

---

## Document Lineage

| Source Document | Endpoints Derived |
|-----------------|-------------------|
| CD-021 | Course detail structure, user profile structure, ST listing |
| US-P007-P013 | Authentication endpoints |
| US-S057-S061, CD-021 | Course filtering, objectives, includes, per-course STs |
| CD-015 | Session booking, availability |
| CD-020 | Payment/payout endpoints |
| CD-013 | Feed endpoints |
| CD-018 | Follow endpoints, profile updates |
| CD-023 | Summons CRUD, goodwill points, availability toggle, available helpers |
| CD-024 | Instructor feed, post promotion, feed access levels, instructor followers |

---

## Notes for Implementation

1. **REST vs GraphQL:** Default assumption is REST; RUN phase may specify GraphQL
2. **Authentication:** JWT-based, refresh token rotation
3. **Rate Limiting:** Apply per endpoint based on abuse potential
4. **Pagination:** Cursor-based preferred for scalability
5. **Versioning:** Consider /v1/ prefix for future compatibility
6. **getstream.io:** Feed operations may use Stream SDK directly instead of API
7. **BBB API:** Session creation integrates with Blindside Networks API

---

## API Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2025-12-23 | Initial API surface from user stories and CD-021 |
