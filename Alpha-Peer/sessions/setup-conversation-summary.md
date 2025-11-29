# Alpha Peer Setup - Conversation Summary

**Date:** November 25, 2025  
**Context:** Initial project setup and MCP configuration

## MCP Configuration Journey

### Problem Encountered
- MCP filesystem server wasn't loading initially
- Config file was created in wrong location: `/Library/Application Support/Claude` (system-level)
- Should have been: `~/Library/Application Support/Claude` (user-level)

### Solution
Created `~/Library/Application Support/Claude/claude_desktop_config.json` with:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/pomixis/MyResearch"
      ]
    }
  }
}
```

### Verification
- Confirmed npx installed (v10.2.4, Node v20.11.1)
- Manually tested MCP server - worked correctly
- Full quit and restart of Claude Desktop required
- Successfully connected after config file in correct location

## Project Structure Design

### Key Requirements Identified
- Web application project
- Iterative and opportunistic development approach
- Not comprehensive evaluation unless specifically requested
- Separate tracking for: prompts, learnings, decisions
- Need handoff document (Needs.md) for Claude Code later

### Folder Structure Created
```
Alpha-Peer/
├── readme.md
├── STRUCTURE.md (master guide)
├── Needs.md (evolving requirements)
├── /research/ (technology research)
├── /user-stories/ (user stories & requirements)
├── /sessions/ (session tracking)
├── /prompts/ (reusable prompts)
├── /learnings/ (knowledge capture)
└── /decisions/ (decision log)
```

### Naming Conventions Established
- Zero-padded 3-digit numbering (001, 002, etc.)
- Lowercase filenames with hyphens
- Specific patterns for each file type
- ISO 8601 dates (YYYY-MM-DD)

## Files Created

### Core Documentation
- **STRUCTURE.md** - Master organization guide with all conventions
- **Needs.md** - Template for evolving requirements document
- **prompt-library.md** - Reusable prompt templates
- **learnings-index.md** - Learning tracking system
- **session-2025-11-25-1.md** - First session log

### Folder Structure
Created all planned folders with appropriate organization

## Claude Desktop Projects Discussion

### Pros
- Persistent custom instructions
- Isolated conversation history
- Project knowledge files
- Focused context

### Cons
- Can't reference conversations outside project
- Switching overhead for multiple projects
- Less flexible once committed

### Decision
**Created Alpha Peer Project** with:
- STRUCTURE.md in Project Knowledge
- Custom instructions to consult STRUCTURE.md and track work

## Key Learnings

1. **MCP location critical:** User-level (`~`) vs system-level (`/`)
2. **Full restart required:** Claude Desktop must completely quit/restart for MCP
3. **Projects vs Chat:** Projects provide persistent context, good for focused work
4. **No slash commands:** Claude Desktop doesn't have CC-style slash commands
5. **Template approach:** Use prompt-library.md for reusable workflows

## Next Steps Discussed

1. Convert to Project setup (completed)
2. Begin actual Alpha Peer research
3. Create first user stories
4. Start technology evaluation

## Working Model Going Forward

- **All Alpha Peer work:** In the Project
- **General topics/troubleshooting:** Regular chat
- **Session tracking:** Create session file each working session
- **Continuous updates:** Needs.md evolves with each discovery
- **Document decisions:** Use /decisions/ folder for rationale

## Useful Context for Future Sessions

- Username: pomixis
- System: MacBook Air (2017), macOS Monterey 12.7.6
- Node/npx: v20.11.1 / v10.2.4
- MCP access: ~/MyResearch (includes all subfolders)
- Claude Desktop: v1.0.1217 (latest as of 2025-11-24)

## Original Chat Context

The conversation started with troubleshooting Google Meet cursor visibility issue, then transitioned to setting up file access for Alpha Peer project planning work.
