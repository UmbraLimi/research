# Page: Earnings Detail (Creator)

**Code:** CEAR
**URL:** `/studio/earnings`
**Access:** Authenticated (Creator role)
**Priority:** P0
**Status:** In Scope

---

## Purpose

Provide Creators with detailed view of their earnings, revenue breakdown by course, payout history, and pending balances.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| CDSH | "View Earnings" link | From earnings summary |
| CANA | "View Earnings" link | From analytics |
| Nav | "Earnings" link | Creator navigation |
| STUD | "Earnings" tab | From Creator Studio |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| CDET | Course name click | View course |
| SETT | "Payment Settings" | Update payout method |
| CDSH | Back/breadcrumb | Return to dashboard |
| (Stripe) | "View in Stripe" | External link |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| payment_splits | amount_cents, status, released_at (where recipient = creator) | Revenue records |
| transactions | enrollment_id, amount_cents, paid_at | Transaction source |
| payouts | amount_cents, status, paid_at, approved_at | Payout records |
| courses | id, title | Course breakdown |
| enrollments | course_id | Link transactions to courses |

---

## Sections

### Header
- Page title: "Earnings"
- Period selector: This month / Last month / This year / All time

### Earnings Summary Cards
- **Available Balance** - Ready for payout
- **Pending** - In escrow, not yet released
- **This Period** - Earned in selected period
- **Lifetime Earnings** - Total ever earned
- "Request Payout" button (if balance > threshold)

### Revenue Chart
- Bar/line chart: Revenue over time
- Monthly or weekly granularity
- Stacked by course (optional)

### Revenue by Course

| Column | Content |
|--------|---------|
| Course | Title |
| Enrollments | Count in period |
| Gross Revenue | Total course revenue |
| Your Royalty (15%) | Creator's share |
| Status | Released / Pending |

### Transaction History

| Column | Content |
|--------|---------|
| Date | Transaction date |
| Student | Student name |
| Course | Course title |
| Amount | Gross amount |
| Your Share | 15% royalty |
| Status | Pending / Released / Paid |

- Expandable for full transaction details
- Filter by course, status, date range
- Pagination or infinite scroll

### Payout History

| Column | Content |
|--------|---------|
| Date | Payout date |
| Amount | Payout amount |
| Status | Processing / Completed / Failed |
| Reference | Stripe transfer ID |

### Pending Releases
- List of transactions still in escrow
- Expected release dates
- Conditions for release (student completion, time-based)

### Payment Settings Summary
- Connected Stripe account status
- Payout threshold
- "Update Settings" → SETT

---

## User Stories Fulfilled

- US-C035: View detailed earnings
- US-C050: Track revenue by course
- US-C051: View payout history
- US-C052: Request payouts

---

## States & Variations

| State | Description |
|-------|-------------|
| Default | Current month earnings |
| Filtered | By date range or course |
| Has Balance | Payout button enabled |
| No Balance | Payout button disabled |
| Stripe Not Connected | Prompt to connect Stripe |
| Empty | No earnings yet |

---

## Mobile Considerations

- Summary cards scroll horizontally
- Transaction list is primary view
- Charts simplified
- Payout action prominent

---

## Error Handling

| Error | Display |
|-------|---------|
| Load fails | "Unable to load earnings. [Retry]" |
| Payout request fails | "Unable to process. Try again." |
| Stripe disconnected | "Reconnect your Stripe account" |

---

## Analytics Events

| Event | Trigger | Data |
|-------|---------|------|
| `page_view` | Page load | balance, period |
| `payout_requested` | Request clicked | amount |
| `period_changed` | Date range changed | new_period |
| `transaction_viewed` | Row expanded | transaction_id |

---

## Notes

- CD-020: Creator gets 15% royalty
- CD-033: 85/15 split (ST gets 85%, Creator gets 15%)
- Stripe Connect for payouts
- Consider tax documentation features (future)
