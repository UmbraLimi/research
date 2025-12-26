# Page: Creator Newsletters

**Code:** CNEW
**URL:** `/studio/newsletters`
**Access:** Authenticated (Creator role)
**Priority:** P3
**Status:** Out of Scope (Post-MVP)

---

## Purpose

Allow Creators to publish newsletters to their subscribers, with optional paid subscription tiers.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| STUD | "Newsletters" nav item | Creator Studio sidebar |
| CDSH | "Manage Newsletters" link | Dashboard quick action |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| STUD | Back/breadcrumb | Return to studio |
| (External) | "Preview" button | Opens newsletter preview |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| newsletters | id, title, content, status, sent_at, creator_id | Newsletter records |
| newsletter_subscribers | user_id, creator_id, tier, subscribed_at | Subscriber list |
| newsletter_tiers | id, name, price, description | Subscription tiers |

---

## Sections

### Header
- Page title: "Newsletters"
- "Create Newsletter" button

### Newsletter List
- Table/cards of past newsletters
- Columns: Title, Status (Draft/Sent), Sent Date, Opens, Clicks
- Actions: Edit, Duplicate, Delete, View Stats

### Create/Edit Newsletter
- Title field
- Rich text editor for content
- Subscriber tier selector (who receives)
- Schedule or send immediately
- Preview button

### Subscriber Management
- Subscriber count by tier
- Export subscribers
- Tier management (create/edit tiers)

---

## User Stories Fulfilled

- US-C026: As a Creator, I need to publish newsletters (potentially with subscription payments) so that I can engage my audience

---

## States & Variations

| State | Description |
|-------|-------------|
| Empty | No newsletters yet - show "Create your first newsletter" CTA |
| List | Viewing all newsletters |
| Editing | Creating/editing a newsletter |
| Sending | Newsletter being sent (progress indicator) |

---

## Mobile Considerations

- Newsletter editing may be limited on mobile (complex rich text)
- Consider mobile-optimized preview

---

## Error Handling

| Error | Display |
|-------|---------|
| Send fails | "Newsletter failed to send. [Retry]" |
| No subscribers | "You have no subscribers yet" |

---

## Notes

- P3 feature - future consideration
- May integrate with external email service (Resend, SendGrid)
- Consider Substack-like experience
- Paid tiers would need Stripe integration
