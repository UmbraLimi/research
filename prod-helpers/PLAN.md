# PLAN.md

## Current Status

**Phase 1 — Foundation** (in progress — 1.4 complete except deferred test harness)

---

## Phase 1: Foundation

Establish the infrastructure before migrating data or building agents.

### 1.1 API & Access Audit
- [ ] Confirm Dynalist API access and document endpoints needed (CRUD tasks, search, tags)
- [ ] Confirm Joplin Clipper API access and document endpoints (notebooks, notes, tags, export)
- [ ] Confirm Obsidian CLI (v1.12+) capabilities and document commands available
- [ ] Document rate limits, auth mechanisms, and data formats for each

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

## Decisions

See `DECISIONS.md` for cumulative record.

## Open Questions

- What Obsidian CLI commands are available in v1.12? Need to verify before committing to that interface.
- Whisper approach: use MacWhisper Pro (already owned) or OpenAI's downloadable Whisper? Trade-offs to evaluate.
- Tag mapping granularity: 1:1 mapping sufficient or do some tags need many-to-many?
- How should the Comm-Helpers sister project coordinate with this one? Shared skills? Shared tag table?
