# PeerLoop - Database Schema

**Version:** v1
**Last Updated:** 2025-12-23
**Status:** GATHER Phase - Accumulating from source documents
**Primary Source:** CD-021 (Database Schema Sample)

> This document accumulates database schema requirements during GATHER phase. During RUN phase, scenarios may have variations based on technology choices.

---

## Entity Overview

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   users     │────<│enrollments  │>────│  courses    │
└─────────────┘     └─────────────┘     └─────────────┘
      │                                       │
      │ 1:N                              1:N  │
      ▼                                       ▼
┌─────────────┐                        ┌─────────────┐
│qualifications│                        │ curriculum  │
└─────────────┘                        │  (modules)  │
      │                                └─────────────┘
      │ 1:N                                   │
      ▼                                       ▼
┌─────────────┐                        ┌─────────────┐
│  expertise  │                        │ objectives  │
│   (tags)    │                        └─────────────┘
└─────────────┘                               │
                                              ▼
                                       ┌─────────────┐
                                       │  includes   │
                                       └─────────────┘
```

---

## Core Entities

### users

Primary user table supporting multiple roles (Student, Student-Teacher, Creator, Admin, Moderator).

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | CD-021 | Primary key |
| email | string | Yes | US-P007 | Unique, for auth |
| password_hash | string | Yes | US-P007 | Hashed password |
| name | string | Yes | CD-021 | Display name |
| handle | string | Yes | CD-018 | Unique @handle (e.g., @gabriel) |
| title | string | No | CD-021 | Professional title |
| avatar_url | string | No | CD-021 | Profile image URL |
| bio | text | No | CD-021 | Extended biography |
| bio_short | string(160) | No | CD-018 | Short bio for cards |
| teaching_philosophy | text | No | CD-025 | Instructor's teaching approach (for creators) |
| website | string | No | CD-021 | External website URL |
| role | enum | Yes | CD-003 | primary role: student, student_teacher, creator, admin, moderator |
| is_creator | boolean | Yes | CD-017 | Can create courses |
| is_student_teacher | boolean | Yes | CD-018 | Available to teach |
| is_admin | boolean | Yes | CD-003 | Platform admin |
| is_moderator | boolean | Yes | CD-010 | Community moderator |
| privacy_public | boolean | Yes | CD-018 | Profile visibility toggle |
| email_verified | boolean | Yes | US-P013 | Email verification status |
| created_at | timestamp | Yes | - | Record creation |
| updated_at | timestamp | Yes | - | Last update |

**Indexes:** email (unique), handle (unique)

**Source:** CD-021 (instructorsDatabase), CD-018 (Student Profile System)

---

### user_qualifications

Creator/instructor credentials and certifications.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| user_id | uuid | Yes | CD-021 | FK to users |
| sentence | text | Yes | CD-021 | Full credential statement |
| display_order | int | Yes | - | Sort order on profile |
| created_at | timestamp | Yes | - | Record creation |

**Source:** CD-021 (qualifications array)

---

### user_expertise

Expertise/specialty tags for creators and student-teachers.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| user_id | uuid | Yes | CD-021 | FK to users |
| tag | string | Yes | CD-021 | Expertise tag (e.g., "AI Prompting") |

**Indexes:** user_id, tag (unique together)

**Source:** CD-021 (expertise array), US-C036

---

### user_stats

Aggregated statistics for users (may be computed view or cached).

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| user_id | uuid | Yes | CD-021 | FK to users, primary key |
| students_taught | int | Yes | CD-021 | Total students taught |
| courses_created | int | Yes | CD-021 | Courses created (creators) |
| courses_completed | int | Yes | - | Courses completed (students) |
| average_rating | decimal | Yes | CD-021 | Average rating received |
| total_reviews | int | Yes | CD-021 | Total reviews received |
| updated_at | timestamp | Yes | - | Last calculation |

**Note:** Consider implementing as computed view for real-time accuracy.

**Source:** CD-021 (stats object), CD-018

---

### user_interests

Student interest tags for content matching.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| user_id | uuid | Yes | CD-018 | FK to users |
| tag | string | Yes | CD-018 | Interest tag |

**Source:** CD-018 (3-5 interest tags per student)

---

### follows

Social graph - who follows whom.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| follower_id | uuid | Yes | CD-018 | FK to users (who is following) |
| followed_id | uuid | Yes | CD-018 | FK to users (who is followed) |
| created_at | timestamp | Yes | - | When follow occurred |

**Indexes:** follower_id, followed_id (unique together)

**Source:** CD-018 (social graph), US-S048

---

### course_follows

Users following courses (not enrolled, just following).

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| user_id | uuid | Yes | CD-018 | FK to users |
| course_id | uuid | Yes | CD-018 | FK to courses |
| created_at | timestamp | Yes | - | When follow occurred |

**Source:** CD-018, US-S006 (Follow Course action)

---

## Course Entities

### courses

Core course information.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | CD-021 | Primary key |
| creator_id | uuid | Yes | CD-021 | FK to users (instructorId) |
| title | string | Yes | CD-021 | Course title |
| slug | string | Yes | CD-025 | URL-friendly identifier (e.g., "intro-to-claude-code") |
| tagline | string(150) | No | CD-025 | Short marketing text (e.g., "Master AI-powered coding...") |
| description | text | Yes | CD-021 | Extended description |
| duration | string | Yes | CD-021 | Human-readable (e.g., "6 weeks") |
| duration_weeks | int | No | CD-021 | Numeric weeks for filtering |
| total_duration | string | No | CD-025 | Total time (e.g., "3 hours") for short courses |
| session_count | int | No | CD-025 | Number of live sessions (e.g., 2) |
| module_count | int | No | CD-025 | Number of modules |
| lesson_count | int | No | CD-025 | Number of lessons |
| format | string | No | CD-025 | Delivery format (e.g., "Live 1-on-1 sessions") |
| level | enum | Yes | CD-021 | beginner, intermediate, advanced |
| price_cents | int | Yes | CD-021 | Price in cents (e.g., 39900 = $399) |
| currency | string(3) | Yes | CD-025 | Currency code (e.g., "USD") - default "USD" |
| thumbnail_url | string | No | CD-021 | Course image URL |
| category_id | uuid | Yes | CD-021 | FK to categories |
| rating | decimal | No | CD-021 | Average rating (4.5-5.0) |
| rating_count | int | No | CD-022 | Number of reviews for this course |
| student_count | int | Yes | CD-021 | Enrollment count |
| badge | enum | No | CD-022 | Promotional badge: popular, new, bestseller, featured, null |
| lifetime_access | boolean | Yes | CD-025 | Lifetime access to materials (default true) |
| has_certificate | boolean | Yes | CD-025 | Awards certificate on completion |
| certificate_name | string | No | CD-025 | Certificate title (e.g., "Certificate of Completion") |
| is_active | boolean | Yes | CD-004 | Course available for enrollment |
| is_retired | boolean | Yes | US-C004 | Course retired by creator |
| created_at | timestamp | Yes | - | Record creation |
| updated_at | timestamp | Yes | - | Last update |

**Indexes:** creator_id, category_id, level, is_active, slug (unique)

**Source:** CD-021 (coursesDatabase), CD-025 (real course data)

---

### categories

Course category taxonomy.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| name | string | Yes | CD-021 | Category name |
| slug | string | Yes | - | URL-friendly name |
| display_order | int | Yes | - | Sort order |

**Sample data from CD-021:** AI & Product Management, Machine Learning, Computer Vision, NLP, Data Science, Business Analytics, Backend Development, Cloud Computing, Full-Stack Development, DevOps, System Design, AI & Robotics, AI in Healthcare, AI Coding, AI & Prompt Engineering

**Source:** CD-021 (category field), US-S058

---

### course_tags

Course topic tags for search and filtering.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| course_id | uuid | Yes | CD-021 | FK to courses |
| tag | string | Yes | CD-021 | Topic tag |

**Source:** CD-021 (tags array)

---

### course_objectives

Learning objectives ("What you'll learn").

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| course_id | uuid | Yes | CD-021 | FK to courses |
| objective | text | Yes | CD-021 | Learning objective statement |
| display_order | int | Yes | - | Sort order |

**Source:** CD-021 (learningObjectives array), US-S059

---

### course_includes

What's included with the course.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| course_id | uuid | Yes | CD-021 | FK to courses |
| item | string | Yes | CD-021 | Included item description |
| display_order | int | Yes | - | Sort order |

**Sample items from CD-021:** Full course access, 1-on-1 peer teaching sessions, Certificate on completion, Lifetime access to materials, Access to prompt library templates, Discord community access

**Source:** CD-021 (includes array), US-S060

---

### course_prerequisites

Course prerequisites with tiered categorization (from CD-025).

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| course_id | uuid | Yes | CD-025 | FK to courses |
| type | enum | Yes | CD-025 | required, nice_to_have, not_required |
| content | string | Yes | CD-025 | Prerequisite statement |
| display_order | int | Yes | - | Sort order within type |

**Sample data from CD-025 (Intro to Claude Code):**
- **required:** "Computer with terminal (Windows or Mac)", "Claude account (Pro or Max plan)"
- **nice_to_have:** "Basic computer navigation skills"
- **not_required:** "No coding experience needed", "No command-line knowledge required"

**Source:** CD-025 (prerequisites section)

---

### course_target_audience

Who the course is designed for.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| course_id | uuid | Yes | CD-025 | FK to courses |
| description | string | Yes | CD-025 | Target audience description |
| display_order | int | Yes | - | Sort order |

**Sample data from CD-025:**
- "Non-coders wanting to use AI for development"
- "Vibe coders looking to enhance productivity"
- "Professionals wanting to automate tasks with AI"
- "Beginners curious about AI coding tools"

**Source:** CD-025 (target_audience section)

---

### course_testimonials

Student testimonials for courses.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| course_id | uuid | Yes | CD-025 | FK to courses |
| quote | text | Yes | CD-025 | Testimonial quote |
| student_name | string | Yes | CD-025 | Student first name |
| student_role | string | No | CD-025 | Student role/title (e.g., "Course Graduate", "Entrepreneur") |
| is_featured | boolean | Yes | - | Show on course page |
| created_at | timestamp | Yes | - | When submitted |

**Sample data from CD-025:**
- "I went from knowing nothing about coding to building my first web app in just two sessions." - Sarah, Course Graduate
- "The hands-on approach is perfect. You're not just watching - you're building real things from day one." - Marcus, Now a Student-Teacher

**Source:** CD-025 (curriculum.md testimonials section)

---

### course_curriculum

Course modules/lessons structure.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| course_id | uuid | Yes | CD-021 | FK to courses |
| session_number | int | No | CD-025 | Live session grouping (e.g., 1, 2) |
| title | string | Yes | CD-021 | Module title |
| description | text | Yes | CD-021 | Module description |
| duration | string | Yes | CD-021 | Duration (e.g., "2h 30min", "Week 1", "20 min") |
| learning_objectives | text | No | CD-025 | Module-level objectives (bullet points or JSON array) |
| topics_covered | text | No | CD-025 | Topics covered in module (bullet points or JSON array) |
| hands_on_exercise | text | No | CD-025 | Description of hands-on exercise |
| video_count | int | No | CD-021 | Number of videos |
| reading_count | int | No | CD-021 | Number of readings |
| has_assessment | boolean | No | CD-021 | Module has assessment |
| module_order | int | Yes | - | Sort order within course |
| video_url | string | No | CD-019 | External video link (YouTube/Vimeo) |
| document_url | string | No | CD-019 | External doc link (Google Drive/Notion) |

**Note:** `session_number` groups modules for live session courses (e.g., Session 1 contains modules 1-4, Session 2 contains modules 5-7).

**Source:** CD-021 (curriculum array), CD-019 (Course Content Delivery), CD-025 (real course data)

---

### peerloop_features

PeerLoop-specific course features (1-on-1 teaching model).

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| course_id | uuid | Yes | CD-021 | FK to courses, primary key |
| one_on_one_teaching | boolean | Yes | CD-021 | Supports 1-on-1 peer teaching |
| certified_teachers | boolean | Yes | CD-021 | Has certified Student-Teachers |
| earn_while_teaching | boolean | Yes | CD-021 | Students can earn by teaching |
| teacher_commission | int | Yes | CD-021 | Commission % (e.g., 70) |

**Source:** CD-021 (peerloopFeatures object)

---

## Enrollment & Progress

### enrollments

Student course enrollments.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| student_id | uuid | Yes | - | FK to users |
| course_id | uuid | Yes | - | FK to courses |
| student_teacher_id | uuid | No | US-S061 | FK to users (assigned ST) |
| status | enum | Yes | - | enrolled, in_progress, completed, cancelled |
| enrolled_at | timestamp | Yes | - | Enrollment date |
| completed_at | timestamp | No | - | Completion date |
| cancelled_at | timestamp | No | - | Cancellation date |
| cancel_reason | text | No | US-S015 | Reason for cancellation |

**Source:** CD-003, CD-019

---

### module_progress

Student progress through course modules.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| enrollment_id | uuid | Yes | - | FK to enrollments |
| module_id | uuid | Yes | - | FK to course_curriculum |
| is_complete | boolean | Yes | CD-019 | Self-marked completion |
| completed_at | timestamp | No | - | When marked complete |

**Source:** CD-019 (checkbox progress tracking), US-S055

---

### student_teachers

Student-Teacher certifications per course.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| user_id | uuid | Yes | CD-021 | FK to users |
| course_id | uuid | Yes | CD-021 | FK to courses |
| certified_date | date | Yes | CD-021 | When certified |
| students_taught | int | Yes | CD-021 | Count of students taught |
| is_active | boolean | Yes | - | Currently accepting students |
| approved_by | uuid | Yes | CD-012 | FK to users (creator who approved) |

**Source:** CD-021 (studentTeachers array), CD-018

---

## Sessions & Scheduling

### availability

Teacher availability slots.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| user_id | uuid | Yes | CD-015 | FK to users (ST or Creator) |
| day_of_week | int | Yes | - | 0-6 (Sunday-Saturday) |
| start_time | time | Yes | - | Slot start time |
| end_time | time | Yes | - | Slot end time |
| timezone | string | Yes | US-P022 | User's timezone |
| is_recurring | boolean | Yes | - | Weekly recurring slot |

**Source:** CD-015 (Calendar/Scheduling), US-C006, US-T001

---

### sessions

Booked tutoring sessions.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| enrollment_id | uuid | Yes | - | FK to enrollments |
| teacher_id | uuid | Yes | - | FK to users (ST or Creator) |
| student_id | uuid | Yes | - | FK to users |
| scheduled_start | timestamp | Yes | CD-015 | Session start time |
| scheduled_end | timestamp | Yes | - | Session end time |
| status | enum | Yes | - | scheduled, in_progress, completed, cancelled |
| bbb_meeting_url | string | No | CD-014 | BBB/video meeting link |
| recording_url | string | No | US-V005 | Session recording URL |
| cancelled_by | uuid | No | - | FK to users (who cancelled) |
| cancel_reason | text | No | - | Cancellation reason |
| created_at | timestamp | Yes | - | Booking time |

**Source:** CD-014 (Video Conferencing), CD-015 (Calendar/Scheduling)

---

### session_assessments

Post-session mutual assessments.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| session_id | uuid | Yes | - | FK to sessions |
| assessor_id | uuid | Yes | US-V006 | FK to users (who gave assessment) |
| assessee_id | uuid | Yes | - | FK to users (who received) |
| rating | int | Yes | - | 1-5 stars |
| comment | text | No | - | Optional feedback |
| created_at | timestamp | Yes | - | Assessment time |

**Source:** CD-003 (US-V006), CD-018

---

## Payments & Transactions

### transactions

Payment records.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| enrollment_id | uuid | Yes | - | FK to enrollments |
| amount_cents | int | Yes | CD-020 | Total payment amount |
| stripe_payment_id | string | Yes | CD-020 | Stripe transaction ID |
| status | enum | Yes | - | pending, completed, refunded, failed |
| paid_at | timestamp | No | - | Payment confirmation time |
| created_at | timestamp | Yes | - | Record creation |

**Source:** CD-020 (Payment & Escrow)

---

### payment_splits

Revenue split tracking (70/15/15).

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| transaction_id | uuid | Yes | - | FK to transactions |
| recipient_id | uuid | Yes | CD-020 | FK to users |
| recipient_type | enum | Yes | - | platform, creator, student_teacher |
| amount_cents | int | Yes | CD-020 | Split amount |
| percentage | int | Yes | CD-020 | Split % (15, 15, or 70) |
| status | enum | Yes | - | pending, released, paid |
| released_at | timestamp | No | - | When released from escrow |
| paid_at | timestamp | No | - | When paid out |

**Source:** CD-020 (70/15/15 split), CD-001

---

### payouts

Payout records to recipients.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| recipient_id | uuid | Yes | - | FK to users |
| amount_cents | int | Yes | CD-020 | Payout amount |
| stripe_transfer_id | string | No | CD-020 | Stripe transfer ID |
| status | enum | Yes | - | pending, processing, completed, failed |
| approved_by | uuid | Yes | CD-020 | FK to users (admin who approved) |
| approved_at | timestamp | Yes | - | Approval time |
| paid_at | timestamp | No | - | Payment time |
| created_at | timestamp | Yes | - | Record creation |

**Source:** CD-020 (Admin payout dashboard)

---

## Certificates

### certificates

Issued certificates.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| user_id | uuid | Yes | - | FK to users |
| course_id | uuid | Yes | - | FK to courses |
| type | enum | Yes | CD-011 | completion, mastery, teaching |
| issued_at | timestamp | Yes | - | Issue date |
| issued_by | uuid | Yes | CD-012 | FK to users (creator who issued) |
| recommended_by | uuid | No | CD-012 | FK to users (ST who recommended) |
| certificate_url | string | No | - | Generated certificate file |

**Source:** CD-011 (dual certificate system), CD-012, US-S021, US-S022, US-S032

---

## Feed Access (from CD-024)

### instructor_followers

Track users who have ever purchased any course from an instructor (grants instructor feed access).

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| instructor_id | uuid | Yes | CD-024 | FK to users (creator) |
| follower_id | uuid | Yes | CD-024 | FK to users (student) |
| first_enrollment_at | timestamp | Yes | CD-024 | When first course was purchased |
| created_at | timestamp | Yes | - | Record creation |

**Note:** Created automatically when a user enrolls in any course from an instructor. Used to determine instructor feed access.

**Indexes:** instructor_id, follower_id (unique together)

**Source:** CD-024, US-P084

---

### promoted_posts

Posts promoted from course feeds to the main Peer Loop feed (using goodwill points).

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| post_id | uuid | Yes | CD-024 | FK to posts |
| promoted_by | uuid | Yes | CD-024 | FK to users |
| points_spent | int | Yes | CD-024 | Goodwill points used for promotion |
| promoted_at | timestamp | Yes | - | When promoted |
| expires_at | timestamp | No | - | When promotion ends (optional) |

**Source:** CD-024, US-P085

---

## Community Feed

### posts

Community feed posts.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| author_id | uuid | Yes | CD-013 | FK to users |
| course_id | uuid | No | CD-013 | FK to courses (if course-specific) |
| content | text | Yes | CD-013 | Post content |
| post_type | enum | Yes | CD-013 | post, announcement, teaching_tip, availability |
| is_pinned | boolean | Yes | CD-013 | Pinned by moderator/creator |
| parent_id | uuid | No | - | FK to posts (for replies) |
| created_at | timestamp | Yes | - | Post time |
| updated_at | timestamp | No | - | Edit time |

**Note:** Will integrate with getstream.io for feed infrastructure.

**Source:** CD-013 (Community Feed)

---

### post_interactions

Likes, bookmarks, reposts.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| post_id | uuid | Yes | CD-013 | FK to posts |
| user_id | uuid | Yes | CD-013 | FK to users |
| type | enum | Yes | CD-013 | like, bookmark, repost |
| created_at | timestamp | Yes | - | Interaction time |

**Source:** CD-013, US-S037, US-S038, US-S040

---

### content_flags

Flagged content for moderation.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| post_id | uuid | Yes | CD-013 | FK to posts |
| flagged_by | uuid | Yes | CD-013 | FK to users |
| reason | text | Yes | - | Flag reason |
| status | enum | Yes | - | pending, reviewed, dismissed, actioned |
| reviewed_by | uuid | No | - | FK to users (moderator) |
| reviewed_at | timestamp | No | - | Review time |
| created_at | timestamp | Yes | - | Flag time |

**Source:** CD-013, US-S041, US-M009

---

## Messaging

### conversations

Direct message conversations.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| created_at | timestamp | Yes | - | Conversation start |
| updated_at | timestamp | Yes | - | Last message time |

**Source:** CD-002, US-S019

---

### conversation_participants

Who is in each conversation.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| conversation_id | uuid | Yes | - | FK to conversations |
| user_id | uuid | Yes | - | FK to users |
| joined_at | timestamp | Yes | - | When joined |
| last_read_at | timestamp | No | - | Last read timestamp |

---

### messages

Individual messages.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| conversation_id | uuid | Yes | - | FK to conversations |
| sender_id | uuid | Yes | - | FK to users |
| content | text | Yes | - | Message content |
| created_at | timestamp | Yes | - | Send time |

**Source:** CD-003, US-S016, US-S017, US-S018

---

## Employer/Funder

### employer_sponsorships

Employer-sponsored enrollments.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| employer_id | uuid | Yes | CD-003 | FK to users (employer) |
| student_id | uuid | Yes | - | FK to users |
| enrollment_id | uuid | Yes | - | FK to enrollments |
| created_at | timestamp | Yes | - | Sponsorship date |

**Source:** CD-003 (Employer/Funder role), US-E001

---

## Notifications

### notifications

User notifications.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| user_id | uuid | Yes | - | FK to users |
| type | enum | Yes | - | session_reminder, payment, message, certificate, etc. |
| title | string | Yes | - | Notification title |
| body | text | Yes | - | Notification body |
| action_url | string | No | - | Click target URL |
| is_read | boolean | Yes | - | Read status |
| created_at | timestamp | Yes | - | Notification time |

**Source:** US-P017, US-P018

---

## Goodwill Points System (Block 2+)

*Note: Not MVP - Goodwill points are a community currency replacing 5-star reviews.*

### user_goodwill

Goodwill point balances per user.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| user_id | uuid | Yes | CD-023 | FK to users, primary key |
| total_earned | int | Yes | CD-023 | Lifetime total (public) |
| balance | int | Yes | CD-023 | Available to give (private) |
| spent | int | Yes | CD-023 | Given to others (private) |
| last_awarded_to_user_id | uuid | No | CD-023 | Anti-gaming tracking |
| last_awarded_at | timestamp | No | CD-023 | Cooldown tracking |
| updated_at | timestamp | Yes | - | Last update |

**Formula:** `balance = total_earned - spent`

**Source:** CD-023

---

### goodwill_transactions

Transaction log for all goodwill point transfers.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| from_user_id | uuid | No | CD-023 | FK to users (null for system awards) |
| to_user_id | uuid | Yes | CD-023 | FK to users (recipient) |
| points | int | Yes | CD-023 | Points transferred (5-100) |
| reason | enum | Yes | CD-023 | Transaction reason |
| course_id | uuid | No | CD-023 | FK to courses (if course-related) |
| summon_id | uuid | No | CD-023 | FK to help_summons (if from summon) |
| created_at | timestamp | Yes | - | Transaction time |

**Reason Enum:**
- `summon_help` - Responded to a Summon request (10-25 points)
- `question_answer` - Answered a question in chat (5 points)
- `first_session_mentor` - Helped new S-T through first session (50 points)
- `referral` - Referred a student who enrolled (100 points)
- `remedial_volunteer` - Volunteered for remedial session (30 points)
- `availability_bonus` - Daily bonus for being available (5 points)

**Source:** CD-023

---

### help_summons

Help summon requests from students to S-Ts.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| student_id | uuid | Yes | CD-023 | FK to users (requester) |
| course_id | uuid | Yes | CD-023 | FK to courses |
| module_id | uuid | No | CD-023 | FK to course_curriculum (specific module) |
| status | enum | Yes | CD-023 | pending, responded, completed, cancelled |
| responder_id | uuid | No | CD-023 | FK to users (S-T who responded) |
| responded_at | timestamp | No | - | When S-T responded |
| completed_at | timestamp | No | - | When session completed |
| points_awarded | int | No | CD-023 | Points given (10-25) |
| session_duration_mins | int | No | CD-023 | Duration for 5-min minimum check |
| created_at | timestamp | Yes | - | Summon request time |

**Status Flow:** pending → responded → completed (or cancelled)

**Source:** CD-023

---

### user_availability

S-T availability status for help summons.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| user_id | uuid | Yes | CD-023 | FK to users, primary key |
| is_available | boolean | Yes | CD-023 | "Available to Help" toggle |
| last_available_at | timestamp | No | CD-023 | For daily availability bonus |
| updated_at | timestamp | Yes | - | Status change time |

**Source:** CD-023

---

### goodwill_rewards

Reward thresholds and unlocks.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| points_threshold | int | Yes | CD-023 | Points required (500, 1000, 2500, 5000) |
| reward_type | enum | Yes | CD-023 | badge, discount, free_session, revenue_bonus |
| reward_value | string | Yes | CD-023 | "Community Helper", "10%", "5%" |
| description | text | Yes | CD-023 | Reward description |

**Thresholds (from CD-023):**
- 500 points → Badge: "Community Helper"
- 1,000 points → 10% discount on next course
- 2,500 points → Free 1-on-1 session with any Creator
- 5,000 points → Revenue share bonus (extra 5% on teaching)

**Source:** CD-023

---

### user_reward_unlocks

Track which users have unlocked which rewards.

| Field | Type | Required | Source | Notes |
|-------|------|----------|--------|-------|
| id | uuid | Yes | - | Primary key |
| user_id | uuid | Yes | CD-023 | FK to users |
| reward_id | uuid | Yes | CD-023 | FK to goodwill_rewards |
| unlocked_at | timestamp | Yes | - | When unlocked |
| redeemed_at | timestamp | No | - | When used (if applicable) |

**Source:** CD-023

---

## Document Lineage

| Source Document | Entities Derived |
|-----------------|------------------|
| CD-021 | users, user_qualifications, user_expertise, user_stats, courses, categories, course_tags, course_objectives, course_includes, course_curriculum, peerloop_features, student_teachers |
| CD-022 | courses.rating_count, courses.badge (new fields) |
| CD-023 | user_goodwill, goodwill_transactions, help_summons, user_availability, goodwill_rewards, user_reward_unlocks |
| CD-024 | instructor_followers, promoted_posts (feed access states, feed promotion) |
| CD-025 | courses (12 new fields: slug, tagline, currency, format, etc.), course_prerequisites, course_target_audience, course_testimonials, course_curriculum (session_number, learning_objectives, etc.), users.teaching_philosophy |
| CD-018 | user_interests, follows, course_follows, privacy fields |
| CD-019 | module_progress, external video/doc URLs |
| CD-020 | transactions, payment_splits, payouts |
| CD-015 | availability, sessions |
| CD-014 | sessions (BBB fields), session recordings |
| CD-013 | posts, post_interactions, content_flags |
| CD-003 | enrollments, certificates, messages, employer_sponsorships |
| CD-011 | certificate types (mastery vs completion) |

---

## Notes for Implementation

1. **UUIDs vs Integer IDs:** UUIDs recommended for distributed systems and security
2. **Timestamps:** Use UTC, handle timezone display in application layer
3. **Soft Deletes:** Consider `deleted_at` columns for audit trail
4. **Computed Fields:** user_stats may be better as computed view
5. **getstream.io:** Posts/feed may be managed externally; local tables for reference data
6. **Stripe:** transactions link to Stripe via payment_id for reconciliation

---

## Schema Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2025-12-23 | Initial schema from CD-021 analysis |
