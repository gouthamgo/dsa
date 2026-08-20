# Intervals - Complete Guide

## 🎯 What are Interval Problems?

Problems involving ranges/intervals of time, space, or values.

**Visual:**
```
Intervals: [[1,3], [2,6], [8,10]]

Timeline:
  1---3
   2------6
              8--10

Overlapping? Yes! [1,3] and [2,6]
```

## 🔍 Trigger Phrases

| Phrase in the problem | What it means |
|-----------------------|---------------|
| "meetings", "bookings", "calendar", "schedule" | Interval overlap / room counting |
| "merge overlapping" | Sort by start, sweep |
| "minimum number of rooms / platforms / servers" | Max concurrent overlap → heap or sweep line |
| "remove the fewest" | Greedy by earliest end time |
| "can one person attend all" | Pairwise overlap check after sorting |
| "free time", "gaps", "available slots" | Merge, then look between blocks |
| "burst all balloons with fewest arrows" | Interval scheduling in disguise |
| ranges given as `[start, end]` pairs | Almost certainly this pattern |

If the input is a list of pairs and the answer depends on how they line up on
a number line, you are in interval territory.

## 🧠 Core Technique: Sort!

**Almost always sort intervals first!**

```python
intervals.sort(key=lambda x: x[0])  # Sort by start time
```

### Sort by start, or sort by end?

This single choice decides most interval problems:

| Sort by | Use when | Why |
|---------|----------|-----|
| **start** | Merging, inserting, counting rooms | Guarantees any overlap involves the *most recent* block, so one backward look suffices |
| **end** | Keeping/removing the most intervals | The earliest finisher leaves the most room for everything after it |

**Sorting by duration is essentially never right.** It feels intuitive for
"fit the most meetings" but breaks: `[0,3], [4,7], [1,5]` — the shortest is
`[0,3]`… fine here, but `[0,10],[1,2],[3,4]` shows a short interval in a bad
position blocking nothing while a long one blocks everything. Earliest-end is
the provably correct rule.

## ⚠️ The Overlap Condition (state your convention!)

Two intervals `a = [a0, a1]` and `b = [b0, b1]`:

```
CLOSED intervals — endpoints included:
    overlap  ⟺  a0 <= b1  and  b0 <= a1
    [1,3] and [3,5]  ->  OVERLAP (they share the point 3)

HALF-OPEN intervals [start, end) — end excluded:
    overlap  ⟺  a0 <  b1  and  b0 <  a1
    [1,3] and [3,5]  ->  NO OVERLAP (the 3 o'clock handoff is fine)
```

**Derive it, don't memorise it.** It is much easier to write the *negation*:
they do NOT overlap when one ends before the other starts,
`a1 < b0 or b1 < a0`. Negate → the condition above.

**Which convention does each problem want?**

| Problem | Convention | Touching means |
|---------|-----------|----------------|
| Merge Intervals | closed | `[1,4]` + `[4,5]` = `[1,5]` — merge them |
| Insert Interval | closed | same |
| Meeting Rooms I / II | half-open | a meeting ending at 3 frees the room at 3 |
| Non-overlapping Intervals | half-open | `[1,2]` and `[2,3]` can both be kept |
| Min Arrows to Burst Balloons | closed | one arrow at `x` pops a balloon ending at `x` |

**This is the #1 bug in the topic.** The difference is always a single `<`
versus `<=`. Decide which convention the problem uses *before* you write the
comparison, and put it in a comment.

## 🎨 Common Patterns

### 1. Merge Overlapping Intervals
```python
def merge(intervals):
    intervals.sort()
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:  # Overlap
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged
```

Note the `max()`. The incoming interval may be entirely **nested** inside the
block you're building (`[1,10]` then `[2,3]`); assigning `last[1] = current[1]`
would shrink it.

### 2. Insert Interval
```python
def insert(intervals, newInterval):
    result = []
    i = 0

    # Add all before
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    result.append(newInterval)

    # Add remaining
    while i < len(intervals):
        result.append(intervals[i])
        i += 1

    return result
```

The whole point of this problem is that the input is **already sorted and
merged**, so you skip the sort and get O(n) instead of O(n log n).

### 3. Meeting Rooms
```python
def canAttendMeetings(intervals):
    intervals.sort()

    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i+1][0]:
            return False  # Overlap!

    return True
```

Only **adjacent** pairs need checking: if meeting `i` doesn't reach `i+1`'s
start, it can't reach any later one either.

### 4. Erase Overlapping Intervals (greedy by end time)
```python
def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])   # earliest FINISH first

    kept, last_end = 1, intervals[0][1]
    for start, end in intervals[1:]:
        if start >= last_end:            # half-open: touching is fine
            kept += 1
            last_end = end
        # else drop this one — never the previously kept one,
        # because that one ends no later than this one does

    return len(intervals) - kept
```

### 5. Meeting Rooms II — min-heap of end times
```python
import heapq

def minMeetingRooms(intervals):
    intervals.sort(key=lambda x: x[0])
    rooms = []                            # min-heap of end times in use

    for start, end in intervals:
        if rooms and rooms[0] <= start:   # soonest-freeing room is available
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)

    return len(rooms)                     # peak concurrency
```

### 6. Meeting Rooms II — sweep line / chronological ordering
```python
def minMeetingRooms(intervals):
    starts = sorted(i[0] for i in intervals)
    ends   = sorted(i[1] for i in intervals)

    rooms = max_rooms = 0
    s = e = 0
    while s < len(starts):
        if starts[s] < ends[e]:   # a meeting begins before one ends
            rooms += 1; s += 1
            max_rooms = max(max_rooms, rooms)
        else:                     # a room frees up
            rooms -= 1; e += 1

    return max_rooms
```

Sorting starts and ends **independently** is legal because we only need the
*count* of concurrent meetings, never which meeting is in which room.

## 🧭 Decision Guide

```
What is the question asking for?

"Combine / clean up the ranges"
    ──> sort by START, sweep, merge into the last block
        (Merge Intervals, Insert Interval, Employee Free Time)

"How many can I keep / how few must I remove?"
    ──> sort by END, greedily keep anything that fits
        (Non-overlapping Intervals, Min Arrows, Activity Selection)

"How many resources at once?"
    ──> max concurrent overlap
        ├── min-heap of end times          (easy to explain)
        └── sweep line with +1/-1 events   (generalises to weights)
        (Meeting Rooms II, Car Pooling, My Calendar III)

"Does ANY pair overlap?"
    ──> sort by START, check adjacent pairs only
        (Meeting Rooms I)

"Query against a set of intervals, many times"
    ──> sort + binary search, or a min-heap keyed by the query
        (Minimum Interval to Include Each Query)
```

## ⚡ Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| Sort | O(n log n) | O(n) (Python's Timsort) |
| Merge sweep (after sort) | O(n) | O(n) output |
| Insert Interval (pre-sorted input) | **O(n)** | O(n) |
| Erase overlapping | O(n log n) | O(1) extra |
| Meeting Rooms I | O(n log n) | O(1) extra |
| Meeting Rooms II (heap) | O(n log n) | O(n) |
| Meeting Rooms II (sweep) | O(n log n) | O(n) |
| Interval intersections (two sorted lists) | O(m + n) | O(m + n) |

**The sort dominates everything.** The interesting question in an interview is
usually "can you avoid the sort?" — and the answer is yes only when the input
arrives sorted (Insert Interval) or you can bucket by a bounded range.

## 🔬 Worked Example: Meeting Rooms II, Traced

```
intervals = [[0,30], [5,10], [15,20]]
```

**Timeline:**
```
0                          30
|===========================|      meeting A
      5    10
      |=====|                      meeting B
              15   20
              |====|               meeting C

At t=7:  A and B running     -> 2 rooms
At t=17: A and C running     -> 2 rooms
Peak = 2
```

**Heap approach, step by step** (sorted by start: `[0,30], [5,10], [15,20]`):

```
[0,30]:  heap is empty, nothing to reuse
         push 30                        heap = [30]        rooms = 1

[5,10]:  heap[0] = 30, is 30 <= 5?  NO  -> room A still busy at t=5
         push 10                        heap = [10, 30]    rooms = 2

[15,20]: heap[0] = 10, is 10 <= 15? YES -> meeting B is over, reuse its room
         pop 10                         heap = [30]
         push 20                        heap = [20, 30]    rooms = 2

Answer: len(heap) = 2 ✓
```

The heap never shrinks below the peak, so its final size *is* the answer.

**Sweep-line approach on the same input:**
```
starts = [0, 5, 15]
ends   = [10, 20, 30]

s=0,e=0:  0  < 10  -> rooms=1, max=1, s=1
s=1,e=0:  5  < 10  -> rooms=2, max=2, s=2
s=2,e=0:  15 < 10? NO -> a room frees, rooms=1, e=1
s=2,e=1:  15 < 20  -> rooms=2, max=2, s=3
s == len(starts), stop.

Answer: 2 ✓
```

Note the `<` rather than `<=` on line 3 of the loop: that is exactly what makes
a meeting ending at 15 release its room for one starting at 15.

## 🚨 Common Pitfalls

1. **The touching-interval off-by-one.** `[1,3]` and `[3,5]`: merge them
   (closed) or not (half-open)? Pick per problem, write it in a comment.

2. **Forgetting `max()` when extending a merged block.** Nested intervals
   (`[1,10]` then `[2,3]`) will silently truncate your result.

3. **Mutating the caller's input.** `merged = [intervals[0]]` stores a
   *reference*; `last[1] = ...` then edits the original list. Use
   `[list(intervals[0])]` if the input must survive.

4. **Sorting by start when the problem wants earliest-end greedy.** For
   Non-overlapping Intervals, sorting by start gives wrong answers on
   `[[1,100],[2,3],[3,4]]` — start-order keeps `[1,100]` and discards two.

5. **Empty input.** `intervals[0]` on `[]` raises. Guard at the top.

6. **Single-element input.** Loops like `range(len(intervals) - 1)` handle it
   fine, but `merged[-1]` patterns need the initial element to exist.

7. **In the heap solution, comparing against the wrong heap element.** You
   want `rooms[0]` (the *earliest* end), not `rooms[-1]`. `heapq` only
   guarantees index 0 is the minimum — the rest of the list is not sorted.

8. **Sweep-line with events: getting the tie order wrong.** Sorting
   `(time, delta)` tuples puts `-1` before `+1` at the same timestamp, which
   encodes "a room frees before the next meeting claims it" (half-open). If a
   problem wants closed semantics, flip the deltas' sort order.

9. **Assuming the input is sorted.** Only Insert Interval promises that. Sort
   defensively everywhere else.

## 🔑 When to Use

- ✅ Calendar/scheduling problems
- ✅ Merging ranges
- ✅ Finding overlaps
- ✅ Resource allocation

## ⚡ Key Problems

**Medium:**
- Merge Intervals ⭐ — sort by start, sweep; the archetype
- Insert Interval ⭐ — three-phase O(n) walk on pre-sorted input
- Non-overlapping Intervals ⭐ — greedy by earliest end time
- Meeting Rooms — pairwise adjacency check
- Meeting Rooms II ⭐ — max concurrency via heap or sweep line
- Interval List Intersections — two pointers over two sorted lists

**Hard:**
- Employee Free Time — flatten everyone's schedule, merge, read the gaps
- Minimum Number of Arrows to Burst Balloons — earliest-end greedy again
- Minimum Interval to Include Each Query — sort queries, min-heap by width

⭐ = must-know. Merge Intervals, Insert Interval, and Meeting Rooms II cover
the three mechanics (merge sweep, greedy by end, max concurrency) that every
other interval problem recombines.

## 💡 Pro Tips

1. **Always sort first** (by start or end time)
2. **Draw timeline** to visualize
3. **Check edge cases**: adjacent, nested, no overlap
4. **Use sweep line** for complex problems
5. **Write the overlap condition once, at the top, as a comment.** Half the
   bugs in this topic are a `<` that should have been a `<=`.
6. **The three configurations to test**: disjoint (`[1,2],[5,6]`), touching
   (`[1,3],[3,5]`), and nested (`[1,10],[2,3]`). If your code handles all
   three, it handles everything.

Time: O(n log n) for sorting
Space: O(n) for result

## 🚀 Next Steps

1. Study the `template.py` file — overlap test, merge, insert, greedy erase, both Meeting Rooms II approaches
2. Start with **Merge Intervals** (the pattern everything else builds on)
3. Then **Insert Interval** (same idea, but exploit the sorted input)
4. Then **Non-overlapping Intervals** (switch to sorting by end time)
5. Finish with **Meeting Rooms II** — implement it *both* ways, heap and sweep

---
**Master interval merging - it's a top interview pattern!** 📅
