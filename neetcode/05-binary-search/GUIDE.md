# Binary Search - Complete Guide

## 🎯 What is Binary Search?

Search algorithm that finds target in **sorted** array by repeatedly dividing search space in half.

**Visual:**
```
Array: [1, 3, 5, 7, 9, 11, 13]
Target: 7

Step 1: Check middle (7) → Found! ✓

If not found, eliminate half:
- target < mid → search left half
- target > mid → search right half
```

## 🧠 Core Concept

Divide and conquer on **sorted** data.
- Each comparison eliminates half the remaining elements
- O(log n) time - MUCH faster than O(n)

For n=1,000,000:
- Linear search: 1 million comparisons
- Binary search: 20 comparisons! 🚀

## 🎨 Template

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

## 🔑 When to Use

- ✅ Array is sorted
- ✅ Find element in sorted data
- ✅ Find boundary/threshold
- ✅ "Minimize maximum" or "Maximize minimum"
- ✅ Search in rotated sorted array

## 💡 Variations

### 1. Find First Occurrence
### 2. Find Last Occurrence
### 3. Search Insert Position
### 4. Search in Rotated Array
### 5. Search in 2D Matrix

## ⚡ Key Problems

**Easy:**
- Binary Search ⭐
- Search Insert Position
- First Bad Version

**Medium:**
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array
- Koko Eating Bananas

**Hard:**
- Median of Two Sorted Arrays
- Split Array Largest Sum

## 💡 Pro Tips

1. Use `mid = left + (right - left) // 2` to avoid overflow
2. Decide on `left <= right` vs `left < right`
3. Watch for infinite loops
4. Draw it out!

Time: O(log n)
Space: O(1)

---
**Binary search is simple but tricky - practice the boundaries!** 🔍
