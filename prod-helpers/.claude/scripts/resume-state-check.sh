#!/bin/bash
# Check if RESUME-STATE.md exists and show its saved date
if [ -f RESUME-STATE.md ]; then
  echo "EXISTS — saved on:"
  head -5 RESUME-STATE.md | grep 'Saved:'
else
  echo "No existing RESUME-STATE.md"
fi
