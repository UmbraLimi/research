#!/bin/bash
# List all markdown files in docs/
find docs -name '*.md' 2>/dev/null | sort | sed 's|^|- |' || echo "- (no docs found)"
