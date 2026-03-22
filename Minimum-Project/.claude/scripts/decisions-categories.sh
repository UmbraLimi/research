#!/bin/bash
# Extract category headings from DECISIONS.md
DOCS_ROOT="${CLAUDE_PROJECT_DIR:-$(pwd)}"
grep '^## ' "$DOCS_ROOT/DECISIONS.md" 2>/dev/null | sed 's/^## /- /' || echo "- (unable to read DECISIONS.md)"
