# Backtracking - Complete Guide

## 🎯 What is Backtracking?

An algorithmic technique that builds solutions incrementally and abandons ("backtracks") when a solution can't be completed.

Think: **Try, check, undo, try again**

**Visual:**
```
Finding all subsets of [1,2,3]:

         []
       /  |  \
     [1] [2] [3]
     /|   |
[1,2][1,3]...

Try adding element → Recurse → Remove (backtrack)
```

It is **DFS over a decision tree you never actually build**. The tree exists
only as the call stack: each recursive call is a node, each loop iteration an
edge. `path` is your current position in that tree, and `path.pop()` is how
you walk back up.

## 🧠 Core Template

```python
def backtrack(path, choices):
    if is_solution(path):
        result.append(path.copy())
        return

    for choice in choices:
        # Make choice
        path.append(choice)

        # Recurse
        backtrack(path, new_choices)

        # Undo choice (BACKTRACK!)
        path.pop()
```

### Why the undo is mandatory

There is exactly **one** `path` list, shared by every call in the recursion.
When a branch returns, `path` must be left exactly as the caller handed it
over — otherwise the next sibling branch starts from polluted state.

```
path = [1]
  ├─ append 2 → [1,2] → explore → pop → [1]   ✅ sibling sees [1]
  └─ append 3 → [1,3]                          ✅ correct

path = [1]                    (WITHOUT the pop)
  ├─ append 2 → [1,2] → explore → (no pop) → [1,2]  ☠️
  └─ append 3 → [1,2,3]                              ☠️ wrong branch
```

Same rule applies to *every* piece of shared state: a `used[]` array, a
`visited` set, a modified board cell, the three sets in N-Queens. **Whatever
you mutated on the way in, unmutate on the way out.**

## 🔑 When to Use

- ✅ Find all combinations/permutations
- ✅ Solve puzzles (Sudoku, N-Queens)
- ✅ Generate all possibilities
- ✅ Constraint satisfaction problems

### Trigger phrases in the problem statement

| You read this... | It's backtracking |
|---|---|
| "return **all** possible..." | enumerate the whole tree |
| "find **every** combination / permutation / subset" | classic |
| "generate all valid ..." | build + prune on validity |
| "**how many ways** can..." (and n is small) | count the leaves |
| "partition the string into..." | choose where each cut goes |
| "place N items so that no two conflict" | constraint tracking |
| "solve this puzzle / board" | try, recurse, undo |

**The size check.** Backtracking is exponential, so the constraints tell you
it's intended: n ≤ 20 for subsets (2²⁰ ≈ 1M), n ≤ 10 for permutations
(10! ≈ 3.6M), a 9×9 Sudoku. If n can be 10⁵, it is **not** backtracking —
you're looking at greedy or DP.

**Backtracking vs DP.** Both explore choices. If the question asks for *all
the actual solutions*, you must enumerate them → backtracking. If it asks
only for a *count* or an *optimum* and subproblems repeat, memoise → DP.
"List every path" is backtracking; "how many paths" with big n is DP.

## 💡 Common Patterns

### 1. Subsets
```python
def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path.copy())

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # Backtrack!

    backtrack(0, [])
    return result
```

### 2. Permutations
```python
def permute(nums):
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path.copy())
            return

        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()

    backtrack([], nums)
    return result
```

### 3. Combination Sum
```python
def combinationSum(candidates, target):
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(path.copy())
            return
        if total > target:
            return  # Prune!

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return result
```

### 4. The `start` index — the single most important dial

Look at what changes between the three patterns above. It's one argument:

| Recursive call | Meaning | Produces |
|---|---|---|
| `backtrack(i + 1, ...)` | each element usable **once**, order irrelevant | subsets, combinations |
| `backtrack(i, ...)` | element **reusable**, order irrelevant | combination sum |
| no `start`, loop from 0 with `used[]` | each element once, **order matters** | permutations |

`start` is what prevents `[1,2]` and `[2,1]` from both appearing. Drop it and
you get permutations; keep it and you get combinations. Understanding this
one line turns five "different" problems into one.

### 5. Handling duplicates — sort and skip

When the input has repeats, identical branches produce identical answers.
Sort so equal values are adjacent, then skip a value that equals its left
neighbour *at the same tree level*:

```python
nums.sort()
for i in range(start, len(nums)):
    if i > start and nums[i] == nums[i - 1]:
        continue          # this value was already tried at this level
```

`i > start` is the crux. The **first** copy at a level is allowed; later
copies would only rebuild a branch already explored.

```
[1,2,2] without the skip          [1,2,2] with the skip
  [] [1] [1,2] [1,2,2]              [] [1] [1,2] [1,2,2]
  [1,2] ← duplicate!                [2] [2,2]
  [2] [2,2] [2] ← duplicate!        6 unique subsets ✅
```

For **permutations** with duplicates the guard is different — you need
`not used[i-1]`, which forces duplicates to be consumed left to right:

```python
if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
    continue
```

### 6. Constraint tracking (N-Queens)

Rather than re-scanning the board for conflicts, maintain sets of what's
already attacked. The diagonal identities are the trick:

```
r - c is constant along a "\" diagonal
r + c is constant along a "/" diagonal
```

```
r+c values (anti-diagonals)     r-c values (diagonals)
  0 1 2 3                         0 -1 -2 -3
  1 2 3 4                         1  0 -1 -2
  2 3 4 5                         2  1  0 -1
  3 4 5 6                         3  2  1  0
```

Place one queen per row (rows can't clash by construction), and each conflict
check becomes an O(1) set lookup. Remember to remove from **all** the sets
when backtracking.

## ⚡ Complexity Analysis

| Problem | Time | Space (excl. output) |
|---|---|---|
| Subsets | O(n · 2ⁿ) | O(n) |
| Permutations | O(n · n!) | O(n) |
| Combinations C(n,k) | O(k · C(n,k)) | O(k) |
| Combination Sum | O(n^(target/min)) | O(target/min) |
| Word Search (grid) | O(rows · cols · 4^L) | O(L) |
| N-Queens | O(n!) | O(n) |
| Palindrome Partitioning | O(n · 2ⁿ) | O(n) |

**How to derive these.** Count the leaves, then multiply by the cost of
recording one solution:

- Subsets: each element is in or out → 2ⁿ leaves, × O(n) to copy the path.
- Permutations: n choices, then n−1, then n−2 → n! leaves, × O(n) to copy.
- Word Search: any of rows·cols starting cells, then ≤4 directions (really 3
  after the first, since you can't go back) for L levels → 4^L.

**Space is O(depth), not O(leaves)** — the recursion stack only ever holds
one root-to-node path. The output itself is separate and usually dominates.

**Pruning doesn't change the big-O but hugely changes the wall clock.**
N-Queens is O(n!) on paper; the three-set conflict check kills branches so
early that n=8 solves instantly.

## 🐛 Common Pitfalls

1. **Forgetting `path.pop()`.** The number-one bug. Results come out
   progressively longer and wrong.

2. **Appending `path` instead of `path.copy()`.** You store a *reference* to
   the one mutable list, so every entry in `result` ends up identical
   (usually all empty, since `path` is `[]` by the time you return):
   ```python
   result.append(path)         # ☠️ all entries alias the same list
   result.append(path[:])      # ✅ snapshot
   ```

3. **Undoing only *some* of the state.** In N-Queens it's easy to remove from
   `cols` but forget `anti_diagonals`. In permutations, easy to `path.pop()`
   but forget `used[i] = False`. Undo everything you did.

4. **`i` vs `start` in the duplicate skip.** `if i > 0 and ...` instead of
   `if i > start and ...` for subsets wrongly kills valid branches — it
   forbids `[2,2]` entirely.

5. **Forgetting to sort before the skip trick.** The whole technique relies
   on duplicates being adjacent. No sort, no dedup.

6. **Passing `i` when you meant `i + 1`** (or vice versa). `i` allows reuse
   and will infinite-loop if a candidate is 0 or negative; `i + 1` forbids it.

7. **Not restoring the grid in Word Search.** `board[r][c] = '#'` needs its
   matching `board[r][c] = temp` on every exit path, including early returns.
   Put the restore after the recursion, never inside a branch.

8. **Pruning too late.** Checking `if total > target` only at the top of the
   call is fine, but checking it *before* recursing saves an entire call. On
   sorted input, `break` beats `continue` — once one candidate overshoots,
   all later ones do too.

9. **Mutating the input and returning it.** `permutations_swap` restores the
   array, but you must append `nums[:]` (a copy) at the base case.

## 🔬 Worked Example: Subsets of [1,2,3], Traced

`backtrack(start, path)` records `path` on entry, then loops `i` from
`start`. Indentation = recursion depth.

```
call(0, [])            record []
  i=0: append 1 → [1]
    call(1, [1])       record [1]
      i=1: append 2 → [1,2]
        call(2,[1,2])  record [1,2]
          i=2: append 3 → [1,2,3]
            call(3,...) record [1,2,3]   (loop body empty, returns)
          pop → [1,2]
        returns
      pop → [1]
      i=2: append 3 → [1,3]
        call(3,[1,3])  record [1,3]
      pop → [1]
    returns
  pop → []
  i=1: append 2 → [2]
    call(2,[2])        record [2]
      i=2: append 3 → [2,3]
        call(3,[2,3])  record [2,3]
      pop → [2]
    returns
  pop → []
  i=2: append 3 → [3]
    call(3,[3])        record [3]
  pop → []
returns
```

Result, in generation order:
`[] [1] [1,2] [1,2,3] [1,3] [2] [2,3] [3]` — 8 = 2³ subsets. ✅

**Two things to notice.** First, `path` returns to `[]` at the end — every
append was matched by a pop. That's the invariant to check when debugging.
Second, `[2,1]` never appears: `start` guarantees indices only ever increase.

## 📝 Problems in This Category

### Medium
1. **Subsets** ⭐ — the canonical starting point. Learn this shape first.
2. **Combination Sum** ⭐ — introduces reuse (`i` not `i+1`) and pruning.
3. **Permutations** ⭐ — introduces `used[]` and "order matters".
4. **Subsets II** — Subsets + the sort-and-skip trick.
5. **Combination Sum II** — reuse forbidden *and* duplicates present.
6. **Word Search** — backtracking on a 2D grid; in-place marking.
7. **Palindrome Partitioning** — the choice is *where to cut*, not what to take.
8. **Letter Combinations of a Phone Number** — choices come from a lookup table.

### Hard
9. **N-Queens** ⭐ — constraint tracking with three sets; the payoff problem.

Also worth doing once you're comfortable: **Sudoku Solver** (same shape as
N-Queens with richer constraints) and **Word Search II** (topic 08 — trie +
backtracking combined).

**Suggested order:** Subsets → Combination Sum → Permutations → Subsets II →
Combination Sum II → Letter Combinations → Word Search → Palindrome
Partitioning → N-Queens.

## 💡 Pro Tips

1. **Draw the decision tree**
2. **Prune early** to save time
3. **Remember to backtrack** (undo choice)
4. **Use `path.copy()`** when adding to result
5. **Ask "what is the choice at this level?"** before writing any code — the
   loop body follows from the answer. Choices are usually: which element to
   take next, or where to make the next cut, or which cell to move to.
6. **Debug by printing `path` at each entry** with indentation `"  " * depth`.
   The tree it prints is the tree you drew — if they differ, you found the bug.
7. **Check the invariant:** `path` must be empty again when the top-level call
   returns. If it isn't, a pop is missing.

Time: Often O(2ⁿ) or O(n!) - exponential!
Space: O(n) for recursion stack

## 🚀 Next Steps

1. Study `template.py` — all ten patterns
2. Write Subsets from a blank file until the skeleton is automatic
3. Do Permutations and Combination Sum; note that only `start` changed
4. Attempt N-Queens once the shape feels natural

---
**Backtracking is brute force done smart!** 🔄
