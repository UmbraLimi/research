#!/bin/bash
# List recent Dev session files for the current month
MONTH=$(date '+%Y-%m')
find docs/sessions/$MONTH -name '*Dev.md' 2>/dev/null | sort | tail -5 | sed 's|^|- |' || echo "- (none yet this month)"
