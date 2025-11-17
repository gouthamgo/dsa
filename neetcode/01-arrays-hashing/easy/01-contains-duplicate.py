"""
Problem: Contains Duplicate
Difficulty: Easy
Topics: Array, Hash Table

Problem Statement:
-----------------
Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.

Examples:
---------
Example 1:
    Input: nums = [1,2,3,1]
    Output: true
    Explanation: 1 appears twice

Example 2:
    Input: nums = [1,2,3,4]
    Output: false
    Explanation: All elements are distinct

Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

Constraints:
-----------
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

LEARNING NOTES:
--------------
This is the PERFECT first problem for arrays & hashing!

Key Insight: Use a Set to track what we've seen. Sets give O(1) lookup time.

Pattern: "Have I seen this before?" → Use a Set!

Visualization:
    nums = [1, 2, 3, 1]
             ↓
    seen = {}

    Step 1: 1 not in seen → seen = {1}
    Step 2: 2 not in seen → seen = {1, 2}
    Step 3: 3 not in seen → seen = {1, 2, 3}
    Step 4: 1 IS in seen! → Return True ✅
"""


# ============================================================================
# SOLUTION 1: Using Hash Set (Optimal)
# ============================================================================

def containsDuplicate(nums):
    """
    Approach: Use a set to track seen numbers.

    Algorithm:
    1. Create empty set
    2. For each number:
       - If already in set → duplicate found!
       - Otherwise → add to set
    3. If we finish loop → no duplicates

    Time Complexity: O(n) - single pass through array
    Space Complexity: O(n) - set can store up to n elements
    """
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


# ============================================================================
# SOLUTION 2: One-liner using Set (Also Optimal)
# ============================================================================

def containsDuplicate_v2(nums):
    """
    Clever approach: Compare lengths!

    Logic:
    - Set automatically removes duplicates
    - If set length < array length → duplicates existed!

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return len(set(nums)) < len(nums)


# ============================================================================
# SOLUTION 3: Sorting Approach (Alternative)
# ============================================================================

def containsDuplicate_sorting(nums):
    """
    Approach: Sort first, then check adjacent elements.

    Why this works:
    - After sorting, duplicates will be next to each other
    - Just check if any adjacent pair is equal

    Time Complexity: O(n log n) - due to sorting
    Space Complexity: O(1) or O(n) depending on sort implementation

    Trade-off: Slower but uses less space (in some cases)
    """
    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True

    return False


# ============================================================================
# SOLUTION 4: Brute Force (Don't use in interviews!)
# ============================================================================

def containsDuplicate_bruteforce(nums):
    """
    Approach: Compare every pair.

    Time Complexity: O(n²) - Too slow!
    Space Complexity: O(1)

    Why it's bad: For n=10000, this does 100,000,000 comparisons!
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False


# ============================================================================
# TEST CASES
# ============================================================================

def test():
    """Test all solutions"""

    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([1], False),
        ([1, 2], False),
    ]

    solutions = [
        ("Hash Set", containsDuplicate),
        ("One-liner", containsDuplicate_v2),
        ("Sorting", containsDuplicate_sorting),
    ]

    for name, solution in solutions:
        print(f"\n{'='*50}")
        print(f"Testing: {name}")
        print('='*50)

        all_passed = True
        for i, (nums, expected) in enumerate(test_cases, 1):
            result = solution(nums.copy())  # .copy() to prevent modification
            status = "✅" if result == expected else "❌"
            print(f"Test {i}: {status} Input: {nums} → Output: {result} (Expected: {expected})")
            if result != expected:
                all_passed = False

        if all_passed:
            print(f"\n🎉 All tests passed for {name}!")


# ============================================================================
# WHAT YOU SHOULD LEARN
# ============================================================================

"""
KEY TAKEAWAYS:
-------------
1. Hash Set is your friend for "have I seen this?" problems
2. Time vs Space trade-off: Hash set is O(n) time/space, sorting is O(n log n) time
3. Always think: "Can I trade space for speed?"

PATTERN RECOGNITION:
-------------------
When you see:
- "Find duplicate"
- "Appears at least twice"
- "Check if element exists"

Think: HASH SET!

INTERVIEW TIPS:
--------------
1. Start with the optimal solution (hash set)
2. Mention the sorting approach as alternative
3. Explain time/space trade-offs
4. Never mention brute force unless asked!

NEXT STEPS:
----------
✅ Understood the problem
✅ Know multiple approaches
→ Now solve: Valid Anagram (next problem!)
"""


if __name__ == "__main__":
    # Run tests
    test()

    # Interactive demo
    print("\n" + "="*50)
    print("INTERACTIVE DEMO")
    print("="*50)

    sample = [1, 2, 3, 1]
    print(f"\nInput: {sample}")
    print("\nStep-by-step execution:")

    seen = set()
    for i, num in enumerate(sample, 1):
        if num in seen:
            print(f"Step {i}: {num} is in seen! → DUPLICATE FOUND ✅")
            break
        seen.add(num)
        print(f"Step {i}: {num} added to seen. Current seen: {seen}")
