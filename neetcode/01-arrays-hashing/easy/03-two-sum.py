"""
Problem: Two Sum
Difficulty: Easy
Topics: Array, Hash Table

Problem Statement:
-----------------
Given an array of integers nums and an integer target, return indices of
the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you
may not use the same element twice.

You can return the answer in any order.

Examples:
---------
Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: nums[0] + nums[1] = 2 + 7 = 9

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    Explanation: nums[1] + nums[2] = 2 + 4 = 6

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
-----------
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists

Follow-up:
---------
Can you come up with an algorithm that is less than O(n²) time complexity?

LEARNING NOTES:
--------------
This is THE CLASSIC interview problem! Must know this!

Key Insight: Use COMPLEMENT SEARCH!
    If we need: a + b = target
    Then: b = target - a
    Store what we've seen, and look for complement!

Pattern: "Find pair that sums to X" → Hash Map + Complement!

Visualization:
    nums = [2, 7, 11, 15], target = 9

    i=0, num=2
        complement = 9-2 = 7
        seen = {} (empty)
        7 not in seen → store: seen = {2: 0}

    i=1, num=7
        complement = 9-7 = 2
        seen = {2: 0}
        2 IS in seen! → Found at index 0
        Return [0, 1] ✅
"""


# ============================================================================
# SOLUTION 1: Hash Map - One Pass (OPTIMAL!)
# ============================================================================

def twoSum(nums, target):
    """
    Approach: Use hash map to store value→index as we iterate.

    Algorithm:
    1. For each number, calculate complement (target - num)
    2. Check if complement exists in hash map
    3. If yes → found! Return indices
    4. If no → store current number and continue

    Why it works:
    - When we're at index i looking for complement
    - If complement exists, we already saw it earlier
    - Hash map remembers where we saw it!

    Time Complexity: O(n) - single pass
    Space Complexity: O(n) - hash map stores up to n elements
    """
    seen = {}  # value → index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []  # No solution (won't happen per problem constraints)


# ============================================================================
# SOLUTION 2: Hash Map - Two Pass (Also works but slower)
# ============================================================================

def twoSum_twopass(nums, target):
    """
    Approach: First store all, then search.

    Algorithm:
    1. Pass 1: Store all numbers in hash map
    2. Pass 2: For each number, look for complement

    Time Complexity: O(n) - two passes
    Space Complexity: O(n)

    Why one-pass is better:
    - Same complexity but faster in practice
    - Less code
    """
    # Pass 1: Store all
    value_to_index = {}
    for i, num in enumerate(nums):
        value_to_index[num] = i

    # Pass 2: Search
    for i, num in enumerate(nums):
        complement = target - num
        if complement in value_to_index and value_to_index[complement] != i:
            return [i, value_to_index[complement]]

    return []


# ============================================================================
# SOLUTION 3: Brute Force (DON'T use! Just for learning)
# ============================================================================

def twoSum_bruteforce(nums, target):
    """
    Approach: Try all pairs.

    Time Complexity: O(n²) - Too slow!
    Space Complexity: O(1)

    For n=10000: 100 million comparisons! 😱
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


# ============================================================================
# SOLUTION 4: Sorting + Two Pointers (Changes indices!)
# ============================================================================

def twoSum_sorting(nums, target):
    """
    Approach: Sort first, then use two pointers.

    Problem: Sorting changes positions, so need to track original indices!

    Time Complexity: O(n log n)
    Space Complexity: O(n) - for storing pairs

    Why it's not ideal:
    - Slower than hash map
    - Need extra work to track indices
    - Hash map is simpler!
    """
    # Store (value, original_index)
    pairs = [(num, i) for i, num in enumerate(nums)]
    pairs.sort()  # Sort by value

    left = 0
    right = len(pairs) - 1

    while left < right:
        current_sum = pairs[left][0] + pairs[right][0]

        if current_sum == target:
            return [pairs[left][1], pairs[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []


# ============================================================================
# TEST CASES
# ============================================================================

def test():
    """Test all solutions"""

    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 5, 3, 7], 8, [0, 3]),  # or [1, 2]
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ]

    solutions = [
        ("Hash Map (Optimal)", twoSum),
        ("Two Pass", twoSum_twopass),
        ("Brute Force", twoSum_bruteforce),
        ("Sorting", twoSum_sorting),
    ]

    for name, solution in solutions:
        print(f"\n{'='*50}")
        print(f"Testing: {name}")
        print('='*50)

        all_passed = True
        for i, (nums, target, expected) in enumerate(test_cases, 1):
            result = solution(nums.copy(), target)

            # Check if sum is correct (order doesn't matter)
            if result:
                actual_sum = nums[result[0]] + nums[result[1]]
                is_correct = actual_sum == target
            else:
                is_correct = False

            status = "✅" if is_correct else "❌"
            print(f"Test {i}: {status} nums={nums}, target={target} → {result}")
            if not is_correct:
                all_passed = False

        if all_passed:
            print(f"\n🎉 All tests passed for {name}!")


# ============================================================================
# VISUAL DEMO
# ============================================================================

def visual_demo(nums, target):
    """
    Visual step-by-step demonstration
    """
    print(f"\n{'='*70}")
    print(f"VISUAL DEMO: Find two numbers that sum to {target}")
    print(f"Input: {nums}")
    print('='*70)

    seen = {}

    print("\nStep-by-step execution:\n")

    for i, num in enumerate(nums):
        complement = target - num

        print(f"Step {i+1}:")
        print(f"  Current index: {i}, value: {num}")
        print(f"  Complement needed: {target} - {num} = {complement}")
        print(f"  Current hash map: {seen}")

        if complement in seen:
            print(f"  ✅ FOUND! Complement {complement} is at index {seen[complement]}")
            print(f"  Answer: [{seen[complement]}, {i}]")
            print(f"  Verification: {nums[seen[complement]]} + {num} = {target}")
            return

        seen[num] = i
        print(f"  ❌ Not found yet. Storing {num} at index {i}")
        print()

    print("  No solution found")


# ============================================================================
# WHAT YOU SHOULD LEARN
# ============================================================================

"""
KEY TAKEAWAYS:
-------------
1. COMPLEMENT SEARCH is a powerful pattern!
2. Hash map trades space for speed (O(n²) → O(n))
3. One-pass is elegant and efficient
4. This pattern appears in MANY problems

PATTERN RECOGNITION:
-------------------
When you see:
- "Find pair that sums to X"
- "Two numbers add up to target"
- "Complement" or "difference"

Think: HASH MAP + COMPLEMENT SEARCH!

THE COMPLEMENT TRICK:
--------------------
If a + b = target, then:
  b = target - a

So instead of searching for "b", search for "target - a"!

INTERVIEW TIPS:
--------------
1. Start with the hash map solution (optimal)
2. Walk through example step-by-step
3. Explain why hash map: "O(1) lookup saves us from O(n²)"
4. Handle edge cases: duplicate values, negative numbers
5. Mention: "This pattern extends to 3Sum, 4Sum, etc."

COMMON MISTAKES:
---------------
❌ Using same element twice: Check indices!
❌ Forgetting to return indices (not values)
❌ Not handling duplicates (like [3,3], target=6)

VARIATIONS:
----------
- Two Sum II (sorted array) → Use two pointers instead!
- Two Sum III (design class) → Different trade-offs
- 3Sum, 4Sum → Extensions of this pattern

TIME COMPLEXITY COMPARISON:
--------------------------
Brute Force:     O(n²) time, O(1) space
Sorting:         O(n log n) time, O(n) space
Hash Map:        O(n) time, O(n) space ← BEST!

NEXT STEPS:
----------
✅ Mastered complement search
✅ Know hash map pattern
→ Now try: Group Anagrams (medium level!)
→ Or explore: Two Pointers topic

PRACTICE MORE:
-------------
Similar problems to practice this pattern:
- Two Sum II (sorted array)
- 3Sum
- 4Sum
- Two Sum IV (BST)
"""


if __name__ == "__main__":
    # Run tests
    test()

    # Visual demonstrations
    visual_demo([2, 7, 11, 15], 9)
    visual_demo([3, 2, 4], 6)
    visual_demo([3, 3], 6)

    # Interactive practice
    print("\n" + "="*70)
    print("YOUR TURN TO TRACE!")
    print("="*70)
    print("\nTry tracing through this example yourself:")
    print("nums = [1, 5, 3, 7, 9], target = 10")
    print("\nWhat would happen at each step?")
    print("Write it out, then run: visual_demo([1, 5, 3, 7, 9], 10)")
