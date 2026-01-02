---
description: Complete end-of-session workflow
argument-hint: ''
---

# End Session Workflow

**Purpose:** End-of-session workflow that captures learnings, updates PLAN.md, and commits. Creates session files and ensures documentation is current before committing.

Execute the following steps in order:

## Step 1: Create Session Files

**Always execute all three commands** — don't pre-assess whether they're "needed." Valuable history is lost when these are skipped based on poor judgment.

1. Execute `/par-learnings` command
2. Execute `/par-prompts` command
3. Execute `/par-decisions` command

If a session truly had no learnings/prompts/decisions (rare), the command itself will determine that — don't skip preemptively.

## Step 2: Update PLAN.md

**Always run `/par-update`** — Review PLAN.md against session work and update as needed.

Even if PLAN.md was recently modified, that change may have been for a different purpose. A full review ensures nothing is missed.

## Step 3: Commit Options

Display summary and offer commit choices:

```
✅ Session Files Created

Learnings:  docs/sessions/YYYY-MM/YYYY-MM-DD_HH-MM-SS Learnings.md
Prompts:    docs/sessions/YYYY-MM/YYYY-MM-DD_HH-MM-SS Prompts.md
Decisions:  docs/sessions/YYYY-MM/YYYY-MM-DD_HH-MM-SS Decisions.md

PLAN.md: Updated

Current Status: Phase X.Y - [Section Name]
Next: [Next immediate task]

Ready to commit?
- /r-commit   → Commit only this project's changes
- /repo-commit → Commit all changes across the repo
```

**Ask user** which commit scope they prefer, then execute the chosen command.
