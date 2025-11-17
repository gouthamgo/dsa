# 🚀 Advanced Problem-Solving Strategies

**Level Up from Medium to Hard: Advanced Techniques for FAANG**

> "The difference between a good engineer and a great engineer isn't raw intelligence—it's pattern recognition and strategic thinking."

---

## 🎯 When You Need This Guide

```
Use this guide when you've:
✅ Solved 150+ problems
✅ Mastered basic patterns
✅ Can solve Medium in < 30 min
✅ Ready to tackle Hard problems
✅ Preparing for senior roles (L5+)

This guide covers:
- Advanced problem-solving techniques
- How to approach Hard problems
- Optimization strategies
- Company-specific patterns
- Interview mind tricks
```

---

## 📊 The Hard Problem Framework

### Why Hard Problems Are Hard:

```
Easy/Medium:           Hard:
One pattern       →    Multiple patterns combined
Clear input       →    Ambiguous requirements
One approach      →    Many possible approaches
Fast solution     →    Optimization required
```

### The 4-Step Hard Problem Approach:

```
STEP 1: DECOMPOSE (10 minutes)
──────────────────────────────
Break into sub-problems
Identify each pattern separately

STEP 2: SOLVE SUB-PROBLEMS (20 minutes)
──────────────────────────────────────
Solve each piece independently
Don't optimize yet

STEP 3: COMBINE (10 minutes)
───────────────────────────
Merge solutions
Handle edge cases at boundaries

STEP 4: OPTIMIZE (15 minutes)
─────────────────────────────
Now think about efficiency
Apply advanced techniques
```

---

## 🧠 Advanced Pattern Combinations

### Pattern: Two Pointers + Binary Search
```
Example: Find K Closest Elements

┌─────────────────────────────────────┐
│ [1, 2, 3, 4, 5]  k=4, x=3          │
└─────────────────────────────────────┘

Approach:
1. Binary Search → Find closest to x
2. Two Pointers → Expand window to get k elements

def findClosestElements(arr, k, x):
    # Binary search for starting position
    left = 0
    right = len(arr) - k

    while left < right:
        mid = (left + right) // 2
        # Compare distances
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left:left + k]

Time: O(log n + k)
```

### Pattern: Sliding Window + Hash Map
```
Example: Longest Substring with At Most K Distinct Characters

"eceba", k=2 → "ece" (length 3)

Approach:
1. Sliding Window → Manage substring
2. Hash Map → Track character counts

def lengthOfLongestSubstringKDistinct(s, k):
    if k == 0:
        return 0

    left = 0
    max_len = 0
    char_map = {}

    for right in range(len(s)):
        # Add char to window
        char_map[s[right]] = char_map.get(s[right], 0) + 1

        # Shrink window if more than k distinct
        while len(char_map) > k:
            char_map[s[left]] -= 1
            if char_map[s[left]] == 0:
                del char_map[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

Time: O(n)
```

### Pattern: DFS + Memoization (Top-Down DP)
```
Example: Word Break II (return all possible sentences)

Approach:
1. DFS → Try all word combinations
2. Memoization → Cache results for substrings

def wordBreak(s, wordDict):
    memo = {}

    def dfs(start):
        if start in memo:
            return memo[start]

        if start == len(s):
            return [[]]

        result = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in wordDict:
                # Recursively get solutions for rest
                for sub_solution in dfs(end):
                    result.append([word] + sub_solution)

        memo[start] = result
        return result

    sentences = dfs(0)
    return [' '.join(words) for words in sentences]
```

### Pattern: BFS + Pruning
```
Example: Word Ladder (shortest transformation sequence)

Approach:
1. BFS → Find shortest path
2. Pruning → Use visited set to avoid revisits

from collections import deque

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    wordList = set(wordList)
    queue = deque([(beginWord, 1)])
    visited = {beginWord}

    while queue:
        word, length = queue.popleft()

        if word == endWord:
            return length

        # Try all possible one-letter changes
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]

                if next_word in wordList and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, length + 1))

    return 0
```

---

## 🎯 Advanced Techniques

### 1. Space Optimization in DP

**Problem:** Most DP uses O(n²) or O(n×m) space
**Solution:** Often can reduce to O(n) or O(1)

```python
# Original: Longest Common Subsequence (LCS)
# Uses O(m × n) space

def lcs_space_optimized(text1, text2):
    if len(text1) < len(text2):
        text1, text2 = text2, text1

    m, n = len(text1), len(text2)
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(prev[j], curr[j-1])

        prev, curr = curr, prev

    return prev[n]

# Reduced from O(m × n) to O(n) space!
```

**Key Insight:** If DP only depends on previous row/column, keep only that!

### 2. Monotonic Stack (Advanced Stack Usage)

**When to use:** Find next greater/smaller element

```python
# Next Greater Element
def nextGreaterElements(nums):
    """
    [2, 1, 2, 4, 3] → [4, 2, 4, -1, -1]
    """
    result = [-1] * len(nums)
    stack = []  # Store indices

    for i in range(len(nums)):
        # While current element is greater than stack top
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result

# Visual:
# [2, 1, 2, 4, 3]
#  ↓  ↓  ↓  ↓  ↓
#  4  2  4  -1 -1

# Stack maintains decreasing order
# When we find larger element → pop and assign
```

**Applications:**
- Stock span problem
- Largest rectangle in histogram
- Trapping rain water

### 3. Union Find (Disjoint Set)

**When to use:** Detect cycles, connected components, dynamic connectivity

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """Find with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union by rank"""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already connected

        # Attach smaller tree under larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

# Example: Detect cycle in undirected graph
def hasCycle(n, edges):
    uf = UnionFind(n)

    for u, v in edges:
        if not uf.union(u, v):
            return True  # Cycle detected!

    return False
```

### 4. Prefix Sum (Advanced Usage)

**Beyond basics:** Subarray problems with conditions

```python
# Subarray Sum Equals K
def subarraySum(nums, k):
    """
    Count subarrays with sum = k

    [1, 2, 3] k=3 → answer: 2
    (subarray [1,2] and [3])
    """
    count = 0
    curr_sum = 0
    sum_freq = {0: 1}  # Important: empty subarray has sum 0

    for num in nums:
        curr_sum += num

        # If curr_sum - k exists, we found subarray!
        if curr_sum - k in sum_freq:
            count += sum_freq[curr_sum - k]

        sum_freq[curr_sum] = sum_freq.get(curr_sum, 0) + 1

    return count

# Trick: curr_sum - previous_sum = k
#        → previous_sum = curr_sum - k
```

### 5. Binary Search on Answer

**Mind-bending concept:** Binary search not on input, but on answer!

```python
# Koko Eating Bananas
def minEatingSpeed(piles, h):
    """
    Find minimum eating speed to finish in h hours

    piles = [3, 6, 7, 11], h = 8
    Answer: 4 bananas/hour
    """
    def canFinish(speed):
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed  # Ceiling division
        return hours <= h

    # Binary search on speed (1 to max(piles))
    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2
        if canFinish(mid):
            right = mid  # Try slower
        else:
            left = mid + 1  # Need faster

    return left

# Pattern: When answer is in range, binary search that range!
```

### 6. Topological Sort (Kahn's Algorithm)

**When to use:** Task scheduling, course prerequisites, dependency resolution

```python
from collections import deque, defaultdict

def findOrder(numCourses, prerequisites):
    """
    Course Schedule II: Find valid course order
    """
    # Build graph
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Start with courses having no prerequisites
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)

        # Remove this course from graph
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    # If we processed all courses, valid order exists
    return order if len(order) == numCourses else []
```

---

## 🎯 Company-Specific Patterns

### Google Favorites

**1. Google loves complexity analysis:**
```
Always discuss:
- Time complexity with reasoning
- Space complexity
- Why this is optimal
- Trade-offs

Example answer:
"This uses O(n log n) time due to sorting. We can't do better
than O(n log n) for comparison-based approaches because [explain].
Space is O(1) if we modify input, or O(n) for a stable sort."
```

**2. Google loves clean code:**
```python
# Bad:
def f(a, b):
    c = []
    for i in range(len(a)):
        if a[i] > b:
            c.append(a[i])
    return c

# Good:
def filterGreaterThan(numbers: List[int], threshold: int) -> List[int]:
    """Returns all numbers greater than threshold."""
    return [num for num in numbers if num > threshold]
```

**3. Google pattern: Array manipulation**
- Practice: Rotate array, product except self, jump game

### Meta Favorites

**1. Meta loves graphs and trees:**
```
75% of Meta problems involve:
- Tree traversal (BFS/DFS)
- Graph problems (shortest path, connected components)
- Social network problems
```

**2. Meta pattern: BFS for shortest path**
```python
# Meta loves these types:
- Word Ladder
- Shortest Path in Binary Matrix
- 01 Matrix (distance to nearest 0)
- Minimum Knight Moves

Template:
from collections import deque

def bfs_shortest_path(start, target):
    queue = deque([(start, 0)])  # (node, distance)
    visited = {start}

    while queue:
        node, dist = queue.popleft()

        if node == target:
            return dist

        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1  # No path found
```

**3. Meta values iteration speed:**
- Prioritize working solution over perfect solution
- Can optimize later if time permits
- Show you can "move fast"

### Amazon Favorites

**1. Amazon loves arrays and strings:**
```
Most common Amazon patterns:
- Two Sum variations
- Subarray problems
- String manipulation
- Basic tree/graph traversal
```

**2. Amazon pattern: Sliding window with conditions**
```python
# Very common at Amazon:
- Longest substring without repeating characters
- Minimum window substring
- Fruits into baskets
- Longest subarray with sum ≤ k

Template:
def slidingWindowTemplate(arr, condition):
    left = 0
    result = 0
    window_state = {}  # Track window state

    for right in range(len(arr)):
        # Expand window
        update_state(window_state, arr[right])

        # Shrink window if condition violated
        while violates_condition(window_state):
            remove_from_state(window_state, arr[left])
            left += 1

        # Update result
        result = max(result, right - left + 1)

    return result
```

**3. Amazon's secret: Test basic understanding well**
- They prefer 2 easy-medium over 1 hard
- Focus on correctness and edge cases
- Explain trade-offs clearly

---

## 🧠 Problem-Solving Mind Tricks

### Trick 1: Work Backwards
```
Problem: Minimum steps to reach 1

Instead of thinking "how do I get TO 1?"
Think: "how did I get HERE from 1?"

This reverses the problem and often simplifies it.
```

### Trick 2: Solve for Small Input First
```
Problem: Find pattern in array

Don't think about n=10000
Solve for n=3 by hand
Then n=4
Then n=5

Pattern will emerge!
```

### Trick 3: Visualize with Drawings
```
Always draw for:
- Trees (draw the tree!)
- Graphs (draw nodes and edges!)
- Arrays (draw the array with pointers!)
- Matrices (draw the grid!)

Your brain processes visual info 60,000x faster than text.
```

### Trick 4: State Machine for Complex Conditions
```
Problem: Stock buy/sell with cooldown

States:
- RESET (can buy)
- HELD (holding stock, can sell)
- SOLD (just sold, must cooldown)

Draw state transition diagram:
RESET → (buy) → HELD
HELD → (sell) → SOLD
SOLD → (cooldown) → RESET

Now code is obvious!
```

### Trick 5: Greedy vs DP Decision
```
Ask: "Does making locally optimal choice guarantee global optimum?"

YES → Greedy
- Activity Selection
- Jump Game

NO → DP
- 0/1 Knapsack
- House Robber
```

---

## 📊 Optimization Checklist

When stuck on Hard problem, try these in order:

### Level 1: Basic Optimizations
```
□ Remove nested loops (can you use hash map?)
□ Avoid repeated work (can you cache?)
□ Sort first (does ordering help?)
□ Use two pointers (is array sorted/searchable?)
□ Binary search (is data sorted/searchable?)
```

### Level 2: Data Structure Swap
```
□ Array → Hash Map (for O(1) lookup)
□ Array → Set (for O(1) existence check)
□ Array → Heap (for min/max operations)
□ List → Deque (for both-end operations)
```

### Level 3: Algorithm Techniques
```
□ Sliding window (for subarray/substring)
□ Prefix sum (for subarray sum queries)
□ Monotonic stack (for next greater/smaller)
□ Union find (for connectivity)
□ Topological sort (for dependencies)
```

### Level 4: Advanced Optimizations
```
□ DP space optimization (2D → 1D)
□ Bit manipulation (for set operations)
□ Math formula (instead of simulation)
□ Greedy (if DP too slow)
```

---

## 🎯 The "Stuck" Protocol

### You've been stuck for 15 minutes. Now what?

```
STEP 1: Admit you're stuck (don't waste time)

STEP 2: In interview → Ask for hint
        "I'm thinking about X approach, but I'm stuck on Y.
         Could you give me a hint about...?"

STEP 3: In practice → Look at one hint
        - Category (DP? Graph?)
        - Similar problem
        - First step only

STEP 4: Try again for 10 minutes with hint

STEP 5: If still stuck → Look at solution
        BUT: Study it, understand WHY, then re-solve from scratch

STEP 6: Mark problem for review in 3 days
```

**Important: Don't waste hours stuck!**
- In interview: Max 5 min stuck before asking hint
- In practice: Max 30 min stuck before looking at hints

---

## 💡 Interview Communication Tips

### What to Say Out Loud:

```
✅ "I'm thinking about using a hash map to store..."
✅ "The brute force would be O(n²), but we can optimize by..."
✅ "Let me trace through an example..."
✅ "I'm considering two approaches: X and Y. Let me compare..."
✅ "Can I assume the input is sorted?"
✅ "What should I return if there's no valid answer?"

❌ *silence while thinking*
❌ "This is easy"
❌ "I've seen this before"
❌ "I'm not sure" (without trying)
```

### Structure Your Communication:

```
1. Repeat problem (show you understand)
   "So I need to find the longest substring without
    repeating characters..."

2. Clarify assumptions
   "Can the string be empty? Are all characters lowercase?"

3. Explain approach
   "I'll use sliding window with a hash set to track characters..."

4. Trace example
   "Let me trace 'abcabcbb'..."

5. Code while narrating
   "I'll initialize left pointer at 0..."

6. Test with example
   "Let me verify with the original example..."

7. Discuss complexity
   "Time is O(n), space is O(min(n, 26)) for the character set..."
```

---

## 🚀 From Good to Great

### Good Engineers:
- Solve the problem
- Get correct answer
- Write working code

### Great Engineers (What FAANG wants):
- Solve the problem **efficiently**
- Consider edge cases **proactively**
- Write **clean, readable** code
- Explain **trade-offs**
- Think about **scalability**
- Ask **clarifying questions**
- Communicate **clearly**

---

## 📝 Advanced Practice Plan

### Once You've Mastered Basics (150+ problems):

**Week 1-2: Pattern Combinations**
- Solve problems requiring 2+ patterns
- Focus on: Two Pointers + BS, SW + HM, DFS + Memo

**Week 3-4: Hard Problems Only**
- 2-3 Hard problems/day
- Don't skip even if stuck
- Study editorial after 30 min

**Week 5-6: Company-Specific**
- 30 problems each: Google, Meta, Amazon
- Focus on their favorite patterns

**Week 7-8: Contests & Speed**
- LeetCode weekly contest
- Timed practice (45 min per problem)
- Simulate interview pressure

---

## ✅ Advanced Readiness Checklist

You're ready for Hard problems when:
- [ ] Solved 200+ problems
- [ ] 90%+ success rate on Medium
- [ ] Can identify pattern in < 2 minutes
- [ ] Know when to use each data structure
- [ ] Understand time/space trade-offs
- [ ] Can optimize after getting working solution
- [ ] Completed 10+ Hard problems
- [ ] Comfortable with multiple-pattern problems

---

## 🎯 Final Wisdom

```
"There are no hard problems, only unfamiliar patterns."

Every "hard" problem is just:
- A combination of familiar patterns
- Applied in an unfamiliar way

The more patterns you master,
The more "hard" problems become "medium"

Keep solving.
Keep learning patterns.
Keep optimizing.

You got this! 🚀
```

---

**Next Steps:**
1. Return to FAANG_ROADMAP.md for complete timeline
2. Practice one advanced technique per week
3. Solve company-specific problems
4. Do mock interviews to test these strategies

**Remember: Advanced techniques are useless without solid fundamentals!**
Make sure you've mastered basic patterns first (PATTERN_RECOGNITION.md).
