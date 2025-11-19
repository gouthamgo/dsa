#!/bin/bash

# FINAL FIX - This will completely replace main with clean history
# Run this from your cloned repository

set -e  # Exit on any error

echo "=========================================="
echo "FINAL REPOSITORY CLEANUP"
echo "This will replace main with ONLY your commits"
echo "=========================================="
echo ""

# Get current directory
if [ ! -d ".git" ]; then
    echo "ERROR: Not in a git repository!"
    echo "Please run this from your dsa repository directory"
    exit 1
fi

echo "Step 1: Fetching all branches..."
git fetch origin

echo ""
echo "Step 2: Showing CURRENT contributors on remote main..."
echo "Current origin/main contributors:"
git log origin/main --format="%an <%ae>" | sort | uniq
echo ""

echo "Step 3: Showing CLEAN branch contributors..."
echo "Clean branch contributors:"
git log origin/claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu --format="%an <%ae>" | sort | uniq
echo ""

read -p "Continue with cleanup? (yes/no): " confirm
if [ "$confirm" != "yes" ]; then
    echo "Aborted."
    exit 0
fi

echo ""
echo "Step 4: Deleting local main branch..."
git checkout claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu
git branch -D main 2>/dev/null || true

echo "Step 5: Creating new main from clean branch..."
git checkout -b main origin/claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu

echo "Step 6: Verifying new main is clean..."
echo "New main contributors:"
git log --format="%an <%ae>" | sort | uniq
echo ""

echo "Step 7: Force pushing to origin/main..."
git push origin main --force

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to push to main"
    echo "You may need to:"
    echo "1. Check your authentication"
    echo "2. Ensure you have write access"
    echo "3. Disable branch protection rules temporarily"
    exit 1
fi

echo ""
echo "Step 8: Deleting ALL other remote branches..."
git push origin --delete claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu 2>/dev/null || echo "  - claude/consolidate branch already deleted or doesn't exist"
git push origin --delete claude/understand-repo-012MCzUH5auh8Nr7ANGXrCBm 2>/dev/null || echo "  - claude/understand branch already deleted or doesn't exist"
git push origin --delete practise 2>/dev/null || echo "  - practise branch already deleted or doesn't exist"
git push origin --delete problems 2>/dev/null || echo "  - problems branch already deleted or doesn't exist"

echo ""
echo "Step 9: Cleaning up local references..."
git fetch --prune origin

echo ""
echo "Step 10: Deleting all local branches except main..."
git checkout main
git branch | grep -v "^* main$" | xargs -r git branch -D 2>/dev/null || true

echo ""
echo "=========================================="
echo "✓✓✓ SUCCESS ✓✓✓"
echo "=========================================="
echo ""
echo "Final state:"
echo "------------"
echo "Branches:"
git branch -a
echo ""
echo "Contributors:"
git log --all --format="%an <%ae>" | sort | uniq
echo ""
echo "Recent commits:"
git log --oneline -5
echo ""
echo "=========================================="
echo "Repository is now clean!"
echo "=========================================="
echo ""
echo "IMPORTANT: GitHub's contributor graph caches data."
echo "If you still see old contributors on GitHub:"
echo "1. Go to: https://github.com/gouthamgo/dsa"
echo "2. Click 'Insights' > 'Contributors'"
echo "3. Wait 24-48 hours for GitHub to recalculate"
echo ""
echo "You can verify the commit history is clean by running:"
echo "  git log --all --format='%an <%ae>' | sort | uniq"
echo ""
