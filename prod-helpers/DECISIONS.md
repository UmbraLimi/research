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
