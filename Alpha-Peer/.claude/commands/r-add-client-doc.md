---
description: Process and index client document(s) from file_holding
argument-hint: "[--overwrite]"
---

# Add Client Document

**Purpose:** Process and index client document(s) that were just uploaded to chat.

## Actions

1. Detect which file(s) were just dragged into chat
2. **Check for duplicates:** For each file, check if it already exists in `/client-docs/`
   - If exists and no `--overwrite` flag: Inform user and stop (don't process)
   - If exists with `--overwrite` flag: Proceed with re-analysis and replacement
   - If doesn't exist: Proceed normally
3. For each file to process:
   - Read from `/file_holding/[filename]`
   - Analyze and extract key information:
     - Business requirements
     - User journeys and value propositions
     - Technical implications
     - Non-functional requirements
   - Move to `/client-docs/[filename]` (replacing if --overwrite)
   - Add/update entry in `client-docs-index.md`
   - Delete from file_holding
4. Update session file with all documents processed

## Workflow

1. Drop file(s) into `/MyResearch/file_holding/` on your Mac
2. Drag file(s) from file_holding into Claude chat
3. Type `/r-add-client-doc` (no filename needed - Claude sees what you uploaded)
4. Claude processes all files automatically

## Flags

- `--overwrite`: Re-analyze and replace existing document in client-docs

## Error Handling

- If file is not in file_holding folder: "File is missing from file-holding folder"
- If file already exists in client-docs (no --overwrite): "File [filename] is already in client-docs folder. Use `/r-add-client-doc --overwrite` to re-analyze."

## Examples

- Single file: Drag `requirements.pdf` into chat → `/r-add-client-doc`
- Re-analyze existing: Drag `requirements.pdf` → `/r-add-client-doc --overwrite`
- Multiple files: Drag `requirements.pdf`, `mockups.pdf`, `user-research.pdf` → `/r-add-client-doc`
