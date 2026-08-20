"""
Problem: Longest Repeating Character Replacement
Difficulty: Medium
Topics: Hash Table, String, Sliding Window

Problem Statement:
-----------------
You are given a string s and an integer k. You can choose any character of
the string and change it to any other uppercase English character. You can
perform this operation AT MOST k times.

Return the length of the longest substring containing the same letter you
can get after performing the above operations.

Examples:
---------
Example 1:
    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's (or vice versa),
                 giving "BBBB" — a run of length 4.

Example 2:
    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' at index 3 with 'B' to form
                 "AABBBBA". The substring "BBBB" has length 4.

Example 3:
    Input: s = "AAAA", k = 0
    Output: 4
    Explanation: No replacements allowed, but the string is already one run.

Constraints:
-----------
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters
- 0 <= k <= s.length

LEARNING NOTES:
--------------
This is the sliding window problem where the WINDOW CONDITION is the
clever part, not the pointers. 🪟

Key Insight: Never think about WHICH letter to keep!
    For any window, the cheapest plan is obviously "keep the letter that
    already appears most often, replace everything else."

    replacements_needed = window_size - max_frequency_in_window

    Window is VALID  ⟺  (right - left + 1) - maxFreq <= k

    EXPAND right, and while that inequality is violated, SHRINK left.

Pattern: "Longest substring after at most K edits"
         → Variable Size Window + frequency count + a validity formula.

The formula IS the problem. Once you write
`window_size - maxFreq <= k` on the whiteboard, the code is the template.

Visualization:
    s = "AABABBA", k = 1

    right=0 'A'  window="A"       counts{A:1}      size1-max1=0 <=1 ✓ best=1
        [A]A B A B B A
    right=1 'A'  window="AA"      counts{A:2}      size2-max2=0 <=1 ✓ best=2
        [A A]B A B B A
    right=2 'B'  window="AAB"     counts{A:2,B:1}  size3-max2=1 <=1 ✓ best=3
        [A A B]A B B A
    right=3 'A'  window="AABA"    counts{A:3,B:1}  size4-max3=1 <=1 ✓ best=4
        [A A B A]B B A
    right=4 'B'  window="AABAB"   counts{A:3,B:2}  size5-max3=2 >1  ✗
        SHRINK once: drop s[0]='A' → left=1
        A[A B A B]B A                              size4-max3=1 <=1 ✓ best=4
        (maxFreq stays at its high-water mark of 3 — see Solution 1 for
         why that is safe. The window SLIDES rather than shrinking.)
    right=5 'B'  slides once more → size 4, best=4
    right=6 'A'  slides once more → size 4, best=4

    Answer: 4 ✅
"""


# ============================================================================
# SOLUTION 1: Sliding Window + Non-Decreasing maxFreq (OPTIMAL!)
# ============================================================================

def characterReplacement(s, k):
    """
    Approach: Grow a window; it is valid while size - maxFreq <= k.

    Algorithm:
    1. count = {} holds letter frequencies inside the window
    2. maxFreq = the largest frequency ever seen in a VALID window
    3. For each right:
         a. count[s[right]] += 1                     (EXPAND)
         b. maxFreq = max(maxFreq, count[s[right]])
         c. While (right - left + 1) - maxFreq > k:  (SHRINK)
              count[s[left]] -= 1; left += 1
         d. best = max(best, right - left + 1)
    4. Return best

    The famous trick — why we never DECREASE maxFreq:
    - We only care about the LONGEST valid window, never shorter ones.
    - A window can only beat our record if it contains some letter more
      often than maxFreq — and that would raise maxFreq on the spot.
    - So a stale (too large) maxFreq can only make us skip windows that
      were already too short to matter. The final answer is unaffected.
    - Consequence: the window never actually shrinks, it just SLIDES, and
      the while loop runs at most once per step.

    Time Complexity: O(n) - single pass, O(1) work per character
    Space Complexity: O(1) - the count map holds at most 26 uppercase keys
    """
    count = {}       # letter → frequency inside the window
    left = 0
    max_freq = 0     # highest frequency seen so far (never decreased)
    best = 0

    for right in range(len(s)):
        # EXPAND: pull s[right] into the window
        count[s[right]] = count.get(s[right], 0) + 1
        max_freq = max(max_freq, count[s[right]])

        # SHRINK while we'd need more than k replacements
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best


# ============================================================================
# SOLUTION 2: Sliding Window + Recomputed maxFreq (Easier to justify)
# ============================================================================

def characterReplacement_recompute(s, k):
    """
    Approach: Same window, but recompute maxFreq honestly on every check.

    Algorithm:
    1. Identical to Solution 1, except the validity test uses
       max(count.values()) — the TRUE current maximum — instead of a
       remembered high-water mark.

    Why bother:
    - No cleverness to defend. The invariant is literally
      "this window needs at most k replacements", at all times.
    - If the stale-maxFreq argument doesn't click during an interview,
      write THIS, get it correct, then mention the optimization.

    Time Complexity: O(26n) = O(n) - the alphabet is a constant 26 letters
    Space Complexity: O(1) - at most 26 keys

    Slower by a constant factor, identical answers. Verified by the tests.
    """
    count = {}
    left = 0
    best = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1

        # True max frequency currently inside the window
        while (right - left + 1) - max(count.values()) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]   # keep max() honest
            left += 1

        best = max(best, right - left + 1)

    return best


# ============================================================================
# SOLUTION 3: One Window Per Candidate Letter (Nice mental model)
# ============================================================================

def characterReplacement_perletter(s, k):
    """
    Approach: Fix the letter we intend to keep, then slide a simple window.

    Algorithm:
    1. For each distinct letter c appearing in s:
         a. Slide a window counting how many characters are NOT c
         b. While that count exceeds k → shrink from the left
         c. Track the largest valid window
    2. Return the best over all 26 letters

    Why show this:
    - It makes the problem obvious: "keep c, replace up to k others."
    - Solution 1 is exactly this, run for all letters SIMULTANEOUSLY by
      always betting on the current most frequent letter.

    Time Complexity: O(26n) = O(n) - one linear pass per letter
    Space Complexity: O(1) - a couple of counters
    """
    best = 0

    for c in set(s):
        left = 0
        not_c = 0   # characters in the window that must be replaced

        for right in range(len(s)):
            if s[right] != c:
                not_c += 1

            while not_c > k:
                if s[left] != c:
                    not_c -= 1
                left += 1

            best = max(best, right - left + 1)

    return best


# ============================================================================
# SOLUTION 4: Brute Force over All Substrings (DON'T use! Just for learning)
# ============================================================================

def characterReplacement_bruteforce(s, k):
    """
    Approach: Check every substring against the replacement budget.

    Algorithm:
    1. For every start i, walk j forward maintaining a count map
    2. size = j - i + 1, needed = size - max(count.values())
    3. If needed <= k, the substring is achievable → record its length

    Time Complexity: O(26n²) ≈ O(n²) - Too slow!
    Space Complexity: O(1) - 26 keys

    For n=100000: ~5 BILLION inner steps. 😱 Guaranteed TLE.
    Note this version is already "smart" brute force (counts are built
    incrementally). The truly naive O(n³) version is even worse.
    """
    best = 0

    for i in range(len(s)):
        count = {}
        for j in range(i, len(s)):
            count[s[j]] = count.get(s[j], 0) + 1
            size = j - i + 1
            needed = size - max(count.values())
            if needed <= k:
                best = max(best, size)

    return best


# ============================================================================
# TEST CASES
# ============================================================================

def test():
    """Test all solutions"""

    test_cases = [
        ("ABAB", 2, 4),          # replace both A's → "BBBB"
        ("AABABBA", 1, 4),       # classic example → "BBBB"
        ("AAAA", 0, 4),          # already one run, no budget needed
        ("ABCDE", 0, 1),         # no budget → longest existing run
        ("ABAB", 0, 1),          # alternating, no budget
        ("A", 0, 1),             # single character
        ("ABBB", 2, 4),          # replace the lone A
        ("AABBBCCC", 2, 5),      # ⭐ budget can't cover the whole string
        ("XYYX", 2, 4),          # k equals the number of odd letters
        ("ABAA", 0, 2),          # trailing run wins
        ("AAAB", 0, 3),          # leading run wins
        ("ABCDE", 5, 5),         # k >= length → whole string
        ("AABABBA", 0, 2),       # ⭐ same string, zero budget
        ("", 0, 0),              # empty input (defensive)
    ]

    solutions = [
        ("Window + maxFreq (Optimal)", characterReplacement),
        ("Window + recomputed maxFreq", characterReplacement_recompute),
        ("One window per letter", characterReplacement_perletter),
        ("Brute Force", characterReplacement_bruteforce),
    ]

    for name, solution in solutions:
        print(f"\n{'='*50}")
        print(f"Testing: {name}")
        print('='*50)

        all_passed = True
        for i, (s, k, expected) in enumerate(test_cases, 1):
            result = solution(s, k)
            is_correct = result == expected

            status = "✅" if is_correct else "❌"
            print(f"Test {i}: {status} s={s!r}, k={k} → {result} "
                  f"(expected {expected})")
            if not is_correct:
                all_passed = False

        if all_passed:
            print(f"\n🎉 All tests passed for {name}!")


# ============================================================================
# VISUAL DEMO
# ============================================================================

def visual_demo(s, k):
    """
    Visual step-by-step demonstration of the window and its validity formula
    """
    print(f"\n{'='*70}")
    print("VISUAL DEMO: Longest Repeating Character Replacement")
    print(f"Input: s={s!r}, k={k}")
    print('='*70)

    if not s:
        print("\nEmpty string → answer is 0")
        return

    count = {}
    left = 0
    max_freq = 0
    best = 0
    best_window = ""

    print("\nRule: window is VALID while (size - maxFreq) <= k")
    print("      because we replace every non-majority letter.\n")

    for right in range(len(s)):
        c = s[right]
        count[c] = count.get(c, 0) + 1
        max_freq = max(max_freq, count[c])

        print(f"Step {right + 1}: right={right}, char={c!r}")
        size = right - left + 1
        print(f"  Added {c!r} → counts "
              f"{ {ch: n for ch, n in sorted(count.items()) if n > 0} }")
        print(f"  size={size}, maxFreq={max_freq}, "
              f"replacements needed = {size} - {max_freq} = "
              f"{size - max_freq}")

        while (right - left + 1) - max_freq > k:
            print(f"  ⚠️  needs {(right - left + 1) - max_freq} > k={k} → "
                  f"shrink: drop {s[left]!r}, left {left} → {left + 1}")
            count[s[left]] -= 1
            left += 1

        size = right - left + 1
        picture = s[:left] + "[" + s[left:right + 1] + "]" + s[right + 1:]
        print(f"  Window: {picture}   → {s[left:right + 1]!r} (len {size})")

        if size > best:
            best = size
            best_window = s[left:right + 1]
            print(f"  ✅ New longest: {best_window!r} (length {best})")
        print()

    print(f"FINAL: best window {best_window!r}, length = {best} 🎯")
    if best_window:
        keep = max(set(best_window), key=best_window.count)
        used = len(best_window) - best_window.count(keep)
        print(f"  Keep {keep!r}, replace the other {used} character(s) "
              f"(budget was {k})")


# ============================================================================
# WHAT YOU SHOULD LEARN
# ============================================================================

"""
KEY TAKEAWAYS:
-------------
1. The hard part is the VALIDITY FORMULA, not the pointer mechanics:
       replacements needed = window_size - maxFreq
2. You never choose the target letter. The most frequent letter in the
   current window is always the right bet.
3. maxFreq may be left stale (never decreased) and the answer stays
   correct — because only a LONGER window can beat the record, and any
   such window would push maxFreq up itself.
4. With a stale maxFreq the window never shrinks, it slides: strict O(n).
5. When in doubt, recompute maxFreq (Solution 2). O(26n) is still O(n)
   and it is far easier to prove on a whiteboard.

PATTERN RECOGNITION:
-------------------
When you see:
- "At most K changes / flips / replacements"
- "Longest subarray of all 1s after flipping K zeros"
- "Longest run of the same value with a budget"

Think: SLIDING WINDOW + COUNT MAP + "size - best_count <= budget"!

INTERVIEW TIPS:
--------------
1. Derive the formula out loud before coding. That is the whole signal.
2. Offer the per-letter version (Solution 3) as an intuition warm-up —
   it shows you understand WHY the maxFreq trick works.
3. Say why the window never shrinks under the optimization; interviewers
   ask this exact follow-up.
4. Trace "AABABBA", k=1 by hand. It exercises both expand and shrink.
5. Edge cases: k = 0 (longest existing run) and k >= len(s) (whole string).

COMMON MISTAKES:
---------------
❌ Trying all 26 letters INSIDE the loop and calling it O(n) — it's O(26n),
   fine here, but know what you actually wrote.
❌ Forgetting `count[s[left]] -= 1` when shrinking → counts drift and the
   formula silently lies.
❌ In the recompute version, leaving zero-valued keys in the map. Harmless
   for max(), fatal if you ever switch to `len(count)` as your condition.
❌ Using `if` instead of `while` for shrinking in the recompute version.
❌ Calling max(count.values()) on an empty map — guard the empty string.

VARIATIONS:
----------
- Max Consecutive Ones III → same window, values are just 0/1
- Longest Substring Without Repeating Characters → the k=0-ish sibling
- Permutation in String → FIXED size window + exact frequency match
- Minimum Window Substring → shrink to MINIMIZE instead of maximize

TIME COMPLEXITY COMPARISON:
--------------------------
Brute Force:          O(26n²) time, O(1) space
Per-letter windows:   O(26n)  time, O(1) space
Recomputed maxFreq:   O(26n)  time, O(1) space
Tracked maxFreq:      O(n)    time, O(1) space ← BEST!

NEXT STEPS:
----------
✅ Mastered the "budget" style window condition
✅ Know the stale-maxFreq argument
→ Now try: Permutation in String (fixed size window)
→ Then: Minimum Window Substring (hard, shrink-to-minimize)

PRACTICE MORE:
-------------
Similar problems to practice this pattern:
- Max Consecutive Ones III
- Permutation in String
- Minimum Window Substring (hard)
- Longest Substring with At Most K Distinct Characters
- Fruit Into Baskets
"""


if __name__ == "__main__":
    # Run tests
    test()

    # Visual demonstrations
    visual_demo("AABABBA", 1)
    visual_demo("ABAB", 2)

    # Interactive practice
    print("\n" + "="*70)
    print("YOUR TURN TO TRACE!")
    print("="*70)
    print("\nTry tracing through this example yourself:")
    print('s = "AABBBCCC", k = 2')
    print("\nWhich letter wins the window? Where does left stop?")
    print('Write it out, then run: visual_demo("AABBBCCC", 2)')
