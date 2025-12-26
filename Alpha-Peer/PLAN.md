# Alpha Peer - Research & Planning Roadmap

**Goal:** Produce a comprehensive SPECS.md document for handoff to implementation.

**Last Updated:** 2025-12-26

---

## Project Status

| Phase | Status | Plan File |
|-------|--------|-----------|
| **GATHER** | ✅ Nearly Complete | [GATHER-PLAN.md](GATHER-PLAN.md) |
| **RUN** | 🔥 RUN-001 Under Review | [RUN-PLAN.md](RUN-PLAN.md) |

**Next Step:** Client review of RUN-001 scenario, then begin Block 0 implementation.

---

## Current Metrics

| Metric | Value |
|--------|-------|
| Client Docs Processed | 33 (CD-001 to CD-033) |
| Goals Documented | 27 (GO-001 to GO-027) |
| User Stories | 334 (144 P0, 109 P1, 71 P2, 8 P3) |
| User Roles | 9 |
| Tech Research Docs | 7 |
| Directives | 6 (DIR-001 to DIR-006) |
| Page Flow Docs | 41 pages/screens |
| Feature Registry | ~286 features (~554 hours) |
| Budget | $75,000 |
| Timeline | 4 months (fixed) |
| Domain | peerloop.com |
| Open Questions | 21 open, 3 deferred, 2 resolved |

---

## Plan Files

| File | Purpose |
|------|---------|
| [GATHER-PLAN.md](GATHER-PLAN.md) | Phases 1-2.8: Client docs, user stories, tech research |
| [RUN-PLAN.md](RUN-PLAN.md) | Phases 3-5: Architecture, scenarios, handoff |
| [MISC-PLAN.md](MISC-PLAN.md) | Session logs, resolved questions, archived content |

---

## Key Documents

### Core Specifications
| Document | Content |
|----------|---------|
| GOALS.md | 27 goals with source traceability (v3) |
| USER-STORIES.md | Index → 334 stories in 9 role files (v9) |
| DIRECTIVES.md | 6 constraints for scenario generation |
| SPECS.md | Final technical specifications (from approved run) |

### Architecture
| Document | Content |
|----------|---------|
| DB-SCHEMA.md | 37+ tables with fields and relationships |
| PAGES.md | 27 pages with data requirements |
| COMPONENTS.md | 41 reusable UI components |
| API.md | 65 API endpoints |

### RUN-001 Assets
| Location | Content |
|----------|---------|
| runs/run-001/scenario.md | 14-section technical specification |
| runs/run-001/pages/ | 41 page/screen documents |
| runs/run-001/features/ | Feature registry split by block |
| runs/run-001/SCOPE.md | Feature tracking (MVP/POST-MVP/DONE) |
| runs/run-001/STORY-DEPENDENCIES.md | Dependency chains + 10-block order |
| runs/run-001/ACCESS-MATRIX.md | Role × page access permissions |

### Reference
| Location | Content |
|----------|---------|
| research/ | 7 technology research documents |
| client-docs/client-docs-index.md | 33 source document summaries |
| client-docs/QUESTIONS-FOR-BRIAN.md | 26 questions for client |

---

## Commands

| Command | Purpose |
|---------|---------|
| `/r-add-client-doc` | Process new client documents |
| `/r-add-software <url>` | Research and document a software/service |
| `/r-add-user-story` | Add individual user stories |
| `/r-add-directive` | Add constraints for scenarios |
| `/r-status` | Show current project status |
