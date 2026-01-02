---
description: Complete end-of-session workflow
argument-hint: ''
---

# End Session Workflow

**Purpose:** Simplified end-of-session workflow that captures learnings and documents work. Creates session files and optionally updates documentation before committing.

Execute the following steps in order:

## Step 1: Create Session Files

1. Execute `/par-learnings` command
2. Execute `/par-prompts` command (if useful prompts were used this session)
3. Execute `/par-decisions` command (if decisions were made this session)

## Step 2: Optional Documentation Update

**Ask user:** "Does PLAN.md need updating?

**If YES:** Run `/par-update` then proceed to Step 3

**If NO:** Skip to Step 3

## Step 3: Commit Options

Display summary and offer commit choices:

```
✅ Session Files Created

Learnings:  docs/sessions/2025-11/2025-11-16_14-30-00 Learnings.md
Prompts:    docs/sessions/2025-11/2025-11-16_14-30-00 Prompts.md (if created)
Decisions:  docs/sessions/2025-11/2025-11-16_14-30-00 Decisions.md (if created)

Documentation: [Updated/Already current]

Current Status: Phase X.Y - [Section Name]
Next: [Next immediate task]

Ready to commit?
- /r-commit   → Commit only this project's changes
- /repo-commit → Commit all changes across the repo
```

**Ask user** which commit scope they prefer, then execute the chosen command.
