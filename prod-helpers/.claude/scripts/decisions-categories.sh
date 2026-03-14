#!/bin/bash
# Extract category headings from DECISIONS.md
grep '^## ' DECISIONS.md 2>/dev/null | sed 's/^## /- /' || echo "- (unable to read DECISIONS.md)"
