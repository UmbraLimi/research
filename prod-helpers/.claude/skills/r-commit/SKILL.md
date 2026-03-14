---
name: r-commit
description: Commit only this folder's changes
argument-hint: ""
allowed-tools: Read, Edit, Bash, Glob
---

# Commit Current Folder

Commit only changes within this project folder, leaving other folders' changes unstaged.

---

## Pre-computed Context

**Current folder:**
!`basename $(pwd)`

**Folder status:**
!`git status -- . 2>/dev/null || echo "(not in a git repo)"`

**Diff summary:**
!`git diff --stat -- . 2>/dev/null`

---

## Workflow

### Step 1: Review Changes

Use the pre-injected status above. If more detail is needed:

```bash
git diff -- .
```

### Step 2: Stage and Commit

**Stage only this folder's changes:**

```bash
git add .
```

**Verify staging** (confirm no other folders were staged):

```bash
git status
```

### Step 3: Commit Message Format

```
Concise title describing the change

Changes:
- Specific change with file or component affected
- Another change with context

Docs:
- Documentation files created or updated

Date: YYYY-MM-DD

Co-Authored-By: Claude <noreply@anthropic.com>
```

**Title:** Imperative mood, under 72 chars.

**Body:** Group bullets by category. Only include relevant sections (skip empty ones). Be specific — name files, topics, decisions.

### Step 4: Verify

```bash
git status
```

Confirm working tree is clean and commit was successful.

---

## Rules

- **Do NOT push** unless explicitly requested
- **Do NOT amend** previous commits unless explicitly requested
- **Do NOT use `--no-verify`** to skip hooks unless explicitly requested
- **Always commit ALL changes in this folder** — use `git add .`
- If other folders have staged changes, unstage them first with `git reset HEAD <other-folder>/`
