#!/bin/bash

# Complete Repository Cleanup Script
# This will ensure only YOU are in the commit history

echo "=========================================="
echo "Repository Cleanup Script"
echo "=========================================="
echo ""

# Step 1: Fetch the cleaned branch
echo "Step 1: Fetching cleaned branch..."
git fetch origin claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu

# Step 2: Delete old main if exists
echo "Step 2: Cleaning up old branches..."
git branch -D main 2>/dev/null || true

# Step 3: Create fresh main from cleaned branch
echo "Step 3: Creating fresh main branch..."
git checkout -b main origin/claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu

# Step 4: Verify authorship
echo "Step 4: Verifying authorship..."
echo "Contributors in history:"
git log --all --format="%an <%ae>" | sort | uniq
echo ""

# Step 5: Force push to main
echo "Step 5: Force pushing to main..."
git push -u origin main --force

if [ $? -eq 0 ]; then
    echo "✓ Successfully pushed to main"
else
    echo "✗ Failed to push to main"
    exit 1
fi

# Step 6: Delete old branches from remote
echo "Step 6: Deleting old remote branches..."
git push origin --delete claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu 2>/dev/null || echo "Branch already deleted or doesn't exist"
git push origin --delete claude/understand-repo-012MCzUH5auh8Nr7ANGXrCBm 2>/dev/null || echo "Branch already deleted or doesn't exist"

# Step 7: Clean up local tracking branches
echo "Step 7: Cleaning up local references..."
git fetch --prune origin

# Step 8: Verify final state
echo ""
echo "=========================================="
echo "Final Verification"
echo "=========================================="
echo "Local branches:"
git branch -a
echo ""
echo "Contributors:"
git log --all --format="%an <%ae>" | sort | uniq
echo ""
echo "Recent commits:"
git log --oneline -10
echo ""
echo "=========================================="
echo "✓ Cleanup Complete!"
echo "=========================================="
echo ""
echo "Note: GitHub's contributor graph may take 24-48 hours to update."
echo "If you still see old contributors, go to:"
echo "https://github.com/gouthamgo/dsa/graphs/contributors"
echo "and wait for GitHub to recalculate."
