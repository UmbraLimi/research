#!/bin/bash
# Read .conv-current (ephemeral session file) and display value
# Used by ! backtick pre-computation in r-commit and r-end
if [ -f .conv-current ]; then
    cat .conv-current
else
    echo "MISSING — no active conv (run /r-start first)"
fi
