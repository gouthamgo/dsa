# Sliding Window - Complete Guide

## 🎯 What is Sliding Window?

A technique using two pointers to create a "window" that slides over data to find subarrays/substrings meeting certain criteria.

**Visual:**
```
Array: [1, 3, 2, 6, 4, 5]
        ↑     ↑
       left  right

Window = [1, 3, 2]  (sum = 6)

Slide right →
        [3, 2, 6]  (sum = 11)
```

## 🧠 Two Types

### Fixed Size Window
Window size stays constant - just slide!
```python
# Window of size k
for i in range(len(arr) - k + 1):
    window = arr[i:i+k]
```

### Variable Size Window
Window expands/shrinks based on condition
```python
left = 0
for right in range(len(arr)):
    # Expand window
    add arr[right]

    while condition_violated:
        # Shrink window
        remove arr[left]
        left += 1
```

## 🔑 When to Use

- ✅ Find longest/shortest substring
- ✅ Maximum/minimum in subarrays
- ✅ Contiguous subarray with condition
- ✅ Distinct characters problems

## 💡 Common Problems

**Easy:**
- Best Time to Buy and Sell Stock
- Maximum Average Subarray

**Medium:**
- Longest Substring Without Repeating Characters ⭐
- Longest Repeating Character Replacement
- Permutation in String

**Hard:**
- Minimum Window Substring
- Sliding Window Maximum

## ⚡ Template

```python
def sliding_window(arr):
    left = 0
    result = 0

    for right in range(len(arr)):
        # Expand: add arr[right]

        while window_invalid:
            # Shrink: remove arr[left]
            left += 1

        # Update result
        result = max(result, right - left + 1)

    return result
```

Time: O(n) - each element visited at most twice
Space: O(1) or O(k) for tracking window state

---
**Master this for substring/subarray problems!** 🪟
