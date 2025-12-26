# Page: Notifications

**Code:** NOTF
**URL:** `/notifications`
**Access:** Authenticated
**Priority:** P0
**Status:** In Scope

---

## Purpose

Display all user notifications in one place, allowing users to view, mark as read, and act on notifications.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| Nav | Notification bell icon | Global navigation |
| Any page | Bell with badge | Unread indicator |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| SROM | Session notification click | Join upcoming session |
| MSGS | Message notification click | View message thread |
| SDSH/TDSH/CDSH | Approval notification click | View pending items |
| CDET | Course notification click | View course |
| PROF | Follower notification click | View who followed |
| SETT | "Notification Settings" | Manage preferences |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| notifications | id, type, title, body, action_url, is_read, created_at | Notification list |
| users (related) | name, avatar | For follow/message notifications |

---

## Sections

### Header
- Page title: "Notifications"
- "Mark All as Read" button
- "Settings" link → SETT (notifications section)

### Filter/Tabs (Optional)
- All / Unread
- By type: Sessions, Messages, Courses, Social

### Notification List
- Chronological list, newest first
- Each notification shows:
  - Icon by type (session, message, certificate, etc.)
  - Title (bold if unread)
  - Body text (preview)
  - Timestamp (relative: "2 hours ago")
  - Unread indicator (dot)
- Click → navigate to action_url
- Swipe to mark read/delete (mobile)

### Notification Types
| Type | Icon | Example |
|------|------|---------|
| session_reminder | Calendar | "Your session starts in 15 minutes" |
| session_booked | Calendar+ | "[Student] booked a session with you" |
| new_message | Message | "New message from [Name]" |
| course_update | Book | "[Course] has new content" |
| certificate_earned | Award | "You earned a certificate!" |
| st_application | User+ | "[Name] applied to be an ST" |
| cert_request | Clipboard | "[ST] recommends [Student] for certification" |
| new_follower | User | "[Name] started following you" |
| payment | Dollar | "Payout of $X processed" |
| system | Info | Platform announcements |

### Empty State
- "No notifications yet"
- "You're all caught up!"

### Load More / Infinite Scroll
- Pagination or infinite scroll for older notifications

---

## User Stories Fulfilled

- US-P017: View all notifications
- US-P018: Manage notification preferences (via link to SETT)

---

## States & Variations

| State | Description |
|-------|-------------|
| Has Unread | Unread items highlighted, badge in nav |
| All Read | No badge, items in normal style |
| Empty | No notifications, encouraging message |
| Filtered | Showing specific type only |

---

## Mobile Considerations

- Full-screen list
- Pull-to-refresh
- Swipe gestures for mark read / delete
- Notification bell in bottom nav

---

## Error Handling

| Error | Display |
|-------|---------|
| Load fails | "Unable to load notifications. [Retry]" |
| Mark read fails | Toast: "Unable to update. Try again." |

---

## Analytics Events

| Event | Trigger | Data |
|-------|---------|------|
| `page_view` | Page load | unread_count |
| `notification_clicked` | Notification clicked | notification_type, notification_id |
| `mark_all_read` | Mark all clicked | count_marked |
| `mark_read` | Single marked read | notification_id |
| `notification_deleted` | Deleted | notification_id |

---

## Notes

- Real-time updates: New notifications appear without refresh
- Push notification bridge: In-app notifications mirror push
- Consider notification grouping (3 new followers → "3 people followed you")
- Retention: Auto-delete notifications older than 30 days?
