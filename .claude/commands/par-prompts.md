---
description: Document session prompts
argument-hint: "[append <filepath>]"
---

# Document Session Prompts

Create or append to a session prompts document.

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
   - Filename: `XYZ Prompts.md` (where `XYZ` is FILENAME from step 1)
   - Example: `docs/sessions/2025-11/2025-11-21_12-15-34 Prompts.md`

   **If appending:**
   - Use the filepath provided in argument
   - Add separator before new content:
     ```markdown
     ---
     ## Continued — HH:MM

     [Continue numbering from last prompt]
     ```

3. **Document the prompts:**
   - List all questions/instructions (in sequence) that the user made
   - When appending, continue numbering from where the existing file left off

4. **Confirm completion:**
   - Display file path (created or appended)

This command ensures the user can benefit from prompts in this session by manually selecting from this ordered list.
