---
name: r-docs
description: Update all project documentation
argument-hint: "[--recreate] - use conv artifacts for context"
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# Update Project Documentation

Execute at the end of a conv to update documentation affected by this conversation's changes.

---

## Pre-computed Context

**Changed files this conv:**
!`git diff --name-only HEAD~1 -- . 2>/dev/null || git diff --name-only -- . 2>/dev/null || echo "(no changes detected — use conv context)"`

**Current docs structure:**
!`.claude/scripts/docs-list.sh`

---

## Arguments

**`--recreate`** (optional): When starting a new conv, gather extra context from recent conv artifacts.

When `$ARGUMENTS` contains `--recreate`, also read:
1. Most recent conv files (Learnings, Decisions, Dev) from `docs/sessions/YYYY-MM/`
2. Recent git commits beyond what the changed-files list captured

---

## Action Plan

> **⚠️ CRITICAL: TodoWrite ALL discovered gaps.**
> If you find undocumented endpoints, stale docs, missing coverage, or ANY issue you won't fix right now — **TodoWrite it immediately**. Do NOT mention it in commentary as "pre-existing" or "out of scope" without also creating a TodoWrite task. The words "pre-existing", "missing", "stale", "gap", "undocumented" in your output are a trigger: if you're saying it but not fixing it, TodoWrite it. This applies to all findings during manual review.

Work through these steps in order. Skip any step where no relevant changes were made this conv.

1. **Check reference docs** — If external tools/APIs were researched or tested, update the relevant file in `docs/reference/`
2. **Check design docs** — If pre-build specs were discussed or decided, update the relevant file in `docs/as-designed/`
3. **Check as-built docs** — If implemented systems were documented, create or update a file in `docs/as-built/`
4. **Walk the Change Detection Matrix** — For each category of work done this conv, check the matrix below and update the corresponding docs
5. **Update CLAUDE.md** — If project structure, design principles, or workflows changed

---

## Change Detection Matrix

<!-- CUSTOMIZE: Replace these entries with your project's domains after /init -->

| If You Changed... | Update These Docs |
|-------------------|-------------------|
| External tool/API findings | `docs/reference/{tool-name}.md` |
| Design decisions or specs | `docs/as-designed/{topic}.md` |
| Implemented a system | `docs/as-built/{system-name}.md` |
| Scripts created or modified | Shadow doc for the script |
| Skills created or modified | Shadow doc for the skill |
| Phase/task completed | *Run `/r-update-plan`* |
| Design decisions made | `DECISIONS.md` |
| Project goals or scope changed | `PURPOSE.md` |
| Skills or commands added | `CLAUDE.md` (if user-facing) |

---

## Shadow Documentation

Every agent, skill, Python script, and bash script gets a shadow doc. When a new one is created this conv, create its shadow doc with:

```markdown
# {Name}

**Type:** agent | skill | script
**Created:** YYYY-MM-DD
**Location:** {path to the file}

## Purpose

[Why this exists]

## Usage

[How to invoke or use it]

## Design Rationale

[Why it was built this way]

## History

- YYYY-MM-DD: Created — [initial purpose]
```

Place shadow docs alongside the file they document, or in `docs/reference/` if the file is in a location that doesn't support adjacent docs.

---

## Confirmation

```
Documentation Updated
─────────────────────
- [List of docs created or updated]
- [Or "No documentation changes needed"]
```
