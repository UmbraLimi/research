# Screen: Admin Courses

**Code:** ACRS
**URL:** `/admin/courses` (route within Admin SPA)
**Access:** Authenticated (Admin role)
**Priority:** P0
**Status:** In Scope

---

## Purpose

CRUD interface for managing all courses - view, edit, feature, suspend, and oversee course content and settings.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| ADMN | "Courses" nav item | Admin sidebar |
| AENR | Course name click | From enrollment |
| AUSR | "View Courses" on creator | Filtered to creator |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| CDET | "View Public Page" | Opens in new tab |
| AENR | "View Enrollments" | Filtered to course |
| ASES | "View Sessions" | Filtered to course |
| AUSR | Creator name click | View creator |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| courses | All fields | Course records |
| users (creators) | id, name | Creator info |
| enrollments | count per course | Enrollment stats |
| student_teachers | count per course | ST count |
| categories | id, name | Category reference |

---

## Sections

### Header
- Screen title: "Course Management"
- "Add Course" button (rarely used by admin)
- Export button

### Search & Filters
- **Search:** Title, creator name
- **Category filter:** All / specific category
- **Status filter:** All / Published / Draft / Suspended / Retired
- **Level filter:** Beginner / Intermediate / Advanced
- **Featured filter:** Featured only

### Courses Table

| Column | Content |
|--------|---------|
| Course | Thumbnail + title |
| Creator | Creator name |
| Category | Category name |
| Price | Price display |
| Students | Enrollment count |
| Rating | Stars + count |
| Status | Published / Draft / Suspended |
| Featured | Star icon |
| Actions | Edit, Feature, Suspend |

### Course Detail Panel

**View Mode:**
- Full course info
- Creator info (link to AUSR)
- Curriculum summary
- Stats:
  - Enrollments (link to AENR)
  - Active STs
  - Sessions completed
  - Revenue generated
- Moderation notes

**Edit Mode:**
- Title, description (editable)
- Price (editable)
- Category (editable)
- Status (published/suspended)
- Featured toggle
- Badge assignment (Popular, New, Bestseller)
- Admin notes

### Actions

| Action | Description |
|--------|-------------|
| Edit | Modify course settings |
| Feature | Add/remove from featured |
| Set Badge | Assign promotional badge |
| Suspend | Hide course, block enrollments |
| Unsuspend | Restore suspended course |
| Delete | Remove course (if no enrollments) |
| Transfer | Change course owner |

---

## API Calls

| Endpoint | When | Purpose |
|----------|------|---------|
| `GET /api/admin/courses` | Page load | Paginated, filterable course list |
| `GET /api/admin/courses/:id` | Detail open | Full course data with stats |
| `PATCH /api/admin/courses/:id` | Save edit | Update course settings |
| `DELETE /api/admin/courses/:id` | Delete | Remove course (no enrollments) |
| `POST /api/admin/courses/:id/feature` | Feature | Add to featured |
| `DELETE /api/admin/courses/:id/feature` | Unfeature | Remove from featured |
| `POST /api/admin/courses/:id/suspend` | Suspend | Hide course |
| `POST /api/admin/courses/:id/unsuspend` | Unsuspend | Restore course |
| `POST /api/admin/courses/:id/transfer` | Transfer | Change owner |

**Query Parameters:**
- `q` - Search title, creator name
- `category_id` - Filter by category
- `status` - published, draft, suspended, retired
- `level` - beginner, intermediate, advanced
- `featured` - true/false
- `page`, `limit` - Pagination

**Course Response:**
```typescript
GET /api/admin/courses/:id
{
  course: { ...all fields... },
  creator: { id, name },
  stats: {
    enrollments: number,
    active_sts: number,
    sessions_completed: number,
    revenue: number
  }
}
```

---

## States & Variations

| State | Description |
|-------|-------------|
| List | Default course list |
| Filtered | Search/filter applied |
| Detail | Course panel open |
| Editing | Edit mode active |

---

## Error Handling

| Error | Display |
|-------|---------|
| Load fails | "Unable to load courses. [Retry]" |
| Update fails | "Unable to save changes. [Retry]" |
| Delete blocked | "Cannot delete course with enrollments" |

---

## Notes

- Admin rarely creates courses (creators do)
- Focus on oversight: featuring, suspending, moderating
- Course transfer for creator account changes
