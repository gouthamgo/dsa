"""
Heap / Priority Queue - Code Templates
======================================

Python's `heapq` is a MIN-heap operating in-place on a plain list.
There is no max-heap - you get one by negating on the way in AND on the
way out. Forgetting either half of that negation is the classic bug.
"""

import heapq
from collections import Counter

# ============================================================================
# TEMPLATE 1: heapq Basics (min-heap, max-heap, tuples)
# ============================================================================

def min_heap_basics():
    """Core min-heap operations. Smallest element always sits at heap[0]."""
    heap = []

    heapq.heappush(heap, 5)             # O(log n) - sift up
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 3)

    smallest = heap[0]                  # O(1) peek - does NOT remove
    popped = heapq.heappop(heap)        # O(log n) - removes and returns 1

    # heapify turns an existing list into a heap IN PLACE, O(n) - much
    # cheaper than n pushes at O(n log n).
    nums = [9, 4, 7, 1, 8]
    heapq.heapify(nums)

    # Pop-then-push in one O(log n) pass (pushpop does push first):
    replaced = heapq.heapreplace(nums, 6)   # pop min, then push 6
    pushed = heapq.heappushpop(nums, 0)     # push 0, then pop min

    return smallest, popped, replaced, pushed


def max_heap_basics(nums):
    """
    Max-heap via the negation trick.

    Negate on push, negate again on pop. The heap stores -x, so the
    numerically smallest stored value is the largest real value.
    """
    max_heap = []

    for num in nums:
        heapq.heappush(max_heap, -num)      # NEGATE going in

    largest = -max_heap[0]                  # NEGATE when peeking too

    order = []
    while max_heap:
        order.append(-heapq.heappop(max_heap))   # NEGATE coming out

    return largest, order                   # order is descending


def heap_of_tuples(items):
    """
    Heaps compare tuples element by element, so element 0 is the priority.

    Include a tiebreaker (an index/counter) before any non-comparable payload,
    otherwise equal priorities make Python try to compare the payloads and
    raise TypeError.
    """
    heap = []
    for i, (priority, payload) in enumerate(items):
        heapq.heappush(heap, (priority, i, payload))    # i breaks ties safely

    return [heapq.heappop(heap)[2] for _ in range(len(heap))]


# ============================================================================
# TEMPLATE 2: Top K Elements
# ============================================================================

def top_k_frequent(nums, k):
    """
    The k most frequent values.

    Keep a MIN-heap capped at size k: the weakest survivor is always at the
    top, so a better candidate evicts it in O(log k).

    Time: O(n log k)   Space: O(n)
    """
    counts = Counter(nums)
    heap = []                               # holds (frequency, value)

    for value, freq in counts.items():
        heapq.heappush(heap, (freq, value))
        if len(heap) > k:
            heapq.heappop(heap)             # drop the least frequent so far

    return [value for freq, value in heap]


def top_k_builtin(nums, k):
    """Same thing with the library helper - O(n log k) under the hood."""
    counts = Counter(nums)
    return [value for value, freq in counts.most_common(k)]


def k_closest_points(points, k):
    """
    K points nearest the origin.

    Use squared distance - the ordering is identical and sqrt is wasted work.
    A MAX-heap of size k lets us evict the current farthest point.

    Time: O(n log k)   Space: O(k)
    """
    max_heap = []                           # stores (-dist, x, y)

    for x, y in points:
        dist = x * x + y * y
        heapq.heappush(max_heap, (-dist, x, y))     # NEGATE in
        if len(max_heap) > k:
            heapq.heappop(max_heap)         # pops the LARGEST real distance

    return [[x, y] for neg_dist, x, y in max_heap]


# ============================================================================
# TEMPLATE 3: K-th Largest / Smallest
# ============================================================================

def kth_largest(nums, k):
    """
    The k-th largest value.

    Maintain a MIN-heap of the k largest seen so far; its root is the answer.

    Time: O(n log k)   Space: O(k)
    """
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)             # evict the smallest of the k+1

    return heap[0]                          # smallest of the top k


def kth_smallest(nums, k):
    """Mirror image: a MAX-heap of size k, root is the k-th smallest."""
    max_heap = []

    for num in nums:
        heapq.heappush(max_heap, -num)      # NEGATE in
        if len(max_heap) > k:
            heapq.heappop(max_heap)         # evict the largest of the k+1

    return -max_heap[0]                     # NEGATE out


class KthLargestStream:
    """
    Streaming version: report the k-th largest after each new value.

    The heap never exceeds k elements, so add() is O(log k).
    """

    def __init__(self, k, nums):
        self.k = k
        self.heap = list(nums)
        heapq.heapify(self.heap)            # O(n)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# ============================================================================
# TEMPLATE 4: Merge K Sorted Lists / Arrays
# ============================================================================

def merge_k_sorted_arrays(arrays):
    """
    Merge k sorted arrays into one sorted array.

    Invariant: the heap holds one candidate per array - the smallest value
    not yet emitted. Whatever is at the heap root is globally next.

    Time: O(N log k), N = total elements   Space: O(k)
    """
    heap = []

    # Seed with the head of every non-empty array: (value, array_idx, pos).
    for arr_idx, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], arr_idx, 0))

    merged = []
    while heap:
        value, arr_idx, pos = heapq.heappop(heap)
        merged.append(value)

        # Refill from the SAME array the value came from.
        next_pos = pos + 1
        if next_pos < len(arrays[arr_idx]):
            heapq.heappush(heap, (arrays[arr_idx][next_pos], arr_idx, next_pos))

    return merged


class ListNode:
    """Minimal linked-list node for the merge-k-lists template."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_sorted_lists(lists):
    """
    Same idea over linked lists.

    The arr_idx in the tuple is a TIEBREAKER: without it, two equal .val
    entries would make Python compare ListNode objects and raise TypeError.

    Time: O(N log k)   Space: O(k)
    """
    heap = []

    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))

    dummy = ListNode()
    tail = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = node

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    tail.next = None                        # sever any stale tail pointer
    return dummy.next


# ============================================================================
# TEMPLATE 5: Two Heaps - Running Median
# ============================================================================

class MedianFinder:
    """
    Median of a stream, using two heaps that split the data in half.

        small = MAX-heap of the lower half (negated values)
        large = MIN-heap of the upper half

    Invariants: every value in `small` <= every value in `large`, and
    len(small) is either equal to or exactly one more than len(large).
    The median is then small's root, or the average of both roots.

    addNum: O(log n)   findMedian: O(1)
    """

    def __init__(self):
        self.small = []     # max-heap (store -value)
        self.large = []     # min-heap

    def addNum(self, num):
        # 1. Always push into small first...
        heapq.heappush(self.small, -num)                # NEGATE in

        # 2. ...then move small's max over to large, so ordering holds.
        heapq.heappush(self.large, -heapq.heappop(self.small))   # NEGATE out

        # 3. Rebalance if large grew bigger than small.
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]                       # odd count
        return (-self.small[0] + self.large[0]) / 2      # even count


# ============================================================================
# TEMPLATE 6: Heap-Based Scheduling / Simulation
# ============================================================================

def last_stone_weight(stones):
    """
    Repeatedly smash the two heaviest stones together.

    Textbook max-heap simulation: pop two, push the difference back if any.

    Time: O(n log n)   Space: O(n)
    """
    max_heap = [-s for s in stones]         # NEGATE every value going in
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        first = -heapq.heappop(max_heap)    # NEGATE out
        second = -heapq.heappop(max_heap)

        if first != second:
            heapq.heappush(max_heap, -(first - second))     # NEGATE back in

    return -max_heap[0] if max_heap else 0


def task_scheduler(tasks, n):
    """
    Least time to run all tasks with a cooldown of n between identical ones.

    Greedy: always run the most-frequent available task (max-heap), and park
    a just-run task in a cooldown queue holding (remaining_count, ready_time).

    Time: O(total_time)   Space: O(26)
    """
    from collections import deque

    counts = Counter(tasks)
    max_heap = [-c for c in counts.values()]    # NEGATE in
    heapq.heapify(max_heap)

    cooldown = deque()                          # (remaining_count, ready_time)
    time = 0

    while max_heap or cooldown:
        time += 1

        if max_heap:
            remaining = heapq.heappop(max_heap) + 1     # negative + 1 == one run
            if remaining < 0:                           # still work left
                cooldown.append((remaining, time + n))
        # else: nothing runnable, this tick is an idle slot

        # Anything whose cooldown expired becomes available again.
        if cooldown and cooldown[0][1] == time:
            heapq.heappush(max_heap, cooldown.popleft()[0])

    return time


def min_meeting_rooms(intervals):
    """
    Fewest rooms needed for a set of [start, end] meetings.

    Sort by start time; the heap holds the END times of in-progress meetings.
    Its root is the soonest a room frees up, so one comparison per meeting
    decides reuse-a-room vs open-a-new-one. Heap size = rooms in use.

    Time: O(n log n)   Space: O(n)
    """
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])
    end_times = []                          # min-heap of meeting end times

    for start, end in intervals:
        # The earliest-finishing meeting is already over -> reuse its room.
        if end_times and end_times[0] <= start:
            heapq.heappop(end_times)

        heapq.heappush(end_times, end)

    return len(end_times)                   # peak concurrent meetings


# ============================================================================
# TEMPLATE 7: Custom Priority Objects
# ============================================================================

class Task:
    """
    Wrap a payload and define __lt__ so heapq can order it directly.

    Cleaner than tuple-packing when the priority rule is non-trivial. Here
    higher `priority` wins, which turns the min-heap into a max-heap without
    negating anything.
    """

    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __lt__(self, other):
        # heapq only ever calls __lt__; reverse it for max-heap behaviour.
        return self.priority > other.priority


def run_by_priority(tasks):
    """Drain a heap of Task objects, highest priority first."""
    heap = list(tasks)
    heapq.heapify(heap)
    return [heapq.heappop(heap).name for _ in range(len(heap))]
