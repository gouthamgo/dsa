# Pattern Recognition Master Guide

## 🎯 The Problem: "I See a Problem and Get Stuck"

**This guide solves that!** Learn to recognize patterns instantly and know exactly which template to use.

---

## 🧠 The Mental Framework: 3-Step Pattern Recognition

When you see ANY problem, ask these 3 questions:

### Step 1: What is the INPUT? (5 seconds)
```
□ Array/List of numbers?
□ String?
□ Linked List?
□ Tree/Graph?
□ Matrix/Grid?
□ Intervals/Ranges?
```

### Step 2: What is the OUTPUT? (5 seconds)
```
□ Find a pair/triplet?
□ Find all combinations?
□ Count something?
□ Find min/max?
□ True/False (validation)?
□ Modify in-place?
```

### Step 3: What are the CONSTRAINTS? (5 seconds)
```
□ Is input sorted?
□ Need O(1) space?
□ Need specific time complexity?
□ Can I use extra space?
```

**Total: 15 seconds to identify the pattern!**

---

## 🎨 Visual Pattern Recognition System

### Pattern 1: HASH TABLE (Most Common!)

**Visual Trigger:**
```
Problem mentions:         →  Think: HASH MAP/SET
├── "Find pair"           →  Complement search
├── "Count frequency"     →  Frequency counter
├── "Find duplicate"      →  Existence check
├── "Group by property"   →  Grouping
└── "Have I seen this?"   →  Set membership
```

**Example Keywords:**
- Two Sum
- Anagram
- Duplicate
- Frequency
- Count occurrences

**Visual Mental Model:**
```
Input: [2, 7, 11, 15], target = 9

Think: "For each number, can I find its complement?"
       ↓
     HASH MAP!

    num  →  complement
     2   →  9-2 = 7 (look for 7)
     7   →  9-7 = 2 (found in map!)
```

**Complexity:** O(n) time, O(n) space

---

### Pattern 2: TWO POINTERS

**Visual Trigger:**
```
Problem mentions:              →  Think: TWO POINTERS
├── "Sorted array"             →  Left & Right pointers
├── "Find pair in sorted"      →  Opposite direction
├── "Remove duplicates"        →  Slow & Fast
├── "Reverse"                  →  Opposite direction
├── "Palindrome"               →  Opposite direction
└── "In-place modification"    →  Slow & Fast
```

**Example Keywords:**
- Sorted array
- Pair/Triplet
- Palindrome
- Remove in-place
- Two Sum II

**Visual Mental Model:**
```
Sorted array: [1, 3, 5, 7, 9, 11]
              ↑                 ↑
            left              right

If sum < target → move left (need bigger)
If sum > target → move right (need smaller)

WHY TWO POINTERS?
- Sorted gives us ORDER
- Can eliminate half the search space each step
- O(n) instead of O(n²)
```

**Complexity:** O(n) time, O(1) space

---

### Pattern 3: SLIDING WINDOW

**Visual Trigger:**
```
Problem mentions:                     →  Think: SLIDING WINDOW
├── "Subarray"                        →  Window of elements
├── "Substring"                       →  Window of characters
├── "Contiguous elements"             →  Window
├── "Longest/Shortest substring..."   →  Variable window
├── "Maximum sum of k elements"       →  Fixed window
└── "With/without condition"          →  Expand/shrink window
```

**Example Keywords:**
- Longest substring
- Maximum subarray
- Minimum window
- K elements

**Visual Mental Model:**
```
String: "a b c a b c b b"
         ↑     ↑
       left  right  (window)

Window = [a, b, c]  (no repeats)

Add 'a' → duplicate!
  ↓
Shrink from left until no duplicates
  ↓
Window = [b, c, a]  ✓

WHY SLIDING WINDOW?
- Check all subarrays without nested loops
- O(n) instead of O(n²)
```

**Complexity:** O(n) time, O(k) space for tracking window

---

### Pattern 4: STACK

**Visual Trigger:**
```
Problem mentions:          →  Think: STACK
├── "Matching pairs"       →  Parentheses matching
├── "Nested structure"     →  Stack for tracking
├── "Most recent"          →  LIFO nature
├── "Undo/Redo"           →  History tracking
└── "Next greater/smaller" →  Monotonic stack
```

**Example Keywords:**
- Valid parentheses
- Next greater element
- Decode string
- Remove duplicates

**Visual Mental Model:**
```
Input: "({[]})"

Stack grows:
[ ( {
[ ( { [
[ ( { [ ]  → Match! Pop [
[ ( {      → Match! Pop {
[ (        → Match! Pop (
[          (empty) → Valid!

WHY STACK?
- Need to remember "what we opened last"
- LIFO perfect for matching pairs
- O(n) time
```

**Complexity:** O(n) time, O(n) space

---

### Pattern 5: BINARY SEARCH

**Visual Trigger:**
```
Problem mentions:                →  Think: BINARY SEARCH
├── "Sorted array"               →  Classic binary search
├── "Find in log(n) time"        →  Binary search
├── "Rotated sorted array"       →  Modified binary search
├── "Find threshold/boundary"    →  Binary search on answer
└── "Minimize maximum"           →  Binary search on answer
```

**Example Keywords:**
- Sorted
- O(log n)
- Search
- First/Last occurrence

**Visual Mental Model:**
```
Array: [1, 3, 5, 7, 9], target = 5
        ↑     ↑     ↑
       low   mid  high

Step 1: mid = 5 → Found! ✓

If not found:
- If target < mid → search LEFT half
- If target > mid → search RIGHT half

WHY BINARY SEARCH?
- Each comparison eliminates HALF the data
- 1,000,000 elements → 20 comparisons!
- O(log n) vs O(n)
```

**Complexity:** O(log n) time, O(1) space

---

### Pattern 6: BFS/DFS (Graphs & Trees)

**Visual Trigger:**
```
Problem mentions:        →  Think: DFS/BFS
├── "Tree"               →  DFS (recursion)
├── "Graph"              →  DFS or BFS
├── "All paths"          →  DFS
├── "Shortest path"      →  BFS
├── "Level by level"     →  BFS
├── "Islands"            →  DFS/BFS
└── "Connected"          →  DFS/BFS
```

**DFS vs BFS Decision:**
```
Need shortest path?     →  BFS
Need all paths?         →  DFS
Need level order?       →  BFS
Need to explore deep?   →  DFS
```

**Visual Mental Model (DFS):**
```
        1
       / \
      2   3
     / \
    4   5

DFS: Go DEEP first
Visit: 1 → 2 → 4 → 5 → 3

BFS: Go WIDE first (level by level)
Visit: 1 → 2, 3 → 4, 5

WHY DFS/BFS?
- DFS: Recursion is natural for trees
- BFS: Queue gives level-by-level
- Both O(n) time
```

**Complexity:** O(n) time, O(h) space for DFS, O(w) for BFS

---

### Pattern 7: DYNAMIC PROGRAMMING

**Visual Trigger:**
```
Problem mentions:                    →  Think: DP
├── "Maximum/Minimum value"          →  DP
├── "Count number of ways"           →  DP
├── "Is it possible to..."           →  DP
├── "Optimal solution"               →  DP
├── Overlapping subproblems          →  DP
└── "Find longest/shortest..."       →  DP
```

**How to Identify DP:**
```
Ask: "Can I break this into SMALLER SAME problems?"
     "Do smaller problems OVERLAP?"

If YES → DP!

Example: Fibonacci
fib(5) = fib(4) + fib(3)
         ↓
     fib(4) = fib(3) + fib(2)
              ↓
         fib(3) called TWICE!
         ↓
       OVERLAPPING! → Use DP
```

**Visual Mental Model:**
```
Climbing Stairs: How many ways to reach step n?

Step 0: 1 way
Step 1: 1 way
Step 2: 2 ways (1+1 or 2)
Step 3: 3 ways (from step 1 or step 2)
        dp[3] = dp[2] + dp[1]

WHY DP?
- Avoid recalculating same subproblems
- O(2^n) → O(n) time!
```

**Complexity:** O(n) or O(n²) time, O(n) space

---

### Pattern 8: BACKTRACKING

**Visual Trigger:**
```
Problem mentions:              →  Think: BACKTRACKING
├── "Find all combinations"    →  Backtracking
├── "Find all permutations"    →  Backtracking
├── "Generate all"             →  Backtracking
├── "Solve puzzle"             →  Backtracking
└── "All possible solutions"   →  Backtracking
```

**Example Keywords:**
- All subsets
- All permutations
- N-Queens
- Sudoku

**Visual Mental Model:**
```
Find all subsets of [1,2,3]

         []
       /  |  \
     [1] [2] [3]
     / \  |
[1,2][1,3][2,3]
   |
[1,2,3]

Try → Recurse → Undo (backtrack) → Try next

WHY BACKTRACKING?
- Need to explore ALL possibilities
- Build incrementally
- Undo when path fails
```

**Complexity:** O(2^n) or O(n!) time - exponential!

---

## 🎯 Quick Reference: Problem → Pattern Mapping

| Problem Type | Pattern | Time | Space |
|--------------|---------|------|-------|
| "Find pair that sums to X" | Hash Map | O(n) | O(n) |
| "Find pair in SORTED array" | Two Pointers | O(n) | O(1) |
| "Count frequency" | Hash Map | O(n) | O(n) |
| "Longest substring..." | Sliding Window | O(n) | O(k) |
| "Valid parentheses" | Stack | O(n) | O(n) |
| "Search in sorted array" | Binary Search | O(log n) | O(1) |
| "Tree traversal" | DFS/BFS | O(n) | O(h) |
| "All combinations" | Backtracking | O(2^n) | O(n) |
| "Maximum/Minimum ways" | DP | O(n) | O(n) |
| "Top K elements" | Heap | O(n log k) | O(k) |
| "Shortest path" | BFS | O(V+E) | O(V) |
| "Find cycle" | DFS | O(V+E) | O(V) |

---

## 🚀 Practice Exercise: Identify the Pattern!

### Exercise 1
**Problem:** "Find the longest substring without repeating characters"

**Think:**
1. INPUT: String ✓
2. OUTPUT: Longest substring ✓
3. KEYWORDS: "substring", "longest", "without repeating" ✓

**Pattern:** SLIDING WINDOW! (Substring + condition)

---

### Exercise 2
**Problem:** "Given sorted array, find two numbers that sum to target"

**Think:**
1. INPUT: SORTED array ✓
2. OUTPUT: Two numbers ✓
3. KEYWORDS: "sorted", "two numbers", "sum" ✓

**Pattern:** TWO POINTERS! (Sorted + pair)

---

### Exercise 3
**Problem:** "Count how many times each character appears in a string"

**Think:**
1. INPUT: String ✓
2. OUTPUT: Count of each character ✓
3. KEYWORDS: "count", "frequency" ✓

**Pattern:** HASH MAP! (Counting/frequency)

---

## 💡 Pro Tips for Pattern Recognition

1. **Read the problem TWICE**
   - First time: Understand what it's asking
   - Second time: Look for pattern keywords

2. **Underline keywords**
   - "sorted" → Two Pointers or Binary Search
   - "subarray/substring" → Sliding Window
   - "all combinations" → Backtracking

3. **Draw it out** (Visual thinking!)
   - Small example: [1,2,3]
   - How would YOU solve it by hand?
   - That's likely the pattern!

4. **Check constraints**
   - Need O(1) space? → Can't use Hash Map
   - Need O(log n)? → Binary Search
   - Can modify input? → Two Pointers in-place

5. **Start with brute force**
   - What's the naive solution? O(n²)?
   - Now optimize: Can hash map make it O(n)?

---

## 🎓 Next Steps

1. ✅ Read this guide
2. ✅ Do the practice exercises above
3. ✅ Read HOW_TO_THINK.md next
4. ✅ Use DECISION_TREE.md when stuck
5. ✅ Practice on actual problems!

---

**Remember: Pattern recognition is a SKILL. It gets easier with practice!** 🚀
