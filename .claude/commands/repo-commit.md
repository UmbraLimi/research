---
description: Validate, stage, and commit changes
---

# Commit Command

Execute the following steps to commit changes:

1. Save all unsaved changes anywhere in the codebase

2. Run `git status` to show what will be committed:
   // turbo

```bash
git status
```

3. Stage all changes:
   // turbo

```bash
git add .
```

4. Commit all changes to local git with a concise message and point-form highlights of changes.
   Example: `git commit -m "Title\n\n- Point 1\n- Point 2"`

5. Verify commit success:
   // turbo

```bash
git status
```

6. Do NOT push to remote unless explicitly requested.
