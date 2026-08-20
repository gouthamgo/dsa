"""
Backtracking - Code Templates
=============================

Every template here is the same three-line dance:

    choose   -> path.append(x)      / mark something used
    explore  -> recurse
    unchoose -> path.pop()          / unmark it

If you forget the un-choose, state leaks into sibling branches and the
answers come out wrong. That pop() is not optional.
"""

# ============================================================================
# TEMPLATE 1: The General Backtracking Skeleton
# ============================================================================

def backtrack_skeleton(nums, k):
    """
    The shape every backtracking solution takes, shown on a concrete task:
    collect every k-element combination of `nums`.

    1. BASE CASE   - path is a complete solution: record a COPY and return.
    2. PRUNE       - path can never become valid: return early (huge speedup).
    3. FOR EACH choice available at this level:
         a. CHOOSE   apply the choice to the shared state
         b. EXPLORE  recurse one level deeper
         c. UNCHOOSE undo exactly what (a) did

    `path` is one mutable list reused by the whole recursion, which is why
    step (c) matters and why we append `path[:]` (a copy) to the result.

    Swap the three marked lines and you have subsets, permutations,
    combination sum, N-Queens - the scaffolding never changes.
    """
    result = []

    def backtrack(start, path):
        # 1. BASE CASE - a complete solution
        if len(path) == k:
            result.append(path[:])      # COPY - path keeps mutating after this
            return

        # 2. PRUNE - not enough elements left to ever reach length k
        if len(nums) - start < k - len(path):
            return

        # 3. Iterate over the choices legal at this depth
        for i in range(start, len(nums)):
            path.append(nums[i])        # a. CHOOSE
            backtrack(i + 1, path)      # b. EXPLORE
            path.pop()                  # c. UNCHOOSE  <- never delete this

    backtrack(0, [])
    return result


# ============================================================================
# TEMPLATE 2: Subsets (Power Set)
# ============================================================================

def subsets(nums):
    """
    All 2^n subsets of a distinct-element list.

    Every node of the recursion tree is itself a valid subset, so we record
    on entry rather than only at the leaves. `start` prevents re-picking an
    earlier element, which is what makes [1,2] and [2,1] the same subset.

    Time: O(n * 2^n)   Space: O(n) recursion (excluding output)
    """
    result = []

    def backtrack(start, path):
        result.append(path[:])          # every prefix is a subset

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)      # i+1: each element used at most once
            path.pop()

    backtrack(0, [])
    return result


def subsets_include_exclude(nums):
    """
    Same result, framed as a binary decision per element.

    At index i you either take nums[i] or you don't - two branches, depth n,
    hence exactly 2^n leaves.
    """
    result = []

    def backtrack(i, path):
        if i == len(nums):
            result.append(path[:])
            return

        # Branch A: include nums[i]
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()

        # Branch B: exclude nums[i]
        backtrack(i + 1, path)

    backtrack(0, [])
    return result


# ============================================================================
# TEMPLATE 3: Permutations
# ============================================================================

def permutations(nums):
    """
    All n! orderings, using a `used` boolean array.

    Unlike subsets there is no `start` index: every unused element is a legal
    choice at every level, which is exactly why order matters here.

    Time: O(n * n!)   Space: O(n)
    """
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue            # already placed earlier in this path

            used[i] = True          # CHOOSE
            path.append(nums[i])

            backtrack(path)         # EXPLORE

            path.pop()              # UNCHOOSE - both pieces of state!
            used[i] = False

    backtrack([])
    return result


def permutations_swap(nums):
    """
    In-place variant: swap element i into position `first`, recurse, swap back.

    Avoids the `used` array; the prefix nums[:first] is the fixed part.
    """
    result = []

    def backtrack(first):
        if first == len(nums):
            result.append(nums[:])
            return

        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]     # CHOOSE
            backtrack(first + 1)                            # EXPLORE
            nums[first], nums[i] = nums[i], nums[first]     # UNCHOOSE

    backtrack(0)
    return result


# ============================================================================
# TEMPLATE 4: Combinations (choose k from n)
# ============================================================================

def combinations(n, k):
    """
    All k-sized combinations of 1..n.

    The pruning line is the interesting part: if even taking every remaining
    number cannot fill `path` to length k, stop looping now.

    Time: O(k * C(n, k))   Space: O(k)
    """
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return

        need = k - len(path)                # how many more we must pick
        # Last viable start is n - need + 1; anything beyond can't finish.
        for i in range(start, n - need + 2):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return result


# ============================================================================
# TEMPLATE 5: Combination Sum (unlimited reuse of each candidate)
# ============================================================================

def combination_sum(candidates, target):
    """
    All combinations summing to target; each candidate may be reused.

    The one-character difference from "no reuse" is `backtrack(i, ...)`
    instead of `backtrack(i + 1, ...)` - staying on i lets us pick it again.

    Time: O(n^(target/min_candidate))   Space: O(target/min_candidate)
    """
    result = []
    candidates.sort()               # enables the early break below

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return

        for i in range(start, len(candidates)):
            # Sorted, so once one candidate overshoots, all later ones do too.
            if candidates[i] > remaining:
                break               # PRUNE the whole rest of the loop

            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])   # i, not i+1: reuse
            path.pop()

    backtrack(0, [], target)
    return result


# ============================================================================
# TEMPLATE 6: Duplicates - the Sort-and-Skip Trick
# ============================================================================

def subsets_with_duplicates(nums):
    """
    Subsets II: input may contain duplicates, output must not repeat a subset.

    Sort first so equal values sit together, then at each level skip any
    value identical to its left neighbour. The `i > start` guard is the crux:
    the FIRST copy at this level is allowed, later copies would only rebuild
    a branch we already explored.

    Time: O(n * 2^n)   Space: O(n)
    """
    result = []
    nums.sort()                     # duplicates become adjacent

    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue            # same value already tried at this level

            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


def permutations_with_duplicates(nums):
    """
    Permutations II: distinct orderings when the input has repeats.

    Skip nums[i] if it equals nums[i-1] AND that twin is not currently used -
    i.e. the twin was already tried and undone at this same level. Requiring
    "not used[i-1]" forces duplicates to be consumed left-to-right, so each
    multiset ordering is generated exactly once.

    Time: O(n * n!) worst case   Space: O(n)
    """
    result = []
    nums.sort()
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue            # its identical twin is free -> already tried

            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return result


# ============================================================================
# TEMPLATE 7: Constraint Tracking with Sets (N-Queens style)
# ============================================================================

def solve_n_queens(n):
    """
    Place n queens on an n x n board so none attack each other.

    Place exactly one queen per row, so rows never clash by construction.
    Three sets make each conflict check O(1):

        cols          -> column index
        diagonals     -> (r - c) is constant along a "\" diagonal
        anti_diagonals-> (r + c) is constant along a "/" diagonal

    Time: O(n!)   Space: O(n)
    """
    result = []
    cols = set()
    diagonals = set()           # r - c
    anti_diagonals = set()      # r + c
    board = []                  # board[r] = column of the queen in row r

    def backtrack(row):
        if row == n:
            # Render the solution as the usual list of "..Q.." strings.
            result.append(['.' * c + 'Q' + '.' * (n - c - 1) for c in board])
            return

        for col in range(n):
            diag = row - col
            anti = row + col

            if col in cols or diag in diagonals or anti in anti_diagonals:
                continue                    # square is attacked - PRUNE

            cols.add(col)                   # CHOOSE
            diagonals.add(diag)
            anti_diagonals.add(anti)
            board.append(col)

            backtrack(row + 1)              # EXPLORE

            board.pop()                     # UNCHOOSE - all four pieces
            anti_diagonals.remove(anti)
            diagonals.remove(diag)
            cols.remove(col)

    backtrack(0)
    return result


# ============================================================================
# TEMPLATE 8: Grid Word Search (backtracking on a 2D board)
# ============================================================================

def word_search(board, word):
    """
    True if `word` can be spelled by adjacent cells, no cell reused.

    Marking is done in-place with a sentinel '#': cheaper than a visited set
    and trivially undone on the way out.

    Time: O(rows * cols * 4^L), L = len(word)   Space: O(L) recursion
    """
    if not board or not board[0]:
        return False

    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True                     # matched every character

        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[i]:
            return False                    # also catches the '#' sentinel

        temp = board[r][c]
        board[r][c] = '#'                   # CHOOSE: mark as on-path

        found = (dfs(r + 1, c, i + 1) or
                 dfs(r - 1, c, i + 1) or
                 dfs(r, c + 1, i + 1) or
                 dfs(r, c - 1, i + 1))

        board[r][c] = temp                  # UNCHOOSE: restore the letter
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False


# ============================================================================
# TEMPLATE 9: Partitioning a String (Palindrome Partitioning)
# ============================================================================

def palindrome_partition(s):
    """
    Every way to cut `s` into pieces that are all palindromes.

    The choice at each level is "where does the next piece end?". Only cuts
    that produce a palindrome are explored, which prunes hard.

    Time: O(n * 2^n)   Space: O(n)
    """
    result = []

    def is_palindrome(lo, hi):
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True

    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])          # consumed the whole string
            return

        for end in range(start, len(s)):
            if not is_palindrome(start, end):
                continue                    # PRUNE: bad first piece

            path.append(s[start:end + 1])
            backtrack(end + 1, path)
            path.pop()

    backtrack(0, [])
    return result


# ============================================================================
# TEMPLATE 10: Mapped Choices (Letter Combinations of a Phone Number)
# ============================================================================

def letter_combinations(digits):
    """
    Cartesian product driven by a lookup table.

    Depth = number of digits; branching factor = letters on that digit.

    Time: O(4^n * n)   Space: O(n)
    """
    if not digits:
        return []

    keypad = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
    }

    result = []

    def backtrack(i, path):
        if i == len(digits):
            result.append(''.join(path))
            return

        for char in keypad[digits[i]]:      # choices for THIS digit only
            path.append(char)
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result
