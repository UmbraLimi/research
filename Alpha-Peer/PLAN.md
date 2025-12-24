# Alpha Peer - Research & Planning Roadmap

**Goal:** Produce a comprehensive SPECS.md document that can be handed off to Claude Code for Alpha Peer development.

**Last Updated:** 2025-12-24

---

## Project Phases Overview

| Phase | Name | Status | Description |
|-------|------|--------|-------------|
| **GATHER** | Information Collection | 🔥 IN PROGRESS | Collect client docs, research services, document user stories, build architecture docs |
| **RUN** | Scenario Generation | ⏳ PENDING | Finalize architecture docs, create SPECS.md scenarios from gathered information |

**RUN Phase Breakdown:**
- Phase 3: Architecture Finalization (DB-SCHEMA, PAGES, COMPONENTS, API)
- Phase 4: Scenario Creation
- Phase 5: Final Selection & Handoff

---

## Current Status

### 🎯 Next Step: Review RUN-001 Scenario

**Your task:** Review `runs/run-001/scenario.md` and provide feedback.

**When you resume:**
1. Open `runs/run-001/scenario.md` in your IDE
2. Review the 14 sections (especially: Tech Stack, Scope, Architecture)
3. Note any questions, concerns, or changes needed
4. We'll document your feedback in `runs/run-001/review-notes.md`
5. Then decide: Approve, revise, or create RUN-002

**Quick review checklist:**
- [ ] Technology stack appropriate?
- [ ] Scope (144 P0 stories) achievable in 4 months?
- [ ] Assumptions acceptable for open questions?
- [ ] Block sequence makes sense?
- [ ] Any missing requirements?

---

| Metric | Value |
|--------|-------|
| Current Phase | **RUN Phase** - RUN-001 Under Review |
| Client Docs Processed | 33 (CD-001 to CD-033) |
| Goals Documented | 27 (GO-001 to GO-027) |
| User Stories Created | 329 (144 P0, 106 P1, 71 P2, 8 P3) |
| User Roles | 9 (incl. Visitor/Guest) |
| Tech Docs Created | 7 (tech-001 to tech-006, comp-001) |
| Directives Created | 6 (DIR-001 to DIR-006) |
| Architecture Docs | 4 (DB-SCHEMA, PAGES, COMPONENTS, API) |
| **Runs Created** | **1 (RUN-001 - Under Review)** |
| Doc Versions | GOALS v3, USER-STORIES v8, DIRECTIVES v1, CLAUDE v3 |
| Budget | $75,000 (from CD-008) |
| Timeline | **4 months** (fixed; feature removal if scope exceeds) |
| Domain | peerloop.com (live on Cloudflare) |
| Open Questions | 21 open, 3 deferred, 2 resolved (see `QUESTIONS-FOR-BRIAN.md`) |

---

# GATHER PHASE

*Collect all information needed to create comprehensive technical specifications.*

## Phase 1: Discovery & Context Gathering ✅ COMPLETE

### 1.1 - Client Document Analysis ✅
- [x] Process all client-provided documents (11 docs)
  - CD-001: Business Plan - revenue model, flywheel, go-to-market
  - CD-002: Feature Summary - UI/UX mockups, tech stack, navigation
  - CD-003: User Stories - role-based needs, 6 user types
  - CD-004: Impact Filter - mission, success metrics, vision
  - CD-005: Slack - GetStream feed discussion (Nov 13)
  - CD-006: Slack - Calendar, BBB, Discord (Nov 16)
  - CD-007: Slack - P2P video alternatives: Daily.co, Digital Samba (Nov 18)
  - CD-008: Meeting - Budget $75K, 4mo timeline, Skool prototype, feeds-only Stream (Nov 26)
  - CD-009: Slack - Blindside Networks for BBB, peerloop.com on Cloudflare (Nov 28)
  - CD-010: Miro - Main Activities by Role (5 roles, pain points, Community Moderator NEW)
  - CD-011: Miro - Drivers & Action Items (user motivations, Bluesky confirmed, mastery cert)
- [x] Extract business requirements and constraints → GOALS.md
- [x] Identify user personas and their needs → USER-STORIES.md (7 roles including Community Moderator)
- [x] Document competing or evolving goals across documents → Goal Index table
- [x] Create timeline of document priorities (newer supersedes older)

### 1.2 - Vision & Scope Definition ✅
- [x] Define Alpha Peer's core value proposition → GOALS.md Mission Statement
- [x] Identify primary user personas → 6 roles in USER-STORIES.md
- [x] Establish project boundaries (what's in/out of scope) → MVP = 3 creators, Genesis Cohort
- [x] Document success criteria → GO-005, GO-006, GO-007 (quantified targets)

---

## Phase 2: User Stories & Requirements 🔥 IN PROGRESS

### 2.1 - Core User Stories 🔥 WIP
- [x] Create user stories for primary workflows (105 stories extracted)
- [x] Prioritize stories (MVP vs future) - P0/P1/P2/P3 assigned
- [ ] Define acceptance criteria for P0 stories
- [ ] Identify dependencies between stories
- [ ] Create detailed story files for complex P0 stories

### 2.2 - Non-Functional Requirements
- [ ] Define performance expectations (from CD-004 metrics)
- [ ] Document security requirements (payments, user data)
- [ ] Establish scalability needs (50+ Student-Teachers per creator)
- [ ] Specify reliability/uptime requirements (video sessions)

---

## Phase 2.5: Third-Party Integrations Inventory 📋 NEW

**Purpose:** Catalog all JavaScript packages and third-party services to determine which user stories they can fulfill.

**Context:**
- Final app: React.js with Astro.js, Tailwind CSS
- Deployment: Cloudflare (preferred) or Vercel
- Some services are **required** (client-specified), others are **optional**

### Required Services (Client-Specified)
| Service | Type | Research Doc | User Stories Covered |
|---------|------|--------------|---------------------|
| Big Blue Button | Video Conferencing | `tech-001-bigbluebutton.md` | US-V001-V007, US-A013-A018, US-T007 |
| Stream | Chat/Activity Feeds | `tech-002-stream.md` | US-S016-S019, US-S025, US-C017, US-P002 |

### Video Conferencing Alternatives (From CD-007)
| Service | Type | Research Doc | Notes |
|---------|------|--------------|-------|
| Daily.co | P2P Video SDK | *pending* | Auto P2P switching, 10K free mins/mo |
| Digital Samba | Low-code Video | *pending* | Iframe embed, 10K free mins/mo |
| VideoSDK.live | Budget Video | *pending* | $0.003/min at scale |

**⚠️ Decision Needed:** BBB vs P2P solutions for 1:1 sessions (see CD-006, CD-007)

### Framework & Deployment Stack
| Technology | Type | Research Doc | Status |
|------------|------|--------------|--------|
| Astro.js | Meta-Framework | `tech-003-astrojs.md` | Preferred |
| React.js | UI Library | `tech-004-reactjs.md` | Confirmed |
| Tailwind CSS | CSS Framework | `tech-005-tailwindcss.md` | Confirmed |
| Cloudflare | Deployment/CDN | `comp-001-cloudflare-vs-vercel.md` | Preferred |
| Vercel | Deployment/CDN | `comp-001-cloudflare-vs-vercel.md` | Alternative |

### Optional Services (To Be Evaluated)
| Service | Type | Research Doc | User Stories Covered |
|---------|------|--------------|---------------------|
| *TBD* | Payment Processing | *pending* | US-P026-P033, US-A005, US-A006, US-S002 |
| *TBD* | LMS Integration | *pending* | US-C001-C003 |
| *TBD* | Email/Notifications | *pending* | US-P014-P019, US-A010-A012 |
| *TBD* | Authentication | *pending* | US-P007-P013 |
| *TBD* | Analytics | *pending* | US-A019-A025 |
| *TBD* | Calendar/Scheduling | *pending* | US-P020-P025, US-C006, US-T001 |
| *TBD* | AI Transcription | *pending* | US-V008-V011, US-A015, US-V007 |
| *TBD* | Database | *pending* | US-P034-P037 |
| *TBD* | File/Object Storage | *pending* | US-P038-P045 |
| *TBD* | Image Optimization | *pending* | US-P046-P050 |

### 2.5.1 - Core Research ✅ COMPLETE
- [x] Research Big Blue Button capabilities → `tech-001-bigbluebutton.md`
- [x] Research Stream capabilities → `tech-002-stream.md`
- [x] Research Astro.js for React → `tech-003-astrojs.md`
- [x] Document React.js considerations → `tech-004-reactjs.md`
- [x] Document Tailwind CSS integration → `tech-005-tailwindcss.md`
- [x] Compare Cloudflare vs Vercel → `comp-001-cloudflare-vs-vercel.md`

### 2.5.2 - User Story Mapping
- [x] Map Big Blue Button features to video/session stories (US-V*, US-A013-A018)
- [x] Map Stream features to messaging/feed stories (US-S016-S019, US-S025, US-C017)
- [x] Identify gaps requiring additional services → Added 48 new stories (US-P007-P050, US-V008-V011)
- [ ] Create comparison docs for gap-filling options

### 2.5.3 - Gap-Filling Service Research

**Video Conferencing Alternatives (Priority - from CD-007):**
- [ ] Research Daily.co capabilities → P2P SDK, auto-switching, 10K free mins
- [ ] Research Digital Samba capabilities → Low-code iframe, Zoom-like UI
- [ ] Create comparison: BBB vs Daily.co vs Digital Samba → `comp-002-video-conferencing.md`

**Video Evaluation Criteria (Critical for 1:1 tutoring):**
- [ ] 1:1 optimization: P2P support, latency, cost efficiency for two-person sessions
- [ ] Recording capabilities:
  - Where are recordings stored? (provider cloud, our storage, participant download)
  - Recording format and quality options
  - How can each participant access/playback their session recording?
  - Retention period and storage costs
  - Privacy controls (who can access recordings)
- [ ] Integration with our file storage (US-P038-P042) for session recordings

**Other Services:**
- [ ] Research payment processing options (Stripe Connect) → US-P026-P033
- [ ] Research authentication options (Clerk, Auth.js, Supabase Auth) → US-P007-P013
- [ ] Research email/notification services (Resend, SendGrid) → US-P014-P019
- [ ] Research calendar/scheduling options (Cal.com, Calendly API) → US-P020-P025
- [ ] Research AI transcription services (Whisper, AssemblyAI) → US-V008-V011
- [ ] Research analytics options (Plausible, PostHog, Mixpanel) → US-A019-A025
- [ ] Research database options (Supabase, PlanetScale, Neon) → US-P034-P037
- [ ] Research file/object storage options (Cloudflare R2, S3, Supabase Storage) → US-P038-P045
- [ ] Research image optimization options (Cloudflare Images, Imgix, Cloudinary) → US-P046-P050

## GATHER Completion Criteria

- [x] All client documents processed (32 docs - CD-001 to CD-032)
- [x] All required services researched (BBB, Stream) → tech-001, tech-002
- [ ] All optional service categories researched (payment, auth, email, etc.) → **PARTIALLY DONE**
- [x] User stories mapped to technologies (325 stories with source traceability)
- [x] Gaps identified and documented (26 questions in QUESTIONS-FOR-BRIAN.md)
- [ ] Comparison docs created for key decisions → **PARTIALLY DONE** (only comp-001)

### GATHER Status: **NEARLY COMPLETE**

**What's done:**
- All 32 client documents processed and indexed
- 27 goals extracted with source traceability
- 325 user stories with priority and source
- 4 architecture docs (DB-SCHEMA, PAGES, COMPONENTS, API)
- 7 tech/comparison research docs
- 6 directives for scenario constraints
- 26 open questions documented for Brian

**What's incomplete (but not blocking for RUN phase):**
- Optional service research (payment, auth, email, calendar, AI transcription, analytics, database, storage)
  - These can be decided during scenario creation based on cost/complexity trade-offs
- Comparison docs for pending decisions (video platform BBB vs PlugNmeet, etc.)
  - Question #2/#3 in QUESTIONS-FOR-BRIAN.md covers this

### RUN Phase Readiness Assessment

**Can we start RUN phase?** Yes, with caveats.

**Critical items to resolve before/during RUN:**
1. ~~**Video Platform Decision** (Q#2, Q#3)~~ → **RESOLVED via interface abstraction** (see API.md "Video Platform Interface Contract")
2. ~~**Timeline Clarification** (Q#26)~~ → **RESOLVED: 4 months is fixed**, feature removal if scope doesn't fit
3. **S-T Pricing Visibility** (Q#23) - Affects enrollment funnel design

**Items that can be decided during scenario creation:**
- Payment processor (Stripe assumed, but alternatives exist)
- Authentication (Clerk, Auth.js, Supabase Auth)
- Email service (Resend, SendGrid)
- Calendar integration (Cal.com, Calendly API)
- Database (Supabase, PlanetScale, Neon)

**Recommendation:**
- Get Brian's answers to critical questions (#2, #3, #23, #26)
- Proceed to RUN Phase 3 (Architecture Finalization) in parallel
- Create scenarios with noted decision points for optional services

---

## Phase 2.8: Preparation Tasks (While Awaiting Final Docs) 🔄 OPTIONAL

**Purpose:** Productive work that can be done before final client documents arrive.

### 2.8.1 - Pre-Research Video Conferencing
- [ ] Research Daily.co capabilities and pricing
- [ ] Research Digital Samba capabilities and pricing
- [ ] Draft comparison framework (1:1 optimization, recording, cost, integration complexity)
- [ ] Note questions to clarify with client once docs arrive

### 2.8.2 - Draft PAGES.md Template
- [ ] Create empty PAGES.md with section structure
- [ ] Define page code naming convention
- [ ] List obvious pages from existing user stories (dashboards, auth, profiles, courses)
- [ ] Draft access matrix template with 9 user roles

### 2.8.3 - Review Existing User Stories
- [ ] Audit P0 stories for completeness and clarity
- [ ] Identify stories that imply specific pages
- [ ] Flag stories with unclear acceptance criteria
- [ ] Note potential story dependencies

### 2.8.4 - Non-Functional Requirements Draft
- [ ] Draft performance expectations based on video/real-time features
- [ ] Outline security requirements (payments, user data, video sessions)
- [ ] Document scalability targets (Genesis cohort 60-80, 50+ Student-Teachers per creator)
- [ ] List reliability requirements for critical paths (video, payments)

---

# RUN PHASE

*Transform gathered information into actionable SPECS.md scenarios.*

**Principles:**
- Later client docs override earlier ones (CD-004 > CD-003 > CD-002 > CD-001)
- Goal: Minimize custom development by leveraging existing services
- sc-001 is always the fully-custom baseline (no major SaaS)

## Phase 3: Architecture Documentation 🔄 PARTIALLY COMPLETE

**Purpose:** Create comprehensive architecture documents that map user stories and goals to database schema, pages, components, and API endpoints.

**Depends on:** Client docs processing (ongoing during GATHER)

### 3.1 - Architecture Documents Created ✅
- [x] **DB-SCHEMA.md** - Database entities, fields, relationships (30+ tables)
- [x] **PAGES.md** - Page inventory with data requirements (26 pages)
- [x] **COMPONENTS.md** - Reusable UI component library (39 components)
- [x] **API.md** - Backend API operations surface (60 endpoints)

### 3.2 - Ongoing Updates During GATHER
Architecture docs are now updated via `/r-add-client-doc`:
- [x] CD-021: Database Schema Sample → seeded all 4 docs
- [x] CD-022: Data Structures Doc → added ratingCount, badge fields + CourseBadge component
- [x] CD-023: Goodwill Points Spec → +6 tables, +2 pages, +9 components, +9 endpoints

### 3.3 - Page Inventory ✅ COMPLETE (Basic)
- [x] Identify all pages needed from client docs, goals, and user stories (26 pages)
- [x] Group pages by functional area (Public, Authenticated, Role-Specific)
- [x] Document data sources and user stories per page
- [ ] Assign 3-5 letter codes for easy cross-referencing (e.g., SDASH = Student Dashboard)

### 3.4 - Page Documentation ⏳ PENDING
For each page, complete documentation:
- [x] **Data Sources**: Which DB tables/entities feed this page
- [x] **Purpose**: Which user stories (US-*NNN) this page fulfills
- [ ] **Code**: 3-5 letter unique identifier for cross-referencing
- [ ] **Connections**: Links to other pages (with their codes) and navigation context

### 3.5 - Access Matrix ⏳ PENDING
- [ ] Create role × page access matrix showing which roles can see each page
- [ ] Document role-specific variations (e.g., Creator sees "My Students" vs Student sees "My Teachers")
- [ ] Identify shared pages with conditional content
- [ ] Note authentication requirements (public, logged-in, role-restricted)

### 3.6 - Navigation Patterns ⏳ PENDING
- [ ] Map primary navigation paths for each user role
- [ ] Identify dashboard-centric vs. content-centric flows
- [ ] Document cross-role touchpoints (where different roles interact on same pages)

### 3.7 - Multi-Role User Handling ⏳ PENDING
**Critical:** Users can hold multiple roles simultaneously (e.g., Student + Student-Teacher + Creator). Pages must accommodate this.

- [ ] Design unified dashboard that adapts to user's active roles
  - Sidebar menu sections per role (e.g., "My Learning", "My Teaching", "My Courses")
  - Or tabbed/sectioned layout within single page
  - Role-specific widgets/cards that appear conditionally
- [ ] Identify other pages requiring multi-role awareness
  - Profile pages (showing teaching credentials + learning progress)
  - Settings (role-specific preferences)
  - Notifications (aggregated across roles)
- [ ] Document role combination patterns
  - Student only (most users start here)
  - Student + Student-Teacher (graduated to teaching)
  - Student + Creator (also offers courses)
  - Student + Student-Teacher + Creator (full progression)
  - Admin combinations
- [ ] Define role-switching vs. role-aggregation UX
  - Do users "switch" active role, or see everything at once?
  - How to prevent overwhelm for multi-role users?
  - Mobile vs. desktop layout considerations

### 3.8 - Finalize for Scenario ⏳ PENDING (RUN Phase)
- [ ] Finalize architecture for selected scenario (may vary by tech choices)

**Output:** Complete architecture documents ready for scenario generation

---

## Phase 4: Scenario Creation 🔥 IN PROGRESS

**New RUN Structure:** Scenarios are now created through the `/runs/` system with full traceability.

### 4.1 - RUN-001: Stream + VideoProvider (sc-002) 🔥 UNDER REVIEW
- [x] Created run folder structure (`runs/run-001/`)
- [x] Documented inputs and parameters (`run-001.md`)
- [x] Snapshotted questions state (21 open, 3 deferred, 2 resolved)
- [x] Consulted research files (tech-001 through tech-006, comp-001)
- [x] Generated `scenario.md` - 14-section technical specification
- [x] Created run-specific assets:
  - `assets/video-platform-decisions.md` - VideoProvider interface, BBB vs PlugNmeet
  - `assets/stream-usage.md` - Stream.io feeds-only, 5 feed types
  - `assets/hosting-decisions.md` - Cloudflare stack (Pages, Workers, D1, R2)
  - `assets/payment-decisions.md` - Stripe Connect, 85/15 split
- [ ] Client review of scenario.md
- [ ] Document feedback in `review-notes.md`
- [ ] Decide: Approve, revise, or create RUN-002

### 4.2 - Future Runs (As Needed)
- [ ] RUN-002: If RUN-001 rejected or needs major changes
- [ ] RUN-003: Alternative scenarios as requested
- [ ] Compare runs using `runs/RUN-INDEX.md`

### 4.3 - Run Index
See `runs/RUN-INDEX.md` for status of all runs:
| Run | Status | Key Decisions |
|-----|--------|---------------|
| RUN-001 | Under Review | Stream + VideoProvider, Cloudflare stack, 144 P0 stories |

## Phase 5: Final Selection & Handoff ⏳ PENDING

### 5.1 - Client Review
- [ ] Present scenarios to client
- [ ] Gather feedback and preferences
- [ ] Make adjustments as requested

### 5.2 - Finalize SPECS.md
- [ ] Client selects final scenario
- [ ] Copy selected scenario to root `SPECS.md`
- [ ] Final review for completeness
- [ ] Handoff to implementation

---

## 🏁 Latest Completed

**2025-12-24 (Session 4):** RUN Phase Launch & RUN-001 Generation
- **Processed CD-033:** Slack conversation with Brian clarifying S-T pricing model
  - Resolved Question #23: Course price = S-T price (unified pricing, no Teacher premium)
  - Confirmed 85/15 revenue split
  - Clarified enrollment flow with S-T calendar and "Schedule Later" option
  - Added 4 new user stories (US-S083-S086)
- **Created `/runs/` folder structure:**
  - `RUN-INDEX.md` - Quick reference to all runs
  - `run-NNN/` folder pattern with run file, scenario, assets
  - Formalized checkpoint-based workflow
- **Generated RUN-001 (sc-002: Stream + VideoProvider):**
  - Created `run-001.md` with full input documentation
  - Snapshotted questions state (21 open, 3 deferred, 2 resolved)
  - Generated `scenario.md` - 14-section technical specification
  - Created 4 run-specific assets:
    - `video-platform-decisions.md` - VideoProvider interface abstraction
    - `stream-usage.md` - Feeds-only usage, 5 feed types
    - `hosting-decisions.md` - Cloudflare stack decisions
    - `payment-decisions.md` - Stripe Connect, 85/15 split
- **Established Two-Tier Knowledge System:**
  - Global research (`research/tech-*.md`) for broadly useful info
  - Run-specific assets (`run-NNN/assets/`) for run context
  - Updated STRUCTURE.md and CLAUDE.md (v2→v3) with new workflow
- **Status:** RUN-001 Under Review, awaiting client feedback

**2025-12-24 (Session 3):** Final Client Document Batch & GATHER Assessment
- **Processed 3 client documents:**
  - CD-030: Block 1 Actor Stories (Brian Dec 7) - Actor-organized view of Block 1 capabilities
  - CD-031: User Journeys Summary (Brian Dec 7) - 7 user journeys, 258 stories summary
  - CD-032: Fraser Meeting Notes (Nov 9 - Dec 24) - Developer's meeting notes and observations
- **Added 4 new goals (GO-024 to GO-027):**
  - GO-024: Creator Subscription Revenue Model (monthly + per-course fees)
  - GO-025: Invitation-Only Launch Strategy
  - GO-026: Onboarding & Personalization
  - GO-027: Feed Companion & Noise Reduction
- **Added 26 new user stories:**
  - Creator pricing: US-A031-A033, US-C045-C046
  - Feed companion: US-S076-S079, US-P091-P093
  - Onboarding: US-S080, US-P094-P095
  - Course promotion: US-C047-C048, US-P096
  - Sub-communities: US-S081, US-P097
  - Extra coaching: US-S082, US-T033, US-P098
  - Platform: US-P099-P101 (changelog, feature flags, unified dashboard)
- **Added 4 new questions for Brian** (#23-26):
  - S-T pricing visibility before purchase
  - Course completion/passing criteria
  - Moderator invite mechanics
  - Timeline clarification (4 vs 6 months)
- **GATHER Phase Assessment:** Client documents complete, service research partially complete
- Total now: 32 docs, 27 goals, 325 stories, 26 open questions

**2025-12-24 (Session 2):** Block Sequence Management Document
- **Processed CD-029:** PeerLoop Block Sequence v2.1 - Gabriel's comprehensive management document
  - 33-page HTML document with tabs covering user journeys, hypotheses, block sequence, Brian's review
  - Breaks MVP into hypothesis-driven blocks (0.0-0.7 flywheel, 1.x community)
- **Key insights captured from Brian's Review:**
  - **Trust-building before payment is critical** - new platform needs pre-enrollment communication
  - Suggested tiered pricing ($150×3 instead of $450 single payment)
  - Recommended free 15-minute intro sessions before enrollment
  - Basic inquiry/contact feature needed in Block 0.1 (not deferred to 1.x)
- **Dec 15 Meeting updates:**
  - **Course access model CHANGED:** Students get community feed access upon payment (not after graduation)
  - 4 starter courses confirmed: GitHub, Claude Code, n8n, AI Tools Overview (1-2 sessions each)
- **Dec 19 UX Meeting (Matt McCloskey):**
  - "One-on-one video is the lynchpin" - validates video-first priority
  - Current block sequence (flywheel before community) is correct
- **Added 3 new goals:**
  - GO-021: Trust-Building Before Purchase
  - GO-022: One-on-One Video as Core Value Proposition
  - GO-023: Course Access Upon Payment
- **Added 13 new user stories:**
  - Trust-building: US-G016-G018 (visitor inquiry, free intro sessions, tiered pricing)
  - S-T intro sessions: US-T030-T032 (conduct, mark availability, notifications)
  - Platform infrastructure: US-P086-P090 (inquiry delivery, conversion tracking, BBB rooms)
  - Creator inquiry: US-C043-C044 (receive/respond, analytics)
- **Updated DB-SCHEMA.md:** Added visitor_inquiries and intro_sessions tables
- Total now: 29 docs, 24 goals, 312 stories, 2 new DB tables

**2025-12-24 (Session 1):** Prototype Walkthrough & Questions Consolidation
- **Processed 4 new client documents:**
  - CD-024: Meeting Notes - Brian PeerLoopApp walkthrough (user access states, instructor feeds, Genesis Cohort 4 courses)
  - CD-025: Sample Course - Intro to Claude Code (real course data, schema validation, 12 new fields)
  - CD-026: Genesis Cohort Course Package (3 more courses: n8n, Vibe Coding 101, AI Tools Overview)
  - CD-027: Prototype Walkthrough - Complete (all 5 personas, 20+ pages, 31 keepers)
- **Comprehensive prototype analysis** from https://peerloopllc.github.io/Peerloop-v2/:
  - Walked through all 5 personas (New User, Student, Student & Teacher, Creator, Admin)
  - Documented 20+ pages with detailed structure and data requirements
  - Identified 31 "keepers" (features to document)
  - Found critical gaps: Admin not implemented, Creator same as Student-Teacher, no user menu
  - Discovered new features: homework tracking, session resources, group sessions, earnings dashboard
- **Created QUESTIONS-FOR-BRIAN.md** - consolidated 21 open questions from all source documents
- **Updated USER-STORIES.md** (v3→v5) - added 16 new stories from CD-024 and CD-025
- **Updated schema** - added instructor_followers, promoted_posts, course_prerequisites, course_target_audience, course_testimonials tables
- Total now: 27 docs, 21 goals, 299 stories, 21 open questions for Brian

**2025-12-23:** Architecture Documents & Goodwill System
- **Created 4 new architecture documents** (seeded from CD-021):
  - `DB-SCHEMA.md` - 30+ database tables with field definitions and sources
  - `PAGES.md` - 26 pages with data requirements and user story mappings
  - `COMPONENTS.md` - 39 reusable UI components with props
  - `API.md` - 60 API endpoints with request/response formats
- **Processed 3 new client documents:**
  - CD-021: Database Schema Sample (JS mock data, Creator/Course entities)
  - CD-022: Data Structures Doc (ratingCount, badge fields, prototype URL)
  - CD-023: Goodwill Points Spec (community currency, Summon Help, anti-gaming)
- **Added 25 new user stories** (USER-STORIES v2→v3):
  - 6 stories from CD-021 (course filtering, learning objectives, includes)
  - 19 stories from CD-023 (goodwill system, all P2/P3 Block 2+)
- **Updated GO-019** (Gamification) with detailed goodwill points spec
- **Updated `/r-add-client-doc` command** - now scans for architecture implications (7 docs updated)
- **Updated CLAUDE.md** (v1→v2) - added architecture docs to GATHER/RUN phases
- Architecture doc stats: 30+ tables, 26 pages, 39 components, 60 endpoints
- Total now: 23 docs, 21 goals, 283 stories (136 P0, 94 P1, 50 P2, 3 P3)

**2025-12-04:** MVP Decisions & Visitor Role
- Processed 9 additional client documents (CD-012 to CD-020)
  - CD-012: MVP Review - Fraser/Gabriel feature review, Genesis cohort 60-80 students
  - CD-013: Community Feed - GetStream decision, engagement metrics
  - CD-014: Video Conferencing - BBB/Jitsi decision, calendar/scheduling
  - CD-015: Calendar/Scheduling - Cal.com vs react-big-calendar options
  - CD-016: Rebrand to PeerLoop - branding decision
  - CD-017: Creator Profiles - unified profile system, $8K-11K
  - CD-018: Student Profile System - $14K-19K, social graph
  - CD-019: Course Content Delivery - external LMS, $2K-4K
  - CD-020: Payment & Escrow - Stripe, semi-automated 70/15/15 split, $11K-15K
- **Added Visitor/Guest role (US-G prefix)** - 15 new stories for pre-registration experience
  - Homepage & promotional content (US-G001-G004)
  - Course discovery (US-G005-G007)
  - Creator/teacher discovery (US-G008-G010)
  - Authentication actions (US-G011-G013)
  - Access restrictions (US-G014-G015)
- Updated GOALS.md Goal Index for all new documents
- Total now: 20 docs, 21 goals, 258 stories (135 P0, 89 P1, 32 P2, 2 P3), 9 user roles

**2025-11-30 (Session 3):** Miro Board Processing
- Processed 2 Miro board screenshots as client documents (CD-010, CD-011)
- **CD-010: Main Activities by Role**
  - Mapped activities and pain points for 5 user roles
  - Identified **Community Moderator as NEW role** (distinct from Creator)
  - Added GO-019: Gamification & Engagement System (goodwill points, power user tiers)
  - Added 18 new user stories (US-S029-S031, US-C024-C027, US-P051-P055, US-M001-M005)
- **CD-011: Drivers & Action Items**
  - Documented user motivations and corresponding platform features
  - **Bluesky confirmed** as community tool for all roles
  - **Certificate of Mastery** (separate from completion) - NEW requirement
  - Added GO-020: Credentialing System (completion, mastery, teaching certs)
  - **Bidirectional opt-out** for Student-Teacher relationships
  - **Teacher Student points** for gamification motivation
  - Added 14 new user stories (US-S032-S035, US-T014-T016, US-C028-C030, US-P056-P059)
- Total now: 11 docs, 21 goals, 183 stories (78 P0, 72 P1, 31 P2, 2 P3)

**2025-11-30 (Session 2):** Client Document Batch Processing
- Processed 5 additional client documents (CD-005 to CD-009)
- Added GO-018: MVP Budget & Timeline Constraint ($75K, 4 months)
- Added US-S028: Follow creators before enrolling
- Key decisions confirmed:
  - Budget: $75,000 / Timeline: 4 months
  - BBB Provider: Blindside Networks (managed hosting)
  - Hosting: Cloudflare (peerloop.com live)
  - Stream: Feeds only (not video/chat)
  - Feed prototype: Skool.com
- Added video evaluation criteria (1:1 P2P, recording/playback)

**2025-11-30 (Session 1):** GATHER Phase Framework Complete
- Reorganized PLAN.md into GATHER/RUN phases
- Added 48 infrastructure user stories (US-P007-P050, US-V008-V011)
- Created 6 tech research docs (tech-001 to tech-005, comp-001)
- Created `/scenarios/` folder for SPECS.md variants
- Added `/r-add-software`, `/r-add-user-story`, `/r-add-directive` commands
- Created DIRECTIVES.md with 6 initial directives (DIR-001 to DIR-006)
- Documented GATHER and RUN phases in CLAUDE.md
- Added document versioning system (v1) for scenario lineage tracking
- Phase 2.5.1 (Core Research) marked complete

**2025-11-29:** Phase 1 Complete
- Processed 4 client documents (CD-001 to CD-004)
- Created GOALS.md with 17 goals
- Created USER-STORIES.md with 105 stories
- Established numbering conventions (CD-NNN, GO-NNN, US-[Role]NNN)
- Renamed Needs.md → SPECS.md

---

## ✅ Archived Phases

### Phase 1: Discovery & Context Gathering
Completed 2025-11-29. All client documents processed, goals and user stories extracted.

---

## Open Questions (Resolved)

- ~~What is Alpha Peer's primary purpose?~~ → Peer-to-peer AI education platform with learn-teach-earn flywheel
- ~~Who are the target users?~~ → 6 roles: Student, Student-Teacher, Creator, Employer, Admin, System
- ~~What existing systems need integration?~~ → Open EdX, Big Blue Button, Bluesky (from CD-002)
- ~~What is the timeline/budget context?~~ → **$75K budget, 4 months** (CD-008)
- ~~Hosting/infrastructure decisions?~~ → **Cloudflare** confirmed, peerloop.com live (CD-009)
- ~~BBB provider?~~ → **Blindside Networks** (original BBB creators), managed hosting via API (CD-009)
- ~~Stream scope?~~ → **Feeds only** (not video, chat is low priority) (CD-008)
- ~~Community feed prototype?~~ → **Skool.com** as reference design (CD-008)

## Open Questions (21 Total)

**See `/client-docs/QUESTIONS-FOR-BRIAN.md` for full list with source traceability.**

Key categories:
- **Technology decisions:** GetStream vs Bluesky, BBB vs P2P for 1:1 (6 questions)
- **Feature scope:** AI Assistant, Newsletters, homework system, group sessions (5 questions)
- **Architecture:** Community structure, profile defaults, certificates (4 questions)
- **Prototype gaps:** Creator dashboard, Admin features, user menu (6 questions)

---

## Notes

This plan follows a two-phase approach:
1. **GATHER** - Iteratively collect client docs, research services, document requirements
2. **RUN** - Generate SPECS.md scenarios from gathered information

Phases may be revisited as new information emerges.

**Key Documents:**
- `GOALS.md` - 27 goals with source traceability (v3)
- `USER-STORIES.md` - 329 stories organized by 9 roles (v8)
- `DIRECTIVES.md` - 6 constraints for scenario generation (v1)
- `CLAUDE.md` - Project guidance and phase definitions (v3)
- `DB-SCHEMA.md` - 37+ database tables with fields and relationships (v1)
- `PAGES.md` - 27 pages with data requirements (v1)
- `COMPONENTS.md` - 41 reusable UI components (v1)
- `API.md` - 65 API endpoints with request/response formats (v1)
- `SPECS.md` - Final technical specifications (populated from approved run)
- `/runs/` - RUN phase execution tracking (run-NNN folders with scenarios and assets)
- `/research/` - Technology research documents (7 docs - global knowledge)
- `client-docs/client-docs-index.md` - 33 source document summaries
- `client-docs/QUESTIONS-FOR-BRIAN.md` - 26 questions (21 open, 3 deferred, 2 resolved)

**Commands for Adding Information:**
- `/r-add-client-doc` - Process new client documents (now updates 7 docs including architecture)
- `/r-add-software <url>` - Research and document a software/service
- `/r-add-user-story` - Add individual user stories
- `/r-add-directive` - Add constraints/restrictions for scenarios
