# Alpha Peer - Research & Planning Roadmap

**Goal:** Produce a comprehensive SPECS.md document for handoff to implementation.

**Last Updated:** 2025-12-26

---

## Project Status

| Phase | Status | Plan File |
|-------|--------|-----------|
| **GATHER** | ✅ Complete | [GATHER-PLAN.md](GATHER-PLAN.md) |
| **RUN** | ✅ RUN-001 Complete | [RUN-PLAN.md](RUN-PLAN.md) |

**Status:** Ready for Phase 5 - Final Selection & Handoff (Brian review)

**✅ COMPLETED:** Page API Calls Documentation (2025-12-26)
- All 41 pages now have `## API Calls` or `## Server Integration` sections
- 39 GET endpoints documented across admin pages alone
- Every page documents which internal API endpoints it calls
- Pages with external services (Stripe, Stream, PlugNmeet, Resend) have Server Integration sections

**✅ COMPLETED:** API Documentation Split (2025-12-26)
- Created **DB-API.md** - 200+ internal endpoints with DB-SCHEMA table references
- Created **REMOTE-API.md** - External service endpoints (Stripe, Stream, PlugNmeet, Resend)
- Each endpoint now links to relevant tables in DB-SCHEMA.md
- Developer workflow: Page → API endpoint → DB tables is now traceable

**🎯 NEXT:** Apply Brian's decisions from review session (2025-12-26)

**Pending Updates from Brian Review:**
- [ ] Add homework tables to DB-SCHEMA.md (homework_assignments, homework_submissions)
- [ ] Add homework endpoints to DB-API.md
- [ ] Add session_resources table to DB-SCHEMA.md (R2 storage for recordings/slides/files)
- [ ] Update FEATURE-FLAGS.md - homework = MVP
- [ ] Update DB-SCHEMA.md - users.privacy_public default = false (Private)
- [ ] Document moderator two-step invite flow

**Questions Resolved:** 22 of 26 (3 deferred to implementation, 1 unclear)

---

## Key Decisions (2025-12-26)

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Feature Flags | Database-driven, roles + features | All features documented upfront; flags control release |
| Course Chat | Custom WebSocket (Durable Objects) | Start minimal, build out; avoid Stream Chat dependency |
| No "Out of Scope" | All features planned | Use feature flags instead of excluding features |

---

## Current Metrics

| Metric | Value |
|--------|-------|
| Client Docs Processed | 33 (CD-001 to CD-033) |
| Goals Documented | 27 (GO-001 to GO-027) |
| User Stories | 334 (144 P0, 109 P1, 71 P2, 8 P3) |
| User Roles | 9 |
| Tech Research Docs | 8 (incl. Stripe Connect) |
| Directives | 6 (DIR-001 to DIR-006) |
| Page Flow Docs | 41 pages/screens |
| Feature Registry | ~286 features (~554 hours) |
| Budget | $75,000 |
| Timeline | 4 months (fixed) |
| Domain | peerloop.com |
| Open Questions | 17 open, 0 deferred, 13 resolved |

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
| SERVER.md | Cloudflare stack, adapters, webhooks |
| DB-SCHEMA.md | 47+ tables with fields and relationships (v2) |
| PAGES.md | 27 pages with data requirements |
| COMPONENTS.md | 41 reusable UI components |
| **API.md** | Quick reference index by HTTP method (v3) |
| **DB-API.md** | 200+ internal endpoints with DB-SCHEMA references (v1) |
| **REMOTE-API.md** | External service endpoints (Stripe, Stream, PlugNmeet, Resend) (v1) |

### RUN-001 Assets
| Location | Content |
|----------|---------|
| runs/run-001/scenario.md | 14-section technical specification |
| runs/run-001/pages/ | 41 page docs (17 with Server Integration) |
| runs/run-001/features/ | Feature registry split by block |
| runs/run-001/FEATURE-FLAGS.md | 20 feature flags with dependencies |
| runs/run-001/FLOWS.md | 5 user journey diagrams |
| runs/run-001/SCOPE.md | Feature tracking (MVP/POST-MVP/DONE) |
| runs/run-001/STORY-DEPENDENCIES.md | Dependency chains + 10-block order |
| runs/run-001/ACCESS-MATRIX.md | Role × page access permissions |
| runs/run-001/AMENDMENT-PLAN.md | ✅ Server architecture + page updates |

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
