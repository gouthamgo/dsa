"""
Intervals - Code Templates
==========================

Reusable building blocks for interval problems: merging, inserting, overlap
tests, greedy removal, and room/resource counting.

--------------------------------------------------------------------------
CONVENTION USED IN THIS FILE
--------------------------------------------------------------------------
An interval is [start, end] and is treated as CLOSED unless a template says
otherwise, i.e. it contains both endpoints.

    Two closed intervals a and b overlap  <=>  a[0] <= b[1] and b[0] <= a[1]

Touching intervals like [1,3] and [3,5] therefore DO overlap (they share the
point 3). That is the right call for merging ranges.

Scheduling problems use HALF-OPEN intervals [start, end) instead: a meeting
that ends at 3 frees the room for one starting at 3, so [1,3] and [3,5] do
NOT conflict. Every template below states which convention it assumes; the
difference is always a single `<` vs `<=`, and it is the #1 source of
off-by-one bugs in this topic.
--------------------------------------------------------------------------
"""

import heapq


# ============================================================================
# TEMPLATE 1: The Overlap Test
# ============================================================================

def overlaps_closed(a, b):
    """
    Do closed intervals [a0,a1] and [b0,b1] share at least one point?

    Derivation: it is far easier to negate. They do NOT overlap when one ends
    strictly before the other starts:  a[1] < b[0] or b[1] < a[0].
    Negate that and you get the condition below.

    overlaps_closed([1,3], [3,5]) -> True   (they share the point 3)

    Time: O(1)
    """
    return a[0] <= b[1] and b[0] <= a[1]


def overlaps_half_open(a, b):
    """
    Do half-open intervals [a0,a1) and [b0,b1) share at least one point?

    Same derivation, strict inequalities. Use this for meetings/bookings.

    overlaps_half_open([1,3], [3,5]) -> False  (the 3 o'clock handoff is fine)

    Time: O(1)
    """
    return a[0] < b[1] and b[0] < a[1]


def intersection(a, b):
    """
    The overlapping part of two closed intervals, or None if disjoint.

    The intersection always runs from the LATER start to the EARLIER end.

    Time: O(1)
    """
    start = max(a[0], b[0])
    end = min(a[1], b[1])
    return [start, end] if start <= end else None


# ============================================================================
# TEMPLATE 2: Sort by Start, then Merge
# ============================================================================

def merge_intervals(intervals):
    """
    Merge all overlapping intervals. Closed convention: [1,3] + [3,5] = [1,5].

    Why sorting by start works: after sorting, any interval that overlaps the
    current one must overlap the MOST RECENT merged block, because everything
    earlier ends no later than that block does. So one backward look suffices.

    Time: O(n log n) for the sort, O(n) for the sweep
    Space: O(n) for the output
    """
    if not intervals:
        return []

    # Sort by start. Copy the pairs so we never mutate the caller's lists.
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [list(intervals[0])]

    for start, end in intervals[1:]:
        last = merged[-1]

        if start <= last[1]:
            # Overlaps (or touches) the block we are building — absorb it.
            # max() matters: the new interval may be fully NESTED inside the
            # block, e.g. [1,10] then [2,3]; taking end blindly would shrink it.
            last[1] = max(last[1], end)
        else:
            # Strictly after the block ends — start a new block.
            merged.append([start, end])

    return merged


# ============================================================================
# TEMPLATE 3: Insert Interval into a Sorted, Non-Overlapping List
# ============================================================================

def insert_interval(intervals, new_interval):
    """
    Insert into an already-sorted, already-merged list and re-merge.

    Three clean phases, no sorting needed — that is the whole point of this
    problem: O(n) instead of O(n log n). Closed convention.

    Time: O(n)
    Space: O(n)
    """
    result = []
    new = list(new_interval)  # local copy; we mutate it as we absorb overlaps
    i, n = 0, len(intervals)

    # Phase 1: everything that ends strictly BEFORE new starts — untouched.
    while i < n and intervals[i][1] < new[0]:
        result.append(intervals[i])
        i += 1

    # Phase 2: everything that starts at or before new's end overlaps it.
    # Widen `new` to swallow the whole run.
    while i < n and intervals[i][0] <= new[1]:
        new[0] = min(new[0], intervals[i][0])
        new[1] = max(new[1], intervals[i][1])
        i += 1

    result.append(new)  # place the (possibly widened) interval exactly once

    # Phase 3: everything that starts strictly AFTER new ends — untouched.
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


# ============================================================================
# TEMPLATE 4: Erase Overlapping Intervals (Greedy by End Time)
# ============================================================================

def erase_overlap_intervals(intervals):
    """
    Minimum number of intervals to REMOVE so the rest are non-overlapping.

    Sort by END time, not start. Exchange argument: among all intervals that
    could come next, the one finishing earliest leaves the most room for
    everything after it, so keeping it is never worse than any alternative.

    Uses the half-open convention — [1,2] and [2,3] can both be kept.

    Time: O(n log n)
    Space: O(1) beyond the sort
    """
    if not intervals:
        return 0

    intervals = sorted(intervals, key=lambda x: x[1])  # earliest finish first

    kept = 1
    last_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= last_end:
            # No conflict with the last kept interval — keep this one too.
            kept += 1
            last_end = end
        # else: it conflicts. Drop it. We never drop the previously kept one,
        # because that one ends no later than this one does.

    return len(intervals) - kept


def max_non_overlapping(intervals):
    """
    The flip side: the LARGEST set of mutually non-overlapping intervals.
    Same greedy, and it is exactly `n - erase_overlap_intervals(...)`.

    This is the classic activity-selection / "burst balloons with arrows"
    / "maximum number of meetings" answer.

    Time: O(n log n)
    Space: O(n) for the chosen list
    """
    if not intervals:
        return []

    intervals = sorted(intervals, key=lambda x: x[1])
    chosen = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] >= chosen[-1][1]:
            chosen.append(interval)

    return chosen


# ============================================================================
# TEMPLATE 5: Meeting Rooms I — Can One Person Attend All?
# ============================================================================

def can_attend_meetings(intervals):
    """
    True if no two meetings overlap. Half-open: back-to-back meetings are OK.

    After sorting by start, only ADJACENT pairs can conflict — if meeting i
    doesn't reach meeting i+1's start, it can't reach any later one either.

    Time: O(n log n)
    Space: O(1)
    """
    intervals = sorted(intervals, key=lambda x: x[0])

    for i in range(len(intervals) - 1):
        # Strict >: ending exactly when the next begins is not a conflict.
        if intervals[i][1] > intervals[i + 1][0]:
            return False

    return True


# ============================================================================
# TEMPLATE 6: Meeting Rooms II — Min-Heap of End Times
# ============================================================================

def min_meeting_rooms_heap(intervals):
    """
    Fewest rooms needed to hold all meetings. Half-open convention.

    Process meetings in start order; the heap holds the end times of the
    rooms currently in use, smallest (soonest to free up) on top. Only the
    soonest-freeing room can possibly be reused, so one peek decides it.

    Time: O(n log n)
    Space: O(n) for the heap
    """
    if not intervals:
        return 0

    intervals = sorted(intervals, key=lambda x: x[0])
    rooms = []  # min-heap of end times of in-use rooms

    for start, end in intervals:
        # If the earliest-ending meeting is already over, reuse its room.
        # >= because a room freed at exactly `start` is available now.
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)

        heapq.heappush(rooms, end)  # this meeting now occupies a room

    # The heap never shrank below the peak concurrency, so its final size
    # is the maximum number of simultaneously-occupied rooms.
    return len(rooms)


# ============================================================================
# TEMPLATE 7: Meeting Rooms II — Sweep Line / Chronological Ordering
# ============================================================================

def min_meeting_rooms_sweep(intervals):
    """
    Same answer, no heap: sort starts and ends into two independent lists and
    walk them with two pointers, tracking how many meetings are open.

    Sorting the endpoints apart from each other is legal because we only need
    the COUNT of concurrent meetings, never which meeting is in which room.

    Time: O(n log n)
    Space: O(n)
    """
    if not intervals:
        return 0

    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)

    rooms = 0
    max_rooms = 0
    s = e = 0

    while s < len(starts):
        if starts[s] < ends[e]:
            # A meeting begins before the next one ends → need another room.
            rooms += 1
            s += 1
            max_rooms = max(max_rooms, rooms)
        else:
            # A meeting ends first (or exactly at this start) → a room frees.
            # `<` above rather than `<=` is what makes back-to-back meetings
            # share one room.
            rooms -= 1
            e += 1

    return max_rooms


def min_meeting_rooms_events(intervals):
    """
    Sweep line phrased as +1/-1 events — generalises to "max overlap at any
    point" and to weighted variants (e.g. car pooling capacity).

    Sorting puts an end event (-1) before a start event (+1) at the same
    timestamp, because -1 < +1. That again encodes the half-open convention.

    Time: O(n log n)
    Space: O(n)
    """
    events = []
    for start, end in intervals:
        events.append((start, 1))   # +1 room in use
        events.append((end, -1))    # -1 room freed

    events.sort()

    active = 0
    peak = 0
    for _, delta in events:
        active += delta
        peak = max(peak, active)

    return peak


# ============================================================================
# TEMPLATE 8: Interval Intersection of Two Sorted Lists
# ============================================================================

def interval_intersections(a_list, b_list):
    """
    All overlapping pieces between two sorted, non-overlapping lists.

    Two pointers: compute the intersection of the current pair (Template 1),
    then advance whichever interval ENDS first — it can't intersect anything
    further along in the other list.

    Time: O(m + n)
    Space: O(m + n) for the output
    """
    result = []
    i = j = 0

    while i < len(a_list) and j < len(b_list):
        start = max(a_list[i][0], b_list[j][0])  # later start
        end = min(a_list[i][1], b_list[j][1])    # earlier end

        if start <= end:  # closed convention: a single shared point counts
            result.append([start, end])

        # Retire the one that finishes first.
        if a_list[i][1] < b_list[j][1]:
            i += 1
        else:
            j += 1

    return result


# ============================================================================
# TEMPLATE 9: Employee Free Time / Gaps Between Merged Intervals
# ============================================================================

def find_gaps(intervals):
    """
    The uncovered stretches between intervals, after merging.

    Merge first (Template 2), then every consecutive pair of merged blocks
    leaves exactly one gap between them.

    Time: O(n log n)
    Space: O(n)
    """
    merged = merge_intervals(intervals)

    gaps = []
    for i in range(len(merged) - 1):
        gap_start = merged[i][1]
        gap_end = merged[i + 1][0]
        if gap_start < gap_end:  # strict: zero-width gaps aren't free time
            gaps.append([gap_start, gap_end])

    return gaps


# ============================================================================
# QUICK DEMO
# ============================================================================

if __name__ == "__main__":
    print("overlap [1,3]&[3,5] closed:   ", overlaps_closed([1, 3], [3, 5]))      # True
    print("overlap [1,3]&[3,5] half-open:", overlaps_half_open([1, 3], [3, 5]))   # False
    print("intersection [1,5]&[3,8]:     ", intersection([1, 5], [3, 8]))         # [3,5]

    print("merge:                        ", merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print("merge nested:                 ", merge_intervals([[1, 10], [2, 3], [4, 5]]))   # [[1,10]]
    print("merge touching:               ", merge_intervals([[1, 4], [4, 5]]))            # [[1,5]]

    print("insert:                       ", insert_interval([[1, 3], [6, 9]], [2, 5]))
    print("insert swallowing:            ", insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))

    print("erase overlaps:               ", erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]))  # 1
    print("max non-overlapping:          ", max_non_overlapping([[1, 2], [2, 3], [3, 4], [1, 3]]))

    print("can attend:                   ", can_attend_meetings([[0, 30], [5, 10], [15, 20]]))  # False
    print("can attend back-to-back:      ", can_attend_meetings([[0, 5], [5, 10]]))             # True

    meetings = [[0, 30], [5, 10], [15, 20]]
    print("rooms (heap):                 ", min_meeting_rooms_heap(meetings))    # 2
    print("rooms (sweep):                ", min_meeting_rooms_sweep(meetings))   # 2
    print("rooms (events):               ", min_meeting_rooms_events(meetings))  # 2

    print("intersections:                ", interval_intersections(
        [[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
    print("gaps:                         ", find_gaps([[1, 3], [2, 6], [8, 10]]))  # [[6,8]]
