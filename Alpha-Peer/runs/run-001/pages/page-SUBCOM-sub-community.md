# Page: Sub-Community

**Code:** SUBCOM
**URL:** `/community/:slug`
**Access:** Authenticated (Members only, or Public if open)
**Priority:** P3
**Status:** Out of Scope (Post-MVP)

---

## Purpose

User-created sub-communities for study groups, interest clusters, or private collaboration spaces within the platform.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| FEED | Sub-community card/link | From main feed |
| SDSH | "My Communities" section | Dashboard widget |
| NOTF | Community notification | Invited to join |
| (Direct) | Shared invite link | External share |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| STPR | Click member name | View member profile |
| FEED | Back/breadcrumb | Return to main feed |
| MSGS | "Message" button | DM a member |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| sub_communities | id, name, slug, description, visibility, creator_id | Community info |
| sub_community_members | user_id, community_id, role, joined_at | Membership |
| sub_community_posts | id, content, author_id, created_at | Community feed |
| sub_community_invites | email, token, status | Pending invites |

---

## Sections

### Header
- Community name + description
- Member count
- Join/Leave button (or "Pending" if invite-only)
- Settings gear (for owner/admins)

### Community Feed
- Posts from members only
- Same feed UI as main FEED (cards, reactions, comments)
- "New Post" composer

### Members Sidebar (Desktop) / Tab (Mobile)
- Member list with avatars
- Owner/Admin badges
- "Invite Members" button (if permitted)

### Settings Panel (Owner/Admin only)
- Edit name/description
- Visibility toggle (Public/Invite-only)
- Manage members (remove, promote to admin)
- Invite settings (who can invite)
- Delete community

### Invite Flow
- Search users by name/email
- Send invite (creates notification)
- Pending invites list
- Invite link generation

---

## User Stories Fulfilled

- US-S081: As a Student, I need to create a sub-community and invite specific users so that I can form study groups or interest clusters
- US-P097: As a System, I need to support user-created sub-communities with invite functionality so that users can organize privately

---

## States & Variations

| State | Description |
|-------|-------------|
| Member View | Full access to feed and members |
| Non-Member (Public) | Can see feed, join button visible |
| Non-Member (Private) | "Request to Join" or "Invite Only" message |
| Owner View | Full access + settings panel |
| Empty | No posts yet - prompt to start conversation |

---

## Mobile Considerations

- Members list as bottom sheet or separate tab
- Settings accessed via menu
- Invite flow as modal

---

## Error Handling

| Error | Display |
|-------|---------|
| Load fails | "Unable to load community. [Retry]" |
| Not found | "This community doesn't exist or is private" |
| Already member | "You're already a member" |
| Invite expired | "This invite has expired" |

---

## Analytics Events

| Event | Trigger |
|-------|---------|
| sub_community_viewed | Page load |
| sub_community_joined | User joins |
| sub_community_post_created | New post |
| sub_community_member_invited | Invite sent |

---

## Notes

- P3 feature - future consideration
- Consider limits: max communities per user, max members per community
- Moderation: how do platform moderators handle sub-community content?
- Integration with main feed: should sub-community posts appear in main feed?
- CD-032 source: Fraser Meeting Notes mention study groups
