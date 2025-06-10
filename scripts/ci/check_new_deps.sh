#!/bin/bash
# New Dependencies Checker for Sprint Guard-Rails
# Ensures no new Python dependencies are added during sprint

set -e

echo "Checking for new dependencies..."

# Check if requirements.txt changed
if git diff --name-only main..HEAD | grep -q "requirements.txt"; then
    echo "❌ requirements.txt was modified - new dependencies not allowed"
    echo "Changed files:"
    git diff --name-only main..HEAD | grep requirements.txt
    exit 1
fi

# Check for new pip install commands in any files
if git diff main..HEAD | grep -q "pip install"; then
    echo "❌ Found 'pip install' commands in diff - new dependencies not allowed"
    exit 1
fi

echo "✅ No new dependencies detected"
exit 0 