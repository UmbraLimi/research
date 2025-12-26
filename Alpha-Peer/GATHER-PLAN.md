# GATHER Phase Plan

**Purpose:** Collect all information needed to create comprehensive technical specifications.

**Status:** NEARLY COMPLETE (ready for RUN phase)

---

## Phase 1: Discovery & Context Gathering ✅ COMPLETE

### 1.1 - Client Document Analysis ✅
- [x] Process all client-provided documents (33 docs: CD-001 to CD-033)
- [x] Extract business requirements and constraints → GOALS.md
- [x] Identify user personas and their needs → USER-STORIES.md (9 roles)
- [x] Document competing or evolving goals across documents → Goal Index
- [x] Create timeline of document priorities (newer supersedes older)

### 1.2 - Vision & Scope Definition ✅
- [x] Define Alpha Peer's core value proposition → GOALS.md Mission Statement
- [x] Identify primary user personas → 9 roles in USER-STORIES.md
- [x] Establish project boundaries → MVP = 3 creators, Genesis Cohort
- [x] Document success criteria → GO-005, GO-006, GO-007 (quantified targets)

---

## Phase 2: User Stories & Requirements 🔥 IN PROGRESS

### 2.1 - Core User Stories ✅ MOSTLY COMPLETE
- [x] Create user stories for primary workflows (334 stories extracted)
- [x] Prioritize stories (MVP vs future) - P0/P1/P2/P3 assigned
- [ ] Define acceptance criteria for P0 stories
- [ ] Identify dependencies between stories → See STORY-DEPENDENCIES.md
- [ ] Create detailed story files for complex P0 stories

### 2.2 - Non-Functional Requirements
- [ ] Define performance expectations (from CD-004 metrics)
- [ ] Document security requirements (payments, user data)
- [ ] Establish scalability needs (50+ Student-Teachers per creator)
- [ ] Specify reliability/uptime requirements (video sessions)

---

## Phase 2.5: Third-Party Integrations Inventory

### Required Services (Client-Specified)
| Service | Type | Research Doc | Status |
|---------|------|--------------|--------|
| Big Blue Button | Video Conferencing | `tech-001-bigbluebutton.md` | ✅ Researched |
| Stream | Chat/Activity Feeds | `tech-002-stream.md` | ✅ Researched |

### Framework & Deployment Stack
| Technology | Type | Research Doc | Status |
|------------|------|--------------|--------|
| Astro.js | Meta-Framework | `tech-003-astrojs.md` | ✅ Preferred |
| React.js | UI Library | `tech-004-reactjs.md` | ✅ Confirmed |
| Tailwind CSS | CSS Framework | `tech-005-tailwindcss.md` | ✅ Confirmed |
| Cloudflare | Deployment/CDN | `comp-001-cloudflare-vs-vercel.md` | ✅ Preferred |

### Optional Services (To Be Evaluated)
| Category | Options | User Stories | Status |
|----------|---------|--------------|--------|
| Payment | Stripe Connect | US-P026-P033 | Assumed |
| Auth | Clerk, Auth.js, Supabase | US-P007-P013 | TBD |
| Email | Resend, SendGrid | US-P014-P019 | TBD |
| Calendar | Cal.com, Calendly API | US-P020-P025 | TBD |
| AI Transcription | Whisper, AssemblyAI | US-V008-V011 | TBD |
| Database | Supabase, PlanetScale, Neon | US-P034-P037 | TBD |
| Storage | Cloudflare R2, S3 | US-P038-P045 | TBD |

### 2.5.1 - Core Research ✅ COMPLETE
- [x] Research Big Blue Button → `tech-001-bigbluebutton.md`
- [x] Research Stream → `tech-002-stream.md`
- [x] Research Astro.js → `tech-003-astrojs.md`
- [x] Document React.js → `tech-004-reactjs.md`
- [x] Document Tailwind CSS → `tech-005-tailwindcss.md`
- [x] Compare Cloudflare vs Vercel → `comp-001-cloudflare-vs-vercel.md`

### 2.5.2 - User Story Mapping ✅ COMPLETE
- [x] Map BBB features to video/session stories
- [x] Map Stream features to messaging/feed stories
- [x] Identify gaps requiring additional services → 48 new stories added

### 2.5.3 - Gap-Filling Service Research ⏳ PARTIALLY COMPLETE
Optional service research can be decided during scenario creation based on cost/complexity trade-offs.

---

## GATHER Completion Criteria

| Criterion | Status |
|-----------|--------|
| All client documents processed | ✅ 33 docs (CD-001 to CD-033) |
| Required services researched | ✅ BBB, Stream |
| Optional services researched | ⚠️ Partially done |
| User stories mapped to tech | ✅ 334 stories with source traceability |
| Gaps identified and documented | ✅ 26 questions in QUESTIONS-FOR-BRIAN.md |
| Architecture docs created | ✅ DB-SCHEMA, PAGES, COMPONENTS, API |
| Comparison docs created | ⚠️ Only comp-001 done |

### What's Done
- All 33 client documents processed and indexed
- 27 goals extracted with source traceability
- 334 user stories with priority and source
- 4 architecture docs (DB-SCHEMA, PAGES, COMPONENTS, API)
- 7 tech/comparison research docs
- 6 directives for scenario constraints
- 26 open questions documented for Brian

### What's Incomplete (Not Blocking RUN Phase)
- Optional service research (payment, auth, email, calendar, AI transcription, analytics, database, storage)
- Comparison docs for pending decisions

---

## RUN Phase Readiness Assessment

**Can we start RUN phase?** ✅ Yes

**Resolved Critical Items:**
1. ~~Video Platform Decision~~ → RESOLVED via interface abstraction (API.md)
2. ~~Timeline Clarification~~ → RESOLVED: 4 months fixed, feature removal if scope exceeds

**Items Decidable During Scenario Creation:**
- Payment processor (Stripe assumed)
- Authentication (Clerk, Auth.js, Supabase Auth)
- Email service (Resend, SendGrid)
- Calendar integration (Cal.com, Calendly API)
- Database (Supabase, PlanetScale, Neon)

---

## Phase 2.8: Preparation Tasks (Optional)

*Productive work that can be done while awaiting client feedback.*

### 2.8.1 - Pre-Research Video Conferencing
- [ ] Research Daily.co capabilities and pricing
- [ ] Research Digital Samba capabilities and pricing
- [ ] Draft comparison framework

### 2.8.2 - Review Existing User Stories
- [ ] Audit P0 stories for completeness and clarity
- [ ] Identify stories that imply specific pages
- [ ] Flag stories with unclear acceptance criteria
- [ ] Note potential story dependencies

### 2.8.3 - Non-Functional Requirements Draft
- [ ] Draft performance expectations
- [ ] Outline security requirements
- [ ] Document scalability targets
- [ ] List reliability requirements
