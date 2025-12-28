---
description: Commit only this folder's changes
---

# Commit Current Folder

Commit only changes within this project folder, leaving other folders' changes unstaged.

Execute the following steps:

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
   Example: `git commit -m "Title\n\n- Point 1\n- Point 2"`

6. **Verify commit success:**

```bash
git status
```

7. Do NOT push to remote unless explicitly requested.

**Note:** If other folders have staged changes, unstage them first with `git reset HEAD <other-folder>/` before committing.
