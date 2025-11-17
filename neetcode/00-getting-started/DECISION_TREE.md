# Decision Tree: Which Pattern to Use?

## 🎯 Use This When You're Stuck!

Follow this decision tree to identify the right pattern.

---

## 📊 START HERE: What Type of Input?

```
┌─────────────────────────────────────────┐
│  What is the PRIMARY input data type?  │
└─────────────────────────────────────────┘
                    │
        ┌───────────┼───────────┬───────────┐
        │           │           │           │
     ARRAY       STRING       TREE       GRAPH
        │           │           │           │
        ▼           ▼           ▼           ▼
   [Continue]  [Continue]  [Continue]  [Continue]
```

---

## Branch 1: ARRAY Input

```
┌──────────────────┐
│  Input: ARRAY    │
└──────────────────┘
        │
        ▼
┌─────────────────────┐
│  Is array SORTED?   │
└─────────────────────┘
        │
    ┌───┴───┐
    │       │
   YES     NO
    │       │
    ▼       ▼
```

### If SORTED:
```
┌─────────────────────────────┐
│  What are you looking for?  │
└─────────────────────────────┘
        │
    ┌───┴───┬───────┬──────────┐
    │       │       │          │
Find one Find pair Remove    In-place
element  /triplet duplicate  modify
    │       │       │          │
    ▼       ▼       ▼          ▼
BINARY   TWO      TWO       TWO
SEARCH  POINTERS POINTERS  POINTERS

Examples:
- Binary Search: [1,3,5,7,9] find 5
- Two Pointers:  [1,2,3,4] find pair sum=5
- Two Pointers:  [1,1,2,2,3] remove dups
```

### If NOT SORTED:
```
┌─────────────────────────────┐
│  What are you looking for?  │
└─────────────────────────────┘
        │
    ┌───┴───┬────────┬─────────┐
    │       │        │         │
Find pair Count   Group    Find
/duplicate freq    items    subarray
    │       │        │         │
    ▼       ▼        ▼         ▼
 HASH     HASH     HASH    SLIDING
  MAP      MAP      MAP     WINDOW

Examples:
- Hash Map: [2,7,11,15] two sum
- Hash Map: "hello" count freq
- Hash Map: ["eat","tea","tan"] group anagrams
- Sliding Window: [1,3,-1,3,5] max sum k=3
```

---

## Branch 2: STRING Input

```
┌──────────────────┐
│  Input: STRING   │
└──────────────────┘
        │
        ▼
┌────────────────────────────┐
│  What are you looking for? │
└────────────────────────────┘
        │
    ┌───┴───┬─────────┬──────────┬─────────┐
    │       │         │          │         │
Substring Pattern  Count    Palindrome Matching
with cond. match   chars   check      pairs
    │       │         │          │         │
    ▼       ▼         ▼          ▼         ▼
SLIDING  STRING    HASH      TWO      STACK
WINDOW    DP       MAP     POINTERS
          or KMP

Examples:
- Sliding Window: "abcabcbb" longest unique substring
- DP: "abc" vs "ahbgdc" is subsequence?
- Hash Map: "anagram" vs "nagaram" count chars
- Two Pointers: "racecar" is palindrome?
- Stack: "({[]})" valid parentheses
```

---

## Branch 3: TREE Input

```
┌──────────────────┐
│  Input: TREE     │
└──────────────────┘
        │
        ▼
┌──────────────────────────┐
│  What type of problem?   │
└──────────────────────────┘
        │
    ┌───┴───┬─────────┬─────────┐
    │       │         │         │
Traverse  Search   Modify   Compare
    │       │         │         │
    ▼       ▼         ▼         ▼
 DFS/BFS  DFS/BFS   DFS      DFS
         (BST)     recursion

Examples:
- DFS: Inorder/Preorder/Postorder traversal
- BFS: Level order traversal
- DFS: Search in BST
- DFS: Invert tree, max depth
```

---

## Branch 4: GRAPH Input

```
┌──────────────────┐
│  Input: GRAPH    │
└──────────────────┘
        │
        ▼
┌────────────────────────────┐
│  What are you looking for? │
└────────────────────────────┘
        │
    ┌───┴───┬─────────┬────────┐
    │       │         │        │
Shortest All paths  Cycle  Connected
 path                detect  components
    │       │         │        │
    ▼       ▼         ▼        ▼
  BFS      DFS       DFS     DFS/
                             Union-Find

Examples:
- BFS: Shortest path (unweighted)
- DFS: Find all paths
- DFS: Detect cycle
- Union-Find: Number of islands
```

---

## 🎯 Quick Decision Based on Keywords

### Keywords → Pattern Mapping

```
┌────────────────────────────────────────┐
│         KEYWORD IN PROBLEM             │
└────────────────────────────────────────┘
                    │
        ┌───────────┼────────┬──────────────┐
        │           │        │              │
   "Find pair"  "Substring" "Sorted"   "All combos"
        │           │        │              │
        ▼           ▼        ▼              ▼
     HASH MAP   SLIDING   BINARY      BACKTRACKING
                WINDOW   SEARCH/TWO
```

**Complete Keyword List:**

```
"two sum", "pair", "complement"
  → HASH MAP or TWO POINTERS (if sorted)

"substring", "subarray", "contiguous"
  → SLIDING WINDOW

"sorted array", "search", "O(log n)"
  → BINARY SEARCH

"palindrome", "reverse"
  → TWO POINTERS

"matching", "valid parentheses", "nested"
  → STACK

"all combinations", "all permutations", "generate all"
  → BACKTRACKING

"count ways", "maximum value", "minimum cost"
  → DYNAMIC PROGRAMMING

"top K", "K largest/smallest"
  → HEAP

"shortest path", "level by level"
  → BFS

"all paths", "detect cycle", "islands"
  → DFS

"intervals", "merge", "overlapping"
  → INTERVALS (sort first)

"frequency", "count occurrences", "anagram"
  → HASH MAP
```

---

## 🎨 Visual Decision Flowchart

```
                    START
                      │
                      ▼
              ┌───────────────┐
              │ Sorted input? │
              └───────────────┘
                │           │
               YES         NO
                │           │
                ▼           ▼
        ┌─────────────┐  ┌──────────────┐
        │Binary Search│  │Need to count?│
        │or           │  └──────────────┘
        │Two Pointers │        │
        └─────────────┘    ┌───┴───┐
                          YES     NO
                           │       │
                           ▼       ▼
                      ┌────────┐ ┌─────────────┐
                      │Hash Map│ │Substring    │
                      └────────┘ │problem?     │
                                 └─────────────┘
                                      │
                                  ┌───┴───┐
                                 YES     NO
                                  │       │
                                  ▼       ▼
                           ┌────────────┐ ┌──────────┐
                           │Sliding     │ │Tree/Graph│
                           │Window      │ │problem?  │
                           └────────────┘ └──────────┘
                                               │
                                           ┌───┴───┐
                                          YES     NO
                                           │       │
                                           ▼       ▼
                                      ┌────────┐ ┌──────┐
                                      │DFS/BFS │ │Try DP│
                                      └────────┘ │or    │
                                                 │Back- │
                                                 │track │
                                                 └──────┘
```

---

## 🔍 Detailed Decision Questions

### Question 1: Do I need O(1) space?

```
YES → Rules out: Hash Map, Sliding Window with map
      Consider: Two Pointers, Binary Search

NO  → Any pattern works
      Usually Hash Map is easiest!
```

### Question 2: Is input sorted?

```
YES → Strong signals:
      - Binary Search (search problems)
      - Two Pointers (pair/triplet problems)

NO  → Consider:
      - Hash Map (most flexible)
      - Sorting first (adds O(n log n))
```

### Question 3: Do I need to find ALL solutions?

```
YES → Consider:
      - Backtracking (combinations/permutations)
      - DFS (all paths in tree/graph)

NO  → Other patterns work
```

### Question 4: Is there a pattern in subproblems?

```
Can I break into smaller same problems?
  YES → Dynamic Programming

  Example: fib(n) = fib(n-1) + fib(n-2)
           Same problem, smaller input!
```

### Question 5: Need to process continuously?

```
Is it about contiguous elements?
  YES → Sliding Window

  Example: "longest substring without repeating"
           Need to track continuous characters
```

---

## 💡 When Multiple Patterns Could Work

Sometimes multiple patterns work! Choose based on:

### Hash Map vs Two Pointers (for pair finding)

```
Input is sorted?
  YES → Two Pointers (O(1) space)
  NO  → Hash Map (O(n) space but simpler)

Example: Two Sum
- Unsorted → Hash Map
- Two Sum II (sorted) → Two Pointers
```

### DFS vs BFS (for trees/graphs)

```
Need shortest path?
  YES → BFS

Need to explore deep first?
  YES → DFS

Need level-by-level?
  YES → BFS

Default for trees?
  → DFS (recursion is natural)
```

### Sliding Window vs Two Pointers

```
Is it about contiguous elements with a condition?
  YES → Sliding Window

Is it about finding pair/triplet in sorted array?
  YES → Two Pointers
```

---

## 🚀 Practice: Use This Tree!

### Problem 1: "Find longest substring without repeating characters"

**Walk through tree:**
1. Input type? STRING
2. Looking for? SUBSTRING with condition
3. Pattern? SLIDING WINDOW ✓

### Problem 2: "Search in sorted array"

**Walk through tree:**
1. Input type? ARRAY
2. Sorted? YES
3. Looking for? Single element
4. Pattern? BINARY SEARCH ✓

### Problem 3: "Valid parentheses"

**Walk through tree:**
1. Input type? STRING
2. Looking for? MATCHING PAIRS
3. Pattern? STACK ✓

### Problem 4: "Two numbers sum to target (unsorted)"

**Walk through tree:**
1. Input type? ARRAY
2. Sorted? NO
3. Looking for? PAIR
4. Pattern? HASH MAP ✓

---

## 🎯 Emergency Checklist (When Really Stuck)

```
□ Is input sorted? → Binary Search or Two Pointers
□ Need to count/track? → Hash Map
□ Substring/subarray? → Sliding Window
□ Matching pairs? → Stack
□ Tree/Graph? → DFS or BFS
□ All combinations? → Backtracking
□ Max/min ways? → DP
□ Top K? → Heap

Still stuck? → Start with Hash Map!
Hash Map solves 40% of problems!
```

---

## 🎓 Remember

**This tree is a GUIDE, not a rule!**

With practice, you'll:
1. Recognize patterns instantly
2. Know which template to use
3. Code the solution quickly

**The more you use this tree, the less you'll need it!** 🌳

---

## 📖 Next Steps

1. ✅ Use this tree for next 10 problems
2. ✅ Notice patterns you see often
3. ✅ Build intuition
4. ✅ Soon you won't need the tree!
