---
description: Research a software/service and create tech doc
argument-hint: '<url> [--required|--optional]'
---

# Add Software/Service

**Purpose:** Research a software product or service from its URL, create a tech research document, and update all relevant project files.

## Input
- `$ARGUMENTS` - The URL to research, optionally followed by `--required` (client-specified) or `--optional` (to be evaluated)
- Default status is `--optional` if not specified

## Actions

1. **Parse Arguments:**
   - Extract URL from `$ARGUMENTS`
   - Check for `--required` or `--optional` flag
   - If neither specified, default to `--optional`

2. **Fetch and Research:**
   - Use WebFetch to retrieve information from the provided URL
   - Follow links to documentation, pricing, and API pages as needed
   - Extract:
     - Product name and type (e.g., "Video Conferencing", "Payment Processing")
     - Key features and capabilities
     - Pricing model (free tier, paid tiers)
     - JavaScript/React SDK availability
     - API capabilities
     - Integration complexity
     - Hosting model (SaaS, self-hosted, hybrid)

3. **Check STRUCTURE.md for Next Number:**
   - Read `STRUCTURE.md` "Current State" table
   - Get next `tech-NNN` number

4. **Create Research Document:**
   - Create `/research/tech-NNN-[product-name].md`
   - Use format from existing tech docs (see `tech-001-bigbluebutton.md` as template)
   - Include:
     - Overview
     - Key Capabilities (with table mapping to user stories)
     - Technical Requirements
     - Pricing
     - User Story Coverage (Directly Addresses, Partially Addresses, Does NOT Address)
     - Integration Considerations (Pros/Cons)
     - React/Astro Integration notes
     - Recommendations
     - Open Questions
     - References

5. **Map to User Stories:**
   - Read `USER-STORIES.md`
   - Identify which existing user stories this software could address
   - Note in the tech doc's "User Story Coverage" section

6. **Update PLAN.md:**
   - Read current `PLAN.md`
   - If `--required`: Add to "Required Services (Client-Specified)" table in Phase 2.5
   - If `--optional`: Add to "Optional Services (To Be Evaluated)" table in Phase 2.5
   - Add research task to Phase 2.5.3 if not already present

7. **Update STRUCTURE.md:**
   - Increment "Technologies" next number in "Current State" table
   - Add to "Research Files Created" table if that section exists

8. **Report Summary:**
   - Display: Product name, type, status (required/optional)
   - Display: Tech doc created (path)
   - Display: User stories potentially addressed
   - Display: Files updated

## Example Usage

```
/r-add-software https://stripe.com/connect --required
/r-add-software https://clerk.com
/r-add-software https://resend.com --optional
```

## Notes

- If the URL is inaccessible, report the error and ask for an alternative URL or documentation link
- If the software type overlaps with an existing tech doc, note the comparison opportunity
- Always check if the software is already documented before creating a duplicate
