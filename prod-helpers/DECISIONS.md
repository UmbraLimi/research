# Decisions

Cumulative record of decisions made across sessions. Updated by `/r-learn-decide`.

Last Updated: 2026-03-22

## Data Architecture

| # | Decision | Date | Summary |
|---|----------|------|---------|

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
| 1 | JavaScript/Node as default script language | 2026-03-13 | Default to JS with vitest; Python only when library requires it |
| 2 | Defer script infrastructure | 2026-03-13 | No package.json until first script needed; design structure at that point |
| 3 | Machine-specific credential storage | 2026-03-22 | `credentials/` dir, one `.env` per machine, gitignored. Tokens differ per machine |
