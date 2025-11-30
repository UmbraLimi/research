# Alpha Peer - Research & Planning Roadmap

**Goal:** Produce a comprehensive SPECS.md document that can be handed off to Claude Code for Alpha Peer development.

**Last Updated:** 2025-11-29

---

## Current Status

| Metric | Value |
|--------|-------|
| Current Phase | 2.1 🔥 |
| Client Docs Processed | 4 (CD-001 to CD-004) |
| Goals Documented | 17 (GO-001 to GO-017) |
| User Stories Created | 105 (48 P0, 42 P1, 15 P2) |
| Tech Decisions Made | 0 |
| Learnings Captured | 1 |

---

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

## Phase 3: Technology Research

### 3.1 - Technology Evaluation
- [ ] Research Open EdX integration (LMS - from CD-002)
- [ ] Research Big Blue Button (video conferencing - from CD-002)
- [ ] Research Bluesky protocol (social feed - from CD-002)
- [ ] Research payment processors (15/15/70 split requirements)
- [ ] Create comparison documents for key decisions

### 3.2 - Architecture Decisions
- [ ] Define high-level architecture
- [ ] Document integration points (Open EdX ↔ BBB ↔ Bluesky)
- [ ] Identify technical constraints
- [ ] Decide on AI integration approach

---

## Phase 4: SPECS.md Compilation 📋 NEXT

### 4.1 - Document Assembly
- [ ] Consolidate P0 user stories into SPECS.md
- [ ] Add confirmed technology stack
- [ ] Include architecture decisions
- [ ] Document integration requirements
- [ ] Add non-functional requirements

### 4.2 - Review & Finalize
- [ ] Review for completeness
- [ ] Verify consistency across sections
- [ ] Final approval for handoff

---

## 🏁 Latest Completed

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

This plan follows an iterative research approach. Phases may be revisited as new information emerges from client documents or research findings.

**Key Documents:**
- `GOALS.md` - 17 goals with source traceability
- `USER-STORIES.md` - 105 stories organized by role
- `SPECS.md` - Technical specifications (to be populated)
- `client-docs/client-docs-index.md` - Source document summaries
