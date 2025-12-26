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

## CRUD Operations

| Operation | Endpoint | Notes |
|-----------|----------|-------|
| List | GET /api/admin/categories | Ordered list |
| Create | POST /api/admin/categories | Add category |
| Update | PATCH /api/admin/categories/:id | Edit category |
| Delete | DELETE /api/admin/categories/:id | Only if no courses |
| Reorder | POST /api/admin/categories/reorder | Batch update order |

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
