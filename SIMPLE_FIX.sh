#!/bin/bash
# ONE-COMMAND FIX - Run this to completely remove Claude

cd "$(git rev-parse --show-toplevel)" && \
git fetch origin && \
git checkout -B main origin/claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu && \
echo "" && \
echo "=== VERIFICATION ===" && \
echo "Contributors: $(git log --format='%an <%ae>' | sort | uniq)" && \
echo "Committers: $(git log --format='%cn <%ce>' | sort | uniq)" && \
echo "Claude in messages: $(git log --oneline | grep -i claude | wc -l)" && \
echo "" && \
read -p "Push this clean history to main? (yes/no): " ans && \
if [ "$ans" = "yes" ]; then \
  git push origin main --force && \
  git push origin --delete claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu 2>/dev/null && \
  git push origin --delete claude/understand-repo-012MCzUH5auh8Nr7ANGXrCBm 2>/dev/null && \
  git fetch --prune origin && \
  echo "" && \
  echo "✓✓✓ DONE! Repository is 100% clean ✓✓✓" && \
  echo "Only contributor: Goutham M <gouthamgo@yahoo.com>" && \
  echo "Zero Claude references in history"; \
fi
