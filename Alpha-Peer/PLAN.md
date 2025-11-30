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
| Client Docs Processed | 4 (CD-001 to CD-004) |
| Goals Documented | 17 (GO-001 to GO-017) |
| User Stories Created | 150 (77 P0, 53 P1, 20 P2) |
| Tech Docs Created | 6 (tech-001 to tech-005, comp-001) |
| Directives Created | 6 (DIR-001 to DIR-006) |
| Scenarios Created | 0 |
| Doc Versions | GOALS v1, USER-STORIES v1, DIRECTIVES v1, CLAUDE v1 |

---

# GATHER PHASE

*Collect all information needed to create comprehensive technical specifications.*

## Phase 1: Discovery & Context Gathering ✅ COMPLETE

### 1.1 - Client Document Analysis ✅
- [x] Process all client-provided documents (4 docs)
  - CD-001: Business Plan - revenue model, flywheel, go-to-market
  - CD-002: Feature Summary - UI/UX mockups, tech stack, navigation
  - CD-003: User Stories - role-based needs, 6 user types
  - CD-004: Impact Filter - mission, success metrics, vision
- [x] Extract business requirements and constraints → GOALS.md
- [x] Identify user personas and their needs → USER-STORIES.md (6 roles)
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
| Big Blue Button | Video Conferencing | `tech-001-bigbluebutton.md` | TBD |
| Stream | Chat/Activity Feeds | `tech-002-stream.md` | TBD |

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

**2025-11-30:** GATHER Phase Framework Complete
- Reorganized PLAN.md into GATHER/RUN phases
- Added 48 infrastructure user stories (US-P007-P050, US-V008-V011) - Total now 150
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
- ~~What is the timeline/budget context?~~ → 12 months to break-even, 3 founding creators for MVP

## Open Questions (New)

- Which payment processor best supports the 15/15/70 split model?
- How to handle student-to-student messaging safely ("tricky" per CD-003)?
- AI integration depth: fabric-level vs feature add-on?
- Hosting/infrastructure decisions?

---

## Notes

This plan follows a two-phase approach:
1. **GATHER** - Iteratively collect client docs, research services, document requirements
2. **RUN** - Generate SPECS.md scenarios from gathered information

Phases may be revisited as new information emerges.

**Key Documents:**
- `GOALS.md` - 17 goals with source traceability (v1)
- `USER-STORIES.md` - 150 stories organized by role (v1)
- `DIRECTIVES.md` - 6 constraints for scenario generation (v1)
- `CLAUDE.md` - Project guidance and phase definitions (v1)
- `SPECS.md` - Final technical specifications (populated from selected scenario)
- `/scenarios/` - SPECS.md variants for comparison (with lineage tracking)
- `/research/` - Technology research documents
- `client-docs/client-docs-index.md` - Source document summaries

**Commands for Adding Information:**
- `/r-add-client-doc` - Process new client documents
- `/r-add-software <url>` - Research and document a software/service
- `/r-add-user-story` - Add individual user stories
- `/r-add-directive` - Add constraints/restrictions for scenarios
