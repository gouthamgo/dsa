"""
Greedy - Code Templates
=======================

Reusable building blocks for greedy problems: the general skeleton, running
maxima, reachability, cyclic scanning, and scheduling.

--------------------------------------------------------------------------
WHEN IS GREEDY ACTUALLY CORRECT?
--------------------------------------------------------------------------
Greedy is only valid when the problem has the GREEDY CHOICE PROPERTY: there
is always an optimal solution that agrees with the locally best choice.

The standard proof is an EXCHANGE ARGUMENT:
  1. Take any optimal solution OPT that differs from the greedy choice g.
  2. Swap g into OPT, evicting whatever OPT used instead.
  3. Show the result is still feasible and no worse.
  => Some optimal solution contains g, so taking g never costs you anything.

That argument works for interval scheduling by earliest end time (the earliest
finisher leaves the most room), for Kadane (a negative prefix can only hurt),
and for gas station (a failing start point can never be rescued).

It FAILS whenever a choice's cost depends on future choices in a way a single
swap cannot repair — coin change with coins [1, 3, 4] and target 6 (greedy
takes 4+1+1 = 3 coins, optimal is 3+3 = 2), 0/1 knapsack, longest increasing
subsequence, word break. Those need DP, which considers every choice instead
of committing to one.

Rule of thumb: if you cannot sketch the exchange argument in one sentence,
build a counterexample. If you cannot build a counterexample either, assume
DP is required and let the constraints (n <= 1000 hints O(n^2)) confirm it.
--------------------------------------------------------------------------
"""

from collections import Counter
import heapq


# ============================================================================
# TEMPLATE 1: The Greedy Skeleton
# ============================================================================

def greedy_skeleton(items, key=None):
    """
    The shape almost every greedy solution takes.

    Step 1: impose an order that makes the locally best choice obvious
            (by end time, by value, by deadline, by frequency, ...).
    Step 2: sweep once, committing to each item that is still feasible,
            never revisiting a decision.

    Time: O(n log n) dominated by the sort (O(n) if no sort is needed)
    Space: O(1) beyond the output
    """
    ordered = sorted(items, key=key) if key else sorted(items)

    chosen = []
    state = None  # whatever "where I am now" means — last end time, capacity...

    for item in ordered:
        if state is None or is_feasible(item, state):
            chosen.append(item)
            state = update(item, state)  # commit; never undo

    return chosen


def is_feasible(item, state):
    """Placeholder: can this item be taken given what we've committed to?"""
    return item >= state


def update(item, state):
    """Placeholder: fold the committed item into the running state."""
    return item


# ============================================================================
# TEMPLATE 2: Kadane's Algorithm (Maximum Subarray)
# ============================================================================

def max_subarray(nums):
    """
    Largest sum of any contiguous non-empty subarray.

    Greedy insight: a running sum that has gone negative can only drag down
    whatever comes next, so drop it and restart at the current element. That
    is the exchange argument — removing a negative prefix never hurts.

    Time: O(n)
    Space: O(1)
    """
    best = nums[0]      # best sum seen anywhere
    current = nums[0]   # best sum of a subarray ENDING at index i

    for num in nums[1:]:
        # Either extend the previous subarray, or start fresh at num.
        # max() here is exactly "if current < 0: current = 0" plus num.
        current = max(num, current + num)
        best = max(best, current)

    return best


def max_subarray_with_indices(nums):
    """
    Kadane's that also reports the winning range: (sum, start, end) inclusive.

    Time: O(n)
    Space: O(1)
    """
    best = current = nums[0]
    best_start = best_end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        if current < 0:
            # Restarting: the new candidate subarray begins here.
            current = nums[i]
            temp_start = i
        else:
            current += nums[i]

        if current > best:
            best = current
            best_start, best_end = temp_start, i

    return best, best_start, best_end


# ============================================================================
# TEMPLATE 3: Jump Game I — Can You Reach the End?
# ============================================================================

def can_jump(nums):
    """
    nums[i] = the max jump length from index i. Can you reach the last index?

    Track the furthest index reachable so far. If the scan ever stands on an
    index beyond that reach, there is a gap nothing can cross.

    Time: O(n)
    Space: O(1)
    """
    max_reach = 0

    for i, jump in enumerate(nums):
        if i > max_reach:
            return False  # unreachable gap — every earlier jump fell short
        max_reach = max(max_reach, i + jump)

    return True


def can_jump_backward(nums):
    """
    Same answer, scanned right-to-left: shrink the goal post.

    If index i can reach the current goal, then i becomes the new goal. If the
    goal walks all the way back to 0, the start reaches the end.

    Time: O(n)
    Space: O(1)
    """
    goal = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return goal == 0


# ============================================================================
# TEMPLATE 4: Jump Game II — Minimum Number of Jumps
# ============================================================================

def min_jumps(nums):
    """
    Fewest jumps to reach the last index (the input guarantees it is reachable).

    This is BFS on an implicit graph, done without a queue: [left, right] is
    the current "level" of indices reachable in `jumps` hops. Scan the level,
    compute the furthest reach, and that becomes the next level.

    Time: O(n)
    Space: O(1)
    """
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    left = right = 0  # window of indices reachable in exactly `jumps` steps

    while right < n - 1:
        farthest = 0
        for i in range(left, right + 1):
            farthest = max(farthest, i + nums[i])

        # Advance to the next BFS level. Every index in (right, farthest] is
        # reachable in jumps+1 steps and no fewer.
        left = right + 1
        right = farthest
        jumps += 1

    return jumps


def min_jumps_compact(nums):
    """
    The same O(n) algorithm written as a single pass.

    `current_end` is the boundary of the current level; hitting it means we
    must spend another jump. `farthest` accumulates the next boundary.

    Time: O(n)
    Space: O(1)
    """
    jumps = 0
    current_end = 0
    farthest = 0

    # Stop at n-2: standing ON the last index needs no further jump.
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        if i == current_end:      # exhausted the current level
            jumps += 1
            current_end = farthest

    return jumps


# ============================================================================
# TEMPLATE 5: Gas Station (Circular Scan)
# ============================================================================

def can_complete_circuit(gas, cost):
    """
    Index of the only viable starting station on a circular route, or -1.

    Two greedy facts:
      1. If total gas < total cost, no start works. Otherwise one always does.
      2. If you run dry somewhere between s and i, then NO station in [s, i]
         works either — each of them starts with a non-negative tank at s's
         position or later, so they reach i with no more fuel. Skip to i+1.

    Together those make one pass enough.

    Time: O(n)
    Space: O(1)
    """
    if sum(gas) < sum(cost):
        return -1  # fact 1

    start = 0
    tank = 0

    for i in range(len(gas)):
        tank += gas[i] - cost[i]

        if tank < 0:
            # Fact 2: everything in [start, i] is disqualified at once.
            start = i + 1
            tank = 0

    return start


# ============================================================================
# TEMPLATE 6: Partition Labels (Last-Occurrence Sweep)
# ============================================================================

def partition_labels(s):
    """
    Split s into the most parts such that each letter appears in only one part.

    Precompute each letter's last index. Sweep, extending the current part's
    end to the furthest last-occurrence seen. When the cursor reaches that
    end, nothing inside the part reappears later — cut here. Cutting at the
    earliest legal point maximises the number of parts.

    Time: O(n)
    Space: O(1) — at most 26 letters
    """
    last = {char: i for i, char in enumerate(s)}  # later writes win = last index

    result = []
    start = 0
    end = 0

    for i, char in enumerate(s):
        end = max(end, last[char])  # this part must stretch at least this far

        if i == end:
            result.append(end - start + 1)
            start = i + 1

    return result


# ============================================================================
# TEMPLATE 7: Task Scheduler (Most-Frequent-First)
# ============================================================================

def least_interval(tasks, n):
    """
    Minimum CPU slots to run all tasks with `n` idle slots between repeats.

    Closed form: the most frequent task defines a skeleton of
    (max_count - 1) frames of length (n + 1), plus one final frame holding
    every task that ties for max frequency.

        A _ _ A _ _ A        max_count=3, n=2  ->  (3-1)*(2+1) + 1 = 7

    Other tasks slot into the idle gaps for free — unless there are more tasks
    than gaps, in which case the schedule never idles and the answer is simply
    len(tasks). Hence the max().

    Time: O(n)
    Space: O(1) — 26 task types
    """
    counts = Counter(tasks)
    max_count = max(counts.values())
    # How many distinct tasks are tied at that frequency — each needs a slot
    # in the final frame.
    num_max = sum(1 for c in counts.values() if c == max_count)

    skeleton = (max_count - 1) * (n + 1) + num_max

    return max(skeleton, len(tasks))


def least_interval_heap(tasks, n):
    """
    Simulation variant: always run the most-frequent remaining task, parking
    it on a cooldown queue until its cooldown expires.

    Slower than the closed form but generalises to variable cooldowns and is
    easier to defend out loud.

    Time: O(T log 26) where T is the total number of slots
    Space: O(1)
    """
    counts = Counter(tasks)
    # Python's heapq is a MIN-heap, so negate counts to pop the largest.
    heap = [-c for c in counts.values()]
    heapq.heapify(heap)

    cooldown = []  # list of (ready_time, remaining_count)
    time = 0

    while heap or cooldown:
        time += 1

        # Release anything whose cooldown has elapsed.
        if cooldown and cooldown[0][0] == time:
            heapq.heappush(heap, heapq.heappop(cooldown)[1])

        if heap:
            remaining = heapq.heappop(heap) + 1  # one instance executed
            if remaining < 0:  # still has work left (values are negative)
                heapq.heappush(cooldown, (time + n + 1, remaining))
        # else: idle this slot, waiting on cooldowns

    return time


# ============================================================================
# TEMPLATE 8: Interval Scheduling by Earliest End Time
# ============================================================================

def max_activities(intervals):
    """
    Largest set of mutually non-overlapping intervals (activity selection).

    THE canonical greedy exchange argument: among all activities that can go
    next, the one that finishes earliest leaves the maximum remaining time,
    so swapping it into any optimal solution keeps that solution feasible and
    the same size. Sorting by START or by DURATION both fail — one long early
    activity can block many short ones.

    Half-open convention: [1,2] and [2,3] can both be selected.

    Time: O(n log n)
    Space: O(n) for the result
    """
    if not intervals:
        return []

    ordered = sorted(intervals, key=lambda x: x[1])  # earliest finish first

    chosen = [ordered[0]]
    last_end = ordered[0][1]

    for start, end in ordered[1:]:
        if start >= last_end:
            chosen.append([start, end])
            last_end = end

    return chosen


def min_arrows(points):
    """
    "Minimum Number of Arrows to Burst Balloons" — the same greedy, counting
    groups instead of picks. Shoot at the earliest end point; that arrow pops
    every balloon still open there.

    Balloons are CLOSED intervals here, so touching balloons share an arrow.

    Time: O(n log n)
    Space: O(1)
    """
    if not points:
        return 0

    ordered = sorted(points, key=lambda x: x[1])

    arrows = 1
    arrow_pos = ordered[0][1]

    for start, end in ordered[1:]:
        if start > arrow_pos:  # strict: start == arrow_pos is still hit
            arrows += 1
            arrow_pos = end

    return arrows


# ============================================================================
# TEMPLATE 9: Hand of Straights (Greedy from the Smallest Card)
# ============================================================================

def is_n_straight_hand(hand, group_size):
    """
    Can the hand be split into consecutive runs of length `group_size`?

    The smallest remaining card has no smaller partner, so it MUST begin a
    run — that forces the whole group and removes all choice.

    Time: O(n log n)
    Space: O(n)
    """
    if len(hand) % group_size != 0:
        return False

    counts = Counter(hand)
    # Min-heap so we always process the smallest surviving card first.
    heap = list(counts.keys())
    heapq.heapify(heap)

    while heap:
        smallest = heap[0]

        for card in range(smallest, smallest + group_size):
            if counts[card] == 0:
                return False  # the forced run is missing a card
            counts[card] -= 1
            if counts[card] == 0:
                # Only the current minimum can hit zero mid-run; if some
                # larger card ran out, the run above is already impossible.
                if card != heap[0]:
                    return False
                heapq.heappop(heap)

    return True


# ============================================================================
# QUICK DEMO
# ============================================================================

if __name__ == "__main__":
    print("max subarray:      ", max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))       # 6
    print("  with indices:    ", max_subarray_with_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # (6,3,6)
    print("all negative:      ", max_subarray([-3, -1, -2]))                          # -1

    print("can jump:          ", can_jump([2, 3, 1, 1, 4]))            # True
    print("can jump (blocked):", can_jump([3, 2, 1, 0, 4]))            # False
    print("can jump backward: ", can_jump_backward([3, 2, 1, 0, 4]))   # False
    print("min jumps:         ", min_jumps([2, 3, 1, 1, 4]))           # 2
    print("min jumps compact: ", min_jumps_compact([2, 3, 0, 1, 4]))   # 2

    print("gas station:       ", can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  # 3
    print("gas impossible:    ", can_complete_circuit([2, 3, 4], [3, 4, 3]))              # -1

    print("partition labels:  ", partition_labels("ababcbacadefegdehijhklij"))  # [9,7,8]

    print("task scheduler:    ", least_interval(["A", "A", "A", "B", "B", "B"], 2))       # 8
    print("  heap variant:    ", least_interval_heap(["A", "A", "A", "B", "B", "B"], 2))  # 8
    print("  no idling:       ", least_interval(["A", "A", "A", "B", "B", "B"], 0))       # 6

    print("max activities:    ", max_activities([[1, 3], [2, 4], [3, 5], [0, 6]]))
    print("min arrows:        ", min_arrows([[10, 16], [2, 8], [1, 6], [7, 12]]))  # 2

    print("straight hand:     ", is_n_straight_hand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))  # True
    print("straight hand bad: ", is_n_straight_hand([1, 2, 3, 4, 5], 4))              # False
