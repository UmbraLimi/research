---
name: r-learn-decide
description: Document session learnings and decisions
argument-hint: "[MONTH FILENAME] - optional: 2026-03 20260313_1400"
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Document Session Learnings & Decisions

**Purpose:** Capture insights and choices from a session into two structured files.

---

## Pre-computed Context

**Existing session files this month:**
!`MONTH=$(date '+%Y-%m'); find docs/sessions/$MONTH \( -name '*Learnings.md' -o -name '*Decisions.md' \) 2>/dev/null | sort | tail -10 | sed 's|^|- |' || echo "- (none yet this month)"`

---

## Execution Flow

1. **Get current timestamp:**
   - If `$ARGUMENTS` contains two values (MONTH FILENAME), use them directly
   - Otherwise, run these bash commands:
     ```bash
     date '+%Y-%m'              # MONTH (for directory)
     date '+%Y%m%d_%H%M'        # FILENAME (compact)
     ```

2. **Scan session** for learnings and decisions

3. **Create files** in `docs/sessions/{MONTH}/`:
   - `{FILENAME} Learnings.md`
   - `{FILENAME} Decisions.md` (skip if no decisions)

4. **Route important decisions** to `DECISIONS.md` (see Decision Routing below)

5. **Confirm creation** (see Confirmation below)

---

## Topics (Priority Areas)

These are the key areas for this project. Scan for learnings and decisions in these topics first, but also capture **any others** with appropriate topic names.

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
| `workflow` | Process, tooling, conventions |

### Cross-Cutting Topics

Items often span multiple topics. Tag with all relevant areas:
- **dynalist, obsidian**: Cross-app search, unified results
- **tags, migration**: Tag conversion during data moves
- **agents, skills**: Guard rail patterns that apply to both
- **joplin, migration**: Retirement workflow

---

## Part 1: Learnings

**What to capture:** Insights, discoveries, patterns, gotchas

**Scan for:**
- Problems encountered and how they were solved
- Unexpected behaviors discovered
- Patterns or approaches that worked well
- Gotchas or caveats to remember
- API limitations or quirks

**File format:** `{FILENAME} Learnings.md`

```markdown
# Session Learnings - YYYY-MM-DD

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
# Session Decisions - YYYY-MM-DD

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
| Strategic | Project direction, data architecture, workflow design |
| Implementation | Technical choices, API selection, format decisions |

---

## Decision Routing

**When a decision is important**, also add it to `DECISIONS.md` under the appropriate category.

### Categories in DECISIONS.md

!`grep '^## ' DECISIONS.md 2>/dev/null | sed 's/^## /- /' || echo "- (unable to read DECISIONS.md)"`

### Important Decision Criteria

| Criterion | Example |
|-----------|---------|
| **Architecture choice** | How data flows between apps, tag mapping design |
| **Technology selection** | Which API, which transcription tool, which format |
| **Convention established** | Note format templates, naming patterns |
| **Breaking change** | Migration order that affects other phases |

### Entry Format for DECISIONS.md

```markdown
### [Brief Title]
**Date:** YYYY-MM-DD

[Clear statement of the decision]

**Rationale:** [Why this was chosen]
```

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

If no decisions found, note "No decisions identified this session" and skip Decisions file.
