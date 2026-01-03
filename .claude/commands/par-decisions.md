---
description: Document session decisions
argument-hint: ""
---

# Document Session Decisions

Create a session decisions document:

1. **Get current timestamp:**
   - Execute `/par-timestamp` to get current date and time
   - Store the DATE and MONTH values for consistent use

2. **Create the file:**
   - Directory: `docs/sessions/ABC/` (where `ABC` is MONTH from step 1)
   - Filename: `XYZ Decisions.md` (where `XYZ` is FILENAME from step 1)
   - Example: `docs/sessions/2025-11/2025-11-21_12-15-34 Decisions.md`

3. **Identify decisions from the conversation:**
   - Scan the session for decisions made during discussion
   - Look for patterns like:
     - Options presented and user chose one
     - User asked "should we do X or Y?" and a choice was made
     - User said "let's go with..." or "I prefer..." or "let's do..."
     - Architecture/design changes agreed upon
     - Trade-off discussions that resulted in a direction
   - If no decisions found, ask user if any should be documented
   - If none, skip file creation

4. **Document each decision:**
   - Use this format for each decision:

```markdown
## Decision N: [Brief Title]

**Context**: [What task/situation prompted this decision]

**Options Considered**:
1. [Option A]
2. [Option B] ← Chosen
3. [Option C]

**Decision**: [Clear statement of what was decided]

**Rationale**: [Why this option was chosen]
```

5. **Update DECISIONS.md (authoritative record):**
   - Read `DECISIONS.md` in project root
   - For each decision documented in the session file:
     - Classify as **Operating** (frequent behavior) or **General** (architectural/strategic)
     - Check if decision already exists in the appropriate table
     - If exists: update the row with new choice/rationale if changed
     - If new: add row to the appropriate table
     - If decision resolves an Open Decision: move from Open to appropriate table
   - Update the `*Last Updated:*` timestamp
   - If DECISIONS.md doesn't exist, create it using the template structure

6. **Confirm creation:**
   - Display a brief summary in the chat showing:
     - Session file path created
     - Decisions documented
     - Which decisions were added/updated in DECISIONS.md
