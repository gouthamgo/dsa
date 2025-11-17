# 1D Dynamic Programming - Complete Guide

## 🎯 What is Dynamic Programming?

An optimization technique that solves complex problems by breaking them into simpler subproblems and **storing results** to avoid redundant calculations.

**Key Idea:** Remember the past to solve the future!

## 🧠 Core Concepts

### Memoization (Top-Down)
Start from main problem, recurse down, cache results.

```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

### Tabulation (Bottom-Up)
Start from base cases, build up to answer.

```python
def fib(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

## 🎨 DP Problem-Solving Steps

1. **Define state**: What does dp[i] represent?
2. **Find recurrence**: How does dp[i] relate to previous states?
3. **Base cases**: Initialize starting values
4. **Order**: What order to fill the table?
5. **Answer**: Where is final answer?

## 💡 Classic 1D DP Problems

### 1. Climbing Stairs
```python
def climbStairs(n):
    """How many ways to climb n stairs? (1 or 2 steps at a time)"""
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]  # 1 step or 2 steps

    return dp[n]
```

### 2. House Robber
```python
def rob(nums):
    """Rob houses, can't rob adjacent. Max money?"""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        # Rob current + i-2, or skip current
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])

    return dp[-1]
```

### 3. Longest Increasing Subsequence
```python
def lengthOfLIS(nums):
    """Find length of longest increasing subsequence"""
    if not nums:
        return 0

    dp = [1] * len(nums)  # Each element is subsequence of length 1

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
```

### 4. Coin Change
```python
def coinChange(coins, amount):
    """Minimum coins to make amount"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```

## ⚡ Key Problems

**Easy:**
- Climbing Stairs ⭐
- Min Cost Climbing Stairs
- Fibonacci Number

**Medium:**
- House Robber ⭐
- Longest Increasing Subsequence
- Coin Change
- Word Break
- Decode Ways

**Hard:**
- House Robber II
- Maximum Product Subarray

## 🔑 When to Use DP

Look for:
- ✅ "Count number of ways..."
- ✅ "Minimum/Maximum value..."
- ✅ Overlapping subproblems
- ✅ Optimal substructure

## 💡 DP vs Recursion

**Plain Recursion**: Recalculates same subproblems
```
fib(5) calls fib(4) and fib(3)
fib(4) calls fib(3) and fib(2)
fib(3) called TWICE! ❌
```

**DP**: Calculate each subproblem ONCE
```
fib(3) calculated once, stored ✓
Reuse when needed
```

## ⚡ Complexity

Time: Usually O(n) or O(n²)
Space: O(n) for dp array

**Space Optimization**: Often can use O(1) by keeping only last few states!

```python
def fib(n):
    """O(1) space!"""
    if n <= 1:
        return n

    prev2, prev1 = 0, 1

    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1
```

---
**DP is hard but essential - practice the patterns!** 🧩
