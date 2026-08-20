"""
Problem: Find Minimum in Rotated Sorted Array
Difficulty: Medium
Topics: Array, Binary Search

Problem Statement:
-----------------
Suppose an array of length n sorted in ascending order (with DISTINCT
values) is rotated between 1 and n times. For example, the array
[0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2]   if it was rotated 4 times
    [0,1,2,4,5,6,7]   if it was rotated 7 times (back to the start)

Given the rotated sorted array nums, return the MINIMUM element of this
array.

You must write an algorithm that runs in O(log n) time.

Examples:
---------
Example 1:
    Input: nums = [3,4,5,1,2]
    Output: 1
    Explanation: The original array was [1,2,3,4,5], rotated 3 times.

Example 2:
    Input: nums = [4,5,6,7,0,1,2]
    Output: 0
    Explanation: The original array was [0,1,2,4,5,6,7], rotated 4 times.

Example 3:
    Input: nums = [11,13,15,17]
    Output: 11
    Explanation: Rotated a full n times, so it looks untouched.

Constraints:
-----------
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are UNIQUE
- nums is sorted and rotated between 1 and n times

LEARNING NOTES:
--------------
This is the PIVOT SEARCH hiding inside every rotated-array problem. 🔍

Key Insight: The minimum is the ONE element smaller than its neighbour —
the bottom of the "cliff". Find the cliff without scanning.

    Compare nums[mid] against nums[right]:

        nums[mid] > nums[right]
            The array must fall somewhere after mid, so the cliff (and
            therefore the minimum) is strictly to the RIGHT.
            → left = mid + 1        (mid is definitely NOT the answer)

        nums[mid] < nums[right]
            Everything from mid to right is already ascending, so the
            minimum is at mid or to its LEFT.
            → right = mid           (mid might BE the answer — keep it!)

    Stop when left == right. That single surviving index is the minimum.

Pattern: "Rotated sorted array" → Binary Search against the RIGHT endpoint.

Why compare to nums[right] and NOT nums[left]?
    nums[left] cannot tell a rotated array from an unrotated one. In
    [1,2,3,4,5], nums[mid] > nums[left] — the same signal you get from a
    genuinely rotated array — so you'd need an extra special case.
    nums[right] needs no special case at all.

Visualization:
    nums = [4, 5, 6, 7, 0, 1, 2]

    Step 1: left=0, right=6, mid=3 → nums[3]=7, nums[6]=2
        [ 4,  5,  6,  7,  0,  1,  2]
          L           M           R
        7 > 2 → the cliff is to the RIGHT → left = mid + 1 = 4

    Step 2: left=4, right=6, mid=5 → nums[5]=1, nums[6]=2
        [ 4,  5,  6,  7,  0,  1,  2]
                          L   M   R
        1 < 2 → [1,2] ascends → minimum is at mid or left → right = mid = 5

    Step 3: left=4, right=5, mid=4 → nums[4]=0, nums[5]=1
        [ 4,  5,  6,  7,  0,  1,  2]
                         LM   R
        0 < 1 → keep mid → right = mid = 4

    left == right == 4 → minimum is nums[4] = 0 ✅
"""


# ============================================================================
# SOLUTION 1: Binary Search vs. Right Endpoint (OPTIMAL!)
# ============================================================================

def findMin(nums):
    """
    Approach: Shrink a half-open style range until one candidate remains.

    Algorithm:
    1. left = 0, right = len(nums) - 1
    2. While left < right:                    (NOT <=, see below)
         a. mid = left + (right - left) // 2
         b. nums[mid] > nums[right] → minimum is right of mid → left = mid+1
         c. else                    → mid could be the min    → right = mid
    3. left == right → return nums[left]

    Boundary reasoning — the three rules that make this bug-free:
    - `while left < right`, not `<=`. We are converging on ONE surviving
      index, not testing each candidate. With `<=` and `right = mid` this
      loops forever.
    - `right = mid` (not mid - 1) because mid is still a live candidate.
    - `left = mid + 1` in the other branch guarantees progress. Since
      mid is rounded DOWN, mid can equal left, so the branch that moves
      `left` MUST use mid + 1 or the range would never shrink.

    Note there is no equality case: all values are distinct, so nums[mid]
    is never equal to nums[right] unless mid == right, which the loop
    condition already excludes.

    Time Complexity: O(log n) - the range halves every iteration
    Space Complexity: O(1) - two integers
    """
    if not nums:
        return None

    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            # [mid..right] contains a drop → minimum is strictly after mid
            left = mid + 1
        else:
            # [mid..right] is ascending → minimum is mid or before it
            right = mid

    return nums[left]


# ============================================================================
# SOLUTION 2: Binary Search vs. Left Endpoint + Early Exit
# ============================================================================

def findMin_leftcompare(nums):
    """
    Approach: Compare against nums[left], with a "already sorted" shortcut.

    Algorithm:
    1. result = nums[0]
    2. While left <= right:
         a. If nums[left] < nums[right]: the whole remaining range is
            sorted → nums[left] is the smallest here → record and STOP
         b. mid = left + (right - left) // 2
         c. result = min(result, nums[mid])   (mid is always a candidate)
         d. nums[mid] >= nums[left] → we're on the LEFT ramp, the cliff is
            further right → left = mid + 1
            else                    → we're already past the cliff →
            right = mid - 1
    3. Return result

    Note the extra machinery this shape requires: an explicit `result`
    running minimum AND the early-exit check. That is the price of
    comparing against the left endpoint. Solution 1 needs neither.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    if not nums:
        return None

    left = 0
    right = len(nums) - 1
    result = nums[0]

    while left <= right:
        # Shortcut: this stretch is already ascending → its first is smallest
        if nums[left] < nums[right]:
            result = min(result, nums[left])
            break

        mid = left + (right - left) // 2
        result = min(result, nums[mid])

        if nums[mid] >= nums[left]:
            left = mid + 1      # still on the high (left) ramp
        else:
            right = mid - 1     # already fell past the cliff

    return result


# ============================================================================
# SOLUTION 3: Binary Search on a Predicate (The general lens)
# ============================================================================

def findMin_predicate(nums):
    """
    Approach: Find the FIRST index where the predicate flips to True.

    Define P(i) = "nums[i] <= nums[n-1]".
    Across a rotated sorted array P looks like:

        [4, 5, 6, 7, 0, 1, 2]   with last = 2
         F  F  F  F  T  T  T
                     ↑ first True == the minimum

    P is MONOTONIC (false...false, true...true), which is the only thing
    binary search ever really needs. This is the "lower bound" template.

    Algorithm:
    1. last = nums[n-1], lo = 0, hi = n - 1
    2. While lo < hi:
         mid = lo + (hi - lo) // 2
         P(mid) true  → hi = mid       (mid may be the first True)
         P(mid) false → lo = mid + 1
    3. Return nums[lo]

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Why learn this framing: "binary search the flip point of a monotonic
    predicate" also solves First Bad Version, Koko Eating Bananas, and
    every "minimize the maximum" problem. The array is optional.
    """
    if not nums:
        return None

    last = nums[-1]
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if nums[mid] <= last:
            hi = mid            # predicate True → first True is at or left
        else:
            lo = mid + 1        # predicate False → first True is right

    return nums[lo]


# ============================================================================
# SOLUTION 4: Linear Scan (DON'T use! Just for learning)
# ============================================================================

def findMin_linear(nums):
    """
    Approach: Just look at everything and keep the smallest.

    Time Complexity: O(n) - Too slow! The problem demands O(log n).
    Space Complexity: O(1)

    Yes, `min(nums)` is one character shorter and equally rejected. 😱
    The point of the problem is to exploit the sorted-ness; scanning
    throws that information away.
    """
    if not nums:
        return None

    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num

    return smallest


# ============================================================================
# TEST CASES
# ============================================================================

def test():
    """Test all solutions"""

    test_cases = [
        ([3, 4, 5, 1, 2], 1),                     # classic example
        ([4, 5, 6, 7, 0, 1, 2], 0),               # rotated near the middle
        ([11, 13, 15, 17], 11),                   # ⭐ not rotated at all
        ([1], 1),                                  # single element
        ([2, 1], 1),                               # ⭐ two elements, rotated
        ([1, 2], 1),                               # ⭐ two elements, sorted
        ([5, 1, 2, 3, 4], 1),                      # ⭐ rotated by one
        ([2, 3, 4, 5, 1], 1),                      # ⭐ minimum at the end
        ([1, 2, 3, 4, 5], 1),                      # minimum at the front
        ([3, 1, 2], 1),                            # three elements, rotated
        ([2, 3, 1], 1),                            # three elements, rotated
        ([-5, -4, -3, -2, -1], -5),                # all negative, sorted
        ([-1, -5, -4, -3, -2], -5),                # all negative, rotated
        ([6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 1),      # even length, rotated
        (list(range(500, 1000)) + list(range(500)), 0),  # big, rotated
        ([], None),                                # empty (defensive)
    ]

    solutions = [
        ("Compare to Right (Optimal)", findMin),
        ("Compare to Left + early exit", findMin_leftcompare),
        ("Predicate / Lower Bound", findMin_predicate),
        ("Linear Scan", findMin_linear),
    ]

    for name, solution in solutions:
        print(f"\n{'='*50}")
        print(f"Testing: {name}")
        print('='*50)

        all_passed = True
        for i, (nums, expected) in enumerate(test_cases, 1):
            result = solution(nums.copy())
            is_correct = result == expected

            # Keep huge arrays readable in the output
            shown = nums if len(nums) <= 10 else \
                f"[{nums[0]}, {nums[1]}, ..., {nums[-1]}] (n={len(nums)})"

            status = "✅" if is_correct else "❌"
            print(f"Test {i}: {status} nums={shown} → {result} "
                  f"(expected {expected})")
            if not is_correct:
                all_passed = False

        if all_passed:
            print(f"\n🎉 All tests passed for {name}!")


# ============================================================================
# VISUAL DEMO
# ============================================================================

def visual_demo(nums):
    """
    Visual step-by-step demonstration of converging on the pivot
    """
    print(f"\n{'='*70}")
    print("VISUAL DEMO: Find Minimum in Rotated Sorted Array")
    print(f"Input: {nums}")
    print('='*70)

    if not nums:
        print("\nEmpty array → nothing to return")
        return

    width = max(len(str(n)) for n in nums) + 2
    row = "".join(f"{n:>{width}}" for n in nums)

    left = 0
    right = len(nums) - 1
    step = 1

    print("\nRule: compare nums[mid] with nums[right]")
    print("      bigger  → the cliff is to the RIGHT  (left = mid + 1)")
    print("      smaller → mid could be the minimum   (right = mid)\n")

    while left < right:
        mid = left + (right - left) // 2

        marks = []
        for i in range(len(nums)):
            tag = ""
            if i == left:
                tag += "L"
            if i == mid:
                tag += "M"
            if i == right:
                tag += "R"
            marks.append(f"{tag:>{width}}")

        print(f"Step {step}:")
        print(f"  {row}")
        print(f"  {''.join(marks)}")
        print(f"  left={left}, right={right}, mid={mid}")
        print(f"  nums[mid]={nums[mid]} vs nums[right]={nums[right]}")
        print(f"  Search space: {right - left + 1} element(s)")

        if nums[mid] > nums[right]:
            print(f"  {nums[mid]} > {nums[right]} → a drop lies after mid "
                  f"→ left = mid+1 = {mid + 1}")
            left = mid + 1
        else:
            print(f"  {nums[mid]} < {nums[right]} → [mid..right] ascends "
                  f"→ right = mid = {mid} (keep mid!)")
            right = mid

        step += 1
        print()

    # Show the single surviving index
    marks = []
    for i in range(len(nums)):
        marks.append(f"{('LR' if i == left else ''):>{width}}")
    print("Converged:")
    print(f"  {row}")
    print(f"  {''.join(marks)}")
    print(f"  left == right == {left}")
    print(f"  ✅ MINIMUM = nums[{left}] = {nums[left]} 🎯")


# ============================================================================
# WHAT YOU SHOULD LEARN
# ============================================================================

"""
KEY TAKEAWAYS:
-------------
1. The minimum IS the rotation pivot — the bottom of the single cliff.
2. Compare nums[mid] to nums[RIGHT], not nums[left]. The right endpoint
   distinguishes rotated from unrotated with zero special cases.
3. The `while left < right` + `right = mid` pairing is a different shape
   from the classic search. Learn it as its own template:
       - we are CONVERGING on one index, not testing candidates
       - never write `left = mid` here; mid rounds down → infinite loop
4. When the loop exits, left == right and that index is the answer.
5. Unrotated input falls out for free: nums[mid] < nums[right] every time,
   so right marches down to 0.

PATTERN RECOGNITION:
-------------------
When you see:
- "Rotated sorted array"
- "Find the pivot / rotation count"
- "Find the smallest element in O(log n)"
- Any monotonic predicate: F F F T T T → find the first T

Think: BINARY SEARCH CONVERGENCE (left < right, right = mid)!

Bonus: the index returned here is exactly the ROTATION COUNT of the array.

INTERVIEW TIPS:
--------------
1. Ask about duplicates. With duplicates (LeetCode 154) you must handle
   nums[mid] == nums[right] by doing `right -= 1`, and the worst case
   becomes O(n) — e.g. [1,1,1,0,1] cannot be split reliably.
2. Say why you compare to the right endpoint. That reason is the answer
   the interviewer is fishing for.
3. Trace [2,1] and [1,2] out loud. Two-element arrays kill wrong templates.
4. Point out that this pivot search is the first half of Search in
   Rotated Sorted Array — one insight, two problems.
5. Mention the predicate framing (Solution 3) if asked to generalize.

COMMON MISTAKES:
---------------
❌ `while left <= right` with `right = mid` → INFINITE LOOP.
❌ `left = mid` instead of `left = mid + 1` → INFINITE LOOP when the range
   has two elements (mid rounds down onto left).
❌ `right = mid - 1` in the descending branch → skips the true minimum.
   On [3,1,2] that returns 2 instead of 1.
❌ Comparing against nums[left] without an early-exit for sorted input →
   [11,13,15,17] wrongly walks right and returns 17.
❌ Returning the INDEX when the problem asks for the VALUE (or vice versa).

VARIATIONS:
----------
- Find Minimum in Rotated Sorted Array II (duplicates) → `right -= 1`
  on ties, O(n) worst case
- Search in Rotated Sorted Array → find this pivot, then search a half
- Find Peak Element → same convergence template, no sortedness needed
- First Bad Version → the purest form of "first True" binary search
- Koko Eating Bananas → binary search the ANSWER using a predicate

TIME COMPLEXITY COMPARISON:
--------------------------
Linear Scan:            O(n)     time, O(1) space
Left-compare + exit:    O(log n) time, O(1) space
Predicate/lower bound:  O(log n) time, O(1) space
Compare to right:       O(log n) time, O(1) space ← BEST (cleanest)!

NEXT STEPS:
----------
✅ Own the convergence template (left < right, right = mid)
✅ Understand monotonic predicates
→ Now try: Koko Eating Bananas (binary search on the answer space)
→ Then: Search a 2D Matrix, Time Based Key-Value Store

PRACTICE MORE:
-------------
Similar problems to practice this pattern:
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array II (duplicates)
- Find Peak Element
- First Bad Version
- Koko Eating Bananas
"""


if __name__ == "__main__":
    # Run tests
    test()

    # Visual demonstrations
    visual_demo([4, 5, 6, 7, 0, 1, 2])
    visual_demo([11, 13, 15, 17])

    # Interactive practice
    print("\n" + "="*70)
    print("YOUR TURN TO TRACE!")
    print("="*70)
    print("\nTry tracing through this example yourself:")
    print("nums = [7, 8, 9, 1, 2, 3, 4, 5, 6]")
    print("\nAt each step: does mid beat nums[right]? Where does left land?")
    print("Write it out, then run: visual_demo([7,8,9,1,2,3,4,5,6])")
