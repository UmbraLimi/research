---
description: Add a constraint or directive for scenario generation
argument-hint: '<type> "<directive>" [source]'
---

# Add Directive

**Purpose:** Add a constraint, restriction, or preference to DIRECTIVES.md that must be consulted during the RUN phase.

## Input
- `$ARGUMENTS` - Format: `<type> "<directive text>" [source]`
  - `<type>` - One of: MUST-USE, MUST-AVOID, NO-COMBINE, PREFER, REQUIRES, FEATURE-FLAG
  - `"<directive>"` - Description of the constraint in quotes
  - `[source]` - Optional: Where this came from (client, research, testing)

## Actions

1. **Parse Arguments:**
   - Extract type (validate against allowed types)
   - Extract directive text (text within quotes)
   - Extract source if provided, otherwise ask or mark as "Manual entry"

2. **Get Next Directive ID:**
   - Read `DIRECTIVES.md` "Current State" section
   - Get next `DIR-NNN` number

3. **Validate Type:**
   - MUST-USE: Required software/service
   - MUST-AVOID: Do not use this
   - NO-COMBINE: Technologies that conflict
   - PREFER: Favor when alternatives exist
   - REQUIRES: If X then must also Y
   - FEATURE-FLAG: Specific feature on/off

4. **Add to DIRECTIVES.md:**
   - Add row to "Active Directives" table:
     ```
     | DIR-NNN | [Type] | [Directive] | [Source] | [Today's date] |
     ```

5. **Update Current State:**
   - Increment "Next Directive ID"
   - Increment "Total Directives"
   - Increment count for the specific type

6. **Update Last Updated date**

7. **Check for Related Updates:**
   - If NO-COMBINE: Add to "Compatibility Notes" table
   - If FEATURE-FLAG: Add to "Feature-Specific Directives" table
   - If relates to existing research doc, note the connection

8. **Report:**
   - Display: Directive ID assigned
   - Display: Full directive as added
   - Display: Type and source

## Example Usage

```
/r-add-directive MUST-USE "Stripe Connect for payment processing" "Client requirement"

/r-add-directive MUST-AVOID "Stream Video product" "BBB is required for video"

/r-add-directive NO-COMBINE "Clerk authentication with Cloudflare Workers" "Research finding - compatibility issue"

/r-add-directive PREFER "Supabase over separate DB + Auth + Storage" "Reduces integration complexity"

/r-add-directive REQUIRES "If using Supabase, use Supabase Auth" "Tighter integration"

/r-add-directive FEATURE-FLAG "BigBlueButton: Enable recording by default" "US-V005 requirement"
```

## Notes

- Directives are consulted during RUN phase scenario generation
- sc-001 (fully custom) may override some MUST-USE directives by design
- If directive contradicts an existing one, warn and ask for clarification
- Link to research docs or user stories when relevant
