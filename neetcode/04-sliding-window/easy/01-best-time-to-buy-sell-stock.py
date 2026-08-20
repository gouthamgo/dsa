"""
Problem: Best Time to Buy and Sell Stock
Difficulty: Easy
Topics: Array, Sliding Window, Dynamic Programming

Problem Statement:
-----------------
You are given an array prices where prices[i] is the price of a given stock
on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you
cannot achieve any profit, return 0.

Examples:
---------
Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6).
                 Profit = 6 - 1 = 5.
                 Note: buying on day 2 and selling on day 1 is NOT allowed
                 because you must buy before you sell.

Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: Prices only go down. No transaction is made, profit = 0.

Example 3:
    Input: prices = [2,4,1]
    Output: 2
    Explanation: Buy at 2, sell at 4. Profit = 2. The later 1 is useless.

Constraints:
-----------
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

LEARNING NOTES:
--------------
This is the gentlest introduction to SLIDING WINDOW! 🪟

Key Insight: The window is [buy_day, sell_day]!
    left  = the day we are considering buying  (window start)
    right = the day we are considering selling (window end)

    If prices[right] < prices[left], the window is INVALID as a trade
    (we would lose money), so we SHRINK by jumping left to right.
    That new lower price is a strictly better buy day for everything ahead.

    Otherwise the window is VALID → record the profit and EXPAND right.

Pattern: "Best pair where the earlier one is small" → Variable Size Window
         (track the best-so-far minimum on the left).

Visualization:
    prices = [7, 1, 5, 3, 6, 4]

    left=0(7) right=1(1)
        1 < 7 → losing window! Shrink: left jumps to 1
        [7, 1, 5, 3, 6, 4]
            L=R                     max_profit = 0

    left=1(1) right=2(5)
        5 - 1 = 4 → best so far!
        [7, 1, 5, 3, 6, 4]
            L  R                    max_profit = 4

    left=1(1) right=3(3)
        3 - 1 = 2 → not better
        [7, 1, 5, 3, 6, 4]
            L     R                 max_profit = 4

    left=1(1) right=4(6)
        6 - 1 = 5 → new best!
        [7, 1, 5, 3, 6, 4]
            L        R              max_profit = 5 ✅

    left=1(1) right=5(4)
        4 - 1 = 3 → not better
        [7, 1, 5, 3, 6, 4]
            L           R           max_profit = 5

    Answer: 5
"""


# ============================================================================
# SOLUTION 1: Sliding Window / Two Pointers (OPTIMAL!)
# ============================================================================

def maxProfit(prices):
    """
    Approach: Keep a window [left, right] = [buy day, sell day].

    Algorithm:
    1. Start left = 0 (buy day), right = 1 (sell day)
    2. If prices[left] < prices[right] → profitable window
         → profit = prices[right] - prices[left]
         → max_profit = max(max_profit, profit)
    3. Else (price dropped) → this new price is a better buy day
         → SHRINK the window: left = right
    4. EXPAND: right += 1
    5. Repeat until right runs off the end

    Why shrinking to `right` is safe:
    - If prices[right] <= prices[left], then for ANY future sell day d,
      prices[d] - prices[right] >= prices[d] - prices[left].
    - So the old left can never beat the new one. Drop it forever.

    Time Complexity: O(n) - right visits each day exactly once
    Space Complexity: O(1) - only two pointers and one counter
    """
    if len(prices) < 2:
        return 0

    left = 0          # buy day  (window start)
    right = 1         # sell day (window end)
    max_profit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            # Valid window → take the profit if it's the best we've seen
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            # Price dropped → new, cheaper buy day. Shrink window.
            left = right

        right += 1  # Always expand

    return max_profit


# ============================================================================
# SOLUTION 2: Track Minimum So Far (Same idea, one pointer)
# ============================================================================

def maxProfit_minsofar(prices):
    """
    Approach: The left pointer is really just "cheapest price so far".

    Algorithm:
    1. min_price = infinity, max_profit = 0
    2. For each price:
         a. If price < min_price → update min_price (new buy day)
         b. Else → max_profit = max(max_profit, price - min_price)
    3. Return max_profit

    This is the exact same algorithm as Solution 1, written without an
    explicit `left`. Many people find this version easier to recall in an
    interview. Use whichever you can explain confidently!

    Time Complexity: O(n) - one pass
    Space Complexity: O(1) - two scalars
    """
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit


# ============================================================================
# SOLUTION 3: Maximum Subarray of Daily Changes (Kadane's algorithm)
# ============================================================================

def maxProfit_kadane(prices):
    """
    Approach: Turn prices into daily deltas, then find max subarray sum.

    Insight:
    - Buying at day i and selling at day j gives prices[j] - prices[i]
    - That telescopes into the SUM of daily changes from i+1 to j
    - So "best trade" == "maximum sum contiguous subarray of deltas"

    Algorithm:
    1. current = 0, best = 0
    2. For each consecutive pair, delta = prices[i] - prices[i-1]
    3. current = max(0, current + delta)   (0 = "start a fresh window")
    4. best = max(best, current)

    Time Complexity: O(n) - one pass
    Space Complexity: O(1) - deltas computed on the fly

    Why show this: it connects Sliding Window to Dynamic Programming.
    Same O(n), but the min-so-far version is clearer for this problem.
    """
    current = 0
    best = 0

    for i in range(1, len(prices)):
        delta = prices[i] - prices[i - 1]
        current = max(0, current + delta)
        best = max(best, current)

    return best


# ============================================================================
# SOLUTION 4: Brute Force (DON'T use! Just for learning)
# ============================================================================

def maxProfit_bruteforce(prices):
    """
    Approach: Try every (buy day, sell day) pair.

    Algorithm:
    1. For every buy day i
    2. For every sell day j > i
    3. Track the biggest prices[j] - prices[i]

    Time Complexity: O(n²) - Too slow!
    Space Complexity: O(1)

    For n=100000: ~5 BILLION comparisons! 😱 Guaranteed TLE.
    The optimal version does 100,000. That is the whole lesson.
    """
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit

    return max_profit


# ============================================================================
# TEST CASES
# ============================================================================

def test():
    """Test all solutions"""

    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),      # classic example
        ([7, 6, 4, 3, 1], 0),         # only decreasing → no trade
        ([2, 4, 1], 2),               # best pair is early
        ([1, 2], 1),                  # smallest profitable input
        ([2, 1], 0),                  # two days, price drops
        ([5], 0),                     # single day → cannot sell
        ([], 0),                      # empty input
        ([3, 3, 3, 3], 0),            # flat prices → no profit
        ([1, 4, 2, 10], 9),           # dip in the middle, buy at start
        ([9, 2, 8, 1, 7], 6),         # two separate dips
        ([0, 10000], 10000),          # constraint extremes
    ]

    solutions = [
        ("Sliding Window (Optimal)", maxProfit),
        ("Min So Far", maxProfit_minsofar),
        ("Kadane on Deltas", maxProfit_kadane),
        ("Brute Force", maxProfit_bruteforce),
    ]

    for name, solution in solutions:
        print(f"\n{'='*50}")
        print(f"Testing: {name}")
        print('='*50)

        all_passed = True
        for i, (prices, expected) in enumerate(test_cases, 1):
            result = solution(prices.copy())
            is_correct = result == expected

            status = "✅" if is_correct else "❌"
            print(f"Test {i}: {status} prices={prices} → {result} "
                  f"(expected {expected})")
            if not is_correct:
                all_passed = False

        if all_passed:
            print(f"\n🎉 All tests passed for {name}!")


# ============================================================================
# VISUAL DEMO
# ============================================================================

def visual_demo(prices):
    """
    Visual step-by-step demonstration of the sliding window
    """
    print(f"\n{'='*70}")
    print("VISUAL DEMO: Best Time to Buy and Sell Stock")
    print(f"Input: {prices}")
    print('='*70)

    if len(prices) < 2:
        print("\nFewer than 2 days → cannot buy AND sell. Answer: 0")
        return

    left = 0
    right = 1
    max_profit = 0
    best_days = None

    print("\nStep-by-step execution:\n")

    step = 1
    while right < len(prices):
        # Draw the window
        marks = []
        for i in range(len(prices)):
            if i == left and i == right:
                marks.append("LR")
            elif i == left:
                marks.append("L ")
            elif i == right:
                marks.append("R ")
            else:
                marks.append("  ")

        print(f"Step {step}:")
        print(f"  {prices}")
        print(f"   " + " ".join(f"{m}" for m in marks))
        print(f"  buy day  left={left} (price {prices[left]})")
        print(f"  sell day right={right} (price {prices[right]})")

        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            print(f"  Valid window → profit = {prices[right]} - "
                  f"{prices[left]} = {profit}")
            if profit > max_profit:
                max_profit = profit
                best_days = (left, right)
                print(f"  ✅ New best profit: {max_profit}")
            else:
                print(f"  Not better than current best ({max_profit})")
        else:
            print(f"  Price dropped ({prices[right]} <= {prices[left]}) → "
                  f"shrink: left jumps to {right}")
            left = right

        right += 1
        step += 1
        print()

    print(f"FINAL: max profit = {max_profit}")
    if best_days:
        b, s = best_days
        print(f"  Buy on day {b} at {prices[b]}, "
              f"sell on day {s} at {prices[s]} 📈")
    else:
        print("  No profitable trade exists — hold your cash. 💤")


# ============================================================================
# WHAT YOU SHOULD LEARN
# ============================================================================

"""
KEY TAKEAWAYS:
-------------
1. A sliding window does not have to be about substrings — here the
   window is simply [buy day, sell day].
2. EXPAND with `right`, SHRINK with `left`. That's the whole template.
3. When shrinking, jumping left all the way to right is legal here
   because a lower price dominates every earlier price forever.
4. Each element is visited at most twice → O(n).

PATTERN RECOGNITION:
-------------------
When you see:
- "Buy before you sell" / "j must come after i"
- "Maximum difference where the larger element comes later"
- "Best pair in one pass"

Think: SLIDING WINDOW / TRACK-THE-MINIMUM-SO-FAR!

THE ONE-LINE IDEA:
-----------------
At every day, ask: "If I sell TODAY, what is the cheapest day I could
have bought?" Keep that cheapest price in a variable. Done.

INTERVIEW TIPS:
--------------
1. State the constraint out loud: "I must buy strictly before I sell."
2. Mention brute force O(n²) first, then immediately improve it.
3. Explain the greedy claim: "A new minimum makes every older buy day
   obsolete." That sentence is what the interviewer wants to hear.
4. Handle edge cases: empty list, one day, strictly decreasing prices.
5. Bonus points: mention the Kadane / max-subarray connection.

COMMON MISTAKES:
---------------
❌ Returning max(prices) - min(prices) — ignores the ordering!
   [2, 1] would wrongly give 1 instead of 0.
❌ Initializing max_profit to -infinity — profit can never be negative,
   we're allowed to just NOT trade. Start at 0.
❌ Crashing on an empty or single-element list.
❌ Moving `left` by 1 instead of jumping to `right` (still correct here,
   but slower and shows shakier reasoning).

VARIATIONS:
----------
- Best Time to Buy and Sell Stock II → unlimited transactions (greedy:
  add every positive delta)
- Best Time to Buy and Sell Stock with Cooldown → 2D DP
- Maximum Average Subarray I → FIXED size window instead of variable
- Maximum Subarray → the Kadane version of this very problem

TIME COMPLEXITY COMPARISON:
--------------------------
Brute Force:        O(n²) time, O(1) space
Sliding Window:     O(n)  time, O(1) space ← BEST!
Kadane on deltas:   O(n)  time, O(1) space (same, different lens)

NEXT STEPS:
----------
✅ Understand expand/shrink pointers
✅ Know the "minimum so far" trick
→ Now try: Longest Substring Without Repeating Characters (medium!)
→ Then: Longest Repeating Character Replacement

PRACTICE MORE:
-------------
Similar problems to practice this pattern:
- Maximum Average Subarray I (fixed window)
- Maximum Subarray (Kadane)
- Best Time to Buy and Sell Stock II
- Container With Most Water (two pointers cousin)
"""


if __name__ == "__main__":
    # Run tests
    test()

    # Visual demonstrations
    visual_demo([7, 1, 5, 3, 6, 4])
    visual_demo([7, 6, 4, 3, 1])

    # Interactive practice
    print("\n" + "="*70)
    print("YOUR TURN TO TRACE!")
    print("="*70)
    print("\nTry tracing through this example yourself:")
    print("prices = [3, 8, 1, 9, 2]")
    print("\nWhere does `left` jump? What is the final profit?")
    print("Write it out, then run: visual_demo([3, 8, 1, 9, 2])")
