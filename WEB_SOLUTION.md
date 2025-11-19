# Web-Based Solution (No Local Git Required)

If you don't have Git installed locally or prefer to use GitHub's web interface, follow these steps:

## Step 1: Make 'claude/consolidate-single-branch' the default branch

1. Go to: https://github.com/gouthamgo/dsa/settings/branches
2. Under "Default branch", click the switch icon (⇄)
3. Select: `claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu`
4. Click "Update" and confirm

## Step 2: Delete the old 'main' branch

1. Go to: https://github.com/gouthamgo/dsa/branches
2. Find the "main" branch
3. Click the trash icon next to it to delete
4. Confirm deletion

## Step 3: Rename the clean branch to 'main'

1. Go back to: https://github.com/gouthamgo/dsa/settings/branches
2. Under "Default branch", you should see: `claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu`
3. Unfortunately, GitHub doesn't allow renaming via web UI, so you'll need to use their API or Git

### Using GitHub CLI (if available):
```bash
gh api repos/gouthamgo/dsa/branches/claude/consolidate-single-branch-015LKpc3cxcjM5G4Gydwy2cu/rename -f new_name=main
```

OR use the FINAL_FIX.sh script which does this automatically.

## Step 4: Delete all other branches

1. Go to: https://github.com/gouthamgo/dsa/branches
2. Delete each of these branches by clicking the trash icon:
   - `claude/understand-repo-012MCzUH5auh8Nr7ANGXrCBm`
   - `practise` (if you don't need it)
   - `problems` (if you don't need it)

## Step 5: Verify

1. Go to: https://github.com/gouthamgo/dsa/graphs/contributors
2. You should see ONLY: Goutham M
3. If you still see others, wait 24-48 hours for GitHub to recalculate

## Alternative: Use Codespaces (GitHub's built-in environment)

1. Go to: https://github.com/gouthamgo/dsa
2. Click the green "Code" button
3. Click "Codespaces" tab
4. Click "Create codespace on [current-branch]"
5. Once it opens, run in the terminal:
   ```bash
   chmod +x FINAL_FIX.sh
   ./FINAL_FIX.sh
   ```

This gives you a full Git environment without installing anything locally!
