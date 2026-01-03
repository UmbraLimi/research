---
description: Document session learnings
argument-hint: "[append <filepath>]"
---

# Document Session Learnings

Create or append to a session learnings document.

## Arguments

- **No argument:** Create new session file
- **`append <filepath>`:** Append to existing file (used when continuing a session)

---

## Steps

1. **Get current timestamp:**
   - Execute `/par-timestamp` to get current date and time
   - Store the DATE, TIME, and MONTH values for consistent use

2. **Create or append to file:**

   **If creating new:**
   - Directory: `docs/sessions/ABC/` (where `ABC` is MONTH from step 1)
   - Filename: `XYZ Learnings.md` (where `XYZ` is FILENAME from step 1)
   - Example: `docs/sessions/2025-11/2025-11-21_12-15-34 Learnings.md`

   **If appending:**
   - Use the filepath provided in argument
   - Add separator before new content:
     ```markdown
     ---
     ## Continued — HH:MM

     [New learnings here]
     ```

3. **Document the learnings:**
   - Focus on insights, decisions, best practices, or important discoveries made
   - Present as a clear bulleted or numbered list
   - Include both technical and workflow/process learnings
   - Organize by category if multiple types of learnings (e.g., Technical, Workflow, Documentation, Architecture)

4. **Confirm creation:**
   - Display a brief summary in the chat showing the file path created
