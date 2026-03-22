---
name: r-learn-decide
description: Document conv learnings and decisions
argument-hint: "[MONTH FILENAME] - optional: 2026-03 20260321_1400"
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Document Conv Learnings & Decisions

**Purpose:** Capture insights and choices from a development conversation into two structured files.

---

## Pre-computed Context

**Existing conv files this month:**
!`.claude/scripts/session-files-learn-decide.sh`

---

## Execution Flow

1. **Get current timestamp:**
   - If `$ARGUMENTS` contains two values (MONTH FILENAME), use them directly
   - Otherwise, run these bash commands:
     ```bash
     date '+%Y-%m'              # MONTH (for directory)
     date '+%Y%m%d_%H%M'        # FILENAME (compact)
     ```

2. **Scan conversation** for learnings and decisions

3. **Create files** in `docs/sessions/{MONTH}/`:
   - `{FILENAME} Learnings.md`
   - `{FILENAME} Decisions.md` (skip if no decisions)

4. **Check Important decisions** — route to `DECISIONS.md` or `PLAYBOOK.md` (see Decision Routing below)

5. **Check Insight Capture** — append durable insights to relevant decision entries

6. **Confirm creation** (see Confirmation below)

---

## Topics (Priority Areas)

These are the key areas for this project. Scan for learnings and decisions in these topics first, but also capture **any others** with appropriate topic names.

### Project Topics (→ DECISIONS.md)

| Topic | Scan For |
|-------|----------|
| `dynalist` | Dynalist API, data format, task structure, search |
| `obsidian` | Obsidian CLI, vault structure, note formats, links/backlinks |
| `joplin` | Joplin Clipper API, notebooks, migration |
| `tags` | Tag mapping, naming conventions, translation table |
| `agents` | Agent framework, guard rails, directives, halt conditions |
| `skills` | Skill design, testing, Claude Code skill patterns |
| `migration` | Data migration patterns, format conversion, validation |
| `credentials` | Credential lookup, obfuscation, compiled decoder |
| `youtube` | YouTube Shorts archival, Whisper transcription, thumbnails |

### Workflow Topics (→ PLAYBOOK.md)

| Topic | Scan For |
|-------|----------|
| `workflow` | Process, tooling, conventions |
| `cc-workflow` | Claude Code hooks, skills, config, permissions, session management |
| `docs-infra` | Repo organization, folder structure, file conventions, what goes where |

### Cross-Cutting Topics

Items often span multiple topics. Tag with all relevant areas:
- **dynalist, obsidian**: Cross-app search, unified results
- **tags, migration**: Tag conversion during data moves
- **agents, skills**: Guard rail patterns that apply to both
- **joplin, migration**: Retirement workflow
- **cc-workflow, docs-infra**: Skill paths, $CLAUDE_PROJECT_DIR behavior

### Related Documentation

When documenting, consider if items should also update:

| If item involves... | Consider updating... |
|---------------------|---------------------|
| Machine-specific | `docs/architecture/devcomputers.md` |
| New pattern | Relevant doc in `docs/reference/` or `docs/architecture/` |
| Project architecture | `DECISIONS.md` |
| Workflow/conventions | `PLAYBOOK.md` |

---

## Part 1: Learnings

**What to capture:** Insights, discoveries, patterns, gotchas

**Scan for:**
- Problems encountered and how they were solved
- Unexpected behaviors discovered
- Patterns or approaches that worked well
- Gotchas or caveats to remember

**File format:** `{FILENAME} Learnings.md`

```markdown
# Conv Learnings - YYYY-MM-DD

## 1. Descriptive Title
**Topics:** topic1, topic2

**Context:** What situation led to this

**Learning:** The key insight

**Pattern:** (optional)
Code or reusable approach

---

## 2. Another Learning
...
```

---

## Part 2: Decisions

**What to capture:** Choices made between alternatives

**Scan for:**
- Options presented and which was chosen
- "Should we do X or Y?" discussions
- Architecture/design choices
- Trade-off discussions that reached a conclusion

**File format:** `{FILENAME} Decisions.md`

```markdown
# Conv Decisions - YYYY-MM-DD

## 1. Brief Decision Title
**Type:** Strategic | Implementation
**Topics:** topic1, topic2

**Trigger:** What prompted this decision

**Options Considered:**
1. Option A description
2. Option B description ← Chosen
3. Option C description

**Decision:** Clear statement of what was decided

**Rationale:** Why this option was chosen

**Consequences:** What changed as a result

---

## 2. Another Decision
...
```

### Decision Types

| Type | Description |
|------|-------------|
| Strategic | Project direction, workflow, architecture |
| Implementation | Technical choices, API design, library selection |

---

## Decision Routing

**When a decision is important**, also add it to the correct file based on topic.

### → DECISIONS.md (Project Topics)

Decisions about the productivity system: data architecture, API design, migration patterns, tool selection, agent design.

!`.claude/scripts/decisions-categories.sh`

### → PLAYBOOK.md (Workflow Topics)

Decisions about the repo itself: organization, CC workflow, session conventions, skill behavior.

### Important Decision Criteria

| Criterion | Example |
|-----------|---------|
| **Thwarted by conditions** | Planned approach blocked by platform/library limitations |
| **Architecture choice** | How data flows between apps, tag mapping design |
| **Code style/convention** | Naming patterns, file organization |
| **Technology selection** | Which API, which transcription tool, which format |
| **Breaking change** | Migration order that affects other phases |

### Entry Format (Same for Both Files)

```markdown
### [Brief Title]
**Date:** YYYY-MM-DD

[Clear statement of the decision]

**Rationale:** [Why this was chosen]
```

**Remember:** Update "Last Updated" date at top of whichever file is modified.

---

## Insight Capture

During processing, scan for **durable, informative insights** worth preserving. An insight qualifies if it connects a decision to broader professional context or would teach someone starting a similar project. Append to the relevant decision entry as `> **Insight:**` blockquotes.

---

## Confirmation

Display:
```
Created: docs/sessions/{MONTH}/{FILENAME} Learnings.md
  Learnings: {count}
  Topics: {topics used}

Created: docs/sessions/{MONTH}/{FILENAME} Decisions.md
  Decisions: {count}
  Types: {Strategic: N, Implementation: N}
  Topics: {topics used}
```

If no decisions found, note "No decisions identified this conv" and skip Decisions file.
