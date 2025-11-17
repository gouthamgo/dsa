# Heap / Priority Queue - Complete Guide

## 🎯 What is a Heap?

A binary tree where parent is always greater (max heap) or smaller (min heap) than children. Perfect for finding min/max quickly!

**Visual (Min Heap):**
```
        1
       / \
      3   2
     / \
    7   5

Smallest always at root!
```

## 🧠 Heap Operations

- **Insert**: O(log n)
- **Extract Min/Max**: O(log n)
- **Peek Min/Max**: O(1)
- **Heapify**: O(n)

## 🔑 Python Implementation

```python
import heapq

# Min heap (default in Python)
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

min_val = heapq.heappop(heap)  # Gets 1

# Max heap (negate values)
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
max_val = -heapq.heappop(max_heap)  # Gets 3
```

## 💡 When to Use Heaps

- ✅ Find K largest/smallest elements
- ✅ Merge K sorted lists
- ✅ Running median
- ✅ Top K frequent elements
- ✅ Scheduling/Priority tasks

## 🎨 Common Patterns

### 1. Top K Elements
```python
def topKFrequent(nums, k):
    from collections import Counter
    import heapq

    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
```

### 2. Kth Largest Element
```python
def findKthLargest(nums, k):
    import heapq
    return heapq.nlargest(k, nums)[-1]
```

### 3. Merge K Sorted Lists
```python
def mergeKLists(lists):
    import heapq
    heap = []

    # Initialize heap with first element of each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))

    dummy = ListNode()
    current = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next
```

## ⚡ Key Problems

**Easy:**
- Kth Largest Element in a Stream
- Last Stone Weight

**Medium:**
- Top K Frequent Elements ⭐
- Kth Largest Element in an Array
- Task Scheduler

**Hard:**
- Find Median from Data Stream
- Merge K Sorted Lists

## 💡 Min Heap vs Max Heap

- **Min Heap**: Parent ≤ Children (smallest at root)
- **Max Heap**: Parent ≥ Children (largest at root)

Python only has min heap by default.
For max heap: negate values!

Time: O(log n) for insert/extract
Space: O(n)

---
**Heaps are your friend for "K-th" and "Top K" problems!** 📊
