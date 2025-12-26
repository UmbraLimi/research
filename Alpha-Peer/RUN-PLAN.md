# RUN Phase Plan

**Purpose:** Transform gathered information into actionable SPECS.md scenarios.

**Status:** RUN-001 Under Review

---

## Principles

- Later client docs override earlier ones (CD-033 > CD-001)
- Goal: Minimize custom development by leveraging existing services
- sc-001 is always the fully-custom baseline (no major SaaS)
- Scenarios are created through the `/runs/` system with full traceability

---

## Phase 3: Architecture Documentation ✅ COMPLETE

### 3.1 - Architecture Documents Created ✅
| Document | Content | Status |
|----------|---------|--------|
| DB-SCHEMA.md | 37+ tables with fields and relationships | ✅ |
| PAGES.md | 27 pages with data requirements | ✅ |
| COMPONENTS.md | 41 reusable UI components | ✅ |
| API.md | 65 API endpoints with request/response | ✅ |

### 3.2 - Page Documentation ✅ COMPLETE
For each page in `runs/run-001/pages/`:
- [x] Data Sources (DB tables/entities)
- [x] Purpose (user stories fulfilled)
- [x] Code (3-4 letter identifier)
- [x] Connections (incoming + outgoing navigation)
- [x] UI Sections with elements
- [x] States & Variations
- [x] Mobile Considerations
- [x] Error Handling
- [x] Analytics Events

### 3.3 - Access Matrix ✅ COMPLETE
- [x] Role × page access matrix → `runs/run-001/ACCESS-MATRIX.md`
- [x] Role-specific variations documented
- [x] Authentication requirements noted

### 3.4 - Multi-Role User Handling ✅ COMPLETE
- [x] Unified dashboard design → `runs/run-001/MULTI-ROLE-DASHBOARD.md`
- [x] Role combination patterns documented
- [x] Role-aggregation UX defined

### 3.5 - Finalize for Scenario ⏳ PENDING
- [ ] Finalize architecture for selected scenario (may vary by tech choices)

---

## Phase 4: Scenario Creation 🔥 IN PROGRESS

### 4.1 - RUN-001: Stream + VideoProvider (sc-002) 🔥 UNDER REVIEW

**Created:**
- [x] Run folder structure (`runs/run-001/`)
- [x] Inputs and parameters (`run-001.md`)
- [x] Questions state snapshot (21 open, 3 deferred, 2 resolved)
- [x] `scenario.md` - 14-section technical specification

**Run-specific assets:**
- `assets/video-platform-decisions.md` - VideoProvider interface
- `assets/stream-usage.md` - Stream.io feeds-only, 5 feed types
- `assets/hosting-decisions.md` - Cloudflare stack
- `assets/payment-decisions.md` - Stripe Connect, 85/15 split

**Page flow documentation:**
- `pages/PAGES-INDEX.md` - Schema definition + registry
- 41 individual page files with full documentation

**Scoping & architecture docs:**
- `SCOPE.md` - Feature tracking by page (MVP/POST-MVP/DONE)
- `ACCESS-MATRIX.md` - Role × page access permissions
- `MULTI-ROLE-DASHBOARD.md` - Unified dashboard design
- `STORY-DEPENDENCIES.md` - Dependency chains + 10-block order
- `FEATURES.md` - ~286 features with hours estimates

**Pending:**
- [ ] Client review of scenario.md + page flows
- [ ] Document feedback in `review-notes.md`
- [ ] Decide: Approve, revise, or create RUN-002

### 4.2 - Future Runs (As Needed)
- [ ] RUN-002: If RUN-001 rejected or needs major changes
- [ ] RUN-003: Alternative scenarios as requested

### 4.3 - Run Index
See `runs/RUN-INDEX.md` for status of all runs.

| Run | Status | Key Decisions |
|-----|--------|---------------|
| RUN-001 | Under Review | Stream + VideoProvider, Cloudflare stack, 144 P0 stories |

---

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

## Implementation Guidance

**When you start coding:**
1. Follow block order in STORY-DEPENDENCIES.md
2. Update SCOPE.md as features move to DONE
3. Reassess at each block boundary
4. MVP cut line will emerge from completed blocks

**Current page inventory:**
- P0 (MVP Core): 31 pages/screens
- P1 (Important): 5 pages/screens
- P2 (Block 2+): 2 pages (CHAT, HELP)
- P3 (Future): 3 pages (CNEW, LEAD, SUBCOM)

**Remaining scoping tasks (during implementation):**
- [ ] Mark features as MVP/POST-MVP in SCOPE.md during each block
- [ ] Validate 4-month timeline against completed blocks
