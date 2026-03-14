#!/bin/bash
# Read CONV-COUNTER and display current value
# Used by ! backtick pre-computation in r-start
if [ -f CONV-COUNTER ]; then
    cat CONV-COUNTER
else
    echo "MISSING — CONV-COUNTER file not found"
fi
