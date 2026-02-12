# CC + Obsidian Vault System — Master Plan

## Overview

This document captures the planning and design decisions for a **practice management vault** — a solopreneur's unified knowledge base, work log, and project management system built on Obsidian and integrated with Claude Code (CC). The vault is project-agnostic; PeerLoop is the first project onboarded and serves as the worked example throughout. The goals are:

1. Give CC structured, access-controlled read access to vault knowledge via a local MCP server
2. Move all project narrative (session logs, plans, decisions, learnings) out of git repos and into Obsidian
3. Keep credentials safe using inline `===` markers with MCP-level redaction
4. Start with a fresh Obsidian vault designed for this architecture from day one
5. Maintain Obsidian Sync compatibility for multi-device access (Mac, phone)
6. Separate truly private content into a second vault (deferred — see Deferred Topics)

---

## Background

### The Problem

A single large Obsidian vault contains everything: personal, business, health, hobbies, client projects, and vendor credentials. This vault cannot be exposed wholesale to CC or any cloud LLM. At the same time, CC needs contextual knowledge from the vault (vendor details, project history, reference material) to be maximally useful during coding sessions.

Separately, CC generates valuable session documentation (prompts/responses, learnings, decisions, plan updates) that currently bloats git repos. This documentation belongs in Obsidian where it can be searched, linked, and browsed across projects and over time.

### Approaches Considered

#### Common Patterns (Evaluated and Set Aside)

**Multi-Vault Split by Sensitivity Tier.** Breaking the monolithic vault into separate vaults (public, private, per-client). Rejected for the main vault because it loses cross-linking, adds vault-switching friction, and increases Obsidian Sync costs. However, a separate private vault for truly personal content (health, journal) is planned — see Deferred Topics.

**Single Vault with CC-Targeted Subfolders via Symlinks.** Keeping one vault but symlinking designated subfolders into CC project directories. Considered as an interim approach. Fragile across machines (symlinks break on clone), and unnecessary if the vault is designed from scratch with clean folder boundaries.

**Obsidian as Dashboard, CC as Source of Truth.** CC project folders hold all working files; Obsidian is a read/review layer with sync scripts pulling outputs in. Rejected because it makes Obsidian a second-class citizen and requires ongoing sync maintenance.

#### Innovative Patterns (Evaluated)

**Git-Mediated Bridge with Selective Sync.** Using Git as intermediary with per-note frontmatter tags controlling what flows between Obsidian and CC. Elegant but over-engineered for a solo workflow — the per-note tagging creates ongoing maintenance burden.

**Local LLM Gateway (Path A).** Using Obsidian plugins (Smart Connections, Copilot) with a local model via Ollama for semantic search within Obsidian. Useful as a stopgap but doesn't bridge to CC — queries stay inside Obsidian's UI.

**Local MCP Server as Vault Query Engine (Path B).** A custom MCP server running locally that gives CC structured, access-controlled read access to the vault. Heading-aware parsing, link traversal, semantic search (optional), and credential redaction. This was selected as the core architecture.

**Full Local RAG with Obsidian Plugin (Path C).** Everything in Path B plus a custom Obsidian plugin providing heading-breadcrumb search results within Obsidian itself. Deferred as a future enhancement — building an Obsidian plugin is a separate project.

### Session Documentation Strategies (Evaluated)

Four strategies were considered for moving CC session docs from repos to Obsidian:

**Strategy 1 — Post-Session Sweep.** A CC skill run manually at session end copies docs from repo to vault. Simple but requires remembering to run it.

**Strategy 2 — Symlinks.** Session doc folders in the vault symlinked into repos. Zero post-session work but fragile across machines.

**Strategy 3 — Git Hooks.** Pre-commit hooks intercept session docs, copy to vault, unstage from commit. Automatic but hooks are invisible and fail silently.

**Strategy 4 — CC Writes Obsidian-Native Notes Directly.** CC writes session docs directly to the vault with full Obsidian formatting (frontmatter, wikilinks, tags). Session docs are born as first-class vault citizens. Selected as the target approach.

### Credential Handling

**Decision:** Sensitive credential values in the vault are wrapped in triple equals signs: `===value===`. This convention was chosen because:

- The values are already obfuscated (they require translation that is not documented in the vault), so plaintext storage is not a concern
- Obsidian renders the outer `==` as highlight syntax, making credentials visually prominent — easy to spot and confirm they're properly wrapped
- One regex (`/===(.+?)===/g`) handles detection and redaction in the MCP server
- Easy to audit: search `===` in Obsidian to find all credentials and verify enclosure

Credentials are stored inline within vendor/service notes (e.g., in `reference/`), not in a separate folder. The MCP server strips `===`-wrapped values before returning any content to CC.

### Obsidian Sync Considerations

- Standard plan ($4/mo): 1 synced vault, 1 GB storage
- Plus plan ($8/mo): up to 10 synced vaults, 10 GB storage
- Two vaults (main + private) requires the Plus plan
- Sync is transparent to the MCP server — the server reads local files, Sync updates them in the background, no conflict as long as the MCP server is read-only
- If CC writes session docs directly to the vault, those writes propagate via Sync to phone and other devices automatically
- Sync data is end-to-end encrypted (AES-256) — Obsidian cannot read vault contents on their servers

---

## Decided Architecture

### Core Principles

1. **The repo is code. The vault is narrative.** No session docs, plans, or decision logs in git repos. Repos contain only code, config, README, and CLAUDE.md.
2. **Single access tier for the main vault.** Everything in the main vault is CC-accessible. Truly private content lives in a separate private vault (deferred). The only security mechanism in the main vault is `===` credential redaction.
3. **CC reads from the vault via MCP. CC writes to the vault via global skills.** One path in, one path out, both controlled. Global skills from this project use the `cco-` prefix (e.g., `/cco-session-close`) to avoid collisions with other projects' global commands.
4. **Every project has a parallel presence** in `~/projects/{name}/` (code) and `~/Vaults/main/projects/{name}/` (narrative).
5. **Session docs are Obsidian-native from birth.** Frontmatter, wikilinks, tags — written by CC's `/cco-session-close` skill, not migrated after the fact.
6. **Daily notes are the capture surface. Atomic notes are the knowledge base.** You write freely in daily notes; CC processes qualifying headings into structured atomic notes with frontmatter.
7. **A "project" is anything with a wikilink.** If a heading contains `[[PeerLoop]]` or `[[MeristicsSite]]`, that's a project. No separate project registry needed.

### System Diagram

*Shown with PeerLoop as the example project. Any onboarded project gets the same repo ↔ vault structure.*

```
┌─────────────────────┐         ┌──────────────────────────────┐
│  ~/projects/peerloop │         │  ~/Vaults/main/                    │
│  (git repo)          │         │  (main Obsidian vault)       │
│                      │         │                              │
│  src/                │         │  journal/daily/              │
│  public/             │         │    2026-02-09.md  ◄── you    │
│  CLAUDE.md ──────────┼────┐    │                              │
│  .git/               │    │    │  log/                        │
│                      │    │    │    2026-02-09 • PeerLoop.md  │
│  (no docs, no plan)  │    │    │       ▲                      │
└─────────────────────┘    │    │       │ /cco-process-daily    │
                            │    │                              │
                            │    │  projects/peerloop/          │
                            │    │    PeerLoop.md  (project log)│
                            │    │    PeerLoop-tasks.md         │
                            │    │    plan.md                   │
                            │    │    sessions/                 │
                            │    │      2026-02-09.md ◄── CC    │
                            │    │    decisions.md   ◄── writes │
                            │    │    learnings.md   ◄──        │
                            │    │                              │
                            │    │  reference/  business/       │
                            │    └──────────────┬───────────────┘
                            │                   │
                       ┌────▼───────────────────▼──┐
                       │  MCP Server (local)        │
                       │  - Heading-aware parser     │
                       │  - === credential redaction  │
                       │  - Semantic search (future)  │
                       └──────────────────────────────┘
```

### Vault Folder Structure

```
~/Vaults/main/
│
├── journal/                    CC access: FULL
│   └── daily/                  Daily notes (your capture surface)
│       ├── 2026-02-09.md
│       └── 2026-02-10.md
│
├── log/                        CC access: FULL
│   ├── notes/                  General atomic notes from daily note processing
│   │   ├── 2026-02-09 • PeerLoop.md
│   │   ├── 2026-02-09 • PeerLoop • Cloudflare.md
│   │   └── 2026-02-09 • Health.md
│   ├── coding/                 Coding session timecards
│   ├── non-coding/             Non-coding work timecards
│   ├── meetings/               Meeting timecards
│   ├── slack/                  Slack thread records
│   ├── email/                  Email thread records
│   └── telegram/               Telegram thread records
│
├── projects/                   CC access: FULL
│   ├── peerloop/
│   │   ├── PeerLoop.md         Project log (chronological links to log/ entries)
│   │   ├── PeerLoop-tasks.md   Active tasks with links back to log/ for context
│   │   ├── plan.md
│   │   ├── sessions/           CC session notes (written by /cco-session-close)
│   │   │   └── {date}.md
│   │   ├── decisions.md
│   │   └── learnings.md
│   ├── meristics-site/
│   │   └── (same structure)
│   └── _archive/               Completed projects
│
├── reference/                  CC access: FULL
│   ├── tech-notes/
│   ├── vendors/                Vendor notes (credentials inline with === markers)
│   ├── schemas/                Versioned schemas for structured record types
│   ├── patterns/
│   └── templates/
│
└── business/                   CC access: FULL
    ├── clients/
    ├── meristics/
    └── invoicing/
```

All folders are CC: FULL access. The only redaction is `===`-wrapped credential values, which are stripped by the MCP server regardless of which folder they appear in.

### Project Repo Structure (Per Project)

*Example for PeerLoop. All onboarded projects follow this convention.*

```
~/projects/peerloop/
├── src/
├── public/
├── astro.config.mjs
├── package.json
├── CLAUDE.md                    Points CC to vault project path
├── .git/
└── (code files only — no docs, no plan)
```

### CLAUDE.md Convention

Each repo's `CLAUDE.md` includes a vault integration section. *Example shown for PeerLoop; every onboarded project adds the same block with its own paths.*

```markdown
# PeerLoop

Astro-based web application.

## Vault Integration
- Vault project path: ~/Vaults/main/projects/peerloop
- Vault path: ~/Vaults/main
- Session docs, plan, decisions, and learnings are in the vault, not this repo
- Read plan.md from the vault at session start
- Write session docs to the vault at session end
- Use the `/cco-session-close` global skill to write session documentation
```

### MCP Server Access Rules

```yaml
vault_path: ~/Vault

access_rules:
  full_access:
    - "*"       # All folders in main vault are CC-accessible

credential_redaction:
  pattern: "===(.+?)==="
  replacement: "[REDACTED]"
```

The MCP server is read-only. It never modifies vault files. CC writes to the vault directly via global skills (`/cco-session-close`, `/cco-process-daily`), bypassing the MCP server entirely.

### PLAN.md Format

Each project's `plan.md` in the vault uses named (not numbered) phases and tasks with dot-notation addressing. A separate **Current Sequence** at the top defines execution order, decoupling *what* from *when*. *Format shown for one project; every onboarded project uses the same structure.*

```markdown
# PLAN — PeerLoop

## Current Sequence
1. GLOBAL-SKILLS.SESSION-CLOSE.READ-PROJECT
2. GLOBAL-SKILLS.SESSION-CLOSE.WRITE-FRONTMATTER
3. GLOBAL-SKILLS.SESSION-CLOSE.APPEND-DECISIONS
---

## FOUNDATION ✅
Setup vault structure and initial configuration. → [[COMPLETED-PLAN#FOUNDATION]]

## GLOBAL-SKILLS 🔄

### SESSION-CLOSE
- [ ] READ-PROJECT — Skill reads project name from CLAUDE.md or cwd
- [ ] WRITE-FRONTMATTER — Writes session note with frontmatter, wikilinks, tags
- [ ] APPEND-DECISIONS — Appends to decisions.md and learnings.md

### PROCESS-DAILY
- [ ] IDENTIFY-HEADINGS — Find qualifying headings
- [ ] CREATE-ATOMIC — Create/append atomic notes in log/

## MCP-SERVER
Build local MCP server. Details TBD after GLOBAL-SKILLS.

## SCALE
Migrate remaining projects. TBD.
```

**Conventions:**
- **Named phases:** `FOUNDATION`, `GLOBAL-SKILLS`, `MCP-SERVER` — not numbered, order is fluid
- **Dot-notation addressing:** `GLOBAL-SKILLS.SESSION-CLOSE.READ-PROJECT` — unambiguous references
- **Current Sequence:** Short dependency chain at the top. When exhausted, CC asks what to tackle next
- **Phase markers:** `✅` complete (one-liner + link to COMPLETED-PLAN), `🔄` active (full detail), no marker = future (sparse)
- **COMPLETED-PLAN.md:** Full detail of completed phases moves here. PLAN.md retains just the heading + one-line summary

### Task Conventions

**Human-authored tasks** (under `##` headings) use `+` symbols for importance. During `/cco-process-daily` extraction, CC converts to a queryable inline field:

**In daily note:** `- [ ] Fix token refresh +++++`
**In task file:** `- [ ] Fix token refresh [importance:: 5] — [[2026-02-09 • PeerLoop]]`

More `+` = more important. No cap, but practically 1-5.

**Skill-generated tasks** (inside `####` card sections) are plain `- [ ]` checkboxes — no `[importance::]`. Importance is a human judgment applied to hand-written tasks only.

**Due dates:** Optional. `[due:: YYYY-MM-DD]` inline field, only when a deadline is explicitly mentioned.

**Watching-for marker:** `[[expect]]` wikilink. `- [ ] [[expect]] [[Person]] to do X`. Creates a backlink collection point — CC greps for `[[expect]]` to answer "what am I waiting for?" queries. No Obsidian Tasks plugin emoji (`🔺`, `⏳`).

**Decisions:** `- [ ] Decide: description` prefix for tasks requiring a decision.

No delegation/assignee fields — solo workflow. `[[expect]]` tracks others' commitments, not delegation.

---

## Daily Note Processing Workflow

### Daily Note Format

Daily notes live in `journal/daily/` and are named by date: `2026-02-09.md`. You write freely under headings throughout the day. Headings containing `[[wikilinks]]` are **qualifying headings** — eligible for processing into atomic notes.

**Heading hierarchy:**
- `##` — Qualifying headings (contain `[[wikilinks]]`)
- `###` — Timecard headings (`### 🕒 {CardType} • {start}`)
- `####` — Body sections within a timecard (Discussion, Tasks, etc.)

**Timecard heading regex:** `### 🕒 (.+?) • (\d{2}:\d{2})`

**Card types in daily notes:**

| CardType in heading | Maps to card `type:` | Notes |
|---------------------|---------------------|-------|
| `Meeting` | meeting | via field: Zoom, Google Meet, In-Person |
| `Phone Call` | meeting (via: Phone) | Derived from heading by `/cco-process-daily` |
| `Site Visit` | meeting (via: Site Visit) | Derived from heading by `/cco-process-daily` |
| `Non-Coding` | non-coding | |
| `Slack` | slack | From `/cco-slack` comms skill |
| `Email` | email | From `/cco-email` comms skill |
| `Telegram` | telegram | From future comms skill |

**Coding timecards are NOT entered in daily notes** — they are generated by `/cco-session-close` from git history.

```markdown
## [[PeerLoop]]
Client wants dark mode by March. OAuth bug might be a token refresh timing issue.
- [ ] Investigate token refresh timing +++++
- [ ] Draft dark mode proposal ++
### 🕒 Non-Coding • 07:00
- `Focus  `:: SPA-like navigation with Astro View Transitions
- `Start  `:: 07:00
- `End    `:: 09:00
- `Adjust `:: 40
- `Bill?  `:: Block-04
#### Work Effort
- Added ClientRouter to AppLayout for SPA-like navigation
### 🕒 Meeting • 09:00
- `Focus  `:: Status Update
- `Who    `:: [[Gabriel]] • [[Brian]]
- `Via    `:: [[Zoom]]
- `Record `:: Gabriel
- `Start  `:: 09:00
- `End    `:: 09:50
- `Adjust `:: 0
- `Bill?  `:: Block-04
#### Discussion
- Brian said PL will be invite-only at the beginning
- Gabriel suggested Puppeteer for multi-device testing
#### Decisions
- PeerLoop alpha will be invite-only
#### Tasks
- [ ] Look into Puppeteer MCP server +++

## [[PeerLoop]] • [[Cloudflare]]
Token refresh fails when Cloudflare Workers cold-start after 10min idle.

## Journal
Had a good day. Coffee was excellent.

## Random thoughts
What if we built a CLI for vault queries?
```

### Qualifying Headings

A heading qualifies for processing if it contains at least one `[[wikilink]]`. In the example above:
- `## [[PeerLoop]]` — qualifies (one project)
- `## [[PeerLoop]] • [[Cloudflare]]` — qualifies (two projects)
- `## Journal` — does not qualify (no wikilink, stays in daily note)
- `## [[Health]]` — qualifies
- `## Random thoughts` — does not qualify (stays in daily note)

Non-qualifying headings remain in the daily note untouched.

### Atomic Note Naming

Extracted notes are named: `{date} • {heading text without brackets}.md`

Examples:
- `## [[PeerLoop]]` → `2026-02-09 • PeerLoop.md`
- `## [[PeerLoop]] • [[Cloudflare]]` → `2026-02-09 • PeerLoop • Cloudflare.md`
- `## [[Health]]` → `2026-02-09 • Health.md`

All atomic notes live in the `log/` folder.

### Processing Rules

**Merge rule:** One atomic note per unique heading-signature per day. If you write `## [[PeerLoop]]` twice in the same daily note (morning and evening), both sections merge into a single `2026-02-09 • PeerLoop.md`. If you process the daily note a second time later in the day, CC finds the existing atomic note and appends.

**Multi-project rule:** A heading with multiple wikilinks (e.g., `## [[PeerLoop]] • [[Cloudflare]]`) creates **one** atomic note. Both project logs (`PeerLoop.md` and the Cloudflare equivalent) get a link to that same atomic note.

**Replacement rule:** After extraction, the qualifying heading's content in the daily note is replaced with a wikilink to the new atomic note. The daily note becomes a breadcrumb trail of your day.

**Idempotent processing:** Running `/cco-process-daily` multiple times on the same daily note only processes new or modified qualifying headings. Already-processed headings (now showing links instead of content) are skipped.

### Atomic Note Structure

Each atomic note in `log/` has frontmatter linking it to its projects:

```markdown
---
date: 2026-02-09
projects: [Peerloop, Cloudflare]
source: "[[2026-02-09]]"
---

Token refresh fails when Cloudflare Workers cold-start after 10min idle.
```

### Project Logs

Each project has a log note (e.g., `projects/peerloop/PeerLoop.md`) that serves as the chronological index of all log entries for that project. This is the wikilink target — `[[PeerLoop]]` resolves here.

```markdown
# Peerloop

## 2026-02-09
- [[2026-02-09 • PeerLoop]]
- [[2026-02-09 • PeerLoop • Cloudflare]]

## 2026-02-07
- [[2026-02-07 • PeerLoop]]
```

Hover any link in Obsidian → preview the full atomic note content. This gives a complete chronological project view.

### The `/cco-process-daily` Skill

A CC global skill that processes a daily note. When invoked:

1. Reads the specified daily note (default: today)
2. Identifies all qualifying headings (those containing `[[wikilinks]]`)
3. For each qualifying heading:
   a. Creates (or appends to) the atomic note in `log/notes/` with frontmatter
   b. Identifies `### 🕒 Timecard` sub-headings and extracts each as an individual card note in the appropriate `log/` subfolder (`coding/`, `meetings/`, etc.) with schema frontmatter
   c. Identifies other card-type sub-headings (Slack, email, telegram) and extracts similarly
   d. Updates each referenced project's log note with links to all extracted notes
   e. Extracts tasks into per-project task files, converting `+++++` to `[importance:: 5]` (human-authored tasks only; skill-generated tasks are plain checkboxes)
   f. Replaces the heading's content in the daily note with wikilinks
4. Leaves non-qualifying headings untouched

---

## Task Management

### Where Tasks Live

Tasks originate in daily notes as standard Obsidian checkboxes (`- [ ]`). During `/cco-process-daily` processing, tasks are extracted into per-project task files with bidirectional links.

### Per-Project Task Files

Each project has a `{Project}-tasks.md` file (e.g., `projects/peerloop/PeerLoop-tasks.md`) containing all active tasks for that project:

```markdown
# Peerloop — Tasks

- [ ] Investigate token refresh timing [importance:: 5] [due:: 2026-02-20] — [[2026-02-09 • PeerLoop]]
- [ ] Draft dark mode proposal [importance:: 2] — [[2026-02-09 • PeerLoop]]
- [x] Set up CI pipeline — [[2026-02-07 • PeerLoop]]
```

Each task links back to the atomic note where it was born — hover the link to see the full context explaining *why* the task exists.

### Bidirectional Linking

In the atomic note (`log/2026-02-09 • PeerLoop.md`), extracted tasks are marked as moved:

```markdown
Client wants dark mode by March. OAuth bug might be a token refresh timing issue.
- [x] Investigate token refresh timing → moved to [[PeerLoop-tasks]]
- [x] Draft dark mode proposal → moved to [[PeerLoop-tasks]]
```

The task is marked done in the atomic note (extracted, not completed) and the real task with its status lives in the project tasks file.

### Dataview for Passive Views

Dataview queries in project notes provide always-visible task dashboards:

```dataview
TASK FROM "projects/peerloop/PeerLoop-tasks"
WHERE !completed
SORT priority DESC
```

These render live in Obsidian (including mobile) without CC running.

### CC for Active Task Work

CC can search, filter, update, and report on tasks via MCP access. Natural language queries like "What's outstanding for Peerloop involving Cloudflare?" work across the vault without brittle DQL syntax.

---

## Reports

Three report types are needed:

### 1. Timecards

Work effort tracking with structured schema. Timecards cover:
- CC coding sessions
- Meetings
- Research
- Slack threads
- Any other billable/trackable work

**Timecard schema and storage format: TBD.** Will be designed as part of the `/cco-process-daily` skill. Timecards are level-3 headings (`###`) under project headings in daily notes, with a structured format that CC can parse.

### 2. Project Journal Between Dates

A full chronological record of all log entries for a given project within a date range. CC queries `log/` for atomic notes where `projects` frontmatter contains the project name and `date` falls within range. Returns entries in date order.

Can also be rendered as a Dataview query for passive viewing:

```dataview
TABLE date, projects
FROM "log"
WHERE contains(projects, "Peerloop") AND date >= date("2026-01-01") AND date <= date("2026-02-09")
SORT date ASC
```

### 3. Task Lists by Ad Hoc Criteria

Query tasks across projects by any combination of: project, vendor, priority, due date, completion status. Examples:

- All open tasks for Peerloop
- All tasks involving Cloudflare across all projects
- All overdue tasks across everything

Dataview handles simple versions on desktop; CC handles complex cross-referencing via MCP.

**Mobile limitation:** DataviewJS with external scripts (`dv.view()`) does not work on Android/iOS. Basic DQL queries may work but are unreliable on mobile. Reports that must be visible on mobile should not depend on Dataview — see Mobile Strategy below.

---

## Mobile Strategy

### The Problem

DataviewJS with external scripts (`dv.view()`) does not run on Obsidian mobile (Android/iOS). Even basic Dataview DQL queries are unreliable on mobile. This means live-computed views (task dashboards, reports) cannot depend on Dataview for mobile use.

Pre-rendering reports as static markdown files was considered but rejected — it violates single source of truth by duplicating data.

### Solution: CC Headless Mode on Mac Mini

Claude Code supports headless (non-interactive) execution via `claude -p`. The Mac Mini is always on. When you edit a daily note on your phone, Obsidian Sync propagates the change to the Mac Mini. CC can run headlessly to process the note and write results back to the vault, which Sync then propagates back to your phone.

```
Phone (Obsidian)                    Mac Mini (always on)
┌──────────────┐                   ┌─────────────────────────┐
│ Edit daily    │──Obsidian Sync──→│ Trigger detected         │
│ note on phone │                   │                          │
│               │                   │ claude -p "Process       │
│               │                   │   today's daily note"    │
│               │                   │   --allowedTools "..."   │
│               │                   │                          │
│ See updated   │◄──Obsidian Sync──│ Atomic notes, tasks,     │
│ project logs  │                   │ project logs updated     │
└──────────────┘                   └─────────────────────────┘
```

### Trigger Options

Three ways to trigger headless CC on the Mac Mini:

1. **File watcher** — `fswatch` or `watchman` monitors `journal/daily/` for changes from Obsidian Sync. When a daily note is modified, runs `/cco-process-daily` headlessly. Near-real-time processing.

2. **Cron schedule** — Run `/cco-process-daily` every N minutes. Simple but processes even when nothing changed. Good as a fallback.

3. **Manual trigger from phone** — An Apple Shortcut, Tasker (Android), or simple webhook that SSHes into the Mac Mini and runs the command. On-demand processing when you want it.

### Headless Command Pattern

```bash
claude -p "Process today's daily note at ~/Vaults/main/journal/daily/$(date +%Y-%m-%d).md. \
  Identify qualifying headings (containing [[wikilinks]]). \
  Create/update atomic notes in ~/Vaults/main/log/. \
  Update project logs and task files. \
  Replace processed content with wikilinks." \
  --allowedTools "Read,Write,Edit,Bash(date *)" \
  --append-system-prompt "Follow the /cco-process-daily workflow exactly."
```

### What This Preserves

- **Single source of truth** — no pre-rendered copies. Tasks live in task files, logs live in log files. CC queries and writes the real data.
- **Mobile read access** — all vault content is plain markdown. Obsidian renders it on any device without plugins.
- **Mobile write access** — you write in daily notes on your phone. CC processes them on the Mac Mini. Results sync back.

---

## Schema System

### The Problem with Obsidian Templates

Obsidian templates (via Templater or core Templates plugin) are "stamp once" — they create a note from a template at creation time, and the note is independent from that point forward. If you change the template, existing notes don't update. For structured record types (timecards, Slack threads, email threads, Zoom meetings, site visits), this means schema evolution is painful — you can't add a field and have it appear in all existing records.

### Solution: Versioned Schemas + CC Migration

Every card type has a **schema definition** stored in the vault:

```
reference/schemas/
  coding.md
  non-coding.md
  meeting.md
  slack.md
  email.md
  telegram.md
```

Each schema defines the frontmatter fields, their types, defaults, and a version number:

```markdown
# Coding Card Schema

schema-version: 1

## Fields
| Field | Type | Default | Required | Added |
|-------|------|---------|----------|-------|
| type | string | "coding" | yes | v1 |
| schema-version | integer | 1 | yes | v1 |
| date | date | — | yes | v1 |
| project | string | — | yes | v1 |
| focus | string | — | yes | v1 |
| start | string | — | yes | v1 |
| end | string | — | yes | v1 |
| adjust | integer | 0 | yes | v1 |
| bill | string | "" | no | v1 |
| tools | list | [] | no | v1 |
| machine | string | "" | no | v1 |
| commits | integer | 1 | no | v1 |
| sessions | list | [] | no | v1 |
| commit-range | string | "" | no | v1 |

## Changelog
- v1: Initial schema
```

### How It Works

**At creation time:** CC (or a template) creates a note with frontmatter matching the current schema version:

```yaml
---
type: coding
schema-version: 1
date: 2026-02-02
project: PeerLoop
focus: "SPA-like navigation with Astro View Transitions"
start: "07:00"
end: "09:00"
adjust: 40
bill: Block-04
tools: [Claude Code]
machine: MacMini
commits: 1
sessions: [159]
---
```

**At migration time:** When a schema changes, run `/cco-migrate-schema coding`. The skill:

1. Reads `reference/schemas/coding.md` — current version is (e.g.) 2
2. Finds all notes with `type: coding` where `schema-version` < 2
3. For each outdated note:
   - Adds missing fields with their defaults
   - Renames fields if the changelog specifies a rename
   - Bumps `schema-version` to current
4. Reports: "Updated 47 timecard notes from v2 → v3 (added `billable: true`)"

### Body Content Migrations

Frontmatter changes are mechanical (add field, set default). If a schema change also affects body content (e.g., adding a new section), the changelog describes the body change and CC applies it:

```markdown
## Changelog
- v4: Added `## Follow-up` section after `## Notes` (default: empty)
- v3: Added `billable` field (default: true)
```

### Card Type Specifications

Six card types, all sharing base frontmatter. Each has its own `log/` subfolder, schema, and body structure.

**Card naming convention:** `{date} • {project} • {card-type} • {start-time}.md`

Examples:
- `2026-02-02 • PeerLoop • Coding • 0700.md`
- `2026-02-02 • PeerLoop • Meeting • 0900.md`
- `2026-02-02 • PeerLoop • Slack • 1653.md`
- `2026-02-09 • PeerLoop • Email • 0756.md`

**Summary:**

| Card Type | Timed | CC-generated | Human-entered | Folder |
|-----------|-------|-------------|---------------|--------|
| coding | Yes | Yes (from git) | No | `log/coding/` |
| non-coding | Yes | No | Yes (daily note) | `log/non-coding/` |
| meeting | Yes | No | Yes (daily note) | `log/meetings/` |
| slack | Yes | No | Yes (daily note) | `log/slack/` |
| email | Partial (end optional) | No | Yes (daily note) | `log/email/` |
| telegram | Yes | No | Yes (daily note) | `log/telegram/` |

**Base frontmatter** (shared by all card types):

```yaml
type: <card-type>
schema-version: 1
date: YYYY-MM-DD
project: <ProjectName>
focus: "<one-liner description>"
bill: <billing-block>          # optional, e.g., Block-04
```

---

#### Coding Card

**Created by:** `/cco-session-close` (auto-generated from git history, not from daily notes). Runs from the project repo, writes to vault via path in CLAUDE.md.

**Additional frontmatter:**
```yaml
start: "HH:MM"
end: "HH:MM"
adjust: 0
tools: [Claude Code]
machine: MacMini
commits: 3
sessions: [161, 162, 163]
commit-range: "573b38e..6a37377"
```

**Body sections:**

```markdown
## For Client
- (client-visible changes — optional section)

## For Admin
- (admin-visible changes — optional section)

## Work Effort
- (technical work details — all commits consolidated)

## Learnings
- (optional)

## Git History

### 573b38e — Session 161 — 15:40
Schema consolidation, CurrentUser expansion, settings pages
- Removed deprecated role flags from schema
- 17 files changed, 5 settings pages migrated

### 356be32 — Session 162 — 17:04
bio→bio_full migration, Permission vs State architecture
- Migrated bio field to bio_full across types, APIs, components, loaders

### 6a37377 — Session 163 — 17:42
Removed deprecated role flags, implemented Permission vs State
- Updated 26 source files
```

**Notes:**
- For Client and For Admin are separate sections (for billing). Both optional, one or both may be present.
- Git History uses `### hash — Session N — HH:MM` headings, one per commit.
- All content derived from git commit messages, not from CC session conversation.
- Existing `/q-timecard` skill logic (parse git, synthesize focus/client/work effort) will be integrated into `/cco-session-close`.

---

#### Non-Coding Card

**Created by:** Human entry in daily note → extracted by `/cco-process-daily`

**Daily note heading:** `### 🕒 Non-Coding • HH:MM`

**Additional frontmatter:**
```yaml
start: "HH:MM"
end: "HH:MM"
adjust: 0
bill: Block-04                 # billing block, or "No" if not billable
tools: [Claude Code]           # optional
```

**Body sections (all `####` level):**

```markdown
#### Work Effort
- Documenting glossary flow
- Backfilling glossary terms according to Carlos's review
- We must allow a certain amount of bias in any reviewer including LLMs
#### Tasks
- [ ] Are there LLM / Models that are better at translations?
```

**Notes:**
- Simpler than coding cards — no Git History, no For Client/For Admin, no machine.
- All body sections are `####` to nest under the `###` timecard heading.
- Tasks extracted to project task files during processing.

---

#### Meeting Card

**Created by:** `/cco-meeting` skill (skeleton) + human editing → extracted by `/cco-process-daily`

**Daily note heading:** `### 🕒 Meeting • HH:MM`, `### 🕒 Phone Call • HH:MM`, or `### 🕒 Site Visit • HH:MM`

**Additional frontmatter:**
```yaml
start: "HH:MM"
end: "HH:MM"
adjust: 0
bill: Block-04                 # billing block, or "No" if not billable
who:
  - "[[Gabriel]]"
  - "[[Brian]]"
  - "[[Guy]]"
via: Zoom                      # Zoom, Google Meet, Phone, Site Visit, In-Person, etc.
record: Gabriel                # who is taking notes / recording (optional)
from: them                     # optional — "me", "them", or name. Mainly for phone calls.
where: "123 Main St"           # optional — for site visits
```

**`/cco-process-daily` derives `via`:** For `Phone Call` and `Site Visit` headings, the card type in the heading maps to the `via` field in the card note frontmatter. For `Meeting`, `via` comes from the inline field.

**Body sections (all `####` level, nested under `###` timecard heading):**

Meeting / In-Person:
```markdown
#### Discussion
- Brian said PL will be invite-only at the beginning
- Gabriel suggested Puppeteer for multi-device testing
#### Decisions
- PeerLoop alpha will be invite-only
#### Transcript
(from Otter.ai — inserted by /cco-otter when record field is filled in)
#### Tasks
- [ ] Look into Puppeteer MCP server +++
```

Phone Call / Site Visit:
```markdown
#### Reason
- Follow up on contract revisions
#### Discussion
- ...
#### Tasks
- [ ] ...
```

**Notes:**
- Meeting card covers video calls, phone calls, site visits, and in-person meetings. The `via` field distinguishes them.
- `who` is a YAML list of wikilinks to people notes.
- `from` is optional — mainly for phone calls (who initiated).
- `where` is optional — mainly for site visits (location).
- `record` indicates who is recording or taking notes. When present, `#### Transcript` section may be added by `/cco-otter`.
- Phone calls and site visits use `#### Reason` instead of `#### Decisions`.
- All body sections are `####` to nest under the `###` timecard heading.
- Tasks extracted to project task files during processing.

---

#### Slack Card

**Created by:** `/cco-slack` comms skill (from screenshot/paste) → human editing → extracted by `/cco-process-daily`

**Daily note heading:** `### 💬 Slack • {channel} • HH:MM`

**Additional frontmatter:**
```yaml
start: "HH:MM"
end: "HH:MM"
channel: "#peer-loop-team"
who:
  - "[[Brian LeBlanc]]"
```

**Body sections (all `####` level):**

```markdown
#### Discussion
- [[Brian LeBlanc]] shared news: AAIF launching — Block, Anthropic, OpenAI + Google
- AGENTS.md is "README for AI agents" — adopted by 20K+ repos
- I noted: CLAUDE.md, GEMINI.md, AGENTS.md — can use all three per folder
#### Links
- [AAIF announcement (X)](https://x.com/blockopensource/status/...)
#### Tasks
- [ ] Decide: Standardize file naming for tests
```

**Notes:**
- Timed card (start/end required) — a Slack conversation that becomes billable can have its times used.
- `channel` identifies the Slack channel.
- Links section captures any URLs shared in the thread.
- All body sections are `####` to nest under the `###` timecard heading.

---

#### Email Card

**Created by:** `/cco-email` comms skill (from Gmail) → human editing → extracted by `/cco-process-daily`

**Daily note heading:** `### 📫 Email • {person} • HH:MM`

**Additional frontmatter:**
```yaml
start: "HH:MM"
end: ""                        # optional — may not have a clear end time
subject: "Revised .docx of Agreement"
who:
  - "[[Brian LeBlanc]]"
continued: new                 # or wikilink to prior email card: "[[2026-02-07 • PeerLoop • Email • 1430]]"
```

**Body sections (all `####` or `#####` level):**

```markdown
##### from: Me — 07:56
- Sent revised .docx of engagement letter
- My edits in red text, removals in red strikethrough
##### from: Brian — 10:30
- Confirmed receipt
- Forwarding to lawyer for review
#### Attachments
- (attachment references)
#### Tasks
- [ ] [[expect]] [[Brian LeBlanc]] to deliver lawyer feedback
```

**Notes:**
- Email bodies are **summarized as bullet points**, not quoted verbatim. The original lives in the email client.
- Multiple `##### from:` sections when replies happen the same day (chronological order).
- `continued: new` for new threads; wikilink to prior card for continuations, creating a thread chain.
- `end` is optional — email exchanges don't always have a clear end time.
- All body sections are `####`/`#####` to nest under the `###` timecard heading.

---

#### Telegram Card

**Created by:** Comms skill (future) → human editing → extracted by `/cco-process-daily`

**Daily note heading:** `### 🕒 Telegram • {channel} • HH:MM`

**Additional frontmatter:**
```yaml
start: "HH:MM"
end: "HH:MM"
channel: "group-name"          # or DM
who:
  - "[[Person]]"
```

**Body sections (all `####` level):**

Same structure as Slack card (Discussion, Links, Tasks).

**Notes:**
- Follows the Slack card schema with minor field differences (channel may be a group name or DM indicator instead of a Slack channel with `#` prefix).
- All body sections are `####` to nest under the `###` timecard heading.

---

### Creation Paths

*Both paths work for any onboarded project. PeerLoop shown as example.*

Cards enter the vault via two paths:

**Path 1 — CC-generated (coding cards):**
```
~/projects/peerloop/ (git repo)
  → /cco-session-close
  → reads git history
  → writes coding card to ~/Vaults/main/log/coding/
```

**Path 2 — Human-entered (all other cards):**
```
Daily note (journal/daily/2026-02-09.md)
  → you write under ## [[PeerLoop]] with ### card markers
  → /cco-process-daily extracts cards
  → writes to appropriate log/ subfolder
```

### Relationship to Daily Notes

Human-entered cards originate in daily notes under qualifying headings and are extracted by `/cco-process-daily`. Coding cards are never in daily notes — they're generated directly from git history. The schema system works for both paths — the `type` and `schema-version` frontmatter is the same regardless of how the card was created.

Existing timecards from the old vault can be migrated by pasting them into daily notes and running `/cco-process-daily`, which recognizes the `### 🕒 Timecard` marker and converts to the new standalone format.

---

## CC Session Documentation Workflow

### Session Note Template

CC coding sessions produce their own notes via `/cco-session-close`, separate from daily note processing. One session note per project per day — multiple CC sessions on the same project in the same day merge into one note (skill appends to existing note if present):

```markdown
---
project: {project-name}
type: session
date: {YYYY-MM-DD}
tags: [session, {project-name}]
repo: github.com/fraser/{project-name}
commit-range: {first-commit}..{last-commit}
---

# Session: {YYYY-MM-DD}

## What We Did
Summary of prompts asked and CC responses/actions...

## Learnings
- Discovery or insight → appended to [[{project-name}/learnings]]

## Decisions
- Choice made and rationale → appended to [[{project-name}/decisions]]

## Plan Changes
- What changed in [[{project-name}/plan]] and why
```

### Accumulated Files

The `/cco-session-close` skill maintains two running logs per project by appending new entries from each session:

**decisions.md:**
```markdown
# Decisions — PeerLoop

## 2026-02-09
- Switched from JWT to session cookies — [[sessions/2026-02-09#Decisions]]

## 2026-02-07
- Chose PostgreSQL over SQLite for production — [[sessions/2026-02-07#Decisions]]
```

**learnings.md:**
```markdown
# Learnings — PeerLoop

## 2026-02-09
- OAuth token refresh needs 5-second buffer — [[sessions/2026-02-09#Learnings]]
```

### Daily Workflow

*Example for a PeerLoop session. Same flow applies to any onboarded project.*

```
SESSION START
  cd ~/projects/peerloop
  Start CC
  CC reads plan.md from vault via MCP → knows current priorities

DURING SESSION
  Code in the repo as normal
  CC tracks what it's doing, learning, and deciding

SESSION END
  Run /cco-session-close (CC global skill, from project repo)
  The skill:
    1. Reads vault project path from CLAUDE.md
    2. Generates coding timecard from git history → writes to ~/Vaults/main/log/coding/
       (integrates existing /q-timecard logic: parse commits, synthesize focus/client/work effort)
    3. Writes session note to ~/Vaults/main/projects/peerloop/sessions/{date}.md
    4. Appends new entries to decisions.md and learnings.md
    5. Updates plan.md with completed/new tasks
    6. Commits code changes to git (docs are not in the repo)

DAILY NOTE PROCESSING (anytime, separate from coding sessions)
  Run /cco-process-daily
  The skill:
    1. Processes qualifying headings from today's daily note
    2. Creates/updates atomic notes in log/
    3. Updates project logs and task files
    4. Replaces processed content with links in daily note

REVIEW (anytime, any device)
  Open Obsidian → browse sessions, search decisions, review plan
  On phone via Sync → check plan, read learnings, view tasks
```

---

## Implementation Roadmap

### Phase 1 — Foundation (Do First)

*Builds the vault structure and onboards PeerLoop as the proof-of-concept project.*

- [ ] Create the fresh Obsidian vault (`~/Vaults/main/`) with the folder structure above
- [ ] Create `journal/daily/`, `log/`, `projects/`, `reference/`, `business/`
- [ ] Relocate PeerLoop repo: `mv ~/MyAstro/Peerloop ~/projects/peerloop`
- [ ] Create `~/Vaults/main/projects/peerloop/` with plan.md, PeerLoop.md, PeerLoop-tasks.md, sessions/, decisions.md, learnings.md
- [ ] Move any existing session docs and PLAN.md from the repo to the vault
- [ ] Update PeerLoop's CLAUDE.md with vault integration section
- [ ] Update .gitignore to exclude any remaining doc patterns
- [ ] Configure Obsidian Sync on the new vault
- [ ] Populate `reference/vendors/` with vendor notes using `===` credential convention

### Phase 2 — CC Global Skills

- [ ] Design and build the `/cco-session-close` global skill
- [ ] Skill reads project name and vault path from CLAUDE.md
- [ ] Skill generates coding timecard from git history → writes to `log/coding/`
  - Integrate existing `/q-timecard` logic (parse commits, synthesize focus/client/work effort)
  - Support project-specific settings (bill block, machine) via CLAUDE.md or local config
  - Generate For Client / For Admin sections from commit messages
- [ ] Skill writes session note with frontmatter, wikilinks, tags
- [ ] Skill appends to decisions.md and learnings.md
- [ ] Skill updates plan.md
- [ ] Design and build the `/cco-process-daily` global skill
- [ ] Skill identifies qualifying headings (those with `[[wikilinks]]`)
- [ ] Skill creates/appends atomic notes in `log/notes/` with frontmatter
- [ ] Skill recognizes card-type markers (`### 🕒 Timecard`, `### 💬 Slack`, `### 📫 Email`, etc.) and extracts as individual card notes to appropriate `log/` subfolders
- [ ] Skill updates project log notes with links to all extracted notes
- [ ] Skill extracts tasks into per-project task files, converting `+++++` to `[importance:: 5]`
- [ ] Skill replaces processed content in daily note with wikilinks
- [ ] Skill handles merge rule (same heading-signature, same day = merge)
- [ ] Skill handles multi-project headings (one atomic note, multiple project logs updated)
- [ ] Create initial schemas in `reference/schemas/` for all 6 card types (coding, non-coding, meeting, slack, email, telegram)
- [ ] Build `/cco-migrate-schema` skill for backfilling schema changes to existing notes
- [ ] Test all skills across multiple projects
- [ ] Create a `/cco-project-init` skill that sets up both the repo CLAUDE.md and vault project folder for new projects

### Phase 2.5 — Headless Automation

- [ ] Set up CC headless execution on Mac Mini for `/cco-process-daily`
- [ ] Choose trigger mechanism: file watcher (`fswatch`), cron, or manual trigger
- [ ] Configure `--allowedTools` permissions for headless runs
- [ ] Test end-to-end: edit daily note on phone → Sync → Mac Mini processes → Sync → results visible on phone
- [ ] Set up mobile trigger (Shortcut/Tasker/webhook) if using manual trigger approach
- [ ] Monitor and log headless runs for debugging

### Phase 3 — MCP Server (v1)

- [ ] Build a local MCP server (TypeScript; consider Python for Phase 4 semantic search)
- [ ] Implement heading-aware markdown parser (chunk by heading, store heading breadcrumb path)
- [ ] Implement `===` credential redaction (vault-wide, not folder-specific)
- [ ] Expose as MCP tool: `query_vault(query: string) → results with heading paths`
- [ ] Configure CC to connect to the MCP server
- [ ] Test with PeerLoop: "What's the current plan for PeerLoop?" should return plan.md content

### Phase 4 — MCP Server (v2, Optional Enhancements)

- [ ] Add semantic search using local embeddings (Ollama on Mac Mini M4 Pro)
- [ ] Add link traversal (follow [[wikilinks]] 1-2 hops for richer context)
- [ ] Add query-side gating for credential requests (confirmation prompt)
- [ ] Consider building an Obsidian plugin for heading-breadcrumb search within Obsidian itself (Path C from background)

### Phase 5 — Scale

- [ ] Migrate remaining active projects to the `~/projects/` + `~/Vaults/main/projects/` convention
- [ ] Archive completed projects in `~/Vaults/main/projects/_archive/`
- [ ] Build vault linting skill: scans for credentials outside `===` markers, orphaned session notes, broken wikilinks
- [ ] Evaluate whether the old vault can be fully retired

---

## Deferred Topics

### Private Vault / Local LLM

Truly private content (health, personal journal, etc.) will live in a separate Obsidian vault at `~/Vaults/private/`, not accessible to CC or any remote LLM. This vault may be queried by a local LLM (e.g., Ollama on Mac Mini M4 Pro) for personal use. Details to be designed in PLAN.md under a dedicated section.

**To determine:**
- Which note categories belong in the private vault vs. main vault
- Whether the private vault needs its own MCP server (local LLM only)
- Obsidian Sync implications (Plus plan required for 2 vaults)
- Whether daily notes in the main vault can reference private vault content

---

## Resolved Questions

1. **Vault path:** `~/Vaults/main/` (main vault) and `~/Vaults/private/` (private vault, deferred). Current vault at `~/Obsidian Vaults/main2025` will be retired.
2. **Session granularity:** One session note per project per day. Multiple CC sessions on the same project in the same day merge into one note.
3. **Plan.md format:** Named phases with dot-notation addressing (not numbered). Current Sequence at top defines execution order. COMPLETED-PLAN.md holds full detail of completed phases. See PLAN.md Format section.
4. **Existing project docs:** Start fresh. No migration of old session docs. On a project-by-project basis, some docs may be manually moved over.
5. **MCP server language:** TypeScript for v1. Python to be considered for Phase 4 semantic search/embeddings.
6. **Timecard schema:** Six card types (coding, non-coding, meeting, slack, email, telegram). Base fields shared across all types; timed types add start/end/adjust. Detailed schema samples documented — see Schema System section.
7. **Project log note naming:** `PeerLoop.md` — no spaces in filenames, matches the wikilink target `[[PeerLoop]]`.
8. **Task metadata:** Human tasks use `+` importance symbols (converted to `[importance:: N]` during extraction). Skill-generated tasks are plain checkboxes. `[[expect]]` wikilink for watching-for items. `[due:: YYYY-MM-DD]` for explicit deadlines. `Decide:` prefix for decisions. No delegation — solo workflow.
