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

## 🧠 Core Technique: Sort!

**Almost always sort intervals first!**

```python
intervals.sort(key=lambda x: x[0])  # Sort by start time
```

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

### 3. Meeting Rooms
```python
def canAttendMeetings(intervals):
    intervals.sort()

    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i+1][0]:
            return False  # Overlap!

    return True
```

## 🔑 When to Use

- ✅ Calendar/scheduling problems
- ✅ Merging ranges
- ✅ Finding overlaps
- ✅ Resource allocation

## ⚡ Key Problems

**Medium:**
- Merge Intervals ⭐
- Insert Interval
- Non-overlapping Intervals
- Meeting Rooms II

**Hard:**
- Employee Free Time
- Minimum Number of Arrows to Burst Balloons

## 💡 Pro Tips

1. **Always sort first** (by start or end time)
2. **Draw timeline** to visualize
3. **Check edge cases**: adjacent, nested, no overlap
4. **Use sweep line** for complex problems

Time: O(n log n) for sorting
Space: O(n) for result

---
**Master interval merging - it's a top interview pattern!** 📅
