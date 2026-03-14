---
name: r-docs
description: Update all project documentation
argument-hint: ""
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Update Project Documentation

Execute at the end of a session to update documentation affected by this session's changes.

---

## Pre-computed Context

**Changed files this session:**
!`git diff --name-only HEAD~1 -- . 2>/dev/null || git diff --name-only -- . 2>/dev/null || echo "(no changes detected — use session context)"`

**Current docs structure:**
!`.claude/scripts/docs-list.sh`

---

## Action Plan

Work through these steps in order. Skip any step where no relevant changes were made this session.

1. **Check reference docs** — If APIs were researched or tested, update the relevant file in `docs/reference/`
2. **Check architecture docs** — If designs were discussed or decided, update the relevant file in `docs/architecture/`
3. **Check vendor docs** — If external tools were evaluated, create or update a file in `docs/vendors/`
4. **Walk the Change Detection Matrix** — For each category of work done this session, check the matrix below and update the corresponding docs
5. **Update CLAUDE.md** — If project structure, design principles, or workflows changed

---

## Change Detection Matrix

| If You Changed... | Update These Docs |
|-------------------|-------------------|
| Dynalist API findings | `docs/reference/dynalist-api.md` |
| Joplin API findings | `docs/reference/joplin-api.md` |
| Obsidian CLI findings | `docs/reference/obsidian-cli.md` |
| Tag mapping design | `docs/architecture/tag-mapping.md` |
| Note format templates | `docs/architecture/note-formats.md` |
| Agent guard rail design | `docs/architecture/agent-guardrails.md` |
| Scripts created or modified | Shadow doc for the script |
| Skills created or modified | Shadow doc for the skill |
| New external tool evaluated | `docs/vendors/{tool-name}.md` |
| Phase/task completed | *Run `/r-update-plan`* |
| Design decisions made | `DECISIONS.md` |
| Project goals or scope changed | `PURPOSE.md` |
| Skills or commands added | `CLAUDE.md` (if user-facing) |

---

## Shadow Documentation

Every agent, skill, Python script, and bash script gets a shadow doc. When a new one is created this session, create its shadow doc with:

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
