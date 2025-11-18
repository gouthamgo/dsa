#!/bin/bash

# Verification Script - Check current repository state

echo "=========================================="
echo "Repository Authorship Verification"
echo "=========================================="
echo ""

echo "Current Branch:"
git branch --show-current
echo ""

echo "All Branches:"
git branch -a
echo ""

echo "=========================================="
echo "ALL CONTRIBUTORS IN HISTORY:"
echo "=========================================="
git log --all --format="%an <%ae>" | sort | uniq
echo ""

echo "=========================================="
echo "COMMIT BREAKDOWN BY AUTHOR:"
echo "=========================================="
git shortlog --summary --numbered --email --all
echo ""

echo "=========================================="
echo "RECENT COMMITS (Last 15):"
echo "=========================================="
git log --all --format="%h | %an <%ae> | %s" -15
echo ""

echo "=========================================="
echo "CHECKING SPECIFIC PROBLEMATIC COMMITS:"
echo "=========================================="
echo "Searching for 'Claude' in commit history..."
git log --all --author="Claude" --oneline 2>/dev/null | head -5
if [ $? -ne 0 ] || [ -z "$(git log --all --author='Claude' --oneline 2>/dev/null)" ]; then
    echo "✓ No commits by Claude found!"
else
    echo "✗ Found commits by Claude"
fi
echo ""

echo "Searching for 'TS14' in commit history..."
git log --all --author="TS14" --oneline 2>/dev/null | head -5
if [ $? -ne 0 ] || [ -z "$(git log --all --author='TS14' --oneline 2>/dev/null)" ]; then
    echo "✓ No commits by TS14 found!"
else
    echo "✗ Found commits by TS14"
fi
echo ""

echo "=========================================="
echo "GitHub Contributors Cache Note:"
echo "=========================================="
echo "If you see old contributors on GitHub but not here,"
echo "it's GitHub's cache. It will update in 24-48 hours."
echo ""
echo "To force refresh, try:"
echo "1. Push an empty commit: git commit --allow-empty -m 'Refresh' && git push"
echo "2. Wait for GitHub to recalculate"
echo "3. Check: https://github.com/gouthamgo/dsa/graphs/contributors"
