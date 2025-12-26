# Page: Community Feed

**Code:** FEED
**URL:** `/community` or `/feed`
**Access:** Authenticated
**Priority:** P0
**Status:** In Scope

---

## Purpose

X.com-style algorithmic feed showing posts from followed users, courses, and creators, enabling community engagement and content discovery.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| Nav | "Community" / "Feed" link | Global navigation |
| SDSH | "Community" quick action | From dashboard |
| NOTF | Notification about post | Direct to specific post |
| (External) | Direct URL | `/community` |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| PROF | Author name/avatar click | View poster's profile |
| CDET | Course mention click | View mentioned course |
| CPRO | Creator mention click | View creator profile |
| IFED | "View [Creator] Feed" | Instructor-specific feed |
| (Post Detail) | Post click | Expand post with replies |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| posts | id, author_id, content, post_type, created_at, is_pinned | Feed content |
| users | id, name, avatar, handle | Author display |
| follows | follower_id, followed_id | Who user follows |
| course_follows | user_id, course_id | Course subscriptions |
| post_interactions | post_id, type, count | Like/bookmark counts |
| (Stream API) | feed data | External feed service |

**Note:** Feed is powered by Stream.io (per CD-008, tech-002)

---

## Sections

### Header
- Page title: "Community" or "Your Feed"
- Feed type tabs (optional): "For You" / "Following" / "Courses"

### Post Composer
- Avatar of current user
- Text input: "What's on your mind?"
- Post type selector (optional):
  - General post
  - Question (Q&A)
  - Teaching tip
  - Availability update
- Media attachment (future)
- "Post" button

### Feed
- Infinite scroll of posts
- Each post shows:
  - Author avatar, name, handle, timestamp
  - Post content (text, mentions, links)
  - Post type badge if applicable
  - Engagement bar:
    - Like button + count
    - Reply button + count
    - Repost button + count
    - Bookmark button
    - Share button
  - Reply thread preview (if replies)
- Pinned posts at top (from moderators)

### Sidebar (Desktop)
- **Suggested Follows:**
  - Users/creators to follow
  - Based on interests/courses
- **Trending Topics:**
  - Popular hashtags or themes
- **Upcoming Sessions:**
  - Next scheduled session reminder
- **Who to Follow:**
  - STs from enrolled courses

### Empty State
- New user with no follows: "Follow some creators to see posts here"
- Suggestions for who to follow

---

## User Stories Fulfilled

- US-S025: Access community feed
- US-P002: Platform provides community feed
- US-S036: View posts in algorithmic order
- US-S037: Like posts
- US-S038: Bookmark posts
- US-S039: Reply to posts
- US-S040: Repost content
- US-S041: Flag inappropriate content

---

## States & Variations

| State | Description |
|-------|-------------|
| Default | Algorithmic feed of followed content |
| Empty | No follows, show suggestions |
| Filtered | Viewing specific category (courses, following) |
| Composing | Post composer expanded |
| Loading | Skeleton posts while fetching |

---

## Mobile Considerations

- Full-width post cards
- Floating compose button (FAB)
- Hide sidebar, move to bottom sheet
- Pull-to-refresh
- Infinite scroll with loading indicator

---

## Error Handling

| Error | Display |
|-------|---------|
| Feed load fails | "Unable to load feed. [Retry]" |
| Post fails | "Unable to post. Please try again." |
| Like/action fails | Toast: "Action failed. Try again." |

---

## Analytics Events

| Event | Trigger | Data |
|-------|---------|------|
| `page_view` | Page load | feed_type |
| `post_created` | Post submitted | post_type, has_media |
| `post_liked` | Like clicked | post_id |
| `post_bookmarked` | Bookmark clicked | post_id |
| `post_replied` | Reply submitted | post_id |
| `post_reposted` | Repost clicked | post_id |
| `post_flagged` | Flag submitted | post_id, reason |
| `profile_clicked` | Author clicked | user_id |

---

## Notes

- **Stream.io integration:** Feed infrastructure via GetStream (CD-008)
- CD-013: 5 feed types documented in tech-002-stream.md
- Consider "Mute" feature for noisy users
- Moderation: Flagged posts go to MODQ
- Real-time updates via Stream's real-time infrastructure
