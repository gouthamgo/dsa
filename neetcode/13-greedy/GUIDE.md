# Greedy Algorithms - Complete Guide

## 🎯 What is Greedy?

Make the locally optimal choice at each step, hoping to find a global optimum.

**Think:** "What's the best choice RIGHT NOW?"

**Visual:**
```
Coin change: Make 67 cents
Coins: [25, 10, 5, 1]

Greedy approach:
1. Take 25 (largest) → 42 left
2. Take 25 → 17 left
3. Take 10 → 7 left
4. Take 5 → 2 left
5. Take 1 → 1 left
6. Take 1 → 0 left

Total: 6 coins ✓
```

## 🧠 When Greedy Works

Greedy works when problem has:
1. **Greedy choice property**: Local optimum → global optimum
2. **Optimal substructure**: Optimal solution contains optimal subsolutions

## 🔑 Common Greedy Patterns

### 1. Activity Selection
```python
def maxMeetings(intervals):
    # Sort by end time
    intervals.sort(key=lambda x: x[1])

    count = 1
    last_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= last_end:
            count += 1
            last_end = end

    return count
```

### 2. Jump Game
```python
def canJump(nums):
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])

    return True
```

### 3. Gas Station
```python
def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    tank = 0
    start = 0

    for i in range(len(gas)):
        tank += gas[i] - cost[i]

        if tank < 0:
            start = i + 1
            tank = 0

    return start
```

## ⚡ Key Problems

**Medium:**
- Jump Game ⭐
- Jump Game II
- Gas Station
- Hand of Straights
- Partition Labels

**Hard:**
- Merge Triplets to Form Target
- Valid Parenthesis String

## 💡 Greedy vs DP

**Greedy**: Make best local choice
- Faster: O(n) or O(n log n)
- Simpler code
- Doesn't always work!

**DP**: Consider all choices
- Slower: O(n²) or more
- Always correct
- More complex

## 🎨 How to Identify Greedy

Look for:
- ✅ "Maximum/Minimum number of..."
- ✅ Scheduling/interval problems
- ✅ Sorting helps
- ✅ Simple, intuitive optimal choice

## 💡 Pro Tips

1. **Try sorting first** (by start, end, value, etc.)
2. **Prove greedy works** before implementing
3. **If greedy fails, try DP**
4. **Draw examples** to verify

Time: Usually O(n) or O(n log n)
Space: Usually O(1)

---
**Greedy is simple and fast when it works!** 🎯
