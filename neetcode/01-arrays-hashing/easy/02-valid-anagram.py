"""
Problem: Valid Anagram
Difficulty: Easy
Topics: Hash Table, String, Sorting

Problem Statement:
-----------------
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An anagram is a word formed by rearranging the letters of another word,
using all the original letters exactly once.

Examples:
---------
Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true
    Explanation: Both have same letters: a(3), n(1), g(1), r(1), m(1)

Example 2:
    Input: s = "rat", t = "car"
    Output: false
    Explanation: Different letters

Example 3:
    Input: s = "listen", t = "silent"
    Output: true

Constraints:
-----------
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters

Follow-up:
---------
What if the inputs contain Unicode characters? How would you adapt your solution?

LEARNING NOTES:
--------------
This problem teaches FREQUENCY COUNTING!

Key Insight: Anagrams have the SAME character frequencies.

Pattern: "Count occurrences" → Use Hash Map!

Visualization:
    s = "anagram"
    t = "nagaram"

    Count s: {a:3, n:1, g:1, r:1, m:1}
    Count t: {n:1, a:3, g:1, r:1, m:1}

    Same counts! → True ✅
"""

from collections import Counter


# ============================================================================
# SOLUTION 1: Hash Map Frequency Count (Best for Learning)
# ============================================================================

def isAnagram(s, t):
    """
    Approach: Count character frequencies and compare.

    Algorithm:
    1. If lengths differ → not anagram
    2. Count frequency of each char in s
    3. Count frequency of each char in t
    4. Compare the two frequency maps

    Time Complexity: O(n) where n = length of string
    Space Complexity: O(1) - at most 26 letters (fixed alphabet)
    """
    # Quick check: different lengths → not anagram
    if len(s) != len(t):
        return False

    # Count frequencies in s
    count_s = {}
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1

    # Count frequencies in t
    count_t = {}
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    # Compare
    return count_s == count_t


# ============================================================================
# SOLUTION 2: Using collections.Counter (Pythonic)
# ============================================================================

def isAnagram_v2(s, t):
    """
    Approach: Use built-in Counter class.

    Counter is a hash map specifically for counting!

    Time Complexity: O(n)
    Space Complexity: O(1) - fixed alphabet size
    """
    return Counter(s) == Counter(t)


# ============================================================================
# SOLUTION 3: Sorting Approach (Alternative)
# ============================================================================

def isAnagram_sorting(s, t):
    """
    Approach: Sort both strings and compare.

    Why it works:
    - Anagrams have same characters
    - When sorted, same characters → same sorted string!

    Example:
        "anagram" → sorted → "aaagmnr"
        "nagaram" → sorted → "aaagmnr"
        Same! → True

    Time Complexity: O(n log n) - due to sorting
    Space Complexity: O(1) or O(n) for sorted copies
    """
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)


# ============================================================================
# SOLUTION 4: One Hash Map (Space Optimized)
# ============================================================================

def isAnagram_optimized(s, t):
    """
    Approach: Use single hash map!

    Algorithm:
    1. Increment count for chars in s
    2. Decrement count for chars in t
    3. If all counts are 0 → anagram!

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(s) != len(t):
        return False

    count = {}

    # Increment for s
    for char in s:
        count[char] = count.get(char, 0) + 1

    # Decrement for t
    for char in t:
        count[char] = count.get(char, 0) - 1

    # Check all counts are 0
    for freq in count.values():
        if freq != 0:
            return False

    return True


# ============================================================================
# SOLUTION 5: Array as Hash Map (For lowercase letters only)
# ============================================================================

def isAnagram_array(s, t):
    """
    Approach: Use array of size 26 for counting.

    Since only lowercase letters, we can use array instead of hash map!
    a→0, b→1, c→2, ..., z→25

    Time Complexity: O(n)
    Space Complexity: O(1) - fixed size array (26)
    """
    if len(s) != len(t):
        return False

    # Array of 26 zeros
    count = [0] * 26

    for i in range(len(s)):
        # Increment for s[i]
        count[ord(s[i]) - ord('a')] += 1
        # Decrement for t[i]
        count[ord(t[i]) - ord('a')] -= 1

    # Check all zeros
    return all(c == 0 for c in count)


# ============================================================================
# TEST CASES
# ============================================================================

def test():
    """Test all solutions"""

    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("listen", "silent", True),
        ("hello", "world", False),
        ("a", "a", True),
        ("ab", "ba", True),
        ("ab", "abc", False),
    ]

    solutions = [
        ("Hash Map", isAnagram),
        ("Counter", isAnagram_v2),
        ("Sorting", isAnagram_sorting),
        ("Optimized", isAnagram_optimized),
        ("Array", isAnagram_array),
    ]

    for name, solution in solutions:
        print(f"\n{'='*50}")
        print(f"Testing: {name}")
        print('='*50)

        all_passed = True
        for i, (s, t, expected) in enumerate(test_cases, 1):
            result = solution(s, t)
            status = "✅" if result == expected else "❌"
            print(f"Test {i}: {status} s='{s}', t='{t}' → {result} (Expected: {expected})")
            if result != expected:
                all_passed = False

        if all_passed:
            print(f"\n🎉 All tests passed for {name}!")


# ============================================================================
# VISUAL DEMO
# ============================================================================

def visual_demo(s, t):
    """
    Visual demonstration of the algorithm
    """
    print(f"\n{'='*60}")
    print(f"VISUAL DEMO: Is '{t}' an anagram of '{s}'?")
    print('='*60)

    # Step 1: Check lengths
    print(f"\nStep 1: Check lengths")
    print(f"  Length of '{s}': {len(s)}")
    print(f"  Length of '{t}': {len(t)}")

    if len(s) != len(t):
        print(f"  ❌ Different lengths → NOT anagram")
        return

    print(f"  ✅ Same length → Continue")

    # Step 2: Count frequencies
    print(f"\nStep 2: Count character frequencies")

    count_s = {}
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1

    count_t = {}
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    print(f"\n  Frequencies in '{s}':")
    for char in sorted(count_s.keys()):
        print(f"    '{char}': {count_s[char]}")

    print(f"\n  Frequencies in '{t}':")
    for char in sorted(count_t.keys()):
        print(f"    '{char}': {count_t[char]}")

    # Step 3: Compare
    print(f"\nStep 3: Compare frequencies")

    if count_s == count_t:
        print(f"  ✅ SAME frequencies → IS anagram!")
    else:
        print(f"  ❌ DIFFERENT frequencies → NOT anagram")

        # Show differences
        all_chars = set(count_s.keys()) | set(count_t.keys())
        for char in sorted(all_chars):
            freq_s = count_s.get(char, 0)
            freq_t = count_t.get(char, 0)
            if freq_s != freq_t:
                print(f"    '{char}': {freq_s} in s, {freq_t} in t ❌")


# ============================================================================
# WHAT YOU SHOULD LEARN
# ============================================================================

"""
KEY TAKEAWAYS:
-------------
1. FREQUENCY COUNTING is a fundamental pattern
2. Hash maps are perfect for counting occurrences
3. Python's Counter makes this trivial
4. Sorting is an alternative (slower but simple)

PATTERN RECOGNITION:
-------------------
When you see:
- "Same letters/characters"
- "Rearrange"
- "Permutation"
- "Frequency"

Think: FREQUENCY COUNTING with Hash Map!

INTERVIEW TIPS:
--------------
1. Always check length first (quick optimization)
2. Mention Counter for Python interviews
3. Know the array approach for follow-up
4. For Unicode: use hash map, not array

COMPLEXITY ANALYSIS:
-------------------
Hash Map: O(n) time, O(1) space (fixed alphabet)
Sorting:  O(n log n) time, O(1) space
Array:    O(n) time, O(1) space (only lowercase)

FOLLOW-UP ANSWER:
----------------
Q: What if inputs contain Unicode?
A: Hash map still works! Array won't (Unicode has 143,859 characters).
   Use Counter or regular dict.

NEXT STEPS:
----------
✅ Understood frequency counting
✅ Know multiple approaches
→ Now solve: Two Sum (uses complement search!)
"""


if __name__ == "__main__":
    # Run tests
    test()

    # Visual demos
    visual_demo("anagram", "nagaram")
    visual_demo("rat", "car")
    visual_demo("listen", "silent")
