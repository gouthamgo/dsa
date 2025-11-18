#!/bin/bash

# COMPLETE RESET - Creates entirely new history with single commit
# Use this if cleanup_repo.sh doesn't work

echo "=========================================="
echo "COMPLETE REPOSITORY RESET"
echo "WARNING: This creates a NEW history!"
echo "=========================================="
echo ""

read -p "This will create a completely new history. Continue? (yes/no): " confirm
if [ "$confirm" != "yes" ]; then
    echo "Aborted."
    exit 0
fi

# Step 1: Create a new orphan branch (no history)
echo "Step 1: Creating orphan branch with no history..."
git checkout --orphan temp_main

# Step 2: Add all current files
echo "Step 2: Adding all files..."
git add -A

# Step 3: Create initial commit
echo "Step 3: Creating initial commit..."
git commit -m "Initial commit - Complete DSA repository

This repository contains:
- Data Structures and Algorithms implementations
- NeetCode roadmap and solutions
- FAANG interview preparation materials
- Pattern recognition guides
- Beginner resources and tutorials
- Python essentials for DSA"

# Step 4: Delete old main branch
echo "Step 4: Deleting old main branch..."
git branch -D main 2>/dev/null || true

# Step 5: Rename current branch to main
echo "Step 5: Renaming to main..."
git branch -m main

# Step 6: Force push
echo "Step 6: Force pushing to remote..."
git push -u origin main --force

# Step 7: Delete all other remote branches
echo "Step 7: Cleaning up remote branches..."
git push origin --delete claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu 2>/dev/null || true
git push origin --delete claude/understand-repo-012MCzUH5auh8Nr7ANGXrCBm 2>/dev/null || true

# Step 8: Clean references
echo "Step 8: Cleaning references..."
git fetch --prune origin

echo ""
echo "=========================================="
echo "✓ Complete Reset Done!"
echo "=========================================="
echo "Your repository now has:"
echo "- 1 commit (Initial commit)"
echo "- 1 contributor (you)"
echo "- 1 branch (main)"
echo ""
git log --oneline
echo ""
git log --format="%an <%ae>" | sort | uniq
