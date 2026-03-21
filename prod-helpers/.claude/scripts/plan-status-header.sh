#!/bin/bash
# Extract everything from start of PLAN.md up to first "## Phase" heading
DOCS_ROOT="${CLAUDE_PROJECT_DIR:-$(pwd)}"
sed -n '1,/^## Phase/p' "$DOCS_ROOT/PLAN.md" 2>/dev/null | head -20 || echo "(not found)"
