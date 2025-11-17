# Two Pointers - Complete Guide

## 🎯 What is this pattern?

Two Pointers is a technique where you use **two references** (pointers) to traverse data structures, typically arrays or strings. This pattern is incredibly powerful for optimizing brute force O(n²) solutions to O(n).

## 🧠 Core Concept

Instead of nested loops checking every pair, we use two pointers that move intelligently based on conditions.

**Visual:**
```
Array: [1, 2, 3, 4, 5, 6]
        ↑           ↑
      left        right
```

## 🎨 Types of Two Pointer Patterns

### Pattern 1: Opposite Direction (Left & Right)
Pointers start at opposite ends and move toward each other.

**Use when:** Array is sorted or you need to find pairs.

```
[1, 2, 3, 4, 5, 6]
 ↑              ↑
left          right

Move based on condition:
- If sum too small → left++
- If sum too large → right--
```

### Pattern 2: Same Direction (Slow & Fast)
Both pointers start at beginning, move at different speeds.

**Use when:** Removing duplicates, in-place modifications.

```
[1, 1, 2, 2, 3]
 ↑  ↑
 s  f  (slow, fast)

Fast explores, slow builds result
```

### Pattern 3: Sliding Window
Two pointers define a window that slides/expands/shrinks.

**Use when:** Finding subarrays/substrings with properties.

```
[a, b, c, d, e]
 ↑     ↑
left  right  (window: [a,b,c])
```

## 🔑 When to Use Two Pointers

Use this pattern when:
- ✅ Array/string is sorted
- ✅ Need to find pairs/triplets
- ✅ Need to reverse/palindrome check
- ✅ Remove duplicates in-place
- ✅ Container/area problems
- ✅ Partition problems

## 💡 Common Techniques

### Technique 1: Two Sum (Sorted Array)
```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need bigger sum
        else:
            right -= 1  # Need smaller sum

    return []
```

### Technique 2: Valid Palindrome
```python
def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
```

### Technique 3: Remove Duplicates
```python
def remove_duplicates(nums):
    if not nums:
        return 0

    slow = 0  # Position for unique elements

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1  # New length
```

## ⚡ Complexity

| Approach | Time | Space |
|----------|------|-------|
| Brute Force (nested loops) | O(n²) | O(1) |
| Two Pointers | O(n) | O(1) |

**Huge improvement!** n=1000: 1,000,000 ops → 1,000 ops

## 🎯 Problem Categories

### Easy
1. Valid Palindrome
2. Two Sum II (sorted array)
3. Remove Duplicates from Sorted Array
4. Move Zeroes

### Medium
5. 3Sum
6. Container With Most Water
7. Trapping Rain Water
8. Remove Nth Node From End

### Hard
9. Minimum Window Substring
10. Trapping Rain Water II

## 💡 Key Insights

1. **Sorted arrays** → Think two pointers!
2. **Move pointers intelligently** based on conditions
3. **In-place modifications** → Use slow/fast pattern
4. **Trade nested loops for smart pointer movement**

## 🚀 Next Steps

1. Study `template.py`
2. Open `visualization.html`
3. Start with Valid Palindrome
4. Progress through problems

---
**Master this pattern - it appears in 10-15% of interview questions!** 🎯
