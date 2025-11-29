---
description: Resume work by analyzing PLAN.md and current progress
argument-hint: ''
---

# Resume Work Session

**Purpose:** Analyze PLAN.md to understand current progress and help you resume work efficiently.

## Actions

1. **Read PLAN.md** to identify:

   - Current WIP phase (🔥 emoji)
   - Latest completed phase (🏁 emoji)
   - Next planned phase (📋 emoji)
   - Current subtask checklist status

2. **Analyze Progress**:

   - Count completed vs. remaining subtasks in WIP phase
   - Identify next actionable task
   - Note any blockers or open questions mentioned

3. **Present Context** in this format:

```
📍 Current Position
─────────────────

🔥 WIP: Phase X.Y - [Phase Name]
   Progress: [X] of [Y] subtasks complete ([Z]%)

   ✅ Completed:
   - [List completed subtasks]

   ⏭️  Remaining:
   - [Next immediate task with details]
   - [Subsequent tasks]

🏁 Last Completed: Phase A.B - [Phase Name]

📋 Next Planned: Phase C.D - [Phase Name]

─────────────────
🎯 Recommended Action

[Specific, actionable next step based on current WIP]

Example:
"Start with subtask 5.1.1: Create evaluator schema file at src/nodes/evaluator/schema.ts"

or

"Continue investigating glossary failures by running the reproduction script"

─────────────────
💡 Quick Context

[1-2 sentence summary of what this phase accomplishes and why it matters]

─────────────────

Ready to start? (Y/n)
```

4. **Wait for user confirmation** before proceeding

5. **If user confirms**:
   - Offer to help with the next task
   - Ask if they need any files opened or context reviewed
   - Check if there are any blockers to address first

## Example Response

```
📍 Current Position
─────────────────

🔥 WIP: Phase 4.5 - Glossary Failure Investigation
   Progress: 2 of 3 subtasks complete (67%)

   ✅ Completed:
   - Created upload and summarization of client docs X, Y and Z

   ⏭️  Remaining:
   - Decide: Are there any more docs we need?

🏁 Last Completed: Phase 4.4 - DeepL Glossary Case Investigation

📋 Next Planned: Phase 5.1 - Evaluator: Terminology Track (11 subtasks)

─────────────────
🎯 Recommended Action

Make a decision on more client docs:
1. Will more be significant addition to what we have now?
2. Are we intriducing ambiguity?
3. Is there a change in goals over time in these documents?

─────────────────
💡 Quick Context

We have so far upload and summarized 5 client documents.
Already there are competing goals.
We need to determine if the sequence/timeline of thes docs is being properly handled. i..e. newer documents should supercede older documents for the same treatments and plan
─────────────────

Ready to start? (Y/n)
```

## Notes

- Focus on **next actionable step**, not high-level strategy
- Include **specific file paths** and commands when relevant
- Highlight **blockers** that need resolution before continuing
- Keep context brief but sufficient to resume without reading entire PLAN.md
