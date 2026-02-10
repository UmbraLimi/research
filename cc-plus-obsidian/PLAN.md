# PLAN — CC + Obsidian Integration

## Current Sequence
1. FOUNDATION.SYNC-CONFIG *(manual — open vault in Obsidian, enable Sync)*
2. FOUNDATION.CREDENTIALS *(manual — populate vendor notes with `===` markers)*
3. FOUNDATION.PEERLOOP-REPO cleanup *(remove narrative files, update .gitignore on xx3)*
4. HEADLESS.SETUP
5. HEADLESS.TRIGGER

---

## FOUNDATION 🔄
Set up the vault, folder structure, and first project (PeerLoop) in both vault and repo.

### VAULT-CREATE ✅
- [x] Create `~/Vaults/main/` as a fresh Obsidian vault
- [x] Initialize Obsidian vault settings (`.obsidian/` config)
- [ ] Verify vault opens in Obsidian

### VAULT-FOLDERS ✅
- [x] Create folder tree (17 leaf directories)
- [x] Add `.gitkeep` in each leaf folder

### PEERLOOP-VAULT ✅
- [x] Create `projects/peerloop/` with PeerLoop.md, PeerLoop-tasks.md, plan.md, sessions/, decisions.md, learnings.md
- [x] Populate initial content (fresh start, summary of pre-vault state)

### PEERLOOP-REPO ✅
- [x] Relocate PeerLoop repo: `~/MyAstro/Peerloop` → `~/projects/peerloop`
- [x] Update PeerLoop `CLAUDE.md` with vault integration section (on branch `xx3`)
- [ ] Remove session docs, PLAN.md, and narrative files from repo
- [ ] Update `.gitignore` to exclude doc patterns

### SYNC-CONFIG
- [ ] Configure Obsidian Sync on `~/Vaults/main/`
- [ ] Verify sync works between Mac Mini and other devices
- [ ] Upgrade to Plus plan if second vault is needed

### CREDENTIALS
- [ ] Populate `reference/vendors/` with vendor notes
- [ ] Wrap all credential values with `===value===` convention
- [ ] Verify credentials are visually highlighted in Obsidian (outer `==` renders as highlight)

---

## GLOBAL-SKILLS 🔄
Build the four `cco-` prefixed CC global skills and the schema system.

### SCHEMAS ✅
- [x] Create `reference/schemas/coding.md` — v1 with all fields from PLANNING.md spec
- [x] Create `reference/schemas/non-coding.md` — v1
- [x] Create `reference/schemas/meeting.md` — v1 (covers phone, site visit via `via` field)
- [x] Create `reference/schemas/slack.md` — v1
- [x] Create `reference/schemas/email.md` — v1
- [x] Create `reference/schemas/telegram.md` — v1
- [x] Define base frontmatter shared across all types (`_base.md`)
- [x] Document changelog format and migration conventions

### SESSION-CLOSE ✅
Built `/cco-session-close` at `~/.claude/commands/cco-session-close.md` (348 lines).

- [x] READ-PROJECT — Reads vault path from CLAUDE.md, fallback to cwd basename
- [x] TIMECARD-GEN — Integrates `/q-git-history`, generates coding card with full schema frontmatter
- [x] SESSION-NOTE — Writes session note with merge support for multi-session days
- [x] ACCUMULATE — Appends to decisions.md and learnings.md under date headings
- [x] UPDATE-PLAN — Marks completed tasks, adds new discoveries

### PROCESS-DAILY ✅
Built `/cco-process-daily` at `~/.claude/commands/cco-process-daily.md` (444 lines).

- [x] IDENTIFY-HEADINGS — Parse for `[[wikilinks]]`, skip already-processed
- [x] CREATE-ATOMIC — Create/append atomic notes in `log/notes/` with frontmatter
- [x] EXTRACT-CARDS — Recognize all 6 card-type markers, extract with schema frontmatter
- [x] UPDATE-LOGS — Update project log notes with wikilinks under date headings
- [x] EXTRACT-TASKS — Convert `+++++` to `[importance:: N]`, add to task files
- [x] REPLACE-LINKS — Replace processed content with `→ [[note-name]]` arrows
- [x] MERGE-MULTI — Merge rule, multi-project rule, idempotency

### MIGRATE-SCHEMA ✅
Built `/cco-migrate-schema` at `~/.claude/commands/cco-migrate-schema.md`.

- [x] Accept card type as argument
- [x] Read current schema version, find outdated notes
- [x] Apply frontmatter + body changes incrementally
- [x] Dry-run confirmation before modifying

### PROJECT-INIT ✅
Built `/cco-project-init` at `~/.claude/commands/cco-project-init.md`.

- [x] Accept project name, create vault folder structure
- [x] Add vault integration section to repo CLAUDE.md
- [x] Create project log and task file

### INTEGRATION-TEST ✅
- [ ] Test `/cco-session-close` end-to-end on PeerLoop — deferred to first real use
- [x] Test `/cco-process-daily` with a sample daily note containing all card types
- [x] Test merge rule: duplicate heading same day
- [x] Test multi-project heading: `## [[A]] • [[B]]`
- [x] Test idempotency: process same daily note twice
- [x] Test `/cco-migrate-schema` with a version bump
- [x] Test `/cco-project-init` with a new project

---

## HEADLESS
Set up CC headless mode on Mac Mini for mobile-triggered daily note processing.

### SETUP
- [ ] Configure CC headless execution (`claude -p`) on Mac Mini
- [ ] Define `--allowedTools` permissions for headless runs

### TRIGGER
- [ ] Choose trigger mechanism: file watcher (`fswatch`/`watchman`), cron, or manual
- [ ] Implement chosen trigger with appropriate guards (debounce, dedup)

### E2E-TEST
- [ ] Test: edit daily note on phone → Obsidian Sync → Mac Mini processes → Sync → results on phone
- [ ] Verify latency is acceptable

### MOBILE-TRIGGER
- [ ] Set up on-demand trigger from phone (Apple Shortcut / Tasker / webhook → SSH)
- [ ] Test manual trigger flow

### MONITORING
- [ ] Set up logging for headless runs
- [ ] Alert on failures (optional — email, push notification)

---

## MCP-SERVER
Build the local MCP server (TypeScript v1) for CC vault read access.

### PARSER
- [ ] Implement heading-aware markdown parser
- [ ] Chunk by heading with breadcrumb path (e.g., `# Project > ## Setup > ### Config`)
- [ ] Handle frontmatter extraction

### REDACTION
- [ ] Implement `===(.+?)===` regex stripping vault-wide
- [ ] Test: credentials in any folder are redacted in query results

### QUERY-TOOL
- [ ] Expose MCP tool: `query_vault(query: string) → results with heading paths`
- [ ] Support path-scoped queries (e.g., search within `projects/peerloop/`)

### CC-CONFIG
- [ ] Configure CC to connect to the local MCP server
- [ ] Test: "What's the current plan for PeerLoop?" returns plan.md content

### TESTING
- [ ] End-to-end tests across vault with various query patterns
- [ ] Verify redaction under all access paths

---

## MCP-ADVANCED
Optional enhancements to the MCP server. Low priority — assess after MCP-SERVER is stable.

- [ ] SEMANTIC-SEARCH — Add local embeddings via Ollama on Mac Mini M4 Pro
- [ ] LINK-TRAVERSAL — Follow `[[wikilinks]]` 1-2 hops for richer context
- [ ] QUERY-GATING — Confirmation prompt for credential-adjacent queries
- [ ] OBSIDIAN-PLUGIN — Heading-breadcrumb search within Obsidian itself (Path C)

---

## SCALE
Migrate remaining projects and harden the system. Details TBD after GLOBAL-SKILLS proves stable.

- [ ] MIGRATE-PROJECTS — Move remaining active projects to `~/projects/` + `~/Vaults/main/projects/` convention
- [ ] ARCHIVE — Move completed projects to `projects/_archive/`
- [ ] VAULT-LINT — Build skill to scan for credentials outside `===`, orphaned notes, broken wikilinks
- [ ] RETIRE-OLD — Evaluate whether `~/Obsidian Vaults/main2025` can be fully retired
