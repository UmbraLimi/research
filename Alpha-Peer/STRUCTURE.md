# Alpha Peer - Folder Structure & Conventions

**Last Updated:** 2025-11-29

## Project Overview
Alpha Peer is a web application being developed through iterative research and planning. This structure supports opportunistic exploration while maintaining organization for eventual handoff to Claude Code.

## Folder Structure

```
Alpha-Peer/
├── readme.md                           # Project overview
├── STRUCTURE.md                        # THIS FILE - master guide
├── GOALS.md                            # Mission statement & goals (from client docs)
├── USER-STORIES.md                     # All user stories (from client docs)
├── SPECS.md                            # Technical specs for Claude Code (continuously updated)
│
├── /client-docs/                       # Client-provided context & materials
│   └── README.md                      # Guide for organizing client materials
│
├── /research/                          # Technology & concept research
│   ├── tech-NNN-[name].md             # Individual technology research
│   ├── comp-NNN-[topic].md            # Technology comparisons
│   └── notes-NNN-[topic].md           # General research notes
│
├── /user-stories/                      # User stories & requirements
│   └── story-NNN-[short-title].md     # Individual user stories
│
├── /docs/                              # Documentation & session tracking
│   └── /sessions/                     # Session logs organized by month
│       └── /YYYY-MM/                  # Monthly folder (e.g., 2025-11/)
│           ├── YYYY-MM-DD_HH-MM-SS Learnings.md # Session learnings
│           └── YYYY-MM-DD_HH-MM-SS Prompts.md   # Session prompts archive
│
├── /prompts/                           # Reusable prompts & commands
│   ├── prompt-library.md              # Collection of useful prompts
│   └── workflows.md                   # Common workflows
│
├── /learnings/                         # Knowledge capture
│   ├── learnings-index.md             # Quick reference index
│   └── learning-NNN-[topic].md        # Specific learnings
│
└── /decisions/                         # Decision log
    └── decision-NNN-[topic].md        # Why we chose X over Y
```

## Naming Conventions

### Numbering
- **NNN format:** Zero-padded 3 digits (001, 002, ..., 999)
- Numbering is sequential within each category
- If we exceed 999, switch to NNNN format

### File naming patterns
- **Client Documents:** `CD-NNN` prefix in `client-docs-index.md`
  - Example: `CD-001: Alpha_Peer_Business_Plan.pdf`
  - Used for cross-referencing in GOALS.md, USER-STORIES.md, etc.
- **Goals:** `GO-NNN` in `GOALS.md`
  - Example: `GO-001: Validate the Learn-Teach-Earn Flywheel`
  - Supports up to 999 goals
- **User Stories (in USER-STORIES.md):** `US-[Role]NNN`
  - Role codes: A=Admin, C=Creator, S=Student, T=Student-Teacher, E=Employer, V=Video/Session, P=Platform
  - Example: `US-A001`, `US-S015`, `US-T003`
  - Supports up to 999 stories per role
- **User Story files:** `story-NNN-[2-4-word-description].md`
  - Example: `story-001-user-login.md`
  - For detailed story breakdowns (optional)
- **Technologies:** `tech-NNN-[technology-name].md`
  - Example: `tech-001-supabase.md`
- **Comparisons:** `comp-NNN-[what-being-compared].md`
  - Example: `comp-001-auth-providers.md`
- **Sessions:** `YYYY-MM-DD_HH-MM-SS [Type].md` in `docs/sessions/YYYY-MM/`
  - Types: `Learnings`, `Prompts`
  - Example: `docs/sessions/2025-11/2025-11-25_14-30-00 Learnings.md`
- **Learnings:** `learning-NNN-[topic].md`
  - Example: `learning-001-websocket-basics.md`
- **Decisions:** `decision-NNN-[choice-made].md`
  - Example: `decision-001-chose-vercel-hosting.md`

### Content guidelines
- Use lowercase for filenames (except STRUCTURE.md, SPECS.md, GOALS.md, USER-STORIES.md, PLAN.md)
- Use hyphens for spaces in filenames
- Keep filenames descriptive but concise
- Date format: YYYY-MM-DD (ISO 8601)

## File Purposes

### STRUCTURE.md (this file)
The single source of truth for organization. Claude Desktop consults this to know:
- Where to put new files
- What naming convention to use
- What each folder contains
- Current state of numbering

### GOALS.md
Mission statement and goals extracted from client documents. Contains:
- Mission statement and core philosophy
- Strategic goals (G1, G2, etc.)
- Quantified success metrics and targets
- Platform capability goals
- Goal-to-source document traceability

Updated automatically via `/r-add-client-doc` when new documents are processed.

### USER-STORIES.md
Comprehensive list of user stories extracted from client documents. Contains:
- Stories organized by user role (Admin, Creator, Student, Student-Teacher, Employer, System)
- Priority levels (P0=MVP critical, P1=high, P2=medium, P3=nice-to-have)
- Story ID format: `US-[Role][NN]` (e.g., US-A01, US-S15)
- Source document traceability
- Statistics by role and priority

Updated automatically via `/r-add-client-doc` when new documents are processed.

### SPECS.md
The evolving technical specifications document that will be handed to Claude Code. Contains:
- User stories with technology mappings
- Architecture decisions
- Technology stack choices
- Integration requirements
- Non-functional requirements

### Client documents (/client-docs/)
Original materials provided by the Alpha Peer client:
- Requirements documents and briefs
- Meeting notes from client discussions
- Design mockups, wireframes, brand guidelines
- Business context and market analysis
- Keep originals unchanged; reference in research and decisions
- Source of truth for client requirements and constraints

### Session files (`docs/sessions/`)
Session logs are organized by month in `docs/sessions/YYYY-MM/`. Two file types per session:
- **Learnings.md** - Insights, decisions, best practices discovered
- **Prompts.md** - Archive of user prompts for future reference

Created via `/q-end-session` or individual `/q-learnings`, `/q-prompts` commands.

### Prompt library
Reusable prompts for common tasks:
- Research a technology
- Create a user story
- Compare options
- Update SPECS.md
- Create session summary

### Learnings index
Quick reference showing:
- What we've learned (with links to detailed files)
- Key insights
- Gotchas discovered
- Patterns emerging

## Workflow Principles

1. **Opportunistic:** Follow interesting leads as they emerge
2. **Documented:** Every session and decision gets recorded
3. **Iterative:** SPECS.md evolves continuously, not written once
4. **Traceable:** Can always trace why decisions were made
5. **Handoff-ready:** Structure supports giving everything to Claude Code

## Current State

**Last session:** 2025-11-29

| Category | Next Number |
|----------|-------------|
| Client Documents | CD-005 |
| Goals | GO-018 |
| Technologies | tech-001 |
| Story files | story-001 |
| Comparisons | comp-001 |
| Learnings | learning-001 |
| Decisions | decision-001 |

**Note:** User Story numbers (US-XNNN) are tracked in USER-STORIES.md "Current State" section by role.

## Notes for Claude Desktop

When working in this project:
1. Always check this file first to understand current state
2. Update "Current State" section when creating numbered files
3. Reference this structure when asked "where should this go?"
4. Suggest structure improvements as patterns emerge
5. Keep naming conventions consistent

## Updates to This File

Track significant changes to structure:
- 2025-11-25: Initial structure created
- 2025-11-25: Added /client-docs/ folder for client-provided materials
- 2025-11-29: Changed sessions structure to `docs/sessions/YYYY-MM/` with timestamp-based filenames to align with q- commands
- 2025-11-29: Added GOALS.md for mission statement and goals extracted from client documents
- 2025-11-29: Added USER-STORIES.md for comprehensive user story tracking from client documents
- 2025-11-29: Added CD-NNN numbering convention for client documents; renamed Needs.md to SPECS.md
