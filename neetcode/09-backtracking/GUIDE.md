# Backtracking - Complete Guide

## 🎯 What is Backtracking?

An algorithmic technique that builds solutions incrementally and abandons ("backtracks") when a solution can't be completed.

Think: **Try, check, undo, try again**

**Visual:**
```
Finding all subsets of [1,2,3]:

         []
       /  |  \
     [1] [2] [3]
     /|   |
[1,2][1,3]...

Try adding element → Recurse → Remove (backtrack)
```

## 🧠 Core Template

```python
def backtrack(path, choices):
    if is_solution(path):
        result.append(path.copy())
        return

    for choice in choices:
        # Make choice
        path.append(choice)

        # Recurse
        backtrack(path, new_choices)

        # Undo choice (BACKTRACK!)
        path.pop()
```

## 🔑 When to Use

- ✅ Find all combinations/permutations
- ✅ Solve puzzles (Sudoku, N-Queens)
- ✅ Generate all possibilities
- ✅ Constraint satisfaction problems

## 💡 Common Patterns

### 1. Subsets
```python
def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path.copy())

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # Backtrack!

    backtrack(0, [])
    return result
```

### 2. Permutations
```python
def permute(nums):
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path.copy())
            return

        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()

    backtrack([], nums)
    return result
```

### 3. Combination Sum
```python
def combinationSum(candidates, target):
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(path.copy())
            return
        if total > target:
            return  # Prune!

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return result
```

## ⚡ Key Problems

**Medium:**
- Subsets ⭐
- Permutations
- Combination Sum
- Letter Combinations of a Phone Number
- Palindrome Partitioning

**Hard:**
- N-Queens
- Sudoku Solver
- Word Search II

## 💡 Pro Tips

1. **Draw the decision tree**
2. **Prune early** to save time
3. **Remember to backtrack** (undo choice)
4. **Use `path.copy()`** when adding to result

Time: Often O(2ⁿ) or O(n!) - exponential!
Space: O(n) for recursion stack

---
**Backtracking is brute force done smart!** 🔄
