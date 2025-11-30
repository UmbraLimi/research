---
description: Add a new user story to USER-STORIES.md
argument-hint: '<role> "<story text>" [P0|P1|P2|P3]'
---

# Add User Story

**Purpose:** Add a single user story to USER-STORIES.md with proper numbering, categorization, and cross-reference updates.

## Input
- `$ARGUMENTS` - Format: `<role> "<story text>" [priority]`
  - `<role>` - One of: Admin, Creator, Student, Student-Teacher, Employer, System, Platform
  - `"<story text>"` - The user story in quotes (can be full format or shorthand)
  - `[priority]` - Optional: P0, P1, P2, or P3 (defaults to P1 if not specified)

## Story Format
Stories should follow: **As a [role], I need to [action] so that [benefit].**

If user provides shorthand (just the action), expand to full format.

## Actions

1. **Parse Arguments:**
   - Extract role from `$ARGUMENTS`
   - Extract story text (text within quotes)
   - Extract priority (P0-P3) or default to P1
   - Map role to role code:
     - Admin → A
     - Creator → C
     - Student → S
     - Student-Teacher → T
     - Employer → E
     - System/Session → V
     - Platform/User → P

2. **Get Next Story Number:**
   - Read `USER-STORIES.md` "Current State" table
   - Find the row for the role's prefix (US-A, US-C, etc.)
   - Note the next available number

3. **Format the Story:**
   - If story doesn't start with "As a", convert to proper format:
     - Input: `"upload profile pictures"`
     - Output: `"As a [Role], I need to upload profile pictures so that [ask user for benefit or infer]"`
   - If benefit is missing, ask user or infer from context

4. **Add Story to USER-STORIES.md:**
   - Find the appropriate section for the role
   - Find the appropriate subsection (or create one if needed)
   - Add new row to the table:
     ```
     | US-[Role]NNN | [Full story text] | [Priority] | Manual Entry |
     ```

5. **Update Statistics:**
   - Update "Story Statistics" table:
     - Increment the role's row in the appropriate priority column
     - Increment the Total row
   - Update "Current State" table:
     - Increment next number for the role

6. **Update Last Updated Date:**
   - Change "Last Updated" at top of USER-STORIES.md to today's date

7. **Check for Related Updates:**
   - If story implies a new goal, ask: "Should this be added to GOALS.md as well?"
   - If story relates to a technology gap, note: "This may require adding to Phase 2.5.3 research tasks"

8. **Report:**
   - Display: Story ID assigned (e.g., US-S028)
   - Display: Full story text as added
   - Display: Priority
   - Display: Section added to

## Example Usage

```
/r-add-user-story Student "As a Student, I need to download my certificates as PDF so that I can share them on LinkedIn" P1

/r-add-user-story Admin "bulk import users from CSV" P2

/r-add-user-story Platform "handle webhook events from Stripe" P0
```

## Shorthand Expansion Examples

| Input | Expanded |
|-------|----------|
| `Student "download certificates"` | As a Student, I need to download certificates so that [ask/infer] |
| `System "validate payment webhooks"` | As a System, I need to validate payment webhooks so that [ask/infer] |
| `Creator "set course pricing"` | As a Creator, I need to set course pricing so that [ask/infer] |

## Notes

- Always confirm the story was added by showing the exact row added
- If the role doesn't match known roles, ask for clarification
- If story seems duplicate of existing, warn before adding
- For bulk additions, suggest using `/r-add-client-doc` workflow instead
