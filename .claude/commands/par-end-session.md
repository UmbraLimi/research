---
description: Complete end-of-session workflow
argument-hint: ''
---

# End Session Workflow

**Purpose:** End-of-session workflow that captures learnings, updates PLAN.md, and commits. Creates session files and ensures documentation is current before committing.

Execute the following steps in order:

## Step 0: Check for Recent Session Files

Before creating new session files, check if session files already exist from today:

1. Look in `docs/sessions/YYYY-MM/` for files matching today's date pattern (`YYYY-MM-DD_*`)
2. If recent files exist (from today), ask user:

```
Recent session files found from today:
- YYYY-MM-DD_HH-MM-SS Learnings.md
- YYYY-MM-DD_HH-MM-SS Prompts.md
- YYYY-MM-DD_HH-MM-SS Decisions.md

Options:
1. Append to existing files (add new content to today's files)
2. Create new files (start fresh set with new timestamp)
3. Skip session files (just update PLAN.md and commit)

Which option? (1/2/3)
```

3. Based on choice:
   - **Option 1 (Append):** In Step 1, append new content to existing files rather than creating new ones
   - **Option 2 (Create new):** Proceed normally with new timestamp
   - **Option 3 (Skip):** Jump directly to Step 2 (Update PLAN.md)

If no recent files exist, proceed normally to Step 1.

## Step 1: Create Session Files

**Always execute all three commands** — don't pre-assess whether they're "needed." Valuable history is lost when these are skipped based on poor judgment.

**If creating new (Option 2 or no existing files):**
1. Execute `/par-learnings`
2. Execute `/par-prompts`
3. Execute `/par-decisions`

**If appending (Option 1 from Step 0):**
1. Execute `/par-learnings append <filepath>` (using existing Learnings.md path)
2. Execute `/par-prompts append <filepath>` (using existing Prompts.md path)
3. Execute `/par-decisions append <filepath>` (using existing Decisions.md path)

Each skill will add a separator and continue from where the file left off.

If a session truly had no learnings/prompts/decisions (rare), the command itself will determine that — don't skip preemptively.

## Step 2: Update PLAN.md

**Always run `/par-update`** — Review PLAN.md against session work and update as needed.

Even if PLAN.md was recently modified, that change may have been for a different purpose. A full review ensures nothing is missed.

## Step 3: Commit Options

Display summary and offer commit choices:

```
✅ Session Files [Created/Updated]

Learnings:  docs/sessions/YYYY-MM/YYYY-MM-DD_HH-MM-SS Learnings.md [created/appended]
Prompts:    docs/sessions/YYYY-MM/YYYY-MM-DD_HH-MM-SS Prompts.md [created/appended]
Decisions:  docs/sessions/YYYY-MM/YYYY-MM-DD_HH-MM-SS Decisions.md [created/appended]

DECISIONS.md: [Updated with OP-XX, OP-YY / No changes]

PLAN.md: Updated

Current Status: Phase X.Y - [Section Name]
Next: [Next immediate task]

Ready to commit?
- /r-commit   → Commit only this project's changes
- /repo-commit → Commit all changes across the repo
```

**Ask user** which commit scope they prefer, then execute the chosen command.
