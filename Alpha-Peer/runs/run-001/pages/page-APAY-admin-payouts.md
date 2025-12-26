# Screen: Admin Payouts

**Code:** APAY
**URL:** `/admin/payouts` (route within Admin SPA)
**Access:** Authenticated (Admin role)
**Priority:** P0
**Status:** In Scope

---

## Purpose

Manage platform payouts - process pending payouts to STs and Creators, view transaction history, and handle payment issues.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| ADMN | "Payouts" nav item | Admin sidebar |
| AUSR | "View Payouts" on user | Filtered to user |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| AUSR | Recipient name click | View user |
| AENR | "View Enrollment" | Source enrollment |
| (Stripe) | "View in Stripe" | External link |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| payouts | All fields | Payout records |
| payment_splits | All fields | Revenue splits |
| transactions | All fields | Source transactions |
| users (recipients) | id, name, email, stripe_account | Recipient info |
| courses | id, title | Source course |
| enrollments | id | Source enrollment |

---

## Sections

### Header
- Screen title: "Payout Management"
- "Process Pending" button (batch)
- Pending total badge

### Summary Cards
- **Pending Payouts** - Total $ awaiting processing
- **Processing** - Currently in transit
- **Paid This Month** - Month total
- **Paid All Time** - Lifetime total

### Tabs
- **Pending** - Awaiting admin approval
- **Processing** - Sent to Stripe
- **Completed** - Successfully paid
- **Failed** - Failed payouts

### Pending Payouts Tab

Grouped by recipient:

**Recipient Card:**
- Name + avatar
- Pending balance
- Split: ST amount / Creator amount
- Stripe account status
- "Process Payout" button

**Expandable Details:**
- List of individual payment splits:
  - Transaction date
  - Course
  - Student
  - Gross amount
  - Split amount
  - Split type (ST 85% / Creator 15%)

### Payouts Table (All Tabs)

| Column | Content |
|--------|---------|
| Recipient | Name |
| Type | ST / Creator |
| Amount | Payout amount |
| Transactions | Count of splits included |
| Status | Pending / Processing / Completed / Failed |
| Requested | Date requested |
| Processed | Date processed |
| Actions | Process, View, Cancel |

### Payout Detail Panel

**Payout Info:**
- Recipient info (link to AUSR)
- Amount
- Status + timestamps
- Stripe transfer ID (if processed)

**Included Transactions:**
- List of payment splits in this payout
- Source enrollments
- Split calculations

**For Failed Payouts:**
- Failure reason
- Retry option
- Alternative actions

### Actions

| Action | Description |
|--------|-------------|
| Process Single | Process one payout |
| Process All | Batch process all pending |
| Cancel | Cancel pending payout |
| Retry | Retry failed payout |
| Manual Override | Mark as paid (for offline payment) |

### Process Payout Flow
1. Select payouts to process
2. Review totals
3. Confirm Stripe account status
4. Process (calls Stripe API)
5. Update status

---

## CRUD Operations

| Operation | Endpoint | Notes |
|-----------|----------|-------|
| List Pending | GET /api/admin/payouts/pending | Grouped by recipient |
| List All | GET /api/admin/payouts | All payouts |
| Read | GET /api/admin/payouts/:id | Payout detail |
| Process | POST /api/admin/payouts/:id/process | Initiate Stripe transfer |
| Batch Process | POST /api/admin/payouts/batch | Process multiple |
| Cancel | DELETE /api/admin/payouts/:id | Cancel pending |

---

## Revenue Split Reference (CD-020, CD-033)

| Role | Percentage |
|------|------------|
| Student-Teacher | 85% |
| Creator (Royalty) | 15% |
| Platform | 0% (absorbed in fees) |

---

## States & Variations

| State | Description |
|-------|-------------|
| Pending Tab | Showing pending, grouped by recipient |
| Processing | Payout in progress |
| Completed | Viewing history |
| Failed | Viewing/retrying failures |
| Detail | Payout panel open |

---

## Error Handling

| Error | Display |
|-------|---------|
| Load fails | "Unable to load payouts. [Retry]" |
| Stripe error | "Stripe error: [message]. Check dashboard." |
| No Stripe account | "Recipient has no Stripe account connected" |
| Insufficient balance | "Platform balance insufficient" |

---

## Notes

- CD-020: Semi-automated payouts (admin approves, Stripe transfers)
- Stripe Connect for marketplace payouts
- Consider minimum payout threshold ($50?)
- Tax documentation: 1099 thresholds
- Audit trail critical for financial records
