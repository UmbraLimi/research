# Minimum-Project Template

This folder is a template for new non-programming projects in the ~/MyResearch repository.

## What this folder does and doesn't do

### It is perfect for:

- planning for coding projects (amassing the information you need for creating a PLAN.md)
- researching a topic of any kind
- (more will be added here)

### It is not intended for coding projects.

- Those go into /MyVite, /MyOther, /MyAstro, /MyElectron, /my_n8n and /MyNext

## Usage

1. Copy this entire folder and rename it for your new project:

   ```bash
   cp -r Minimum-Project My-New-Project
   ```

2. Launch Claude Code from your new project folder:
   ```bash
   cd My-New-Project
   claude
   ```
3. Customize `PURPOSE.md` sections for your project:
   - Review the Section Library below
   - Keep core sections, add/remove others as needed
   - Then fill out each section

4. Run `/init` to have CC create `CLAUDE.md` from `README.md` and `PURPOSE.md`
   - After creating CLAUDE.md, CC should offer: "Do you want me to create a basic PLAN.md from what I found in this folder?"

5. Create `PLAN.md` (CC will offer, or ask CC, or create your own skeleton for CC to augment)

## What's Included

| File/Folder         | Purpose                                                          |
| ------------------- | ---------------------------------------------------------------- |
| `README.md`         | These instructions (delete after setup)                          |
| `PURPOSE.md`        | Fill this out with project goals, context, constraints, etc.     |
| `docs/sessions/`    | Session logs created by `/par-learnings` and `/par-prompts`      |
| `.claude/commands/` | Project-specific slash commands (includes `/r-commit`)           |

## Created During Setup

| File        | Created By                                   |
| ----------- | -------------------------------------------- |
| `CLAUDE.md` | `/init` command (step 4)                     |
| `PLAN.md`   | You or Claude Code (step 5)                  |

## Section Library

PURPOSE.md ships with a generic set of sections. Before filling it out, customize the sections for your project type. Use this library as a reference.

### Core Sections (keep for all projects)

| Section | Purpose |
|---------|---------|
| **Goals** | What you're trying to accomplish |
| **Background Information** | Knowledge, documents, resources you bring |
| **Personal Context** | Your skills, time, experience relevant to this |
| **Concerns & Risks** | What could go wrong, known pitfalls |
| **Constraints** | Budget, time, dependencies, limitations |
| **Other Notes** | Catch-all for anything else |

### Writing & Publication Projects

*Examples: nature articles, blog series, newsletter content*

| Section | Purpose |
|---------|---------|
| **Audience** | Who is this for? Age range, expertise level, interests |
| **Content & Sources** | Topics to cover, anecdotes, source materials |
| **Preferences** | Tone, voice, style guidelines |
| **Outputs & Platforms** | Blog, Twitter, Substack, etc. with format requirements |
| **Workflow & Process** | Research → outline → draft → revise, or however you work |

### Research & Comparison Projects

*Examples: evaluating video platforms, choosing a CMS, comparing services*

| Section | Purpose |
|---------|---------|
| **Research Questions** | Specific questions you need answered |
| **Candidates** | Options/products/services being evaluated |
| **Evaluation Criteria** | How you'll judge and compare (features, price, ease, etc.) |
| **Decision Factors** | What matters most? Weighted priorities |
| **Deliverable** | Recommendation doc? Comparison matrix? Decision memo? |

### Hobby & Collection Projects

*Examples: stamp collecting, photography archive, bird life list*

| Section | Purpose |
|---------|---------|
| **Current State** | What do you have now? How is it organized? |
| **Acquisition Goals** | What are you trying to add or complete? |
| **Organization System** | How will items be cataloged, stored, displayed? |
| **Community & Resources** | Groups, references, experts, marketplaces |
| **Budget & Sourcing** | How much to spend, where to find items |

### Planning-for-Code Projects

*Examples: app planning, architecture research, requirements gathering*

| Section | Purpose |
|---------|---------|
| **Technical Aspects** | Technologies, frameworks, integrations involved |
| **Requirements** | What must the eventual code do? |
| **Architecture Questions** | Decisions that need research before coding |
| **Target Repository** | Where will the code eventually live? |
| **Handoff Criteria** | When is planning "done" and coding begins? |

### Skill & Tool Development Projects

*Examples: Claude Code skills, automation helpers, processing utilities*

| Section | Purpose |
|---------|---------|
| **Input Sources** | What formats/platforms/data types will be processed? |
| **Output Format** | What does the deliverable look like? Template/example |
| **Requirements** | Functional and quality requirements for the tool |
| **Use Cases** | Specific scenarios showing how the tool will be used |
| **Technical Aspects** | Implementation details, frameworks, limitations |
| **Workflow & Process** | Build iteratively? Start with one case? How to refine? |

### Mix and Match

Most projects blend types. A nature publication project might include:
- Core sections (always)
- Audience, Content & Sources, Outputs & Platforms (writing)
- Research Questions, Evaluation Criteria (if comparing sources)

Start with core sections, scan the flavors above, add what fits.

## Available Slash Commands

When you launch Claude Code from any project folder, you get:

**Parent-level commands** (from `MyResearch/.claude/commands/`):

- `/par-resume` - Load PLAN.md and show where you left off
- `/par-update` - Save progress to PLAN.md (run frequently!)
- `/par-end-session` - Full wrap-up: learnings, prompts, optional commit
- `/repo-commit` - Stage and commit all changes in repo
- `/par-learnings` - Document what you learned this session
- `/par-prompts` - Save prompts used this session
- `/par-timestamp` - Utility for other commands
- `/par-pare` - Optimize CLAUDE.md by offloading content

**Project-level commands** (from `.claude/commands/`):

- `/r-commit` - Stage and commit only this project's changes

## Adding Project-Specific Commands

Create `.md` files in `.claude/commands/` with this format:

```markdown
---
description: Brief description shown in command list
argument-hint: '<optional-arg>'
---

# Command Name

Instructions for Claude to follow when this command is invoked.
```

Suggested prefix: Use `/r-` for project-specific commands to distinguish from parent `/par-*` commands.

## Caveats

- **PLAN.md is required for session commands** - Create it during setup (step 5). The `/par-resume` and `/par-update` commands expect this file.

- **Two commit options** - Use `/r-commit` to commit only this project's changes, or `/repo-commit` to commit all changes across the repo.

- **Session files are auto-organized** - `/par-learnings` and `/par-prompts` create files in `docs/sessions/YYYY-MM/` automatically.

## Suggestions

- **Run `/par-update` frequently** - Don't wait until end of session. If Claude Code crashes or you lose context, PLAN.md is your recovery point.

- **Keep CLAUDE.md focused** - Put only essential guidance here. Use `/par-pare` if it gets too long.

- **Use phases in PLAN.md** - Break work into numbered phases (1.1, 1.2, 2.1...) for clear progress tracking.

- **Delete this README** - Once you've set up your project, you don't need these instructions cluttering your folder.
