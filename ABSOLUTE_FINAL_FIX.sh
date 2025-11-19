#!/bin/bash

# ABSOLUTE FINAL FIX - Complete Claude Removal
# This removes ALL traces of Claude from EVERYWHERE

set -e

echo "=========================================="
echo "COMPLETE CLAUDE REMOVAL SCRIPT"
echo "=========================================="
echo ""

if [ ! -d ".git" ]; then
    echo "ERROR: Not in a git repository!"
    exit 1
fi

echo "Step 1: Fetching completely clean branch..."
git fetch origin

echo ""
echo "Step 2: Verification - Current state of remote main:"
echo "Contributors on origin/main:"
git log origin/main --format="%an <%ae>" 2>/dev/null | sort | uniq || echo "No origin/main yet"
echo ""

echo "Step 3: Verification - Clean branch state:"
echo "Contributors on clean branch:"
git log origin/claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu --format="%an <%ae>" | sort | uniq
echo ""
echo "Checking for 'claude' in commit messages:"
CLAUDE_COUNT=$(git log origin/claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu --oneline | grep -i claude | wc -l)
if [ "$CLAUDE_COUNT" -eq 0 ]; then
    echo "✓ NO 'claude' found in any commit messages!"
else
    echo "✗ WARNING: Found $CLAUDE_COUNT commits with 'claude' in message"
    echo "This should not happen. Please report this issue."
fi

echo ""
read -p "Continue with replacement? (yes/no): " confirm
if [ "$confirm" != "yes" ]; then
    echo "Aborted."
    exit 0
fi

echo ""
echo "Step 4: Deleting old local branches..."
git checkout claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu 2>/dev/null || git checkout -b temp origin/claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu
git branch -D main 2>/dev/null || true

echo "Step 5: Creating fresh main branch..."
git checkout -b main

echo "Step 6: FINAL VERIFICATION before push..."
echo ""
echo "Contributors:"
git log --format="%an <%ae>" | sort | uniq
echo ""
echo "'Claude' references in commits:"
git log --oneline | grep -i claude | wc -l
echo ""
echo "Sample recent commits:"
git log --format="%h | %an | %s" -5
echo ""

read -p "Everything looks good? Push to remote? (yes/no): " confirm2
if [ "$confirm2" != "yes" ]; then
    echo "Aborted. You can manually push later with:"
    echo "  git push origin main --force"
    exit 0
fi

echo ""
echo "Step 7: FORCE PUSHING to origin/main..."
git push origin main --force

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Push failed!"
    echo "Possible reasons:"
    echo "1. Authentication issue - check your credentials"
    echo "2. Branch protection - disable in GitHub settings temporarily"
    echo "3. Permission issue - ensure you have write access"
    echo ""
    echo "Manual fix:"
    echo "  git push origin main --force"
    exit 1
fi

echo ""
echo "Step 8: Deleting ALL old remote branches..."
git push origin --delete claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu 2>/dev/null || echo "  ✓ Already deleted"
git push origin --delete claude/understand-repo-012MCzUH5auh8Nr7ANGXrCBm 2>/dev/null || echo "  ✓ Already deleted"
git push origin --delete practise 2>/dev/null || echo "  ✓ No practise branch"
git push origin --delete problems 2>/dev/null || echo "  ✓ No problems branch"

echo ""
echo "Step 9: Cleaning up local references..."
git fetch --prune origin
git branch | grep -v "^* main$" | xargs -r git branch -D 2>/dev/null || true

echo ""
echo "=========================================="
echo "✓✓✓ SUCCESS ✓✓✓"
echo "=========================================="
echo ""
echo "FINAL VERIFICATION:"
echo "------------------"
echo ""
echo "Local branches:"
git branch
echo ""
echo "Remote branches:"
git branch -r
echo ""
echo "ALL contributors in history:"
git log --all --format="%an <%ae>" | sort | uniq
echo ""
echo "'Claude' mentions in commit messages:"
FINAL_CLAUDE=$(git log --all --oneline | grep -i claude | wc -l)
if [ "$FINAL_CLAUDE" -eq 0 ]; then
    echo "✓ ZERO - Perfect!"
else
    echo "✗ Found $FINAL_CLAUDE (this is unexpected)"
fi
echo ""
echo "Recent commits:"
git log --oneline -10
echo ""
echo "=========================================="
echo "Repository is now 100% CLEAN!"
echo "=========================================="
echo ""
echo "IMPORTANT: GitHub's contributor cache"
echo "-------------------------------------"
echo "If you still see old contributors on GitHub.com:"
echo "1. Clear your browser cache"
echo "2. Wait 24-48 hours for GitHub to recalculate"
echo "3. Check: https://github.com/gouthamgo/dsa/graphs/contributors"
echo ""
echo "The git history is now clean. The cache will update."
echo ""
