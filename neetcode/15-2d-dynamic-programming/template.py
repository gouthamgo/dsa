"""
2D Dynamic Programming - Code Templates
========================================

Reusable skeletons for problems whose state needs TWO indices: dp[i][j].

Two families dominate:
  - Grid paths      : dp[i][j] = best/count for cell (i, j)
  - Two sequences   : dp[i][j] = answer for first i of A vs first j of B
"""


# ============================================================================
# TEMPLATE 1: 2D Grid DP Skeleton
# ============================================================================

def grid_dp_skeleton(grid):
    """The shape every grid DP takes: base row, base column, then fill."""
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]

    # Base cell: nothing precedes the origin
    dp[0][0] = grid[0][0]

    # Base column: the only way in is from directly above
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Base row: the only way in is from directly left
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Interior: combine the two predecessors. Row-major order guarantees
    # dp[i-1][j] and dp[i][j-1] are already final when dp[i][j] is computed.
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[rows - 1][cols - 1]


def min_path_sum(grid):
    """Minimum Path Sum - the skeleton above, applied directly."""
    return grid_dp_skeleton(grid)


# ============================================================================
# TEMPLATE 2: Unique Paths (Counting Grid Paths)
# ============================================================================

def unique_paths(m, n):
    """Count paths from top-left to bottom-right moving only right/down."""
    # Base row and base column are all 1: exactly one straight-line route
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            # Arrive from above or from the left; the counts simply add
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


def unique_paths_1d(m, n):
    """Same count in O(n) space - one row rolled downward."""
    dp = [1] * n  # the base row

    for _ in range(1, m):
        for j in range(1, n):
            # Before the write, dp[j] still holds the row ABOVE (dp[i-1][j])
            # and dp[j-1] already holds this row (dp[i][j-1]).
            dp[j] += dp[j - 1]

    return dp[n - 1]


def unique_paths_with_obstacles(grid):
    """Unique Paths II - a 1 in the grid marks a blocked cell."""
    rows, cols = len(grid), len(grid[0])

    if grid[0][0] == 1:
        return 0

    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = 1

    # Base column: an obstacle severs everything below it (dp stays 0)
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] if grid[i][0] == 0 else 0

    # Base row: same, to the right
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] if grid[0][j] == 0 else 0

    for i in range(1, rows):
        for j in range(1, cols):
            if grid[i][j] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            # else leave 0: no path may pass through an obstacle

    return dp[rows - 1][cols - 1]


# ============================================================================
# TEMPLATE 3: Two-Sequence DP (Longest Common Subsequence)
# ============================================================================

def longest_common_subsequence(text1, text2):
    """LCS - the reference shape for every "compare two strings" problem."""
    m, n = len(text1), len(text2)

    # (m+1) x (n+1) so row 0 / column 0 mean "empty prefix".
    # Those zeros ARE the base cases - no extra initialisation needed.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # dp[i][j] covers text1[:i] against text2[:j], so the characters
            # being compared are at index i-1 and j-1.
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # match: consume both
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # drop one side

    return dp[m][n]


# ============================================================================
# TEMPLATE 4: Edit Distance (Two Sequences with Non-Zero Base Cases)
# ============================================================================

def min_distance(word1, word2):
    """Minimum insert/delete/replace operations turning word1 into word2."""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases are NOT zero here: emptying a prefix costs one delete per
    # character, and building one up costs one insert per character.
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # free: characters already agree
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # delete word1[i-1]
                    dp[i][j - 1],      # insert word2[j-1]
                    dp[i - 1][j - 1],  # replace word1[i-1] with word2[j-1]
                )

    return dp[m][n]


# ============================================================================
# TEMPLATE 5: 0/1 Knapsack
# ============================================================================

def knapsack_2d(weights, values, capacity):
    """0/1 Knapsack - dp[i][w] = best value using the first i items."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Always allowed: skip item i-1
            dp[i][w] = dp[i - 1][w]

            # Allowed only if it fits: take it, and add the best packing of
            # the REMAINING capacity using the earlier items (row i-1).
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                )

    return dp[n][capacity]


def knapsack_1d(weights, values, capacity):
    """Same answer in O(capacity) space - one row updated in place."""
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        # THE REVERSE LOOP IS THE WHOLE TRICK.
        # dp[w] is being overwritten row by row, so dp[w - weights[i]] must
        # still hold the PREVIOUS row's value (item i not yet used). Going
        # downward from `capacity`, every cell we read (a lower index) has
        # not been touched yet this iteration, so it is still row i-1.
        # Iterating forward would read a cell already updated with item i,
        # letting the same item be taken repeatedly - that is the UNBOUNDED
        # knapsack, a different problem.
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]


def can_partition(nums):
    """Partition Equal Subset Sum - 0/1 knapsack over reachable sums."""
    total = sum(nums)
    if total % 2 != 0:
        return False  # an odd total can never split evenly

    target = total // 2

    # dp[s] = can some subset sum to exactly s?
    dp = [False] * (target + 1)
    dp[0] = True  # the empty subset

    for num in nums:
        # Reverse again, for exactly the reason above: each num is usable once
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]

    return dp[target]


# ============================================================================
# TEMPLATE 6: Coin Change II as a 2D Table
# ============================================================================

def coin_change_ii_2d(coins, amount):
    """Count combinations - the 2D form makes the coin dimension explicit."""
    n = len(coins)
    dp = [[0] * (amount + 1) for _ in range(n + 1)]

    # With any prefix of coins there is exactly one way to make amount 0
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for a in range(1, amount + 1):
            dp[i][a] = dp[i - 1][a]  # skip coin i-1 entirely
            if coins[i - 1] <= a:
                # Use coin i-1 and STAY on row i: it may be reused (unbounded)
                dp[i][a] += dp[i][a - coins[i - 1]]

    return dp[n][amount]


# ============================================================================
# TEMPLATE 7: Interval DP
# ============================================================================

def interval_dp_skeleton(arr):
    """Longest Palindromic Subsequence - the canonical interval-DP shape."""
    n = len(arr)
    if n == 0:
        return 0

    # State: dp[i][j] = answer for the closed interval arr[i..j]
    dp = [[0] * n for _ in range(n)]

    # Base: every single element is an interval of length 1
    for i in range(n):
        dp[i][i] = 1

    # ORDER MATTERS: intervals must be filled by increasing LENGTH, because
    # dp[i][j] depends on strictly shorter intervals inside it. (Equivalently,
    # loop i downward and j upward - both keep the dependencies ready.)
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if arr[i] == arr[j]:
                # Both ends join the answer; recurse on the interior
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                # Drop one end or the other
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # Answer lives in the widest interval: the whole array
    return dp[0][n - 1]


# ============================================================================
# TEMPLATE 8: State-Machine DP (Buy/Sell with Cooldown)
# ============================================================================

def max_profit_with_cooldown(prices):
    """Two states per day - holding a stock, or free to buy."""
    if not prices:
        return 0

    # hold = best profit while owning a share
    # free = best profit while owning nothing and allowed to buy
    # cooling = best profit while owning nothing but just sold (must rest)
    hold = -prices[0]
    free = 0
    cooling = 0

    for price in prices[1:]:
        # Read all three from the PREVIOUS day before overwriting any
        new_hold = max(hold, free - price)      # keep holding, or buy today
        new_free = max(free, cooling)           # stay free, or finish cooldown
        new_cooling = hold + price              # sell today
        hold, free, cooling = new_hold, new_free, new_cooling

    return max(free, cooling)  # never end the day still holding


# Example usage
if __name__ == "__main__":
    print(min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))   # 7
    print(unique_paths(3, 7), unique_paths_1d(3, 7))         # 28 28
    print(unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
    print(longest_common_subsequence("abcde", "ace"))        # 3
    print(min_distance("horse", "ros"))                      # 3
    print(knapsack_2d([1, 3, 4, 5], [1, 4, 5, 7], 7))        # 9
    print(knapsack_1d([1, 3, 4, 5], [1, 4, 5, 7], 7))        # 9
    print(can_partition([1, 5, 11, 5]))                      # True
    print(coin_change_ii_2d([1, 2, 5], 5))                   # 4
    print(interval_dp_skeleton("bbbab"))                     # 4
    print(max_profit_with_cooldown([1, 2, 3, 0, 2]))         # 3
