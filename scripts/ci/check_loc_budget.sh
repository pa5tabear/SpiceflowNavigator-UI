#!/bin/bash
# LOC Budget Checker for Sprint Guard-Rails
# Usage: check_loc_budget.sh <max_lines>

set -e

MAX_LINES=${1:-120}

# Get lines changed in current branch vs main
CHANGED_LINES=$(git diff --stat main..HEAD | tail -1 | grep -o '[0-9]\+ insertions' | grep -o '[0-9]\+' || echo "0")

echo "Lines changed: $CHANGED_LINES"
echo "Budget: $MAX_LINES"

if [ "$CHANGED_LINES" -gt "$MAX_LINES" ]; then
    echo "❌ LOC budget exceeded: $CHANGED_LINES > $MAX_LINES"
    exit 1
else
    echo "✅ LOC budget OK: $CHANGED_LINES ≤ $MAX_LINES"
    exit 0
fi 