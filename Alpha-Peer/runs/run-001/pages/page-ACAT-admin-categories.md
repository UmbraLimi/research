# Screen: Admin Categories

**Code:** ACAT
**URL:** `/admin/categories` (route within Admin SPA)
**Access:** Authenticated (Admin role)
**Priority:** P1
**Status:** In Scope

---

## Purpose

CRUD interface for managing course categories - the taxonomy used to organize and filter courses.

---

## Connections

### Incoming (users arrive from)

| Source | Trigger | Notes |
|--------|---------|-------|
| ADMN | "Categories" nav item | Admin sidebar (under Settings) |

### Outgoing (users navigate to)

| Target | Trigger | Notes |
|--------|---------|-------|
| ACRS | "View Courses" | Courses in category |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| categories | All fields | Category records |
| courses | category_id, count | Usage stats |

---

## Sections

### Header
- Screen title: "Category Management"
- "Add Category" button

### Categories Table

| Column | Content |
|--------|---------|
| Order | Drag handle + display order |
| Name | Category name |
| Slug | URL slug |
| Courses | Count of courses in category |
| Actions | Edit, Delete |

### Category Form (Add/Edit)
- **Name** - Category display name
- **Slug** - URL-friendly slug (auto-generated, editable)
- **Display Order** - Sort order (or drag to reorder)
- **Description** - Optional description
- **Icon** - Optional icon (for UI)
- **Parent** - For sub-categories (future)

### Actions

| Action | Description |
|--------|-------------|
| Add | Create new category |
| Edit | Modify category |
| Reorder | Drag to change display order |
| Delete | Remove category (only if empty) |
| Merge | Merge into another category |

---

## API Calls

| Endpoint | When | Purpose |
|----------|------|---------|
| `GET /api/admin/categories` | Page load | Ordered category list |
| `POST /api/admin/categories` | Add | Create new category |
| `PATCH /api/admin/categories/:id` | Edit | Update category |
| `DELETE /api/admin/categories/:id` | Delete | Remove (if no courses) |
| `POST /api/admin/categories/reorder` | Drag/drop | Update display order |
| `POST /api/admin/categories/:id/merge` | Merge | Merge into another |

**Category Response:**
```typescript
GET /api/admin/categories
{
  categories: [{
    id, name, slug, display_order,
    description, icon,
    course_count: number
  }]
}
```

**Reorder:**
```typescript
POST /api/admin/categories/reorder
{
  order: [
    { id: 'cat_1', display_order: 0 },
    { id: 'cat_2', display_order: 1 }
  ]
}
```

**Merge:**
```typescript
POST /api/admin/categories/:id/merge
{
  into_category_id: string
}
// Moves all courses, then deletes source
```

---

## Sample Categories (from CD-021)

| Name | Slug |
|------|------|
| AI & Product Management | ai-product-management |
| Machine Learning | machine-learning |
| Computer Vision | computer-vision |
| NLP | nlp |
| Data Science | data-science |
| Business Analytics | business-analytics |
| Backend Development | backend-development |
| Cloud Computing | cloud-computing |
| Full-Stack Development | full-stack-development |
| DevOps | devops |
| System Design | system-design |
| AI & Robotics | ai-robotics |
| AI in Healthcare | ai-healthcare |
| AI Coding | ai-coding |
| AI & Prompt Engineering | ai-prompt-engineering |

---

## States & Variations

| State | Description |
|-------|-------------|
| List | Viewing all categories |
| Adding | Create form open |
| Editing | Edit form open |
| Reordering | Drag mode active |

---

## Error Handling

| Error | Display |
|-------|---------|
| Load fails | "Unable to load categories. [Retry]" |
| Duplicate slug | "Slug already exists. Choose another." |
| Delete blocked | "Cannot delete category with X courses" |

---

## Notes

- Categories are platform-wide, not per-creator
- Consider sub-categories for larger scale (future)
- Slug changes affect course URLs (redirect needed)
- Genesis Cohort: May only need 4-5 categories initially
