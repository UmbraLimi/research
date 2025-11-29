# File Holding Area

**Purpose:** Temporary staging area for files before they're processed and moved to their final locations.

## Workflow

1. **You:** Drop files here from your Mac (drag into this folder)
2. **You:** Drag the file from here into Claude Desktop chat
3. **Claude:** Checks if file already exists in destination folder
   - If exists: Notifies you (use `--overwrite` flag to replace)
   - If new: Proceeds with processing
4. **Claude:** Reads and analyzes the file
5. **Claude:** Moves file to appropriate project folder (e.g., client-docs, research)
6. **Claude:** Removes file from file_holding

## Why This Works

Since this folder is within `/Users/pomixis/MyResearch/`, Claude's MCP filesystem access can:
- ✅ Read files here
- ✅ Move/copy files to other project folders
- ✅ Delete files after processing

This is cleaner than manual saving - Claude handles the file organization automatically.

## Supported File Types

- PDFs (client docs, research papers)
- Images (screenshots, diagrams, mockups)
- Documents (Word, text files)
- Spreadsheets (Excel, CSV)
- Any other project-related files

## Note

This folder should always be empty or nearly empty - it's a temporary holding area, not storage.
