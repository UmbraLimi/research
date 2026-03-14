#!/bin/bash
# Extract the Open Questions section from PLAN.md
sed -n '/^## Open Questions/,/^## /p' PLAN.md 2>/dev/null | head -20 || echo "(none found)"
