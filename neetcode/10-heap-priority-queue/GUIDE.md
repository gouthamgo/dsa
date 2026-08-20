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

**Crucially, a heap is only *partially* ordered.** Every parent beats its
children, and that's the entire guarantee. `3` sits above `2`'s subtree and
nobody minds. This is why a heap gives you the min in O(1) but cannot give
you a sorted list without n pops — and why it's cheaper to build than a
sorted array.

**It's an array, not a tree.** The tree is imaginary; the data lives in a
flat list where the children of index `i` are at `2i+1` and `2i+2`:

```
        1                index:  0  1  2  3  4
       / \               array: [1, 3, 2, 7, 5]
      3   2                      ↑  ↑  ↑
     / \                     root  children of 0
    7   5                          children of 1 are at 3,4
```

That's why `heap[0]` is a valid O(1) peek, and why there is no pointer
chasing anywhere in `heapq`.

## 🧠 Heap Operations

- **Insert**: O(log n)
- **Extract Min/Max**: O(log n)
- **Peek Min/Max**: O(1)
- **Heapify**: O(n)

**Why insert is O(log n):** append to the end of the array, then *sift up* —
swap with the parent while you're smaller than it. The tree is complete, so
its height is ⌊log₂ n⌋, bounding the swaps.

**Why extract is O(log n):** the root is the answer; move the *last* element
into the root slot and *sift down*, swapping with the smaller child until
order is restored. Again bounded by the height.

**Why heapify is O(n), not O(n log n):** sifting down from the bottom up,
most nodes are near the leaves and barely move. Half the nodes are leaves
(0 work), a quarter move at most 1 level, and the sum ∑ n/2^k · k converges
to 2n. **Always prefer `heapify(list)` over n separate pushes.**

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

### The full `heapq` toolkit

```python
heapq.heapify(lst)              # O(n)      list → heap, in place
heapq.heappush(h, x)            # O(log n)
heapq.heappop(h)                # O(log n)  removes & returns smallest
h[0]                            # O(1)      peek, does NOT remove
heapq.heapreplace(h, x)         # O(log n)  pop THEN push  (h must be non-empty)
heapq.heappushpop(h, x)         # O(log n)  push THEN pop  (cheaper if x is small)
heapq.nlargest(k, iterable)     # O(n log k)
heapq.nsmallest(k, iterable)    # O(n log k)
```

`heapreplace` and `heappushpop` differ in order and therefore in result —
`heappushpop(h, 0)` on a min-heap just returns 0 straight back, while
`heapreplace(h, 0)` returns the old root.

**There is no `remove(x)`** and no `decrease-key`. If you need to invalidate
an entry, use the *lazy deletion* trick: keep a `set` of stale items and pop
past them when they surface at the root.

### Ordering tuples

Heaps compare tuples element by element, so element 0 is the priority:

```python
heapq.heappush(heap, (priority, index, payload))
```

The **middle tiebreaker is not decoration**. If two entries have equal
priority, Python moves on to compare element 1 — and if that's a `ListNode`
or a dict, you get `TypeError: '<' not supported`. A monotonically
increasing counter or list index makes ties resolve safely and
deterministically.

## 💡 When to Use Heaps

- ✅ Find K largest/smallest elements
- ✅ Merge K sorted lists
- ✅ Running median
- ✅ Top K frequent elements
- ✅ Scheduling/Priority tasks

### Trigger phrases in the problem statement

| You read this... | Reach for a heap |
|---|---|
| "**K**-th largest / smallest" | size-k heap |
| "**top K** / K most frequent / K closest" | size-k heap |
| "find the median of a **stream**" | two heaps |
| "merge K sorted lists/arrays" | heap of k list heads |
| "repeatedly take the largest/smallest, then..." | max/min-heap simulation |
| "schedule tasks by priority" | priority queue |
| "minimum number of rooms / platforms / CPUs" | heap of end times |
| "next element in a **stream**" (unbounded input) | heap, not sorting |

**Heap vs sorting.** Sorting everything is O(n log n) and answers *all*
ranking questions. A size-k heap is O(n log k) and answers only the top-k
question. When k ≪ n that's a real win — and when the input is a *stream*
with no known end, sorting isn't even available. If you need the full order
anyway, just sort.

**Heap vs Quickselect.** For a one-shot "k-th largest" on an in-memory array,
Quickselect is O(n) average and beats the heap's O(n log k). The heap wins on
streams, on repeated queries, and on being much easier to write correctly.

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

### 4. The size-k heap — and which direction it goes

This is the pattern that trips everyone up, so learn the rule:

> **For the K LARGEST, use a MIN-heap. For the K SMALLEST, use a MAX-heap.**

It feels backwards, and here's why it isn't. You keep exactly k survivors.
You need cheap access to **the weakest survivor**, because that's the one a
new candidate must beat. For "k largest", the weakest survivor is the
*smallest* of them — so it must be at the root — so you need a min-heap.

```python
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)   # evict the weakest
return heap[0]                # k-th largest = smallest survivor
```

### 5. Two heaps — running median

Split the data down the middle and keep each half in a heap facing inward,
so both middle elements sit at the two roots:

```
    small (MAX-heap)          large (MIN-heap)
   lower half                upper half
        [1, 2, 3]                [4, 5, 6]
              ↑                   ↑
           root=3              root=4
                  median = (3+4)/2
```

**Invariants:** every value in `small` ≤ every value in `large`, and
`len(small)` equals `len(large)` or exceeds it by exactly one.

The bulletproof `addNum` is three unconditional lines — push into `small`,
immediately move `small`'s max into `large` (this is what enforces the
ordering), then rebalance if `large` got bigger:

```python
heapq.heappush(small, -num)
heapq.heappush(large, -heapq.heappop(small))
if len(large) > len(small):
    heapq.heappush(small, -heapq.heappop(large))
```

No `if num < small[0]` comparison needed, and no edge case for the first
insertion. `findMedian` is then `-small[0]` when sizes differ, else the
average of the two roots.

### 6. Interval scheduling — heap of end times

For "minimum meeting rooms", sort by start time and keep a min-heap of the
**end** times of in-progress meetings. The root is the soonest a room frees:

```
meetings: [0,30] [5,10] [15,20]   sorted by start

[0,30]  → heap empty          → new room   heap=[30]
[5,10]  → root 30 > 5, busy   → new room   heap=[10,30]
[15,20] → root 10 ≤ 15, free! → reuse      heap=[20,30]

answer = len(heap) = 2
```

The heap size *is* the number of concurrent meetings.

## ⚡ Complexity Analysis

| Operation / Pattern | Time | Space |
|---|---|---|
| push / pop | O(log n) | O(1) |
| peek `heap[0]` | O(1) | O(1) |
| `heapify(list)` | O(n) | O(1) in place |
| build by n pushes | O(n log n) | O(n) |
| Top K / K-th largest (size-k heap) | O(n log k) | O(k) |
| `nlargest(k, ...)` | O(n log k) | O(k) |
| Top K by sorting | O(n log n) | O(n) |
| Merge K sorted lists (N total) | O(N log k) | O(k) |
| Running median: add / query | O(log n) / O(1) | O(n) |
| Heapsort (n pops) | O(n log n) | O(1) extra |
| Task Scheduler | O(total time) | O(26) |

Note the heap in "merge K lists" holds **k** items, not N — that's the whole
trick, and why the log factor is log k rather than log N.

## 🐛 Common Pitfalls

1. **Negating on push but not on pop** (or vice versa). The single most
   common heap bug. Max-heap values must be negated on the way in **and**
   on the way out, including at `heap[0]` peeks:
   ```python
   heapq.heappush(h, -x)
   biggest = -h[0]           # ✅ negate the peek too
   biggest = -heapq.heappop(h)
   ```

2. **Getting the size-k direction backwards.** Min-heap for k *largest*. See
   pattern 4 above; if your answer is off, this is the first thing to check.

3. **`TypeError: '<' not supported between instances of X and X`.** Two
   entries tied on priority and Python tried to compare the payloads. Insert
   a counter as a tiebreaker: `(priority, counter, payload)`.

4. **Assuming the heap list is sorted.** `heap[1]` is *not* the second
   smallest. Only `heap[0]` means anything. Printing a heap for debugging
   shows a jumble and that's correct.

5. **Using n pushes when `heapify` would do.** O(n log n) instead of O(n),
   for no reason, when you already have the whole list.

6. **Calling `heapreplace` on an empty heap.** It raises `IndexError` —
   unlike `heappushpop`, which is safe on an empty heap.

7. **Mutating an item already in the heap.** Changing a value in place does
   not re-sift it; the heap invariant silently breaks. Push a new entry and
   lazily discard the stale one.

8. **Negating an entire tuple wrong.** `(-freq, value)` flips only the
   frequency; `value` still sorts ascending. Be deliberate about which
   fields you're reversing.

9. **Forgetting floats in the median.** `(a + b) / 2` in Python 3 gives a
   float, which is what's wanted — but `//` would silently truncate.

## 🔬 Worked Example: K-th Largest of [3,2,1,5,6,4], k=2

Keep a **min-heap of size 2** — the two largest seen so far.

```
num=3  push → [3]                    size 1, under k
num=2  push → [2,3]                  size 2, at k
num=1  push → [1,2,3]  size 3 > 2 → pop 1  → [2,3]
       (1 was the weakest; it can never be top-2)
num=5  push → [2,3,5]  size 3 > 2 → pop 2  → [3,5]
num=6  push → [3,5,6]  size 3 > 2 → pop 3  → [5,6]
num=4  push → [4,5,6]  size 3 > 2 → pop 4  → [5,6]

heap[0] = 5   ← 2nd largest ✅
```

At every step the heap holds exactly the top-2 so far, and its root is the
smaller of the two — i.e. the answer. Six elements, six pushes, four pops,
each O(log 2). Compare with sorting all six to read `sorted[-2]`.

**Now trace the max-heap version wrong on purpose** to see pitfall 1:

```python
heapq.heappush(h, -num)      # negated in
...
return h[0]                  # ☠️ forgot to negate — returns -6, not 6
```

The value is right, the sign is wrong, and the bug survives every test where
the answer happens to be 0.

## ⚡ Min Heap vs Max Heap — quick reference

| Want | Structure | Push | Peek/Pop |
|---|---|---|---|
| smallest overall | min-heap | `heappush(h, x)` | `h[0]` / `heappop(h)` |
| largest overall | max-heap | `heappush(h, -x)` | `-h[0]` / `-heappop(h)` |
| k largest | min-heap of size k | `heappush(h, x)` then evict | `h[0]` = k-th largest |
| k smallest | max-heap of size k | `heappush(h, -x)` then evict | `-h[0]` = k-th smallest |

Python only has min heap by default.
For max heap: negate values!

A cleaner alternative to negating: define `__lt__` on a wrapper class and
reverse the comparison. Worth it when the priority rule is complex or the
values aren't numbers (strings can't be negated at all).

Time: O(log n) for insert/extract
Space: O(n)

## 📝 Problems in This Category

### Easy
1. **Kth Largest Element in a Stream** ⭐ — the size-k min-heap in its purest
   form. Start here.
2. **Last Stone Weight** — max-heap simulation; pop two, push the difference.

### Medium
3. **Kth Largest Element in an Array** ⭐ — same as #1 without the stream;
   compare your heap solution against Quickselect.
4. **K Closest Points to Origin** ⭐ — size-k max-heap on squared distance
   (never call `sqrt`, the ordering is identical).
5. **Task Scheduler** — greedy + max-heap + a cooldown queue.
6. **Design Twitter** — merge k sorted feeds; the merge-k pattern in disguise.

Also classic here: **Top K Frequent Elements** (listed under Arrays &
Hashing, but the heap solution is the canonical one).

### Hard
7. **Find Median from Data Stream** ⭐ — the two-heaps pattern. The single
   highest-value problem in this topic; interviewers love it.

Merge K Sorted Lists lives under Linked Lists but belongs to this pattern
family — do it here.

**Suggested order:** Kth Largest in a Stream → Last Stone Weight → Kth
Largest in an Array → K Closest Points → Top K Frequent → Task Scheduler →
Find Median from Data Stream.

## 🚀 Next Steps

1. Study `template.py` — all seven patterns
2. Say the min/max rule out loud until it sticks: *k largest → min-heap*
3. Solve Kth Largest in a Stream, then K Closest Points
4. Finish with Find Median from Data Stream

---
**Heaps are your friend for "K-th" and "Top K" problems!** 📊
