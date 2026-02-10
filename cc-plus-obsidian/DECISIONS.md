# DECISIONS — CC + Obsidian Integration

*Authoritative net decisions for this project. If a decision was made on Monday and changed on Friday, only the Friday decision appears here. For full rationale and alternatives considered, see PLANNING.md.*

*Last Updated: 2026-02-09 (session 3)*

---

## Vault Architecture

| Decision | Choice |
|----------|--------|
| Main vault path | `~/Vaults/main/` |
| Private vault path | `~/Vaults/private/` (deferred) |
| Old vault (`~/Obsidian Vaults/main2025`) | Will be retired after migration |
| Access model | Single tier — all folders CC: FULL. No folder-based deny/selective. |
| Credential security | Inline `===value===` markers. MCP server strips with `/===(.+?)===/g`. |
| Two-vault rationale | Main vault = CC-accessible. Private vault = CC-denied, local LLM only. Avoids complex per-folder access rules. |

## Daily Note Processing

| Decision | Choice |
|----------|--------|
| Qualifying heading rule | Must contain at least one `[[wikilink]]`. Non-qualifying headings stay in the daily note untouched. |
| Atomic note naming | `{date} • {heading text without brackets}.md` |
| Atomic note location | `log/notes/` |
| Merge rule | One atomic note per unique heading-signature per day. Duplicate headings append. |
| Multi-project headings | One atomic note, all project logs updated. `## [[A]] • [[B]]` creates `{date} • A • B.md`. |
| Replacement rule | After extraction, heading content replaced with `→ [[note-name]]` arrows. |
| Idempotency | Re-running `/cco-process-daily` only processes new/unprocessed headings. |

## Card Types & Schemas

| Decision | Choice |
|----------|--------|
| Card types | 6: coding, non-coding, meeting, slack, email, telegram |
| Card naming | `{date} • {project} • {card-type} • {start-time}.md` |
| Card storage | Each type has its own `log/` subfolder |
| Coding cards | CC-generated from git history via `/cco-session-close`. Never in daily notes. |
| All other cards | Human-entered in daily notes, extracted by `/cco-process-daily` |
| Meeting card scope | Covers video calls, phone calls, site visits, in-person. `via` field distinguishes them. |
| Email card body | Summarized as bullet points, not quoted verbatim. Original lives in email client. |
| Email threading | `continued: new` for new threads; wikilink to prior card for continuations. |
| Slack/Telegram cards | Timed (start/end required). Separate fields, not compressed. |
| Schema versioning | Versioned schemas in `reference/schemas/`. `/cco-migrate-schema` backfills changes. |
| Schema language | Markdown files with field tables and changelog sections. |
| No spaces in filenames | `PeerLoop.md` not `Peer Loop.md`. Matches wikilink target `[[PeerLoop]]`. |

## Task Management

| Decision | Choice |
|----------|--------|
| Importance notation | `+` symbols in daily notes (e.g., `+++++`). CC converts to `[importance:: 5]` during extraction. |
| Due dates | Optional. Only when there's a real deadline. |
| Delegation/assignee | None. Solo workflow. |
| Urgency field | None. Urgent work gets scheduled directly. |
| Task extraction | Tasks move from atomic notes to `{Project}-tasks.md` with back-link to source. |
| Task dedup | Extracted tasks marked `→ moved to [[{Project}-tasks]]` in atomic note. |

## CC Skills

| Decision | Choice |
|----------|--------|
| Skill implementation | Markdown prompt files in `~/.claude/commands/`, not TypeScript/Python code. CC interprets and executes step-by-step. |
| Skill prefix | `cco-` for all vault integration skills. Prevents collision with `q-*`, `par-*`, `r-*`. |
| Skill list | `/cco-session-close`, `/cco-process-daily`, `/cco-migrate-schema`, `/cco-project-init` |
| Card marker detection | Loose matching on keywords (`Timecard` + `Coding`, `Slack`, etc.), not exact emoji sequences. Tolerates device/version variation. |
| Skill execution order | Documented at bottom of skill file when steps have data dependencies. |
| `/cco-session-close` | Runs from project repo. Reads vault path from CLAUDE.md. Generates coding card + session note + appends learnings/decisions + updates plan. |
| `/cco-process-daily` | Runs from anywhere. Targets `~/Vaults/main` hardcoded. Processes today's daily note by default. |

## Mobile & Headless

| Decision | Choice |
|----------|--------|
| Mobile constraint | DataviewJS with external scripts does NOT work on Obsidian mobile. |
| Obsidian Sync | **Deferred.** CC reads/writes vault directly via native file tools. Sync only needed if mobile editing becomes a priority. |
| Mobile strategy | CC headless mode (`claude -p`) on Mac Mini processes daily notes. Mobile access deferred until Sync is set up. |
| Pre-rendered dashboards | Rejected — violates single source of truth. |
| Trigger mechanism | TBD — file watcher, cron, or manual (Apple Shortcut / webhook → SSH). |

## MCP Server

| Decision | Choice |
|----------|--------|
| MCP server | **Deferred.** CC's native file tools (Glob, Grep, Read, Write) provide full vault access. MCP adds no value until semantic search is needed. |
| Credential security | `===value===` inline markers remain the convention. Without MCP redaction, CC sees raw credentials — acceptable since CC is local and credentials go only to Anthropic's API. |
| Revisit trigger | When keyword search (Grep) proves insufficient for vault queries, build MCP with semantic search. |

## Project Structure

| Decision | Choice |
|----------|--------|
| Code repos | `~/projects/{name}/` — code only, no narrative docs |
| Vault projects | `~/Vaults/main/projects/{name}/` — plan, sessions, decisions, learnings, tasks, log |
| Parallel presence | Every project has both a repo folder and a vault folder. |
| CLAUDE.md convention | Each repo has `## Vault Integration` section pointing to vault project path. |
| Session granularity | One session note per project per day. Multiple CC sessions merge into one note. |
| Existing docs | Start fresh. No migration of old session docs. Manual move on case-by-case basis. |

## Documentation Format

| Decision | Choice |
|----------|--------|
| PLAN.md phases | Named (not numbered). Dot-notation addressing (e.g., `GLOBAL-SKILLS.SESSION-CLOSE.READ-PROJECT`). |
| PLAN.md ordering | Current Sequence at top defines execution order. Decoupled from phase structure. |
| Completed work | Full detail moves to COMPLETED-PLAN.md. PLAN.md retains heading + one-line summary. |
| Phase markers | ✅ complete, 🔄 active, no marker = future |
| File roles | CLAUDE.md = CC guidance. PLAN.md = task tracking. DECISIONS.md = net decisions. PLANNING.md = full design rationale. |

## Git & Workflow

| Decision | Choice |
|----------|--------|
| History-changing commands | Always ask for explicit permission: rebase, merge, reset --hard, push --force, commit --amend. |
| PeerLoop repo location | `~/projects/peerloop` (moved from `~/MyAstro/Peerloop`) |
| PeerLoop vault branch | `xx3` (branched from `staging`, not `main` which is stale) |
