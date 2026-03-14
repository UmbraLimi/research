#!/bin/bash
# Find WIP markers and checkboxes in PLAN.md
grep -n '🔥\|WIP\|\[x\]\|\[ \]' PLAN.md 2>/dev/null | head -30 || echo "(no WIP markers found)"
