# Page: Leaderboard

**Code:** LEAD
**URL:** `/community/leaderboard`
**Access:** Authenticated
**Priority:** P3
**Status:** Out of Scope (Post-MVP)

---

## Purpose

Display community rankings based on goodwill points, helping users see their standing and motivating engagement.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| FEED | "Leaderboard" link/tab | Community navigation |
| PROF | "View Leaderboard" link | From profile stats |
| SDSH | "Community Standing" widget | Dashboard link |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| STPR | Click on user name | View user profile |
| FEED | Back/breadcrumb | Return to feed |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| users | id, name, avatar, goodwill_points | User rankings |
| goodwill_transactions | points, created_at | Points history |
| user_badges | badge_type, earned_at | Achievement display |

---

## Sections

### Header
- Page title: "Community Leaderboard"
- Time period filter (All Time, This Month, This Week)

### Your Ranking
- Current user's position highlighted
- Points total
- Rank change indicator (↑↓)

### Top Rankings Table

| Column | Content |
|--------|---------|
| Rank | Position number |
| User | Avatar + name |
| Points | Goodwill points total |
| Badges | Badge icons earned |
| Change | Rank movement since last period |

### Leaderboard Categories (Tabs)
- **Overall** - Total goodwill points
- **Helpers** - Points from helping others
- **Teachers** - S-T session ratings
- **Contributors** - Content creation points

### Rewards Tiers
- Visual display of point thresholds (500, 1000, 2500, 5000)
- What unlocks at each tier
- User's progress toward next tier

---

## User Stories Fulfilled

- US-P053: As a System, I need to display leaderboards/rankings so that community standing is transparent
- US-P082: As a System, I need to unlock rewards at point thresholds (500, 1000, 2500, 5000) so that goodwill points have tangible value

---

## States & Variations

| State | Description |
|-------|-------------|
| Default | Showing overall leaderboard |
| Category | Filtered to specific category |
| Time Period | Filtered to week/month/all-time |
| Loading | Fetching rankings |

---

## Mobile Considerations

- Simplified table for mobile (hide some columns)
- Swipeable category tabs
- Sticky "Your Ranking" section at top

---

## Error Handling

| Error | Display |
|-------|---------|
| Load fails | "Unable to load leaderboard. [Retry]" |
| No data | "Leaderboard updates daily" (if new) |

---

## Analytics Events

| Event | Trigger |
|-------|---------|
| leaderboard_viewed | Page load |
| leaderboard_category_changed | Category tab switch |
| leaderboard_user_clicked | Click on user row |

---

## Notes

- P3 feature - future consideration
- Anti-gaming measures needed (prevent point manipulation)
- Consider privacy option to opt-out of leaderboard
- Cache rankings (update hourly, not real-time)
- CD-023 defines point thresholds: 500, 1000, 2500, 5000
