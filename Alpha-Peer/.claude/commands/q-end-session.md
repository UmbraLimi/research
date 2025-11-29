---
description: Complete end-of-session workflow
argument-hint: ''
---

# End Session Workflow

**Purpose:** Simplified end-of-session workflow that captures learnings and documents work. Creates session files and optionally updates documentation before committing.

Execute the following steps in order:

## Step 1: Create Session Files

1. Execute `/q-learnings` command
2. Execute `/q-prompts` command (if useful prompts were used this session)

## Step 2: Optional Documentation Update

**Ask user:** "Does PLAN.md need updating?

**If YES:** Run `/q-update` then proceed to Step 3

**If NO:** Skip to Step 3

## Step 3: Commit Prompt

Display summary and ask about commit:

```
✅ Session Files Created

Learnings: docs/sessions/2025-11/2025-11-16_14-30-00 Learnings.md
Prompts:   docs/sessions/2025-11/2025-11-16_14-30-00 Prompts.md (if created)

Documentation: [Updated/Already current]

Current Status: Phase X.Y - [Section Name]
Next: [Next immediate task]

Would you like to run `/q-commit` to commit all changes?
```
