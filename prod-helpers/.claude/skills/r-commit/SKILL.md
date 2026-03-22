---
name: r-commit
description: Commit only this folder's changes
argument-hint: ""
allowed-tools: Bash, Read, Glob
---

# Commit Current Folder

Commit only changes within this project folder, leaving other folders' changes unstaged.

---

## Pre-computed Context

**Machine:**
!`cat ~/.claude/.machine-name 2>/dev/null || echo "(unknown)"`

**Project prefix:**
!`grep '^prefix:' PROJECT.yaml | awk '{print $2}'`

**Conv:**
!`.claude/scripts/conv-read-current.sh`

**Repo status:**
!`git status --short -- . 2>/dev/null || echo "(unavailable)"`

---

## Workflow

### Step 1: Review Changes

Use the pre-injected repo status above. If more detail is needed:

```bash
git status -- .
git diff --stat -- .
```

### Step 2: Stage and Commit

**Always stage everything in this folder.** Do not selectively stage files.

```bash
git add .
```

Verify staging (confirm no other folders were staged):

```bash
git status
```

**Note:** If other folders have staged changes, unstage them first with `git reset HEAD <other-folder>/` before committing.

### Step 3: Commit Message Format

```
{PREFIX}-{CONV}: Concise title describing the change

Changes:
- Specific change with file/component name
- Another change with context

Fixes:
- Bug or issue fixed (if applicable)

Stats: X files changed

Conv: [from pre-computed context]
Machine: [from pre-computed context]

Co-Authored-By: Claude <noreply@anthropic.com>
```

**Title:** Start with `{PREFIX}-{CONV}:`, imperative mood, under 72 chars total.

**Conv line:** If Conv shows "MISSING", warn the user that `/r-start` was not run, but proceed with the commit (omit the Conv line).

**Body:** Group bullets by category. Only include relevant sections (skip empty ones). Be specific — name files, components, endpoints.

### Step 4: Verify

```bash
git status
```

### Step 5: Report

```
Committed
─────────
Commit: [commit hash] [title]       (or "nothing to commit")
Conv: [NNN]
```

---

## Rules

- **Do NOT push** unless explicitly requested
- **Do NOT amend** previous commits unless explicitly requested
- **Do NOT use `--no-verify`** to skip hooks
- **Always commit ALL changes** in this folder — use `git add .` without exception
