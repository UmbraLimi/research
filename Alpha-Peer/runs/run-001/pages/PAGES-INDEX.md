# RUN-001 Pages Index

**Run:** RUN-001 (Stream + VideoProvider)
**Created:** 2025-12-25
**Total Pages:** 41 (10 public, 21 authenticated, 3 role-specific, 7 admin screens)

---

## Page Schema Definition

Each page file (`page-CODE-name.md`) follows this standard schema:

```markdown
# Page: [Page Name]

**Code:** [3-4 letter code]
**URL:** [URL pattern]
**Access:** [Public | Authenticated | Role-specific (which roles)]
**Priority:** [P0 | P1 | P2 | P3]
**Status:** [In Scope | Out of Scope | Partial]

---

## Purpose
[One sentence describing why this page exists and what user need it serves]

---

## Connections

### Incoming (users arrive from)
| Source | Trigger | Notes |
|--------|---------|-------|
| CODE | [Button/Link/Redirect description] | [Optional notes] |

### Outgoing (users navigate to)
| Target | Trigger | Notes |
|--------|---------|-------|
| CODE | [Button/Link/Redirect description] | [Optional notes] |

---

## Data Requirements

| Entity | Fields Used | Purpose |
|--------|-------------|---------|
| [table_name] | [field1, field2, ...] | [Why needed] |

---

## Sections

### [Section Name]
- [Element 1]
- [Element 2]
- ...

[Repeat for each section]

---

## User Stories Fulfilled
- US-XXXX: [Story title]
- ...

---

## States & Variations
[Different states the page can be in, e.g., empty state, loading, error]

---

## Mobile Considerations
[Any mobile-specific layout or behavior notes]

---

## Error Handling
[What errors can occur and how they're displayed]

---

## Analytics Events
[Key events to track on this page]

---

## Notes
[Any additional context, open questions, or implementation notes]
```

### Schema Extension Rules

1. **Custom sections allowed** - Add sections specific to a page as needed
2. **Evaluate for promotion** - If a custom section appears useful across multiple pages, add it to this schema
3. **Backfill on promotion** - When a section is added to the schema, update all existing page files

---

## Page Code Registry

| Code | Page Name | URL | Access | Priority | File |
|------|-----------|-----|--------|----------|------|
| **Public Pages** |||||
| HOME | Homepage | `/` | Public | P0 | [page-HOME-homepage.md](page-HOME-homepage.md) |
| CBRO | Course Browse | `/courses` | Public | P0 | [page-CBRO-course-browse.md](page-CBRO-course-browse.md) |
| CDET | Course Detail | `/courses/:slug` | Public | P0 | [page-CDET-course-detail.md](page-CDET-course-detail.md) |
| CRLS | Creator Listing | `/creators` | Public | P0 | [page-CRLS-creator-listing.md](page-CRLS-creator-listing.md) |
| CPRO | Creator Profile | `/creators/:handle` | Public | P0 | [page-CPRO-creator-profile.md](page-CPRO-creator-profile.md) |
| STDR | ST Directory | `/student-teachers` | Public | P1 | [page-STDR-st-directory.md](page-STDR-st-directory.md) |
| STPR | ST Profile | `/@:handle` | Public | P0 | [page-STPR-st-profile.md](page-STPR-st-profile.md) |
| LGIN | Login | `/login` | Public | P0 | [page-LGIN-login.md](page-LGIN-login.md) |
| SGUP | Sign Up | `/signup` | Public | P0 | [page-SGUP-signup.md](page-SGUP-signup.md) |
| PWRS | Password Reset | `/reset-password` | Public | P0 | [page-PWRS-password-reset.md](page-PWRS-password-reset.md) |
| **Authenticated Pages** |||||
| SDSH | Student Dashboard | `/dashboard` | Auth (Student) | P0 | [page-SDSH-student-dashboard.md](page-SDSH-student-dashboard.md) |
| TDSH | ST Dashboard | `/dashboard` | Auth (ST) | P0 | [page-TDSH-st-dashboard.md](page-TDSH-st-dashboard.md) |
| CDSH | Creator Dashboard | `/dashboard` | Auth (Creator) | P0 | [page-CDSH-creator-dashboard.md](page-CDSH-creator-dashboard.md) |
| FEED | Community Feed | `/community` | Auth | P0 | [page-FEED-community-feed.md](page-FEED-community-feed.md) |
| MSGS | Messages | `/messages` | Auth | P0 | [page-MSGS-messages.md](page-MSGS-messages.md) |
| PROF | Profile | `/profile` | Auth | P0 | [page-PROF-profile.md](page-PROF-profile.md) |
| SETT | Settings | `/settings` | Auth | P0 | [page-SETT-settings.md](page-SETT-settings.md) |
| NOTF | Notifications | `/notifications` | Auth | P0 | [page-NOTF-notifications.md](page-NOTF-notifications.md) |
| SBOK | Session Booking | `/book/:st_id` | Auth (Enrolled) | P0 | [page-SBOK-session-booking.md](page-SBOK-session-booking.md) |
| SROM | Session Room | `/session/:id` | Auth (Participants) | P0 | [page-SROM-session-room.md](page-SROM-session-room.md) |
| CCNT | Course Content | `/learn/:course_id` | Auth (Enrolled) | P0 | [page-CCNT-course-content.md](page-CCNT-course-content.md) |
| CHAT | Course Chat | `/courses/:id/chat` | Auth (Enrolled) | P2 | [page-CHAT-course-chat.md](page-CHAT-course-chat.md) |
| HELP | Summon Help | Modal | Auth (Enrolled) | P2 | [page-HELP-summon-help.md](page-HELP-summon-help.md) |
| IFED | Instructor Feed | `/@:handle/feed` | Auth (Purchased) | P1 | [page-IFED-instructor-feed.md](page-IFED-instructor-feed.md) |
| LEAD | Leaderboard | `/community/leaderboard` | Auth | P3 | [page-LEAD-leaderboard.md](page-LEAD-leaderboard.md) |
| SUBCOM | Sub-Community | `/community/:slug` | Auth (Members) | P3 | [page-SUBCOM-sub-community.md](page-SUBCOM-sub-community.md) |
| **Creator Pages** |||||
| CMST | My Students | `/studio/students` | Auth (Creator) | P0 | [page-CMST-my-students.md](page-CMST-my-students.md) |
| CSES | Session History | `/studio/sessions` | Auth (Creator) | P0 | [page-CSES-session-history.md](page-CSES-session-history.md) |
| CANA | Creator Analytics | `/studio/analytics` | Auth (Creator) | P1 | [page-CANA-creator-analytics.md](page-CANA-creator-analytics.md) |
| CEAR | Earnings Detail | `/studio/earnings` | Auth (Creator) | P0 | [page-CEAR-earnings-detail.md](page-CEAR-earnings-detail.md) |
| CNEW | Creator Newsletters | `/studio/newsletters` | Auth (Creator) | P3 | [page-CNEW-creator-newsletters.md](page-CNEW-creator-newsletters.md) |
| **Role-Specific Pages** |||||
| STUD | Creator Studio | `/studio` | Auth (Creator) | P0 | [page-STUD-creator-studio.md](page-STUD-creator-studio.md) |
| ADMN | Admin Dashboard | `/admin` | Auth (Admin) | P0 | [page-ADMN-admin-dashboard.md](page-ADMN-admin-dashboard.md) |
| MODQ | Moderator Queue | `/moderate` | Auth (Moderator) | P1 | [page-MODQ-moderator-queue.md](page-MODQ-moderator-queue.md) |
| **Admin SPA Screens** (routes within `/admin`) |||||
| AUSR | Admin Users | `/admin/users` | Auth (Admin) | P0 | [page-AUSR-admin-users.md](page-AUSR-admin-users.md) |
| ACRS | Admin Courses | `/admin/courses` | Auth (Admin) | P0 | [page-ACRS-admin-courses.md](page-ACRS-admin-courses.md) |
| AENR | Admin Enrollments | `/admin/enrollments` | Auth (Admin) | P0 | [page-AENR-admin-enrollments.md](page-AENR-admin-enrollments.md) |
| ASES | Admin Sessions | `/admin/sessions` | Auth (Admin) | P0 | [page-ASES-admin-sessions.md](page-ASES-admin-sessions.md) |
| ACRT | Admin Certificates | `/admin/certificates` | Auth (Admin) | P0 | [page-ACRT-admin-certificates.md](page-ACRT-admin-certificates.md) |
| APAY | Admin Payouts | `/admin/payouts` | Auth (Admin) | P0 | [page-APAY-admin-payouts.md](page-APAY-admin-payouts.md) |
| ACAT | Admin Categories | `/admin/categories` | Auth (Admin) | P1 | [page-ACAT-admin-categories.md](page-ACAT-admin-categories.md) |

---

## Pages by Priority

### P0 - MVP Core (31 pages/screens)
| Code | Page Name |
|------|-----------|
| HOME | Homepage |
| CBRO | Course Browse |
| CDET | Course Detail |
| CRLS | Creator Listing |
| CPRO | Creator Profile |
| STPR | ST Profile |
| LGIN | Login |
| SGUP | Sign Up |
| PWRS | Password Reset |
| SDSH | Student Dashboard |
| TDSH | ST Dashboard |
| CDSH | Creator Dashboard |
| FEED | Community Feed |
| MSGS | Messages |
| PROF | Profile |
| SETT | Settings |
| NOTF | Notifications |
| SBOK | Session Booking |
| SROM | Session Room |
| CCNT | Course Content |
| STUD | Creator Studio |
| CMST | My Students (Creator) |
| CSES | Session History (Creator) |
| CEAR | Earnings Detail (Creator) |
| ADMN | Admin Dashboard |
| AUSR | Admin Users |
| ACRS | Admin Courses |
| AENR | Admin Enrollments |
| ASES | Admin Sessions |
| ACRT | Admin Certificates |
| APAY | Admin Payouts |

### P1 - Important (5 pages/screens)
| Code | Page Name |
|------|-----------|
| STDR | ST Directory |
| IFED | Instructor Feed |
| MODQ | Moderator Queue |
| CANA | Creator Analytics |
| ACAT | Admin Categories |

### P2 - Block 2+ (2 pages)
| Code | Page Name |
|------|-----------|
| CHAT | Course Chat (Goodwill) |
| HELP | Summon Help (Goodwill) |

### P3 - Future Consideration (3 pages)
| Code | Page Name |
|------|-----------|
| CNEW | Creator Newsletters |
| LEAD | Leaderboard |
| SUBCOM | Sub-Community |

---

## Connection Summary

*Quick reference for navigation paths. See individual page files for full details.*

### Primary User Journeys

**Visitor → Student Journey:**
```
HOME → CBRO → CDET → SGUP → LGIN → SBOK → SDSH
```

**Student → Learning Journey:**
```
SDSH → CCNT → SBOK → SROM → CCNT → (complete) → SDSH
```

**Student → ST Journey:**
```
SDSH → (certified) → TDSH → SROM → TDSH
```

**Creator Journey:**
```
LGIN → CDSH → STUD → (create course) → CDSH
```

**Creator Management Journey:**
```
CDSH → CMST (students) → CSES (sessions) → CANA (analytics) → CEAR (earnings)
```

**Admin Journey:**
```
LGIN → ADMN → AUSR/ACRS/AENR/ASES/ACRT/APAY/ACAT (SPA routes)
```

---

## Document History

| Date | Changes |
|------|---------|
| 2025-12-25 | Added 3 P3 pages: CNEW (Creator Newsletters), LEAD (Leaderboard), SUBCOM (Sub-Community) |
| 2025-12-25 | Added 11 pages: Creator (CMST, CSES, CANA, CEAR) + Admin screens (AUSR, ACRS, AENR, ASES, ACRT, APAY, ACAT) |
| 2025-12-25 | Initial creation with 27 pages, schema definition |
