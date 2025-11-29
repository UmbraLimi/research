---
description: Document session prompts
argument-hint: ""
---

# Document Session Prompts

Create a seesion prompts document:

1. **Get current timestamp:**
   - Execute `/q-timestamp` to get current date and time
   - Store the DATE and MONTH values for consistent use

2. **Create the file:**
   - Directory: `docs/sessions/ABC/` (where `ABC` is MONTH from step 1)
   - Filename: `XYZ Prompts.md` (where `XYZ` is FILENAME from step 1)
   - Example: `docs/sessions/2025-11/2025-11-21_12-15-34 Prompts.md`

3. **Document the prompts:** 
    - list of all the questions/instructions (in sequence) that the user has made in this session.

This command ensures that the user can benefit in the future from some prompts in this session, by manually selecting from this ordered list.
