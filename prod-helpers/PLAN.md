# PLAN.md

## Current Status

**Phase 1 — Foundation** (in progress — 1.1 documented, 1.4 complete except deferred test harness)

---

## Phase 1: Foundation

Establish the infrastructure before migrating data or building agents.

### 1.1 API & Access Audit
- [x] Confirm Dynalist API access and document endpoints needed (CRUD tasks, search, tags)
- [x] Confirm Joplin Clipper API access and document endpoints (notebooks, notes, tags, export)
- [x] Confirm Obsidian CLI (v1.12+) capabilities and document commands available
- [x] Document rate limits, auth mechanisms, and data formats for each
- [ ] Configure Dynalist API token on MacMiniM4 (credentials/MacMiniM4.env)
- [ ] Configure Joplin API token on MacMiniM4 (credentials/MacMiniM4.env)
- [ ] Configure Dynalist API token on MacMiniM4-Pro (credentials/MacMiniM4-Pro.env)
- [ ] Configure Joplin API token on MacMiniM4-Pro (credentials/MacMiniM4-Pro.env)

### 1.2 Tag Mapping System
- [ ] Inventory existing tags in Dynalist
- [ ] Inventory existing tags in Joplin
- [ ] Inventory existing note titles used as tags in Obsidian
- [ ] Design translation table format (likely YAML or JSON, stored outside both apps)
- [ ] Build initial mapping table

### 1.3 Note Format Templates
- [ ] Define Obsidian note format for migrated Joplin notes
- [ ] Define Obsidian note format for migrated Dynalist node trees
- [ ] Define Dynalist format for migrated Obsidian tasks
- [ ] Define format for archived YouTube Shorts (transcript + thumbnail + metadata)
- [ ] Define format for credential lookup notes (JSON/YAML with obfuscated keys)

### 1.4 Project Structure
- [x] Set up directory structure for skills, agents, scripts, and shadow docs
- [x] Create shadow doc template (defined in r-docs skill)
- [x] Machine tracking in commits (Machine: line via r-commit skill)
- [x] Conversation numbering system (CONV-COUNTER, /r-start, /r-end)
- [ ] Update /r-start, /r-end, /r-commit skills to use PROJECT.yaml prefix in conv numbering and commit messages
- [ ] Set up test harness / test conventions (deferred — will establish when first script is created)

---

## Phase 2: Skills (On-Demand Tools)

Build Claude Code skills invoked manually for specific tasks.

### 2.1 Data Migration Skills
- [ ] Joplin → Obsidian note migration skill
- [ ] Joplin → Dynalist task migration skill
- [ ] Dynalist marked-node-trees → Obsidian notes skill
- [ ] Obsidian tasks → Dynalist migration skill

### 2.2 Lookup & Search Skills
- [ ] Cross-app search skill (query Dynalist + Obsidian, return unified results)
- [ ] Credential lookup skill (find in Dynalist/Obsidian, run compiled decoder)

### 2.3 Content Capture Skills
- [ ] YouTube Shorts archival skill (transcript via Whisper + thumbnail + metadata → Obsidian)

---

## Phase 3: Agents (Autonomous with Guard Rails)

Build agents that run under strict directives and halt on unexpected situations.

### 3.1 Agent Framework
- [ ] Define agent directive format (what's covered, what triggers halt)
- [ ] Build guard rail system (condition checking, halt-and-report mechanism)
- [ ] Build agent test harness (simulate expected + unexpected inputs)

### 3.2 Migration Agents
- [ ] Joplin retirement agent (batch migrate with human checkpoints)
- [ ] Tag sync agent (keep translation table current as tags change)

### 3.3 2nd Brain Agents
- [ ] Comm-Helpers integration agent (route Slack/Email/Telegram summaries into correct Obsidian locations)

---

## Phase 4: Cross-App Integration

### 4.1 Unified Tagging
- [ ] Implement tag sync between Dynalist and Obsidian via translation table
- [ ] Validate bidirectional tag resolution

### 4.2 Cross-App Search
- [ ] Unified search across Dynalist + Obsidian with context preview
- [ ] Credential search workflow (find → decode → display)

---

## XFER-COMM-HELPERS: Merge Comm-Helpers into Prod-Helpers

Merge the entire `~/research/Comm-Helpers/` folder into this repo, convert all skills to SKILLS 2.0 format, migrate all docs and files, then remove the original folder. Git history stays as-is — this is a folder-level merge, not a git rewrite.

### XFER-1 Copy Comm-Helpers tree into prod-helpers

- [ ] Copy all Comm-Helpers files into a `comm-helpers/` subdirectory (or decided location) within prod-helpers
- [ ] Verify nothing was lost in the copy (file count, spot-check contents)
- [ ] Commit the raw import before any transformations

### XFER-2 Convert r-slack to SKILLS 2.0

- [ ] Create `.claude/skills/r-slack/SKILL.md` from `.claude/commands/r-slack.md`
- [ ] Adapt to SKILLS 2.0 structure (frontmatter, pre-computed context, execution flow)
- [ ] Remove old command file

### XFER-3 Convert r-email to SKILLS 2.0

- [ ] Create `.claude/skills/r-email/SKILL.md` from `.claude/commands/r-email.md`
- [ ] Adapt to SKILLS 2.0 structure
- [ ] Remove old command file

### XFER-4 Convert r-otter to SKILLS 2.0

- [ ] Create `.claude/skills/r-otter/SKILL.md` from `.claude/commands/r-otter.md`
- [ ] Adapt to SKILLS 2.0 structure
- [ ] Remove old command file

### XFER-5 Convert slack-reference to SKILLS 2.0

- [ ] Create `.claude/skills/slack-reference/SKILL.md` from `.claude/commands/slack-reference.md`
- [ ] Adapt to SKILLS 2.0 structure
- [ ] Remove old command file

### XFER-6 Convert email-reference to SKILLS 2.0

- [ ] Create `.claude/skills/email-reference/SKILL.md` from `.claude/commands/email-reference.md`
- [ ] Adapt to SKILLS 2.0 structure
- [ ] Remove old command file

### XFER-7 Convert r-commit to SKILLS 2.0

- [ ] Create `.claude/skills/r-commit/SKILL.md` from Comm-Helpers' `.claude/commands/r-commit.md` (merge with existing prod-helpers r-commit if overlapping)
- [ ] Adapt to SKILLS 2.0 structure
- [ ] Remove old command file

### XFER-8 Migrate docs, scripts, and project files

- [ ] Migrate session docs (`docs/sessions/2026-01/`) into prod-helpers' `docs/sessions/` structure
- [ ] Migrate scripts (`gmail-thread.py`, `setup-auth.py`) into prod-helpers' `scripts/` directory
- [ ] Migrate project files (PURPOSE.md, DECISIONS.md, README.md) — fold content into prod-helpers equivalents or archive under `docs/`
- [ ] Migrate CLAUDE.md directives — merge relevant instructions into prod-helpers' CLAUDE.md
- [ ] Migrate `.gitignore` entries and `settings.local.json` permissions into prod-helpers equivalents
- [ ] Remove the imported `comm-helpers/` staging directory (if used) after all content is in its final location

### XFER-9 Remove ~/research/Comm-Helpers

- [ ] Verify all content has been migrated and nothing is missing
- [ ] Delete `~/research/Comm-Helpers/` folder
- [ ] Update any references to Comm-Helpers in prod-helpers docs (CLAUDE.md, PURPOSE.md, etc.)

---

## Decisions

See `DECISIONS.md` for cumulative record.

## Open Questions

- Whisper approach: use MacWhisper Pro (already owned) or OpenAI's downloadable Whisper? Trade-offs to evaluate.
- Tag mapping granularity: 1:1 mapping sufficient or do some tags need many-to-many?
