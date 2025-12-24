---
description: Process and index client document(s) from file_holding
argument-hint: '[--overwrite]'
---

# Add Client Document

**Purpose:** Process and index client document(s) that were just placed in /client_docs folder.

## Actions

1. Determine if the file has already been summarized by checking for a summary in `/client-docs/client-docs-index.md`
2. **If the summary is already there**. Ask **"Do you want to update the summary?"**
   2a. **If they say "yes"** go to Step 3
   2b. **If they say "no"** exit any further handling
3. For each file to process:
   - Assign next `CD-NNN` number (check "Next CD Number" in client-docs-index.md)
   - Read from `/client-docs/[filename]`
   - Analyze and extract key information:
     - Business requirements
     - User journeys and value propositions
     - Technical implications
     - Non-functional requirements
   - Add entry to `client-docs-index.md` with `### CD-NNN: [filename]` header
   - Update "Next CD Number" in Index Statistics
   - Update "Quick Reference" table with new document
4. **Update GOALS.md** with any new goals, metrics, or mission-related content discovered:
   - Read current `GOALS.md`
   - Add new goals with `GO-NNN` numbering (check "Next Goal Number" at bottom of GOALS.md)
   - Reference source as `CD-NNN` (e.g., "**Source:** CD-005")
   - Update existing goals if new document provides additional detail
   - Update "Goal Index by Source Document" table
   - Update "Next Goal Number" in Current State section
   - Update "Last Updated" date
5. **Update USER-STORIES.md** with any new user stories discovered:
   - Read current `USER-STORIES.md`
   - Extract user stories from three sources in the document:
     1. Explicit user stories stated in the document
     2. Implied functionality from goals/features described
     3. Specific mockups, UI elements, or wording that implies user needs
   - Add new stories with `US-[Role]NNN` numbering (check "Current State" table per role)
     - Role codes: A=Admin, C=Creator, S=Student, T=Student-Teacher, E=Employer, V=Video/Session, P=Platform, M=Moderator
   - Reference source as `CD-NNN` in Source column
   - Assign priority (P0=MVP critical, P1=high, P2=medium, P3=nice-to-have)
   - Update "Story Statistics" table counts
   - Update "Story Index by Source Document" table
   - Update "Current State" table with next numbers per role
   - Update "Last Updated" date
6. **Scan for Architecture Implications** - Update the 4 architecture documents:
   - **DB-SCHEMA.md** - Check if document implies:
     - New database tables or entities
     - New fields on existing tables
     - New relationships between entities
     - New enum values or data types
     - If changes found: Add entities/fields with `CD-NNN` source, update Document Lineage
   - **PAGES.md** - Check if document implies:
     - New pages or screens
     - New sections on existing pages
     - New data requirements for pages
     - If changes found: Add pages/sections, update Page Count and Document Lineage
   - **COMPONENTS.md** - Check if document implies:
     - New reusable UI components
     - New props or fields on existing components
     - New component categories
     - If changes found: Add components, update Component Count and Document Lineage
   - **API.md** - Check if document implies:
     - New API endpoints
     - New request/response fields
     - New webhook integrations
     - If changes found: Add endpoints, update API Summary and Document Lineage
7. **Update STRUCTURE.md** "Current State" table:
   - Update "Client Documents" row with next available CD-NNN
   - Update "Goals" row if new goals were added
8. Update session file with all documents processed
