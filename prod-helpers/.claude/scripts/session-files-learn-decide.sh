#!/bin/bash
# List recent Learnings and Decisions session files for the current month
MONTH=$(date '+%Y-%m')
find docs/sessions/$MONTH \( -name '*Learnings.md' -o -name '*Decisions.md' \) 2>/dev/null | sort | tail -10 | sed 's|^|- |' || echo "- (none yet this month)"
