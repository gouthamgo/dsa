# Ultimate DSA Cheat Sheet

**Print this and keep it next to you while coding!**

---

## 🎯 Pattern Recognition (Memorize This!)

```
KEYWORDS → PATTERN

"pair", "two sum", "complement"
  → HASH MAP (unsorted) or TWO POINTERS (sorted)

"substring", "subarray", "contiguous"
  → SLIDING WINDOW

"sorted array", "search", "O(log n)"
  → BINARY SEARCH

"palindrome", "reverse", "compare ends"
  → TWO POINTERS (opposite direction)

"matching pairs", "valid parentheses", "nested"
  → STACK

"all combinations", "all permutations", "generate all"
  → BACKTRACKING

"count ways", "maximum value", "minimum cost", "optimal"
  → DYNAMIC PROGRAMMING

"top K", "K largest", "K smallest"
  → HEAP / PRIORITY QUEUE

"shortest path", "level by level", "minimum steps"
  → BFS (Breadth-First Search)

"all paths", "detect cycle", "explore deep"
  → DFS (Depth-First Search)

"intervals", "merge", "scheduling", "overlapping"
  → INTERVALS (sort first!)

"frequency", "count occurrences", "anagram"
  → HASH MAP
```

---

## ⚡ Complexity Cheat Sheet

```
┌────────────────────────────────────────────┐
│         TIME COMPLEXITY SCALE              │
├────────────────────────────────────────────┤
│ O(1)       → ✅ Instant    (hash lookup)   │
│ O(log n)   → ✅ Very fast  (binary search) │
│ O(n)       → ✅ Fast       (single loop)   │
│ O(n log n) → ✅ Good       (efficient sort)│
│ O(n²)      → ⚠️  Slow      (nested loops)  │
│ O(2^n)     → ❌ Very slow  (exponential)   │
│ O(n!)      → ❌ Terrible   (factorial)     │
└────────────────────────────────────────────┘

RULES:
- Single loop = O(n)
- Nested loops = O(n²)
- Halving each step = O(log n)
- Sorting = O(n log n)
- Recursion tree with 2 branches = O(2^n)
```

---

## 📝 Code Templates

### Template 1: Hash Map Pattern
```python
def solve(arr, target):
    seen = {}  # or set()

    for item in arr:
        # Check if what we need is in map
        if target - item in seen:
            return [seen[target - item], item]

        # Store current item
        seen[item] = True

    return []

# Use for: Two Sum, Anagram, Frequency Count
# Time: O(n), Space: O(n)
```

### Template 2: Two Pointers (Opposite)
```python
def solve(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        # Calculate something with both pointers
        if condition:
            left += 1   # Move left if need bigger
        else:
            right -= 1  # Move right if need smaller

    return result

# Use for: Sorted array pairs, Palindrome, Container
# Time: O(n), Space: O(1)
```

### Template 3: Two Pointers (Same Direction)
```python
def solve(arr):
    slow = 0

    for fast in range(len(arr)):
        # Fast explores, slow builds result
        if arr[fast] meets_condition:
            arr[slow] = arr[fast]
            slow += 1

    return slow  # New length

# Use for: Remove duplicates, In-place modification
# Time: O(n), Space: O(1)
```

### Template 4: Sliding Window
```python
def solve(s):
    left = 0
    window = {}  # or set()
    result = 0

    for right in range(len(s)):
        # Expand: add s[right] to window
        window[s[right]] = window.get(s[right], 0) + 1

        # Shrink: while window invalid
        while window_invalid:
            window[s[left]] -= 1
            left += 1

        # Update result
        result = max(result, right - left + 1)

    return result

# Use for: Longest substring, Maximum subarray
# Time: O(n), Space: O(k) where k = window size
```

### Template 5: Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Use for: Search in sorted array
# Time: O(log n), Space: O(1)
```

### Template 6: DFS (Recursive)
```python
def dfs(node, visited):
    if node is None or node in visited:
        return

    visited.add(node)

    # Process node
    result = process(node)

    # Recurse on children
    for neighbor in node.neighbors:
        dfs(neighbor, visited)

    return result

# Use for: Tree/Graph traversal, All paths
# Time: O(n), Space: O(h) where h = height
```

### Template 7: BFS (Iterative)
```python
from collections import deque

def bfs(root):
    if not root:
        return []

    queue = deque([root])
    visited = set([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)

        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

# Use for: Shortest path, Level order
# Time: O(n), Space: O(w) where w = max width
```

### Template 8: Backtracking
```python
def backtrack(path, choices):
    # Base case: found solution
    if is_solution(path):
        result.append(path.copy())  # Must copy!
        return

    # Try each choice
    for choice in choices:
        # Make choice
        path.append(choice)

        # Recurse with updated choices
        backtrack(path, new_choices)

        # Undo choice (BACKTRACK!)
        path.pop()

# Use for: All combinations, Permutations, N-Queens
# Time: O(2^n) or O(n!), Space: O(n)
```

### Template 9: Dynamic Programming (1D)
```python
def dp_1d(n):
    # Create DP array
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = base_case_0
    dp[1] = base_case_1

    # Fill table
    for i in range(2, n + 1):
        # Recurrence relation
        dp[i] = dp[i-1] + dp[i-2]  # Example: Fibonacci

    return dp[n]

# Use for: Climbing stairs, House robber, Coin change
# Time: O(n), Space: O(n)
```

### Template 10: Dynamic Programming (2D)
```python
def dp_2d(m, n):
    # Create 2D table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = init_value
    for j in range(n + 1):
        dp[0][j] = init_value

    # Fill table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Recurrence relation
            dp[i][j] = function(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

# Use for: Longest common subsequence, Edit distance
# Time: O(m*n), Space: O(m*n)
```

---

## 🎯 Problem-Solving Checklist

```
BEFORE CODING:
□ Read problem twice
□ Identify input type (array/string/tree/graph)
□ Identify output type (number/boolean/array)
□ Look for keywords
□ Check PATTERN_RECOGNITION.md
□ Draw small example (3-4 elements)
□ Solve by hand
□ Identify pattern

WHILE CODING:
□ Start with template
□ Add comments first
□ Code step by step
□ Handle edge cases

AFTER CODING:
□ Test with example
□ Test edge cases (empty, single element, duplicates)
□ Calculate complexity
□ Verify logic
```

---

## 🧮 Common Edge Cases

```
Arrays:
□ Empty array []
□ Single element [1]
□ Two elements [1, 2]
□ All same [5, 5, 5]
□ All different [1, 2, 3, 4]

Strings:
□ Empty string ""
□ Single char "a"
□ All same "aaaa"
□ Spaces " "

Trees:
□ None (null)
□ Single node
□ Only left children
□ Only right children
□ Balanced tree

Numbers:
□ Zero
□ Negative
□ Very large (overflow)
□ Very small
```

---

## 💡 Quick Optimization Tricks

```
BRUTE FORCE → OPTIMIZED

Nested loops (O(n²))
  → Hash Map (O(n) time, O(n) space)
  → Two Pointers if sorted (O(n) time, O(1) space)

Searching unsorted (O(n))
  → Sort first + Binary Search (O(n log n))
  → Hash Set for existence (O(n) time, O(n) space)

All substrings/subarrays (O(n³))
  → Sliding Window (O(n) time)

Recursion with repeated work (O(2^n))
  → Dynamic Programming (O(n) or O(n²))
```

---

## 🎨 Visual Debugging

```
ALWAYS DRAW:

Arrays with pointers:
[1, 2, 3, 4, 5]
 ↑     ↑     ↑
 i     j     k

Trees:
    1
   / \
  2   3
 / \
4   5

Graphs:
1 -- 2
|    |
3 -- 4

Hash Maps:
key → value
2 → 0
7 → 1

Stacks:
Top → [3]
      [2]
      [1]
```

---

## 🔥 Most Common Mistakes

```
❌ Not reading problem carefully
✅ Read twice, rephrase in your words

❌ Jumping to code without thinking
✅ Draw example, identify pattern first

❌ Forgetting edge cases
✅ Test: empty, single, duplicates

❌ Off-by-one errors
✅ Draw array with indices

❌ Not checking if value exists in dict
✅ Use .get() or check with 'in'

❌ Modifying list while iterating
✅ Create new list or use indices

❌ Integer overflow
✅ Use mid = left + (right - left) // 2

❌ Shallow copy of nested structures
✅ Use deepcopy or manual copy
```

---

## ⏱️ Time Limits (Interview Context)

```
Easy Problem: 15-20 minutes
  - 3 min: Understand & discuss
  - 5 min: Think & design
  - 10 min: Code
  - 2 min: Test

Medium Problem: 25-30 minutes
  - 5 min: Understand & discuss
  - 10 min: Think & design
  - 12 min: Code
  - 3 min: Test

Hard Problem: 35-45 minutes
  - 7 min: Understand & discuss
  - 15 min: Think & design
  - 18 min: Code
  - 5 min: Test
```

---

## 📚 Quick Reference

```
Hash Map:     Two Sum, Anagram, Frequency
Two Pointers: Palindrome, Sorted pairs, Remove dups
Sliding Win:  Longest substring, Max subarray
Stack:        Valid parentheses, Next greater
Binary:       Search sorted array
DFS:          Tree paths, Graph cycle
BFS:          Shortest path, Level order
DP:           Max/min ways, Optimal solution
Backtrack:    All combinations, N-Queens
```

---

**🎯 Remember:**
- Pattern recognition > Memorization
- Draw before coding
- Test edge cases
- Calculate complexity

**Keep this sheet handy! It's your DSA survival guide.** 💪
