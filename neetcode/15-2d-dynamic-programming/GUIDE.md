# 2D Dynamic Programming - Complete Guide

## 🎯 What is 2D DP?

Dynamic programming where the state depends on **two** parameters, using a 2D table (matrix) to store subproblem solutions.

**Visual:**
```
dp[i][j] = solution for subproblem at position (i,j)

     j →
   0 1 2 3
i  -------
0| 1 1 1 1
1| 1 2 3 4
2| 1 3 6 10
↓
```

## 🧠 Common 2D DP Patterns

### Pattern 1: Grid/Matrix Path
```python
def uniquePaths(m, n):
    """How many ways to reach bottom-right from top-left?"""
    dp = [[0] * n for _ in range(m)]

    # Base: first row and column all = 1
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # Fill table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]
```

### Pattern 2: String Matching
```python
def longestCommonSubsequence(text1, text2):
    """LCS of two strings"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
```

### Pattern 3: Knapsack
```python
def knapsack(weights, values, capacity):
    """0/1 Knapsack problem"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                # Take or don't take
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],  # Take
                    dp[i-1][w]  # Don't take
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]
```

### Pattern 4: Edit Distance
```python
def minDistance(word1, word2):
    """Minimum edits to transform word1 → word2"""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete
                    dp[i][j-1],    # Insert
                    dp[i-1][j-1]   # Replace
                )

    return dp[m][n]
```

## ⚡ Key Problems

**Medium:**
- Unique Paths ⭐
- Longest Common Subsequence ⭐
- Longest Palindromic Substring
- Coin Change 2
- Target Sum

**Hard:**
- Edit Distance ⭐
- Regular Expression Matching
- Interleaving String
- Distinct Subsequences

## 🎨 2D DP Template

```python
def solve_2d_dp(input1, input2):
    m, n = len(input1), len(input2)

    # Create dp table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    # dp[0][...] and dp[...][0]

    # Fill table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Recurrence relation
            dp[i][j] = f(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]
```

## 💡 Space Optimization

Often can reduce from O(m×n) to O(n):

```python
def uniquePaths_optimized(m, n):
    """Use 1D array instead of 2D"""
    dp = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j-1]

    return dp[n-1]
```

## 🔑 When to Use 2D DP

- ✅ Two sequences/strings to compare
- ✅ Grid/matrix problems
- ✅ Knapsack-type problems
- ✅ State depends on two variables

## ⚡ Complexity

Time: O(m × n)
Space: O(m × n) or O(n) with optimization

---
**2D DP is challenging but powerful - visualize the table!** 📊
