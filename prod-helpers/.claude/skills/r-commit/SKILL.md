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

**Conv:**
!`.claude/scripts/conv-read-current.sh`

---

## Workflow

1. **Identify the current folder** relative to the git root:

```bash
FOLDER_NAME=$(basename $(pwd))
echo "Committing changes in: $FOLDER_NAME/"
```

2. **Show what will be committed** (only this folder):

```bash
git status -- .
```

3. **Stage only this folder's changes:**

```bash
git add .
```

4. **Verify staging** (confirm no other folders were staged):

```bash
git status
```

5. **Commit** with a concise message and point-form highlights of changes.

Include `Machine:` in the commit message body using the pre-computed value above.

Format:
```
Concise title describing the change

- Point 1
- Point 2

Conv: [from pre-computed context]
Machine: [from pre-computed context]

Co-Authored-By: Claude <noreply@anthropic.com>
```

If Conv shows "MISSING", warn the user that `/r-start` was not run, but proceed with the commit (omit the Conv line).

6. **Verify commit success:**

```bash
git status
```

7. Do NOT push to remote unless explicitly requested.

**Note:** If other folders have staged changes, unstage them first with `git reset HEAD <other-folder>/` before committing.
