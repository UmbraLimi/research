# CLAUDE.md

**Version:** v2
**Last Updated:** 2025-12-23

> **Version History:** Increment version when substantive changes occur (new phases, changed workflows, new commands). Minor edits (typos, formatting) don't require version bump.

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a research and planning repository for **Alpha Peer**, a web application in the pre-development phase. The project uses iterative research, documentation, and decision tracking to prepare for eventual handoff to implementation. There is no code to build, lint, or test.

## Repository Structure

```
MyResearch/
├── Alpha-Peer/           # Main project folder
│   ├── STRUCTURE.md      # Master guide for organization (check first!)
│   ├── GOALS.md          # Mission statement & goals (from client docs)
│   ├── USER-STORIES.md   # All user stories (from client docs)
│   ├── DIRECTIVES.md     # Constraints & restrictions for RUN phase
│   ├── SPECS.md          # Technical specs for handoff (final scenario)
│   ├── DB-SCHEMA.md      # Database entities, fields, relationships
│   ├── PAGES.md          # Page inventory with data requirements
│   ├── COMPONENTS.md     # Reusable UI component library
│   ├── API.md            # Backend API operations surface
│   ├── client-docs/      # Client-provided materials (don't modify originals)
│   ├── research/         # Technology research (tech-NNN-*.md, comp-NNN-*.md)
│   ├── scenarios/        # SPECS.md variants (sc-NNN-*-SPECS.md)
│   ├── user-stories/     # Detailed story files (story-NNN-*.md)
│   ├── docs/sessions/    # Session logs by month (YYYY-MM/)
│   ├── prompts/          # Commands and prompt templates
│   ├── learnings/        # Knowledge capture (learning-NNN-*.md)
│   ├── decisions/        # Decision records (decision-NNN-*.md)
│   └── .claude/commands/ # Project-specific slash commands (r-*)
└── file_holding/         # Temporary staging for file processing
```

**Important:** Launch Claude Code from `Alpha-Peer/` folder, not `MyResearch/`.

## Key Conventions

### ID Numbering (all support up to 999)
| Prefix | Format | Example | Tracked In |
|--------|--------|---------|------------|
| CD- | CD-NNN | CD-001 | client-docs-index.md |
| GO- | GO-NNN | GO-001 | GOALS.md |
| US- | US-[Role]NNN | US-A001, US-S015 | USER-STORIES.md |

**User Story Role Codes:** A=Admin, C=Creator, S=Student, T=Student-Teacher, E=Employer, V=Video/Session, P=Platform

### File Naming
- Numbers use zero-padded 3 digits: `001`, `002`, etc.
- Lowercase with hyphens for filenames
- Date format: YYYY-MM-DD (ISO 8601)
- Session files use timestamp: `docs/sessions/2025-11/2025-11-25_14-30-00 Learnings.md`

### Before Creating Files
Always check `Alpha-Peer/STRUCTURE.md` for:
- Current numbering state for each category
- Correct folder location
- Naming pattern to follow

After creating numbered files, update the "Current State" section in STRUCTURE.md.

## Slash Commands

Commands are split between two locations:
- **`~/.claude/commands/`** - User-level `/q-*` commands (available in all projects)
- **`Alpha-Peer/.claude/commands/`** - Project-specific `/r-*` commands

### `/q-*` Commands (Session & Git) - User-level

| Command | Purpose |
|---------|---------|
| `/q-resume` | Analyze PLAN.md and show current progress to resume work |
| `/q-update` | Update PLAN.md with current progress (run frequently) |
| `/q-end-session` | Full end-of-session workflow (learnings, prompts, optional commit) |
| `/q-commit` | Stage and commit all changes with descriptive message |
| `/q-learnings` | Document session learnings and insights |
| `/q-prompts` | Save all user prompts from session for future reference |
| `/q-timestamp` | Get current date/time (utility, called by other commands) |
| `/q-pare` | Optimize CLAUDE.md by moving content to OFFLOAD.md |

### `/r-*` Commands (Research & Documentation) - Project-level

| Command | Purpose |
|---------|---------|
| `/r-add-client-doc` | Process client document(s) from file_holding |
| `/r-add-software` | Research software/service from URL, create tech doc |
| `/r-add-user-story` | Add a single user story with proper numbering |
| `/r-add-directive` | Add constraint/restriction for scenario generation |
| `/r-research-tech` | Research a specific technology |
| `/r-compare-tech` | Compare two technologies for a use case |
| `/r-create-story` | Create a new user story |
| `/r-update-specs` | Update SPECS.md with recent work |
| `/r-log-decision` | Document a decision with rationale |
| `/r-status` | Show current project status |
| `/r-review` | Review and suggest improvements to a file |
| `/r-sync-structure` | Update STRUCTURE.md by scanning folders |
| `/r-list` | List files in a specific project folder |

---

## Project Phases

This project progresses through two main phases: **Gather** and **Run**.

### Phase: GATHER (Current)

The Gather phase collects all information needed to create comprehensive technical specifications. This is an iterative process of accumulating and organizing requirements.

**Inputs during Gather:**
| Input Type | Command | Updates |
|------------|---------|---------|
| Client documents | `/r-add-client-doc` | GOALS.md, USER-STORIES.md, client-docs-index.md, DB-SCHEMA.md, PAGES.md, COMPONENTS.md, API.md |
| Software/services | `/r-add-software <url>` | PLAN.md, research/tech-NNN-*.md |
| User stories | `/r-add-user-story` | USER-STORIES.md |
| Directives | `/r-add-directive` | DIRECTIVES.md |

**Key files that grow during Gather:**
- `GOALS.md` - Mission, goals, success metrics (from client docs)
- `USER-STORIES.md` - All user stories with priorities (250+ stories)
- `DIRECTIVES.md` - Constraints and restrictions for RUN phase
- `DB-SCHEMA.md` - Database entities, fields, relationships (from client docs with data samples)
- `PAGES.md` - Page inventory with data requirements (from user stories and mockups)
- `COMPONENTS.md` - Reusable UI components (from pages and data structures)
- `API.md` - Backend API operations (from user stories and data requirements)
- `PLAN.md` - Phases, tasks, technology inventory
- `/research/` - Tech docs for each software/service evaluated
- `/client-docs/` - Original client materials with index

**Gather workflow:**
1. Add client documents → extracts goals and user stories
2. Add software/services → creates research docs, maps to user stories
3. Add individual user stories → as gaps are discovered
4. Research fills gaps → identifies what services are needed for which stories
5. Analyze documents for architecture implications → updates DB-SCHEMA.md, PAGES.md, COMPONENTS.md, API.md

**Architecture document updates during Gather:**
- When processing client docs with data samples (like database schemas), update DB-SCHEMA.md
- When identifying new pages from user stories or mockups, update PAGES.md
- When pages reveal reusable UI patterns, update COMPONENTS.md
- When user stories imply backend operations, update API.md

**Gather is complete when:**
- All client documents processed
- All required/optional services researched
- User stories mapped to technologies
- Architecture documents (DB-SCHEMA, PAGES, COMPONENTS, API) populated
- Gaps identified and addressed
- Ready to create SPECS.md scenarios

### Phase: RUN

The Run phase transforms gathered information into actionable technical specifications by creating scenario variants.

**Run process:**
1. **Input:** All Gather phase information (client docs, user stories, goals, research, **DIRECTIVES.md**, architecture docs)
2. **Specify:** Choose a base scenario and define changes, restrictions, preferences
3. **Generate:** Fill out SPECS.md for that scenario, honoring all directives
4. **Finalize Architecture:** Update DB-SCHEMA.md, PAGES.md, COMPONENTS.md, API.md for the selected scenario

**Architecture documents in RUN phase:**
- Each scenario may have variations in schema (e.g., different fields for different integrations)
- Each scenario may have different pages (e.g., custom video UI vs embedded BBB)
- Each scenario may specify different component implementations
- Each scenario may have different API patterns (REST vs GraphQL, third-party SDKs)

**Key principles:**
- Later client docs override earlier ones when information contradicts
- Goal is to **minimize custom development time** by leveraging existing software/services
- Every scenario will have custom development; the question is how much

**Conflict resolution (document precedence):**
- CD-004 overrides CD-003 overrides CD-002 overrides CD-001
- More recent documents reflect more current client thinking
- When in doubt, note the conflict and ask for clarification

**Scenario structure:**

| Scenario | Description | Custom Dev | Third-Party Services |
|----------|-------------|------------|---------------------|
| `sc-001-fully-custom` | **Baseline** - No major SaaS (no Stream, no BBB) | Maximum | Cloudflare, Vercel, npm packages only |
| `sc-002-*` | Variations with different service combinations | Varies | Mix of required + optional services |
| `sc-NNN-*` | Additional scenarios as needed | Varies | Different trade-offs |

**sc-001 (Fully Custom) is always the baseline:**
- No Stream, no BigBlueButton, no major SaaS platforms
- Heavy use of infrastructure: Cloudflare services, Vercel services
- Relies on npm packages for functionality
- Represents maximum custom development effort
- Used as comparison point: "How much dev time does Service X save?"

**Run workflow:**
1. User specifies: base scenario + changes/restrictions/desires
2. Claude consults all Gather materials + **DIRECTIVES.md**
3. Claude fills out `/scenarios/sc-NNN-[description]-SPECS.md`, honoring directives
4. User reviews, requests adjustments
5. Final scenario becomes root `SPECS.md` for handoff

**Run is complete when:**
- Client has reviewed scenario options
- Client has selected final scenario
- Selected scenario copied to root `SPECS.md`
- Architecture documents finalized for selected scenario:
  - DB-SCHEMA.md reflects final technology choices
  - PAGES.md reflects final page inventory
  - COMPONENTS.md reflects final component specifications
  - API.md reflects final backend design
- Ready for implementation handoff

---

## Workflow Notes

- **Client docs are read-only** - Reference them but don't modify originals
- **SPECS.md is the handoff document** - Update it as decisions are made
- **Architecture docs accumulate** - DB-SCHEMA, PAGES, COMPONENTS, API grow during GATHER, finalize during RUN
- **Trace decisions to sources** - Link back to research, client docs, or learnings
- **file_holding/ is temporary** - Files staged here get processed and moved
- **Scenarios for comparison** - `/scenarios/` holds SPECS.md variants for client review
