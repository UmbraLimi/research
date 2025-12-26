# Page: Creator Analytics

**Code:** CANA
**URL:** `/studio/analytics`
**Access:** Authenticated (Creator role)
**Priority:** P1
**Status:** In Scope

---

## Purpose

Provide Creators with detailed analytics about their courses, student engagement, conversion rates, and revenue performance.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| CDSH | "View Analytics" link | From dashboard |
| STUD | "Analytics" tab | From Creator Studio |
| Nav | "Analytics" link | Creator navigation |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| CDET | Course name click | View course |
| CMST | "View Students" link | Student details |
| CEAR | "View Earnings" link | Revenue details |
| CDSH | Back/breadcrumb | Return to dashboard |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| courses | id, title, student_count, rating | Course list |
| enrollments | course_id, status, enrolled_at, completed_at | Enrollment metrics |
| sessions | course_id, status, scheduled_start | Session metrics |
| module_progress | enrollment_id, is_complete, completed_at | Progress metrics |
| certificates | course_id, type, issued_at | Completion metrics |
| transactions | enrollment_id, amount_cents, paid_at | Revenue data |
| (page_views) | course_id, timestamp | Traffic data (if tracked) |

---

## Sections

### Header
- Page title: "Analytics"
- Date range selector (7d, 30d, 90d, 1y, custom)
- Course filter: All / specific course

### Key Metrics Row
- **Total Revenue** (period)
- **New Enrollments** (period)
- **Completion Rate** (%)
- **Average Rating**
- **Active Students**

### Enrollment Trends Chart
- Line/area chart: Enrollments over time
- Overlay: Revenue over time
- Comparison to previous period

### Course Performance Table

| Column | Content |
|--------|---------|
| Course | Title |
| Enrollments | Total / Period |
| Revenue | Total / Period |
| Completion Rate | % completed |
| Avg Rating | Stars |
| Active | Current active students |

### Funnel Analysis
- Course page views → Enrollments → Completions → Became ST
- Conversion rates at each step
- Drop-off identification

### Student Progress Distribution
- Pie/bar chart: Students by progress stage
  - Not started
  - In progress (0-25%, 25-50%, 50-75%, 75-99%)
  - Completed

### Session Analytics
- Sessions per week trend
- Average session duration
- Session completion rate
- No-show rate

### ST Performance
- Leaderboard: Top STs by students taught
- Average ratings per ST
- Session volume per ST

### Engagement Metrics
- Average time to first session
- Average days to completion
- Module completion rates
- Content engagement (if tracked)

---

## User Stories Fulfilled

- US-C033: View course analytics
- US-C047: Track conversion rates
- US-C048: Monitor student engagement
- US-C049: Analyze revenue trends

---

## States & Variations

| State | Description |
|-------|-------------|
| Default | All courses, last 30 days |
| Filtered | Specific course or date range |
| Comparison | Comparing to previous period |
| Empty | No data yet, "Share your courses" |

---

## Mobile Considerations

- Metrics row scrolls horizontally
- Charts simplified for mobile
- Tables become card lists
- Focus on key metrics

---

## Error Handling

| Error | Display |
|-------|---------|
| Load fails | "Unable to load analytics. [Retry]" |
| Partial data | Show available data with notice |

---

## Analytics Events

| Event | Trigger | Data |
|-------|---------|------|
| `page_view` | Page load | date_range, course_filter |
| `date_range_changed` | Range selected | new_range |
| `course_filtered` | Course selected | course_id |
| `export_requested` | Export clicked | report_type |

---

## Notes

- Consider caching/pre-computing metrics for performance
- Charts should be interactive (hover for details)
- Export to CSV/PDF for reporting
- Future: Cohort analysis, predictive metrics
