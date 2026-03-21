# Decisions

Cumulative record of decisions made across sessions. Updated by `/r-learn-decide`.

Last Updated: 2026-03-14

## Data Architecture

| # | Decision | Date | Summary |
|---|----------|------|---------|
| 1 | Peerloop-docs documentation folder structure | 2026-03-13 | sessions/, reference/, architecture/, vendors/, guides/ — proven across 386+ sessions |

## Tag System

| # | Decision | Session | Summary |
|---|----------|---------|---------|

## Migration Strategy

| # | Decision | Session | Summary |
|---|----------|---------|---------|

## Agent Design

| # | Decision | Session | Summary |
|---|----------|---------|---------|

## Tooling & APIs

| # | Decision | Date | Summary |
|---|----------|------|---------|
| 1 | Skills 2 format for all project skills | 2026-03-13 | `.claude/skills/r-*/SKILL.md` — preserves allowed-tools and `!` interpolation |
| 2 | JavaScript/Node as default script language | 2026-03-13 | Default to JS with vitest; Python only when library requires it |
| 3 | Defer script infrastructure | 2026-03-13 | No package.json until first script needed; design structure at that point |
| 4 | Simplified r-docs without detection scripts | 2026-03-13 | Use git diff + find instead of dedicated bash scripts; add later if needed |
| 5 | Wrapper scripts for piped `!` backtick commands | 2026-03-14 | `.claude/scripts/*.sh` with blanket permission rule; preserves build-time determinism |
| 6 | Preserve `!` backtick determinism as project principle | 2026-03-14 | Never replace pre-computed context with tool-based alternatives without user approval |
| 7 | Machine tracking in commits via skills `!` backtick | 2026-03-14 | Pre-compute `~/.claude/.machine-name` in r-commit SKILL.md; `Machine:` in commit body |
| 8 | "Conv" as conversation numbering short-form | 2026-03-14 | Zero-padded 3-digit, `Conv: NNN` in commits, shared across commits in same conversation |
| 9 | Auto-synced CONV-COUNTER with mandatory pull/push | 2026-03-14 | `/r-start` pulls+increments+pushes; `/r-end` commits+pushes; HALT on sync failure |
| 10 | Separate /r-start and /r-end skills | 2026-03-14 | Start wraps resume; End wraps eos+commit+push; no combined skill |
| 11 | RESUME-STATE.md append mode with max 2 blocks | 2026-03-14 | Oldest-first ordering, conv-labeled headings; /r-save-state refuses 3rd append |
| 12 | /r-resume as consolidation point for multi-block state | 2026-03-14 | Walks blocks, evaluates with evidence, rewrites to single block after user approval |
| 13 | Auto-delete RESUME-STATE.md when all items complete | 2026-03-14 | Both /r-resume and /r-save-state detect all-done state and delete; file exists only for pending work |
| 14 | Unified entry point — always /r-start | 2026-03-14 | /r-start is sole entry point for cold and warm starts; /r-resume is internal only, called by /r-start Step 6 |
| 15 | Per-project conv numbering with 3-letter prefix | 2026-03-21 | PRH-004 format; each project owns its CONV-COUNTER; prefix registered in repo-root PROJECTS.yaml |
| 16 | YAML project identity files (PROJECT.yaml + PROJECTS.yaml) | 2026-03-21 | Subfolder PROJECT.yaml has prefix; repo-root PROJECTS.yaml is authoritative registry; template gets XXX placeholder |
