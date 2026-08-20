"""
Problem: Binary Search
Difficulty: Easy
Topics: Array, Binary Search

Problem Statement:
-----------------
Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search for target in nums. If target
exists, return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Examples:
---------
Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4.

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums, so we return -1.

Example 3:
    Input: nums = [5], target = 5
    Output: 0

Constraints:
-----------
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are UNIQUE
- nums is sorted in ascending order

LEARNING NOTES:
--------------
This is THE foundation problem. Every other binary search is a twist on
these ten lines — get the boundaries perfect here. 🔍

Key Insight: Each comparison ELIMINATES HALF the search space.
    Because the array is sorted, one look at the middle tells you which
    half can possibly contain the target. Throw the other half away.

    For n = 1,000,000:
        Linear search: up to 1,000,000 comparisons
        Binary search: 20 comparisons 🚀

Pattern: "Sorted array + find something" → Binary Search!

The three rules that prevent every classic bug:
    1. mid = left + (right - left) // 2   (overflow-safe idiom)
    2. `while left <= right` pairs with `mid ± 1` updates
    3. Every branch must SHRINK the range, or you get an infinite loop

Visualization:
    nums = [-1, 0, 3, 5, 9, 12], target = 9

    Step 1: left=0, right=5, mid=2 → nums[2]=3
        [-1,  0,  3,  5,  9, 12]
          L       M           R
        3 < 9 → target is to the RIGHT → left = mid+1 = 3

    Step 2: left=3, right=5, mid=4 → nums[4]=9
        [-1,  0,  3,  5,  9, 12]
                      L   M   R
        9 == 9 → FOUND at index 4 ✅

    Two comparisons instead of five. That gap explodes as n grows.
"""


# ============================================================================
# SOLUTION 1: Iterative Binary Search (OPTIMAL!)
# ============================================================================

def search(nums, target):
    """
    Approach: Shrink an inclusive range [left, right] until it's empty.

    Algorithm:
    1. left = 0, right = len(nums) - 1  (both ends INCLUSIVE)
    2. While left <= right:
         a. mid = left + (right - left) // 2
         b. nums[mid] == target → return mid
         c. nums[mid] <  target → answer is right of mid → left = mid + 1
         d. nums[mid] >  target → answer is left of mid  → right = mid - 1
    3. Loop ended → target is not present → return -1

    Boundary reasoning (memorize this pairing):
    - The range is INCLUSIVE on both sides, so `left == right` is still a
      real candidate → the condition must be `<=`, not `<`.
    - mid is already ruled out when we move, so we use mid + 1 / mid - 1.
      Using `left = mid` instead would loop forever when right == left + 1.

    Time Complexity: O(log n) - the range halves every iteration
    Space Complexity: O(1) - three integer variables, no recursion
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        # Overflow-safe midpoint (matters in C++/Java; a good habit anywhere)
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1     # discard mid and everything left of it
        else:
            right = mid - 1    # discard mid and everything right of it

    return -1


# ============================================================================
# SOLUTION 2: Recursive Binary Search (Same logic, different shape)
# ============================================================================

def search_recursive(nums, target):
    """
    Approach: The same halving, expressed as recursion on [left, right].

    Algorithm:
    1. Base case: left > right → the range is empty → return -1
    2. Compute mid, compare
    3. Recurse into whichever half can still contain the target

    Time Complexity: O(log n) - one comparison per level
    Space Complexity: O(log n) - the call stack holds one frame per level

    Trade-off: reads beautifully, but uses stack space the iterative
    version does not. Prefer iterative in interviews unless asked.
    """
    def helper(left, right):
        if left > right:
            return -1

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return helper(mid + 1, right)
        else:
            return helper(left, mid - 1)

    return helper(0, len(nums) - 1)


# ============================================================================
# SOLUTION 3: Half-Open Range / Lower Bound (The variant worth knowing)
# ============================================================================

def search_lowerbound(nums, target):
    """
    Approach: Find the FIRST index whose value is >= target, then verify.

    This uses the half-open range [left, right) — right is EXCLUSIVE.

    Algorithm:
    1. left = 0, right = len(nums)   (note: len, not len - 1)
    2. While left < right:           (note: <, not <=)
         a. mid = left + (right - left) // 2
         b. nums[mid] < target → left = mid + 1
         c. else                → right = mid   (mid may BE the answer)
    3. Now left is the insertion point. Return left if it holds target.

    Boundary reasoning:
    - `right` is exclusive, so `left == right` means "empty range" → `<`.
    - `right = mid` (not mid - 1) because mid is still a candidate answer.
    - `left = mid + 1` keeps the range shrinking, so no infinite loop.

    Why learn this shape:
    - It never returns early, so it generalizes to "first/last occurrence",
      "search insert position", and "smallest x such that f(x) is true".
    - This is the form real library code (Python's bisect) uses.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(nums)      # EXCLUSIVE upper bound

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid    # keep mid as a candidate

    # left is now the insertion point for target
    if left < len(nums) and nums[left] == target:
        return left
    return -1


# ============================================================================
# SOLUTION 4: Standard Library bisect (Know it exists — don't submit it)
# ============================================================================

def search_bisect(nums, target):
    """
    Approach: Let the standard library do the halving.

    Algorithm:
    1. bisect_left gives the leftmost insertion point for target
    2. Check whether that slot actually contains target

    Time Complexity: O(log n) - implemented in C, same algorithm
    Space Complexity: O(1)

    In a real codebase: use this. In an interview: the interviewer wants
    to see Solution 1. Mentioning bisect afterwards shows range, though.
    """
    from bisect import bisect_left

    i = bisect_left(nums, target)
    if i < len(nums) and nums[i] == target:
        return i
    return -1


# ============================================================================
# SOLUTION 5: Linear Search (DON'T use! Just for learning)
# ============================================================================

def search_linear(nums, target):
    """
    Approach: Look at every element until you find the target.

    Time Complexity: O(n) - Too slow, and it ignores the sortedness!
    Space Complexity: O(1)

    For n=10000: up to 10,000 comparisons vs 14 for binary search. 😱
    The problem explicitly demands O(log n), so this is a rejected answer
    even though it produces the right index.
    """
    for i, num in enumerate(nums):
        if num == target:
            return i

    return -1


# ============================================================================
# TEST CASES
# ============================================================================

def test():
    """Test all solutions"""

    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),        # classic example
        ([-1, 0, 3, 5, 9, 12], 2, -1),       # missing, falls between values
        ([5], 5, 0),                          # single element, found
        ([5], -5, -1),                        # single element, missing
        ([], 3, -1),                          # empty array (defensive)
        ([1, 2, 3, 4, 5], 1, 0),              # ⭐ first element (left edge)
        ([1, 2, 3, 4, 5], 5, 4),              # ⭐ last element (right edge)
        ([1, 2, 3, 4, 5], 3, 2),              # exact middle
        ([1, 2, 3, 4, 5], 0, -1),             # ⭐ below the whole range
        ([1, 2, 3, 4, 5], 6, -1),             # ⭐ above the whole range
        ([1, 2, 3, 4], 2, 1),                 # even length, left half
        ([1, 2, 3, 4], 3, 2),                 # even length, right half
        ([-10, -5, 0, 5, 10], -10, 0),        # negatives, left edge
        ([-10, -5, 0, 5, 10], 10, 4),         # negatives, right edge
        (list(range(0, 2000, 2)), 1338, 669),  # big array, even values only
        (list(range(0, 2000, 2)), 1337, -1),   # big array, odd → missing
    ]

    solutions = [
        ("Iterative (Optimal)", search),
        ("Recursive", search_recursive),
        ("Lower Bound (half-open)", search_lowerbound),
        ("bisect (stdlib)", search_bisect),
        ("Linear Search", search_linear),
    ]

    for name, solution in solutions:
        print(f"\n{'='*50}")
        print(f"Testing: {name}")
        print('='*50)

        all_passed = True
        for i, (nums, target, expected) in enumerate(test_cases, 1):
            result = solution(nums.copy(), target)
            is_correct = result == expected

            # Keep huge arrays readable in the output
            shown = nums if len(nums) <= 8 else f"[{nums[0]}..{nums[-1]}] " \
                                                f"(n={len(nums)})"

            status = "✅" if is_correct else "❌"
            print(f"Test {i}: {status} nums={shown}, target={target} → "
                  f"{result} (expected {expected})")
            if not is_correct:
                all_passed = False

        if all_passed:
            print(f"\n🎉 All tests passed for {name}!")


# ============================================================================
# VISUAL DEMO
# ============================================================================

def visual_demo(nums, target):
    """
    Visual step-by-step demonstration of the shrinking search range
    """
    print(f"\n{'='*70}")
    print(f"VISUAL DEMO: Binary Search for {target}")
    print(f"Input: {nums}")
    print('='*70)

    if not nums:
        print("\nEmpty array → answer is -1")
        return

    # Pre-compute a fixed column width so the pointer row lines up
    width = max(len(str(n)) for n in nums) + 1
    row = "".join(f"{n:>{width}}" for n in nums)

    left = 0
    right = len(nums) - 1
    step = 1

    print("\nStep-by-step execution:\n")

    while left <= right:
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
        print(f"  left={left}, right={right}, "
              f"mid={mid} → nums[{mid}]={nums[mid]}")
        print(f"  Search space: {right - left + 1} element(s)")

        if nums[mid] == target:
            print(f"  ✅ FOUND! nums[{mid}] == {target}. Return {mid}")
            return
        elif nums[mid] < target:
            print(f"  {nums[mid]} < {target} → go RIGHT: "
                  f"left = mid+1 = {mid + 1}")
            left = mid + 1
        else:
            print(f"  {nums[mid]} > {target} → go LEFT: "
                  f"right = mid-1 = {mid - 1}")
            right = mid - 1

        step += 1
        print()

    print(f"  ❌ left({left}) > right({right}) → range is empty.")
    print(f"  {target} is not in the array. Return -1")


# ============================================================================
# WHAT YOU SHOULD LEARN
# ============================================================================

"""
KEY TAKEAWAYS:
-------------
1. Binary search needs SORTED data. That precondition is the whole deal.
2. Each step halves the range → O(log n). 10^6 elements in 20 steps.
3. Pair your boundaries correctly:
       [left, right]  inclusive  → `while left <= right`, mid ± 1
       [left, right)  exclusive  → `while left <  right`, right = mid
   Mixing the two is the #1 source of infinite loops.
4. `mid = left + (right - left) // 2` avoids integer overflow in languages
   with fixed-width ints, and reads the same in Python.
5. Every branch must strictly shrink the range.

PATTERN RECOGNITION:
-------------------
When you see:
- "Sorted array" + "find"
- "O(log n) required"
- "Find the smallest/largest value such that ..."
- "Minimize the maximum" / "Maximize the minimum"

Think: BINARY SEARCH!

Binary search is not only about arrays — it works on any MONOTONIC
predicate: false, false, false, TRUE, TRUE. You are hunting the flip point.

INTERVIEW TIPS:
--------------
1. Confirm the array is sorted, and ask about duplicates.
2. Say your invariant out loud: "the answer, if it exists, is always
   inside [left, right]."
3. Trace an even-length array — that is where off-by-ones hide.
4. Test the four edges: first element, last element, below range,
   above range. Those four catch nearly every bug.
5. If asked for "first/last occurrence with duplicates", reach for the
   half-open lower-bound shape (Solution 3), not the early return.

COMMON MISTAKES:
---------------
❌ `while left < right` with an INCLUSIVE right → misses the last element.
   On [5] with target 5 it returns -1 immediately.
❌ `left = mid` instead of `left = mid + 1` → infinite loop when the range
   has two elements (mid keeps landing on left).
❌ `mid = (left + right) // 2` → overflow in C++/Java (fine in Python,
   but interviewers still look for the safe idiom).
❌ Forgetting the empty-array case.
❌ Running binary search on unsorted data and trusting the result.

VARIATIONS:
----------
- Search Insert Position → return `left` instead of -1 (Solution 3 already
  computes it!)
- First Bad Version → binary search over a predicate, not values
- Find First/Last Position of Element → two lower-bound searches
- Search in Rotated Sorted Array → decide which half is sorted first
- Koko Eating Bananas → binary search the ANSWER, not the array

TIME COMPLEXITY COMPARISON:
--------------------------
Linear Search:     O(n)      time, O(1)      space
Recursive BS:      O(log n)  time, O(log n)  space (call stack)
Iterative BS:      O(log n)  time, O(1)      space ← BEST!

NEXT STEPS:
----------
✅ Boundaries locked in
✅ Know both the inclusive and half-open shapes
→ Now try: Search in Rotated Sorted Array (medium!)
→ Then: Find Minimum in Rotated Sorted Array

PRACTICE MORE:
-------------
Similar problems to practice this pattern:
- Search Insert Position
- First Bad Version
- Search a 2D Matrix
- Find First and Last Position of Element in Sorted Array
- Koko Eating Bananas
"""


if __name__ == "__main__":
    # Run tests
    test()

    # Visual demonstrations
    visual_demo([-1, 0, 3, 5, 9, 12], 9)
    visual_demo([-1, 0, 3, 5, 9, 12], 2)

    # Interactive practice
    print("\n" + "="*70)
    print("YOUR TURN TO TRACE!")
    print("="*70)
    print("\nTry tracing through this example yourself:")
    print("nums = [1, 3, 5, 7, 9, 11, 13, 15], target = 13")
    print("\nHow many steps? What are left/right after each comparison?")
    print("Write it out, then run: visual_demo([1,3,5,7,9,11,13,15], 13)")
