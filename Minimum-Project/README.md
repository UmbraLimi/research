# Minimum-Project Template

This folder is a template for new non-programming projects in the ~/research repository.

## What this folder does and doesn't do

### It is perfect for:

- planning for coding projects (amassing the information you need for creating a PLAN.md)
- researching a topic of any kind
- (more will be added here)

### It is not intended for coding projects.

- Those go into /MyVite, /MyOther, /MyAstro, /MyElectron, /my_n8n and /MyNext

## Prerequisites

**Git remote must be configured.** The `/r-start` and `/r-end` skills pull and push to keep the conversation counter in sync across machines. If you're copying this template into a repo that already has a remote (like ~/research), you're fine. If you're starting a standalone project, set up a git remote before running `/r-start`:

```bash
cd My-New-Project
git init
git remote add origin <your-repo-url>
git add -A && git commit -m "Initial project from template"
git push -u origin main
```

Without a remote, `/r-start` will HALT at the pull/push steps.

## Usage

1. Copy this entire folder and rename it for your new project:

   ```bash
   cp -r Minimum-Project My-New-Project
   ```

2. Set your project prefix in `PROJECT.yaml`:
   - Choose a 3-letter prefix (e.g., `MNP` for My New Project)
   - Register it in `/PROJECTS.yaml` at the repo root

3. Launch Claude Code from your new project folder:
   ```bash
   cd My-New-Project
   claude
   ```

4. Customize `PURPOSE.md` sections for your project:
   - Review the Section Library below
   - Keep core sections, add/remove others as needed
   - Then fill out each section

5. Run `/init` to have CC customize `CLAUDE.md` from `PURPOSE.md`:
   - Updates project overview and status
   - Customizes DECISIONS.md categories for your project
   - Customizes topic tables in r-learn-decide skill
   - Customizes change detection matrix in r-docs skill
   - CC should offer: "Do you want me to create a basic PLAN.md from what I found in this folder?"

6. Create `PLAN.md` (CC will offer, or ask CC, or create your own skeleton for CC to augment)

7. Commit your setup changes — `/r-start` will HALT if the repo is dirty:
   ```
   /r-commit
   ```
   Or manually: `git add . && git commit -m "Initial project setup"`

8. Delete this README — it's setup instructions, not project documentation.

---

**Setup complete.** From now on, start every conversation with `/r-start` and end with `/r-end`. See `CONV-FLOWCHART.md` for the full workflow.

## What's Included

### Infrastructure (ready to use)

| File/Folder | Purpose |
|-------------|---------|
| `.claude/skills/` | 10 project-level r-* skills (full conversation lifecycle) |
| `.claude/scripts/` | 10 shell helper scripts for skill pre-computation |
| `.claude/settings.local.json` | Permissions for skills, scripts, and git operations |
| `CONV-COUNTER` | Conversation counter (starts at 0) |
| `CONV-FLOWCHART.md` | Visual guide to conversation lifecycle |
| `.gitignore` | Ignores .DS_Store, .conv-current, credentials/ |

### Project Files (templates to customize)

| File | Purpose | Customized By |
|------|---------|---------------|
| `PURPOSE.md` | Project goals, context, constraints | You (before /init) |
| `CLAUDE.md` | Claude Code guidance for this project | `/init` from PURPOSE.md |
| `PROJECT.yaml` | Project prefix (3-letter code) | You (step 2) |
| `PLAN.md` | Current & pending work | You or CC (step 6) |
| `DECISIONS.md` | Project decision record | `/init` sets categories |
| `DOC-DECISIONS.md` | Workflow conventions | Auto-populated as decisions are made |
| `COMPLETED_PLAN.md` | Archive of completed phases | `/r-update-plan` |

## Conversation Workflow

All conversations follow this pattern:

```
/r-start → work → /r-end → exit
```

See `CONV-FLOWCHART.md` for the full visual guide and quick reference table.

### Available r-* Skills

| Skill | Purpose |
|-------|---------|
| `/r-start` | Start conversation (pull, increment counter, push, resume) |
| `/r-end` | End conversation (docs, save state, commit, push) |
| `/r-eos` | End-of-conv sequence (learn-decide, dump, update-plan, docs) |
| `/r-learn-decide` | Capture learnings and decisions |
| `/r-dump` | Create development conv log |
| `/r-update-plan` | Update PLAN.md with progress |
| `/r-docs` | Update project documentation |
| `/r-save-state` | Save work state for cross-session continuity |
| `/r-commit` | Commit only this folder's changes |
| `/r-resume` | Show current work position (called by /r-start) |

## Standard docs/ Folder Structure

All folders present in every project. This is the standard across all projects:

```
docs/
├── sessions/       # Conv/session logs (learnings, decisions, dev transcripts)
│   └── YYYY-MM/    # Organized by month
├── requirements/   # What needs to be built/done
│   ├── user-stories.md (or user-stories/ dir if split by role)
│   └── rfcs/       # Numbered change requests (RFC-001/, RFC-002/, ...)
├── reference/      # External tools, APIs, services (their docs, our notes)
├── as-designed/    # Pre-build: specs, formats, plans (how things SHOULD work)
├── as-built/       # Post-build: documentation of implemented systems (how things DO work)
└── guides/         # How-to procedures for specific workflows
```

**Lifecycle:** requirements → as-designed → build → as-built

**Root-level docs** (not in docs/):

| File | Purpose |
|------|---------|
| `PLAN.md` | Current & pending work (forward-looking only) |
| `COMPLETED_PLAN.md` | Archive of completed phases (terse) |
| `DECISIONS.md` | Project-domain decision record |
| `DOC-DECISIONS.md` | Repo workflow & documentation conventions |
| `PURPOSE.md` | Project goals, context, constraints |

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

## Parent-Level Commands

Also available from any project folder (from `research/.claude/commands/`):

- `/par-resume` - Load PLAN.md and show where you left off
- `/par-update` - Save progress to PLAN.md
- `/par-end-session` - Full wrap-up: learnings, prompts, optional commit
- `/repo-commit` - Stage and commit all changes in repo
- `/par-learnings` - Document what you learned this session
- `/par-prompts` - Save prompts used this session
- `/par-timestamp` - Utility for other commands
- `/par-pare` - Optimize CLAUDE.md by offloading content
