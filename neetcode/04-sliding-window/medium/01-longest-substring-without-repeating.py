"""
Problem: Longest Substring Without Repeating Characters
Difficulty: Medium
Topics: Hash Table, String, Sliding Window

Problem Statement:
-----------------
Given a string s, find the length of the longest substring without
repeating characters.

A substring is a CONTIGUOUS, non-empty sequence of characters within a
string. (Contrast with a subsequence, which may skip characters.)

Examples:
---------
Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
                 Notice that "pwke" is a SUBSEQUENCE, not a substring!

Constraints:
-----------
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces

LEARNING NOTES:
--------------
This is THE flagship variable-size sliding window problem! ⭐

Key Insight: Keep the window ALWAYS VALID.
    Window = s[left..right] with all-distinct characters.

    EXPAND: right moves forward one character at a time.
    SHRINK: while the new character is already inside the window,
            drop s[left] and move left forward.

    After the while loop the window is valid again, so we can safely
    record its length: right - left + 1.

Pattern: "Longest substring satisfying a condition"
         → Variable Size Window + a hash set/map of window contents.

Why O(n) and not O(n²)?
    `left` never moves backwards and `right` never moves backwards.
    Each index is added once and removed at most once → 2n moves.

Visualization:
    s = "abcabcbb"

    right=0 'a'  window="a"      no dup   → len 1, best=1
        [a]b c a b c b b
    right=1 'b'  window="ab"     no dup   → len 2, best=2
        [a b]c a b c b b
    right=2 'c'  window="abc"    no dup   → len 3, best=3
        [a b c]a b c b b
    right=3 'a'  DUPLICATE 'a'!
        shrink: drop s[0]='a', left=1  → window="bca"
        a[b c a]b c b b                → len 3, best=3
    right=4 'b'  DUPLICATE 'b'!
        shrink: drop s[1]='b', left=2  → window="cab"
        a b[c a b]c b b                → len 3, best=3
    right=5 'c'  DUPLICATE 'c'!
        shrink: drop s[2]='c', left=3  → window="abc"
        a b c[a b c]b b                → len 3, best=3
    right=6 'b'  DUPLICATE 'b'!
        shrink: drop s[3]='a', left=4  → window="bcb"? still dup
        shrink: drop s[4]='b', left=5  → window="cb"
        a b c a b[c b]b                → len 2, best=3
    right=7 'b'  DUPLICATE 'b'!
        shrink: drop s[5]='c', left=6  → still dup
        shrink: drop s[6]='b', left=7  → window="b"
        a b c a b c b[b]               → len 1, best=3

    Answer: 3 ✅
"""


# ============================================================================
# SOLUTION 1: Sliding Window + Hash Set (OPTIMAL!)
# ============================================================================

def lengthOfLongestSubstring(s):
    """
    Approach: Grow a window on the right, shrink from the left on duplicates.

    Algorithm:
    1. window = set() holds the characters currently inside [left, right]
    2. For each right:
         a. While s[right] is already in window → SHRINK:
              remove s[left] from window, left += 1
         b. Add s[right] to window (EXPAND)
         c. best = max(best, right - left + 1)
    3. Return best

    Why the `while` (not `if`)?
    - Only one copy of a character can be in a set-based window at a time,
      so in practice this loop runs until that one duplicate is evicted.
      A `while` states the invariant plainly: "shrink until valid".

    Time Complexity: O(n) - each index enters and leaves the window once
    Space Complexity: O(min(n, m)) - m = size of the character alphabet;
                      the set never holds more than m distinct characters
    """
    window = set()   # characters currently in s[left..right]
    left = 0
    best = 0

    for right in range(len(s)):
        # SHRINK until the window is valid again
        while s[right] in window:
            window.remove(s[left])
            left += 1

        # EXPAND
        window.add(s[right])

        # Window is valid here → safe to record its length
        best = max(best, right - left + 1)

    return best


# ============================================================================
# SOLUTION 2: Sliding Window + Last-Seen Index Map (Fewer steps!)
# ============================================================================

def lengthOfLongestSubstring_jump(s):
    """
    Approach: Remember WHERE each character was last seen, then jump.

    Instead of shrinking one character at a time, teleport `left` directly
    past the previous occurrence of the duplicate.

    Algorithm:
    1. last_seen = {} maps character → its most recent index
    2. For each right:
         a. c = s[right]
         b. If c in last_seen AND last_seen[c] >= left:
              left = last_seen[c] + 1        # jump past the old copy
         c. last_seen[c] = right
         d. best = max(best, right - left + 1)
    3. Return best

    The `last_seen[c] >= left` guard is ESSENTIAL:
    - Stale entries for characters already outside the window must be
      ignored, otherwise `left` could move BACKWARDS and inflate the answer.

    Time Complexity: O(n) - one pass, O(1) work per character
    Space Complexity: O(min(n, m)) - one entry per distinct character
    """
    last_seen = {}   # char → last index where we saw it
    left = 0
    best = 0

    for right, c in enumerate(s):
        # Only jump if the previous copy is INSIDE the current window
        if c in last_seen and last_seen[c] >= left:
            left = last_seen[c] + 1

        last_seen[c] = right
        best = max(best, right - left + 1)

    return best


# ============================================================================
# SOLUTION 3: Brute Force with a Set per Start (DON'T use! Just for learning)
# ============================================================================

def lengthOfLongestSubstring_bruteforce(s):
    """
    Approach: For every start index, walk forward until a repeat appears.

    Algorithm:
    1. For every start i
    2. Walk j from i forward, collecting characters in a set
    3. Stop at the first repeat, record the length

    Time Complexity: O(n²) - Too slow!
    Space Complexity: O(min(n, m))

    For n=50000: up to 1.25 BILLION steps. 😱
    The sliding window does 50,000. Same answer, 25,000x less work.
    """
    best = 0

    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j - i + 1)

    return best


# ============================================================================
# SOLUTION 4: Brute Force over All Substrings (WORST! Educational only)
# ============================================================================

def lengthOfLongestSubstring_allsubstrings(s):
    """
    Approach: Generate every substring and test whether it is all-distinct.

    Algorithm:
    1. For every (i, j) pair, slice s[i:j]
    2. A slice is all-distinct iff len(set(slice)) == len(slice)
    3. Track the longest that passes

    Time Complexity: O(n³) - n² substrings, each costing O(n) to check
    Space Complexity: O(min(n, m))

    This is the naive "just do what the problem says" version. It is here
    purely so you can FEEL the difference. Never write this in an interview
    without immediately saying "...and here is how I'd make it O(n)".
    """
    best = 0

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            piece = s[i:j]
            if len(set(piece)) == len(piece):
                best = max(best, len(piece))

    return best


# ============================================================================
# TEST CASES
# ============================================================================

def test():
    """Test all solutions"""

    test_cases = [
        ("abcabcbb", 3),          # classic example → "abc"
        ("bbbbb", 1),             # all same character
        ("pwwkew", 3),            # answer is "wke", not "pwke"
        ("", 0),                  # empty string
        ("a", 1),                 # single character
        ("au", 2),                # two distinct characters
        ("dvdf", 3),              # ⭐ the famous "jump" trap → "vdf"
        ("abba", 2),              # ⭐ stale-index trap → "ab" / "ba"
        ("tmmzuxt", 5),           # ⭐ another stale-index trap → "mzuxt"
        ("abcdefg", 7),           # all distinct → whole string
        ("aab", 2),               # duplicate at the front
        (" ", 1),                 # a space is a valid character
        ("a b!a b!", 4),          # symbols and spaces count too
    ]

    solutions = [
        ("Sliding Window + Set (Optimal)", lengthOfLongestSubstring),
        ("Sliding Window + Index Jump", lengthOfLongestSubstring_jump),
        ("Brute Force (per start)", lengthOfLongestSubstring_bruteforce),
        ("Brute Force (all substrings)",
         lengthOfLongestSubstring_allsubstrings),
    ]

    for name, solution in solutions:
        print(f"\n{'='*50}")
        print(f"Testing: {name}")
        print('='*50)

        all_passed = True
        for i, (s, expected) in enumerate(test_cases, 1):
            result = solution(s)
            is_correct = result == expected

            status = "✅" if is_correct else "❌"
            print(f"Test {i}: {status} s={s!r} → {result} "
                  f"(expected {expected})")
            if not is_correct:
                all_passed = False

        if all_passed:
            print(f"\n🎉 All tests passed for {name}!")


# ============================================================================
# VISUAL DEMO
# ============================================================================

def visual_demo(s):
    """
    Visual step-by-step demonstration of the expanding/shrinking window
    """
    print(f"\n{'='*70}")
    print("VISUAL DEMO: Longest Substring Without Repeating Characters")
    print(f"Input: {s!r}")
    print('='*70)

    if not s:
        print("\nEmpty string → answer is 0")
        return

    window = set()
    left = 0
    best = 0
    best_substring = ""

    print("\nStep-by-step execution:\n")

    for right in range(len(s)):
        c = s[right]
        print(f"Step {right + 1}: right={right}, char={c!r}")

        # SHRINK phase
        shrinks = 0
        while c in window:
            print(f"  ⚠️  {c!r} already in window {sorted(window)} → "
                  f"shrink: drop {s[left]!r}, left {left} → {left + 1}")
            window.remove(s[left])
            left += 1
            shrinks += 1

        if shrinks == 0:
            print(f"  No duplicate. Window stays anchored at left={left}")

        # EXPAND phase
        window.add(c)
        length = right - left + 1

        # Draw the window as brackets around the substring
        picture = s[:left] + "[" + s[left:right + 1] + "]" + s[right + 1:]
        print(f"  Window: {picture}   → {s[left:right + 1]!r} (len {length})")

        if length > best:
            best = length
            best_substring = s[left:right + 1]
            print(f"  ✅ New longest: {best_substring!r} (length {best})")
        print()

    print(f"FINAL: longest substring = {best_substring!r}, length = {best} 🎯")


# ============================================================================
# WHAT YOU SHOULD LEARN
# ============================================================================

"""
KEY TAKEAWAYS:
-------------
1. The window INVARIANT is everything: "s[left..right] has no repeats."
   Restore the invariant BEFORE measuring the window.
2. EXPAND with `right` in the for loop; SHRINK with `left` in a while loop.
3. A hash set answers "is this character in my window?" in O(1).
4. Both pointers only move forward → O(n), not O(n²).
5. The index-map version is faster in practice but needs the
   `last_seen[c] >= left` guard. That guard is the whole bug surface.

PATTERN RECOGNITION:
-------------------
When you see:
- "Longest / shortest substring such that ..."
- "At most K distinct ..." / "no repeating ..."
- "Contiguous" + "optimize length"

Think: VARIABLE SIZE SLIDING WINDOW + HASH MAP/SET!

THE TEMPLATE (memorize this shape):
----------------------------------
    left = 0
    for right in range(len(s)):
        add s[right] to window state
        while window is invalid:
            remove s[left] from window state
            left += 1
        best = max(best, right - left + 1)

(Solution 1 checks validity before adding, which is the same idea with
the add and the check swapped — pick one and stay consistent.)

INTERVIEW TIPS:
--------------
1. Clarify substring vs subsequence out loud. Interviewers listen for this.
2. Say the invariant before you code: "I'll keep the window duplicate-free."
3. Walk "dvdf" or "abba" by hand — those expose off-by-one bugs instantly.
4. State complexity with the reason: "each index enters and exits once."
5. If asked to return the substring itself, store `left` when you update
   `best`, then slice at the end.

COMMON MISTAKES:
---------------
❌ Using `if` instead of `while` when shrinking in the SET version.
❌ In the index-map version, forgetting `last_seen[c] >= left`.
   On "abba" that moves left BACKWARDS and returns 3 instead of 2.
❌ Setting `left = right` on a duplicate — throws away valid characters.
   On "dvdf" that returns 2 instead of 3.
❌ Measuring the window while it is still invalid.
❌ Off-by-one in the length: it is right - left + 1, not right - left.

VARIATIONS:
----------
- Longest Substring with At Most K Distinct Characters → count map, shrink
  while len(map) > k
- Longest Repeating Character Replacement → shrink on (size - maxFreq) > k
- Permutation in String → FIXED size window + frequency match
- Minimum Window Substring → the hard sibling; shrink to MINIMIZE

TIME COMPLEXITY COMPARISON:
--------------------------
All substrings:     O(n³) time, O(min(n,m)) space
Per-start scan:     O(n²) time, O(min(n,m)) space
Sliding window:     O(n)  time, O(min(n,m)) space ← BEST!

NEXT STEPS:
----------
✅ Mastered the expand/shrink template
✅ Know why both pointers moving forward gives O(n)
→ Now try: Longest Repeating Character Replacement
→ Then: Permutation in String, Minimum Window Substring

PRACTICE MORE:
-------------
Similar problems to practice this pattern:
- Longest Repeating Character Replacement
- Permutation in String
- Minimum Window Substring (hard)
- Longest Substring with At Most Two Distinct Characters
- Fruit Into Baskets
"""


if __name__ == "__main__":
    # Run tests
    test()

    # Visual demonstrations
    visual_demo("abcabcbb")
    visual_demo("dvdf")

    # Interactive practice
    print("\n" + "="*70)
    print("YOUR TURN TO TRACE!")
    print("="*70)
    print("\nTry tracing through this example yourself:")
    print('s = "tmmzuxt"')
    print("\nWatch carefully at the LAST 't' — where does left end up?")
    print('Write it out, then run: visual_demo("tmmzuxt")')
