"""
1D Dynamic Programming - Code Templates
========================================

Reusable skeletons for problems where the state is a single index: dp[i].

The five DP steps (from the guide):
  1. Define state    - what does dp[i] mean?
  2. Find recurrence - how does dp[i] use earlier states?
  3. Base cases      - what is known without computing?
  4. Order           - which direction fills the table?
  5. Answer          - which cell holds the result?
"""

from functools import lru_cache
from bisect import bisect_left


# ============================================================================
# TEMPLATE 1: Memoization (Top-Down) vs Tabulation (Bottom-Up)
# ============================================================================
# The same problem (climbing stairs) written both ways, so the translation
# from one to the other is visible line by line.

def climb_stairs_memo(n):
    """Top-down: recurse toward the base case, cache every answer."""
    memo = {}

    def dp(i):
        # 3. Base cases: 0 or 1 stair left => exactly one way to finish
        if i <= 1:
            return 1
        # Cache hit: this subproblem was already solved
        if i in memo:
            return memo[i]
        # 2. Recurrence: last move was a 1-step or a 2-step
        memo[i] = dp(i - 1) + dp(i - 2)
        return memo[i]

    return dp(n)


def climb_stairs_tab(n):
    """Bottom-up: same recurrence, but filled forward from the base cases."""
    if n <= 1:
        return 1

    # 1. State: dp[i] = number of ways to reach step i
    dp = [0] * (n + 1)

    # 3. Base cases (the memo's `if i <= 1` becomes explicit table entries)
    dp[0] = 1
    dp[1] = 1

    # 4. Order: increasing i, so dp[i-1] and dp[i-2] are already final
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # identical recurrence to the memo version

    # 5. Answer
    return dp[n]


def climb_stairs_lru(n):
    """Top-down with zero boilerplate: let the stdlib own the cache."""

    @lru_cache(maxsize=None)
    def dp(i):
        if i <= 1:
            return 1
        return dp(i - 1) + dp(i - 2)

    return dp(n)


# ============================================================================
# TEMPLATE 2: Space Optimisation with Rolling Variables
# ============================================================================
# When dp[i] only looks back a fixed number of steps, the array is wasted
# space: keep just those last few values in scalars.

def fib(n):
    """Fibonacci in O(1) space - the canonical rolling-variable pattern."""
    if n <= 1:
        return n

    prev2, prev1 = 0, 1  # dp[i-2], dp[i-1]

    for _ in range(2, n + 1):
        # Compute dp[i], then slide the window forward one position
        current = prev1 + prev2
        prev2, prev1 = prev1, current

    return prev1


def min_cost_climbing_stairs(cost):
    """Min Cost Climbing Stairs - rolling variables over the same recurrence."""
    # dp[i] = cheapest cost to *stand on* step i; start free on step 0 or 1
    prev2, prev1 = 0, 0

    for i in range(2, len(cost) + 1):
        # Step from i-1 (paying cost[i-1]) or from i-2 (paying cost[i-2])
        current = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
        prev2, prev1 = prev1, current

    return prev1


# ============================================================================
# TEMPLATE 3: House Robber (Take / Skip Decision)
# ============================================================================

def rob(nums):
    """Max sum with no two adjacent elements taken."""
    # rob1 = best through house i-2, rob2 = best through house i-1
    rob1, rob2 = 0, 0

    for num in nums:
        # Either rob this house (num + best two back) or skip it (best one back)
        take = num + rob1
        skip = rob2
        rob1, rob2 = rob2, max(take, skip)

    return rob2


def rob_circular(nums):
    """House Robber II - houses form a circle, so first and last are adjacent."""
    if len(nums) == 1:
        return nums[0]

    # A circle just forbids using house 0 and house n-1 together.
    # Solve two linear subproblems and take the better one:
    #   - houses [0 .. n-2] (drop the last)
    #   - houses [1 .. n-1] (drop the first)
    return max(rob(nums[:-1]), rob(nums[1:]))


# ============================================================================
# TEMPLATE 4: Unbounded Knapsack (Coin Change Family)
# ============================================================================

def coin_change(coins, amount):
    """Coin Change - fewest coins summing to amount, or -1 if impossible."""
    # State: dp[a] = min coins to make amount a. inf marks "unreachable".
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # zero coins make amount 0

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                # Use one `coin`, then solve the smaller amount a - coin
                dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_ii(coins, amount):
    """Coin Change II - count distinct combinations summing to amount."""
    dp = [0] * (amount + 1)
    dp[0] = 1  # one way to make 0: pick nothing

    # Coins in the OUTER loop => each combination is counted once, in a fixed
    # coin order. Swapping the loops would count permutations instead
    # (1+2 and 2+1 as two answers), which is a different problem.
    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] += dp[a - coin]

    return dp[amount]


# ============================================================================
# TEMPLATE 5: Longest Increasing Subsequence
# ============================================================================

def length_of_lis(nums):
    """LIS in O(n^2) - dp[i] = longest subsequence ENDING at index i."""
    if not nums:
        return 0

    dp = [1] * len(nums)  # every element alone is a subsequence of length 1

    for i in range(1, len(nums)):
        for j in range(i):
            # nums[i] can extend any earlier smaller-ending subsequence
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def length_of_lis_fast(nums):
    """LIS in O(n log n) - patience sorting with binary search."""
    # tails[k] = smallest possible tail value of an increasing subsequence
    # of length k+1. tails is always sorted, so it can be binary-searched.
    tails = []

    for num in nums:
        # bisect_left finds the first tail >= num. Using *left* (not right)
        # keeps the subsequence STRICTLY increasing: an equal tail gets
        # overwritten rather than extended.
        i = bisect_left(tails, num)

        if i == len(tails):
            tails.append(num)  # num beats every tail: LIS grew by one
        else:
            tails[i] = num  # a smaller tail for that length is always better

    # NOTE: tails is not the LIS itself, but its LENGTH is correct.
    return len(tails)


# ============================================================================
# TEMPLATE 6: Word Break (Partition a String)
# ============================================================================

def word_break(s, word_dict):
    """Can s be cut into a sequence of dictionary words?"""
    words = set(word_dict)  # O(1) membership

    # State: dp[i] = True if s[:i] is fully segmentable
    dp = [False] * (len(s) + 1)
    dp[0] = True  # the empty prefix always is

    for i in range(1, len(s) + 1):
        for j in range(i):
            # Split at j: prefix s[:j] must work AND s[j:i] must be a word
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break  # one valid split is enough

    return dp[len(s)]


# ============================================================================
# TEMPLATE 7: Decode Ways (Constrained Counting)
# ============================================================================

def num_decodings(s):
    """Count decodings of a digit string where 1->'A' ... 26->'Z'."""
    if not s or s[0] == '0':
        return 0

    # Rolling variables: dp[i-2], dp[i-1] over "ways to decode s[:i]"
    two_back, one_back = 1, 1  # empty prefix, and first (valid) character

    for i in range(1, len(s)):
        current = 0

        # Take s[i] alone - only legal if it is not '0'
        if s[i] != '0':
            current += one_back

        # Take s[i-1:i+1] as a pair - only legal in the range 10..26
        two_digit = int(s[i - 1:i + 1])
        if 10 <= two_digit <= 26:
            current += two_back

        two_back, one_back = one_back, current

    return one_back


# ============================================================================
# TEMPLATE 8: Expand Around Centre (Palindromes)
# ============================================================================
# Not a table, but the standard 1D-topic alternative to O(n^2) space DP.

def count_palindromic_substrings(s):
    """Palindromic Substrings - count every palindromic substring."""
    total = 0

    def expand(left, right):
        """Grow outward while the two ends match; return how many held."""
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    for i in range(len(s)):
        total += expand(i, i)      # odd length, centred on one character
        total += expand(i, i + 1)  # even length, centred between two

    return total


def longest_palindrome(s):
    """Longest Palindromic Substring - same expansion, tracking the best span."""
    if not s:
        return ""

    start, length = 0, 1

    def expand(left, right):
        nonlocal start, length
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > length:
                start, length = left, right - left + 1
            left -= 1
            right += 1

    for i in range(len(s)):
        expand(i, i)
        expand(i, i + 1)

    return s[start:start + length]


# ============================================================================
# TEMPLATE 9: Running Best (Maximum Product Subarray)
# ============================================================================

def max_product(nums):
    """Max product subarray - track min too, since a negative flips them."""
    result = max(nums)
    cur_max, cur_min = 1, 1

    for num in nums:
        # A negative num swaps the roles of the running max and min, so
        # compute both from the OLD cur_max before overwriting it.
        candidates = (num, cur_max * num, cur_min * num)
        cur_max, cur_min = max(candidates), min(candidates)
        result = max(result, cur_max)

    return result


# Example usage
if __name__ == "__main__":
    print(climb_stairs_memo(5), climb_stairs_tab(5), climb_stairs_lru(5))  # 8 8 8
    print(fib(10))                                    # 55
    print(rob([2, 7, 9, 3, 1]))                       # 12
    print(rob_circular([2, 3, 2]))                    # 3
    print(coin_change([1, 2, 5], 11))                 # 3
    print(coin_change_ii([1, 2, 5], 5))               # 4
    print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))       # 4
    print(length_of_lis_fast([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
    print(word_break("leetcode", ["leet", "code"]))   # True
    print(num_decodings("226"))                       # 3
    print(count_palindromic_substrings("aaa"))        # 6
    print(longest_palindrome("babad"))                # "bab"
    print(max_product([2, 3, -2, 4]))                 # 6
