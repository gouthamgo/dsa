"""
Problem: Search in Rotated Sorted Array
Difficulty: Medium
Topics: Array, Binary Search

Problem Statement:
-----------------
There is an integer array nums sorted in ascending order (with DISTINCT
values). Before being passed to your function, nums is possibly ROTATED at
an unknown pivot index k, so that the array becomes:

    [nums[k], nums[k+1], ..., nums[n-1], nums[0], ..., nums[k-1]]

For example, [0,1,2,4,5,6,7] rotated at pivot index 3 becomes [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not.

You must write an algorithm with O(log n) runtime complexity.

Examples:
---------
Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
    Explanation: 0 sits at index 4 in the rotated array.

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
    Explanation: 3 is not in the array at all.

Example 3:
    Input: nums = [1], target = 0
    Output: -1

Constraints:
-----------
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are UNIQUE
- nums is an ascending array that is possibly rotated
- -10^4 <= target <= 10^4

LEARNING NOTES:
--------------
The array isn't sorted... but it's ALMOST sorted, and that's enough. 🔍

Key Insight: Split at mid — AT LEAST ONE HALF IS ALWAYS SORTED.
    A single rotation can only put one "cliff" in the array. Wherever you
    cut it, the cliff falls in one half, so the OTHER half is clean.

    1. Figure out which half is sorted (compare nums[left] with nums[mid]).
    2. In that sorted half you can test membership with two comparisons.
    3. If target is in there → search it. Otherwise → search the other half.

    Either way you discard half the array → still O(log n).

Pattern: "Sorted but rotated" → Binary Search + "which half is sorted?"

Which half is sorted?
    nums[left] <= nums[mid]  → the LEFT half [left..mid] is sorted
    otherwise                → the RIGHT half [mid..right] is sorted
    (`<=` matters: when left == mid the left half is trivially sorted.)

Visualization:
    nums = [4, 5, 6, 7, 0, 1, 2], target = 0

    Step 1: left=0, right=6, mid=3 → nums[3]=7
        [ 4,  5,  6,  7,  0,  1,  2]
          L           M           R
        nums[L]=4 <= nums[M]=7 → LEFT half [4,5,6,7] is sorted
        Is 0 inside [4, 7)? NO → the cliff and our target are RIGHT
        → left = mid + 1 = 4

    Step 2: left=4, right=6, mid=5 → nums[5]=1
        [ 4,  5,  6,  7,  0,  1,  2]
                          L   M   R
        nums[L]=0 <= nums[M]=1 → LEFT half [0,1] is sorted
        Is 0 inside [0, 1)? YES → search left → right = mid - 1 = 4

    Step 3: left=4, right=4, mid=4 → nums[4]=0
        [ 4,  5,  6,  7,  0,  1,  2]
                         LMR
        0 == 0 → FOUND at index 4 ✅
"""


# ============================================================================
# SOLUTION 1: One-Pass Binary Search (OPTIMAL!)
# ============================================================================

def search(nums, target):
    """
    Approach: At every step, identify the sorted half and decide where to go.

    Algorithm:
    1. left = 0, right = len(nums) - 1
    2. While left <= right:
         a. mid = left + (right - left) // 2
         b. nums[mid] == target → return mid
         c. If nums[left] <= nums[mid]:      # LEFT half is sorted
              if nums[left] <= target < nums[mid] → right = mid - 1
              else                                → left  = mid + 1
         d. Else:                            # RIGHT half is sorted
              if nums[mid] < target <= nums[right] → left  = mid + 1
              else                                 → right = mid - 1
    3. Return -1

    Boundary reasoning (this is where people slip):
    - `nums[left] <= nums[mid]` uses <= so that a one-element left half
      (left == mid) counts as sorted. With `<` a two-element array like
      [3,1] takes the wrong branch.
    - The range checks are HALF-OPEN on the mid side (`< nums[mid]` and
      `> nums[mid]`) because mid was already tested for equality.
    - The other side is INCLUSIVE (`nums[left] <=`, `<= nums[right]`)
      because those endpoints have NOT been tested yet.

    Time Complexity: O(log n) - one half is discarded each iteration
    Space Complexity: O(1) - three integers
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            # LEFT half [left..mid] is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1      # target lives in the sorted left half
            else:
                left = mid + 1       # must be in the messy right half
        else:
            # RIGHT half [mid..right] is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1       # target lives in the sorted right half
            else:
                right = mid - 1      # must be in the messy left half

    return -1


# ============================================================================
# SOLUTION 2: Find Pivot, Then Search the Correct Half (Two passes)
# ============================================================================

def search_findpivot(nums, target):
    """
    Approach: Binary search for the rotation point, then a normal search.

    Algorithm:
    1. Find pivot = index of the SMALLEST element (the rotation point):
         while lo < hi:
             mid = lo + (hi - lo) // 2
             nums[mid] > nums[hi] → the minimum is right → lo = mid + 1
             else                 → mid could BE the minimum → hi = mid
    2. Now [0..pivot-1] and [pivot..n-1] are each plainly sorted.
    3. Pick the half whose value range can contain target.
    4. Run a textbook binary search on that half.

    Why compare against nums[hi] and not nums[lo] in step 1:
    - nums[mid] > nums[hi] means a cliff exists to the right of mid.
    - Comparing to nums[lo] cannot distinguish a non-rotated array.

    Time Complexity: O(log n) - two binary searches, 2·log n
    Space Complexity: O(1)

    Slightly more code than Solution 1, but each piece is a shape you
    already trust. Great fallback if the one-pass logic feels slippery.
    """
    n = len(nums)
    if n == 0:
        return -1

    # --- Pass 1: locate the pivot (index of the minimum) ---
    lo, hi = 0, n - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1     # cliff is to the right, min is beyond mid
        else:
            hi = mid         # mid might be the min itself — keep it
    pivot = lo

    # --- Choose the sorted half that could contain target ---
    if nums[pivot] <= target <= nums[n - 1]:
        lo, hi = pivot, n - 1
    else:
        lo, hi = 0, pivot - 1

    # --- Pass 2: plain binary search on an ordinary sorted range ---
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


# ============================================================================
# SOLUTION 3: Pivot + Index Rotation Trick (Elegant!)
# ============================================================================

def search_rotateindex(nums, target):
    """
    Approach: Pretend the array was never rotated, using modular indices.

    Algorithm:
    1. Find pivot exactly as in Solution 2.
    2. Binary search over VIRTUAL indices 0..n-1, where virtual index i
       maps to the real index (i + pivot) % n.
    3. Reading through that mapping, the array looks perfectly sorted!
    4. Return the REAL index when found.

    Time Complexity: O(log n)
    Space Complexity: O(1) - no array is actually built, just arithmetic

    Why it's worth knowing: "un-rotate with modular arithmetic" shows up
    again in circular-array problems (Gas Station, circular queues).
    """
    n = len(nums)
    if n == 0:
        return -1

    # Find the pivot (index of the minimum)
    lo, hi = 0, n - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    pivot = lo

    # Binary search on the VIRTUAL (un-rotated) array
    lo, hi = 0, n - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        real = (mid + pivot) % n     # translate virtual → real index

        if nums[real] == target:
            return real
        elif nums[real] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


# ============================================================================
# SOLUTION 4: Linear Search (DON'T use! Just for learning)
# ============================================================================

def search_linear(nums, target):
    """
    Approach: Scan every element and ignore the structure entirely.

    Time Complexity: O(n) - Too slow! The problem demands O(log n).
    Space Complexity: O(1)

    For n=5000 this "works" and is fast enough on paper — which is exactly
    the trap. The interviewer is testing whether you can exploit the
    almost-sorted structure, not whether you can write a for loop. 😱
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
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),        # classic example
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),       # missing value
        ([4, 5, 6, 7, 0, 1, 2], 4, 0),        # first element
        ([4, 5, 6, 7, 0, 1, 2], 2, 6),        # last element
        ([4, 5, 6, 7, 0, 1, 2], 7, 3),        # just left of the cliff
        ([1], 0, -1),                          # single element, missing
        ([1], 1, 0),                           # single element, found
        ([], 5, -1),                           # empty array (defensive)
        ([1, 3], 3, 1),                        # ⭐ two elements, no rotation
        ([3, 1], 1, 1),                        # ⭐ two elements, rotated
        ([3, 1], 3, 0),                        # ⭐ two elements, rotated
        ([5, 1, 3], 3, 2),                     # ⭐ three elements, rotated
        ([3, 5, 1], 3, 0),                     # ⭐ rotation point at the end
        ([1, 2, 3, 4, 5, 6, 7], 4, 3),         # not rotated at all
        ([1, 2, 3, 4, 5, 6, 7], 8, -1),        # not rotated, above range
        ([6, 7, 0, 1, 2, 4, 5], 7, 1),         # rotated near the front
        ([4, 5, 6, 7, 8, 1, 2, 3], 8, 4),      # even length, rotated
        ([-4, -2, 0, 2, -10, -8, -6], -10, 4),  # negatives, rotated
    ]

    solutions = [
        ("One-Pass Binary Search (Optimal)", search),
        ("Find Pivot + Search Half", search_findpivot),
        ("Pivot + Index Rotation", search_rotateindex),
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

            status = "✅" if is_correct else "❌"
            print(f"Test {i}: {status} nums={nums}, target={target} → "
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
    Visual step-by-step demonstration of the "which half is sorted?" logic
    """
    print(f"\n{'='*70}")
    print(f"VISUAL DEMO: Search {target} in a rotated sorted array")
    print(f"Input: {nums}")
    print('='*70)

    if not nums:
        print("\nEmpty array → answer is -1")
        return

    width = max(len(str(n)) for n in nums) + 2
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

        if nums[mid] == target:
            print(f"  ✅ FOUND! nums[{mid}] == {target}. Return {mid}")
            return

        if nums[left] <= nums[mid]:
            print(f"  nums[{left}]={nums[left]} <= nums[{mid}]={nums[mid]} "
                  f"→ LEFT half {nums[left:mid + 1]} is SORTED")
            if nums[left] <= target < nums[mid]:
                print(f"  {target} is inside [{nums[left]}, {nums[mid]}) "
                      f"→ search LEFT: right = {mid - 1}")
                right = mid - 1
            else:
                print(f"  {target} is NOT inside [{nums[left]}, {nums[mid]}) "
                      f"→ search RIGHT: left = {mid + 1}")
                left = mid + 1
        else:
            print(f"  nums[{left}]={nums[left]} > nums[{mid}]={nums[mid]} "
                  f"→ RIGHT half {nums[mid:right + 1]} is SORTED")
            if nums[mid] < target <= nums[right]:
                print(f"  {target} is inside ({nums[mid]}, {nums[right]}] "
                      f"→ search RIGHT: left = {mid + 1}")
                left = mid + 1
            else:
                print(f"  {target} is NOT inside ({nums[mid]}, "
                      f"{nums[right]}] → search LEFT: right = {mid - 1}")
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
1. ONE rotation means ONE cliff, so cutting at mid always leaves at least
   one fully sorted half. That single sentence solves the problem.
2. Test membership in the SORTED half — it's the only half where a simple
   range check is trustworthy.
3. `nums[left] <= nums[mid]` needs the `=`. When left == mid (tiny ranges)
   the left half is sorted by definition, and `<` gets it wrong.
4. Half-open on the mid side, inclusive on the far side: mid has already
   been compared to target, the endpoints have not.
5. If the one-pass logic feels risky under pressure, find the pivot first
   (Solution 2). Two clean searches beat one shaky one.

PATTERN RECOGNITION:
-------------------
When you see:
- "Sorted array, possibly rotated"
- "Circular" / "shifted" ordering
- O(log n) demanded on data that isn't quite sorted

Think: BINARY SEARCH + "WHICH HALF IS SORTED?"

The deeper lesson: binary search only needs a MONOTONIC decision rule at
mid — not a globally sorted array.

INTERVIEW TIPS:
--------------
1. Ask about duplicates! With duplicates (LeetCode 81) the worst case
   degrades to O(n), because nums[left] == nums[mid] tells you nothing.
2. Draw the array as two ascending ramps with a cliff between them.
3. Walk [3,1] and [5,1,3] out loud — tiny rotated arrays are where the
   comparisons break.
4. State the invariant: "if target exists, it is inside [left, right]."
5. Mention the pivot-first alternative; showing two routes reads as depth.

COMMON MISTAKES:
---------------
❌ Writing `nums[left] < nums[mid]` instead of `<=` → breaks on [3,1].
❌ Using inclusive bounds on both sides of the range check, e.g.
   `nums[left] <= target <= nums[mid]` → mid was already handled; harmless
   here but it hides the reasoning and breaks in the duplicate variant.
❌ Forgetting that the RIGHT half being sorted means using nums[right].
❌ Assuming the array is rotated. It might not be — the code must handle
   the plain sorted case with no special branch (it does).
❌ Comparing nums[mid] to nums[0] to find the pivot; compare to nums[hi].

VARIATIONS:
----------
- Find Minimum in Rotated Sorted Array → just the pivot search, alone
- Search in Rotated Sorted Array II (duplicates) → shrink hi by 1 when
  nums[mid] == nums[hi]; worst case O(n)
- Rotate Array → the operation that created this input
- Find Peak Element → binary search with no sortedness at all

TIME COMPLEXITY COMPARISON:
--------------------------
Linear Search:        O(n)      time, O(1) space
Pivot + search:       O(2log n) time, O(1) space
One-pass search:      O(log n)  time, O(1) space ← BEST!

NEXT STEPS:
----------
✅ Can reason about partially sorted data
✅ Know the pivot search cold
→ Now try: Find Minimum in Rotated Sorted Array (the pivot search alone!)
→ Then: Koko Eating Bananas (binary search on the ANSWER)

PRACTICE MORE:
-------------
Similar problems to practice this pattern:
- Find Minimum in Rotated Sorted Array
- Search in Rotated Sorted Array II (with duplicates)
- Find Peak Element
- Search a 2D Matrix
- Koko Eating Bananas
"""


if __name__ == "__main__":
    # Run tests
    test()

    # Visual demonstrations
    visual_demo([4, 5, 6, 7, 0, 1, 2], 0)
    visual_demo([4, 5, 6, 7, 0, 1, 2], 3)

    # Interactive practice
    print("\n" + "="*70)
    print("YOUR TURN TO TRACE!")
    print("="*70)
    print("\nTry tracing through this example yourself:")
    print("nums = [6, 7, 8, 1, 2, 3, 4, 5], target = 3")
    print("\nAt each step: which half is sorted, and is the target in it?")
    print("Write it out, then run: visual_demo([6,7,8,1,2,3,4,5], 3)")
