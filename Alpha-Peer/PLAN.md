# Alpha Peer - Research & Planning Roadmap

**Goal:** Produce a comprehensive SPECS.md document that can be handed off to Claude Code for Alpha Peer development.

**Last Updated:** 2025-11-30

---

## Project Phases Overview

| Phase | Name | Status | Description |
|-------|------|--------|-------------|
| **GATHER** | Information Collection | 🔥 IN PROGRESS | Collect client docs, research services, document user stories |
| **RUN** | Scenario Generation | ⏳ PENDING | Create SPECS.md scenarios from gathered information |

---

## Current Status

| Metric | Value |
|--------|-------|
| Current Phase | GATHER (Phase 2.5) 🔥 |
| Client Docs Processed | 11 (CD-001 to CD-011) |
| Goals Documented | 21 (GO-001 to GO-020) |
| User Stories Created | 183 (78 P0, 72 P1, 31 P2, 2 P3) |
| Tech Docs Created | 6 (tech-001 to tech-005, comp-001) |
| Directives Created | 6 (DIR-001 to DIR-006) |
| Scenarios Created | 0 |
| Doc Versions | GOALS v1, USER-STORIES v1, DIRECTIVES v1, CLAUDE v1 |
| Budget | $75,000 (from CD-008) |
| Timeline | 4 months (from CD-008) |
| Domain | peerloop.com (live on Cloudflare) |

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

- [ ] All client documents processed
- [ ] All required services researched (BBB, Stream)
- [ ] All optional service categories researched (payment, auth, email, etc.)
- [ ] User stories mapped to technologies
- [ ] Gaps identified and documented
- [ ] Comparison docs created for key decisions

---

# RUN PHASE

*Transform gathered information into actionable SPECS.md scenarios.*

**Principles:**
- Later client docs override earlier ones (CD-004 > CD-003 > CD-002 > CD-001)
- Goal: Minimize custom development by leveraging existing services
- sc-001 is always the fully-custom baseline (no major SaaS)

## Phase 3: Scenario Creation ⏳ PENDING

### 3.1 - Baseline Scenario
- [ ] Create `sc-001-fully-custom-SPECS.md` (no Stream, no BBB, maximum custom dev)
  - Uses only: Cloudflare services, Vercel services, npm packages
  - Establishes baseline for comparing "dev time saved" by services

### 3.2 - Alternative Scenarios
- [ ] Create `sc-002-*` with required services (Stream + BBB)
- [ ] Create additional scenarios as client requests variations
- [ ] Document trade-offs for each scenario (cost, dev time, flexibility)

### 3.3 - Scenario Comparison
- [ ] Create comparison matrix across scenarios
- [ ] Estimate relative development effort
- [ ] Present options to client

## Phase 4: Final Selection & Handoff ⏳ PENDING

### 4.1 - Client Review
- [ ] Present scenarios to client
- [ ] Gather feedback and preferences
- [ ] Make adjustments as requested

### 4.2 - Finalize SPECS.md
- [ ] Client selects final scenario
- [ ] Copy selected scenario to root `SPECS.md`
- [ ] Final review for completeness
- [ ] Handoff to implementation

---

## 🏁 Latest Completed

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

## Open Questions (New)

- **Video conferencing decision:** BBB vs Daily.co vs Digital Samba for 1:1 sessions? (CD-006, CD-007)
  - BBB: Full-featured, per-session pricing, group support (via Blindside Networks)
  - Daily.co: P2P for 1:1 (cost-effective), auto-switching, SDK
  - Digital Samba: Low-code iframe, quick integration
  - Hybrid option: BBB for groups, P2P for 1:1?
- **Feed technology:** GetStream (CD-005) vs Bluesky protocol (CD-002)?
- Which payment processor best supports the 15/15/70 split model?
- How to handle student-to-student messaging safely ("tricky" per CD-003)?
- AI integration depth: fabric-level vs feature add-on?

---

## Notes

This plan follows a two-phase approach:
1. **GATHER** - Iteratively collect client docs, research services, document requirements
2. **RUN** - Generate SPECS.md scenarios from gathered information

Phases may be revisited as new information emerges.

**Key Documents:**
- `GOALS.md` - 21 goals with source traceability (v1)
- `USER-STORIES.md` - 183 stories organized by 7 roles (v1)
- `DIRECTIVES.md` - 6 constraints for scenario generation (v1)
- `CLAUDE.md` - Project guidance and phase definitions (v1)
- `SPECS.md` - Final technical specifications (populated from selected scenario)
- `/scenarios/` - SPECS.md variants for comparison (with lineage tracking)
- `/research/` - Technology research documents
- `client-docs/client-docs-index.md` - 11 source document summaries

**Commands for Adding Information:**
- `/r-add-client-doc` - Process new client documents
- `/r-add-software <url>` - Research and document a software/service
- `/r-add-user-story` - Add individual user stories
- `/r-add-directive` - Add constraints/restrictions for scenarios
