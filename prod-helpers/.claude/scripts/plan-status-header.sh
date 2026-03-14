#!/bin/bash
# Extract everything from start of PLAN.md up to first "## Phase" heading
sed -n '1,/^## Phase/p' PLAN.md 2>/dev/null | head -20 || echo "(not found)"
