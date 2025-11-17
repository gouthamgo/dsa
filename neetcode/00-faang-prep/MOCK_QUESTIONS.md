# 🎯 Real FAANG Interview Questions with Complete Solutions

**Actual questions asked at Google, Meta, Amazon, Apple, Netflix + How to answer them**

> This guide contains real interview questions from recent FAANG interviews with step-by-step solutions, thought processes, and what interviewers look for.

---

## 📋 How to Use This Guide

For each question, you'll find:
```
1. The exact question asked
2. Company where it was asked
3. Difficulty level
4. What the interviewer is testing
5. Step-by-step thinking process
6. Complete solution with explanation
7. Follow-up questions
8. Common mistakes to avoid
```

---

## 🔥 DSA Questions (Coding Rounds)

### Question 1: Two Sum (Easy - but commonly asked!)

**Asked at:** Google, Amazon, Meta, Apple (Phone screens)

**Question:**
```
Given an array of integers nums and an integer target, return
indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

**What they're testing:**
- Can you recognize the Hash Map pattern?
- Do you think about time complexity?
- Do you ask clarifying questions?

**How to answer (step-by-step):**

```
STEP 1: CLARIFY (30 seconds)
─────────────────────────────
YOU: "A few quick questions:
- Can the array contain negative numbers?"
- Is the array sorted?"
- Can I use extra space?"
- Should I return indices or values?"

INTERVIEWER: "Array can be unsorted, negatives allowed,
extra space is fine, return indices"

STEP 2: EXAMPLE (30 seconds)
────────────────────────────
YOU: "Let me trace through the example by hand..."

[2, 7, 11, 15], target = 9
 ↑  ↑
Need: 2 + 7 = 9 ✓

STEP 3: BRUTE FORCE (1 minute)
──────────────────────────────
YOU: "The brute force would be:
- Try every pair (i, j) where i < j
- Check if nums[i] + nums[j] == target
- Time: O(n²), Space: O(1)"

[Show code on whiteboard/screen]

def twoSum_bruteforce(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

YOU: "This works but O(n²) is slow for large inputs.
Can we do better?"

STEP 4: OPTIMIZE (1 minute)
───────────────────────────
YOU: "I can optimize using a hash map:

Key insight: For each number x, I need to find
(target - x) in the array.

Instead of searching O(n) each time, I can:
- Store each number in a hash map as I iterate
- Check if (target - current) exists in the map
- This gives O(n) time, O(n) space"

STEP 5: SOLUTION (2 minutes)
────────────────────────────
```

```python
def twoSum(nums, target):
    """
    Time: O(n) - single pass through array
    Space: O(n) - hash map stores up to n elements
    """
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num

        # Check if complement exists
        if complement in seen:
            return [seen[complement], i]

        # Store current number
        seen[num] = i

    return []  # No solution found

# Trace through example:
# nums = [2, 7, 11, 15], target = 9

# i=0, num=2:
#   complement = 9 - 2 = 7
#   7 not in seen
#   seen = {2: 0}

# i=1, num=7:
#   complement = 9 - 7 = 2
#   2 IS in seen! ✓
#   return [seen[2], 1] = [0, 1]
```

```
STEP 6: TEST (1 minute)
──────────────────────
YOU: "Let me test edge cases..."

Test 1: nums = [3, 3], target = 6
- i=0: complement=3, not in seen, seen={3:0}
- i=1: complement=3, found at 0! return [0,1] ✓

Test 2: nums = [-1, -2, -3, -4, -5], target = -8
- Works with negatives ✓

Test 3: nums = [1, 2], target = 5
- Returns [] (no solution) ✓

STEP 7: COMPLEXITY (30 seconds)
───────────────────────────────
YOU: "Final complexity:
- Time: O(n) - single pass
- Space: O(n) - hash map

This is optimal because we need to examine
each element at least once."
```

**Common mistakes to avoid:**
```
❌ Forgetting to check if complement exists BEFORE adding to map
❌ Returning [i, i] (using same element twice)
❌ Not handling duplicates correctly
❌ Forgetting edge cases (empty array, no solution)
```

**Follow-up questions they might ask:**
```
1. "What if there are multiple solutions?"
   → Return any valid pair, or return all pairs

2. "What if the array is sorted?"
   → Can use two pointers instead! O(n) time, O(1) space

3. "What if we can't use extra space?"
   → Two pointers if sorted, else brute force O(n²)

4. "Can you do this with only one pass?"
   → Yes, current solution is single pass!
```

---

### Question 2: Longest Substring Without Repeating Characters (Medium)

**Asked at:** Meta, Google, Amazon (Onsite)

**Question:**
```
Given a string s, find the length of the longest substring
without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: "abc" is the longest substring
```

**What they're testing:**
- Sliding window recognition
- Hash map/set usage
- Edge case handling

**Complete solution walkthrough:**

```python
def lengthOfLongestSubstring(s):
    """
    APPROACH: Sliding Window + Hash Set

    Intuition:
    - Expand window by moving right pointer
    - If duplicate found, shrink from left
    - Track maximum length seen

    Time: O(n)
    Space: O(min(n, 26)) for lowercase letters
    """
    # Edge case
    if not s:
        return 0

    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Shrink window until no duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add current char
        char_set.add(s[right])

        # Update max length
        max_length = max(max_length, right - left + 1)

    return max_length

# TRACE EXAMPLE: "abcabcbb"
"""
Step-by-step:

right=0, s[0]='a':
  'a' not in set
  set={'a'}, window="a", len=1, max=1

right=1, s[1]='b':
  'b' not in set
  set={'a','b'}, window="ab", len=2, max=2

right=2, s[2]='c':
  'c' not in set
  set={'a','b','c'}, window="abc", len=3, max=3

right=3, s[3]='a':
  'a' IN set! Shrink:
    remove s[0]='a', left=1
  Now 'a' not in set
  set={'b','c','a'}, window="bca", len=3, max=3

right=4, s[4]='b':
  'b' IN set! Shrink:
    remove s[1]='b', left=2
  Now 'b' not in set
  set={'c','a','b'}, window="cab", len=3, max=3

right=5, s[5]='c':
  'c' IN set! Shrink:
    remove s[2]='c', left=3
  Now 'c' not in set
  set={'a','b','c'}, window="abc", len=3, max=3

right=6, s[6]='b':
  'b' IN set! Shrink:
    remove s[3]='a', left=4
    'b' still in set! Shrink:
    remove s[4]='b', left=5
  Now 'b' not in set
  set={'c','b'}, window="cb", len=2, max=3

right=7, s[7]='b':
  'b' IN set! Shrink:
    remove s[5]='c', left=6
    'b' still in set! Shrink:
    remove s[6]='b', left=7
  set={'b'}, window="b", len=1, max=3

Answer: 3
"""
```

**How to present this in interview:**

```
YOU: "This is a classic sliding window problem. Let me walk
through my approach..."

[Draw on whiteboard]:

"abcabcbb"
 L R          L=left, R=right

"I'll use a sliding window with:
- Right pointer expands window
- Left pointer shrinks when duplicate found
- Hash set tracks characters in current window"

[Write code while explaining each part]

"Key insight: When we find a duplicate, we shrink from
the left until the duplicate is removed."

[Trace through example]

"Let me verify with the example... [trace]"

[Test edge cases]

"Edge cases:
- Empty string → return 0 ✓
- Single char → return 1 ✓
- All unique → return len(s) ✓
- All same → return 1 ✓"

[Complexity]

"Time: O(n) - each character visited at most twice
Space: O(k) where k is charset size, worst case O(n)"
```

**Common mistakes:**
```
❌ Not handling the while loop correctly (only using if)
❌ Off-by-one errors in window size calculation
❌ Forgetting to add current character after shrinking
❌ Using array index instead of character as key
```

**Follow-ups:**
```
1. "What if string has unicode characters?"
   → Same approach works, just larger charset

2. "What if you need to return the substring, not length?"
   → Track start_index when updating max_length

3. "Can you do it with O(1) space?"
   → No, need to track seen characters

4. "What's the optimal sliding window pattern?"
   → Show them your template from PATTERN_RECOGNITION.md!
```

---

### Question 3: LRU Cache (Medium-Hard)

**Asked at:** Google, Meta, Amazon (Onsite, commonly asked!)

**Question:**
```
Design a data structure that follows the constraints of a
Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize with positive capacity
- int get(int key) Return value if exists, else -1
- void put(int key, int value) Update or insert key-value pair.
  If capacity is reached, evict least recently used key.

Both operations should run in O(1) time.

Example:
LRUCache cache = new LRUCache(2);
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
```

**What they're testing:**
- Data structure design
- Hash map + Doubly linked list combination
- O(1) operation implementation
- Real-world system understanding

**Complete solution with explanation:**

```python
class Node:
    """Doubly linked list node"""
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    """
    APPROACH: Hash Map + Doubly Linked List

    Why this combination?
    - Hash map: O(1) access to any node
    - DLL: O(1) add/remove from both ends

    Design:
    - Most recent at head
    - Least recent at tail
    - On access: move to head
    - On eviction: remove from tail

    Visual:
    head <-> [3] <-> [1] <-> [2] <-> tail
             (most recent)  (least recent)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # Dummy head and tail (simplifies edge cases)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove node from list (O(1))"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node):
        """Add node right after head (O(1))"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node):
        """Move existing node to head (mark as recently used)"""
        self._remove(node)
        self._add_to_head(node)

    def _remove_tail(self):
        """Remove least recently used (node before tail)"""
        lru = self.tail.prev
        self._remove(lru)
        return lru

    def get(self, key: int) -> int:
        """
        Get value and mark as recently used
        Time: O(1)
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_head(node)  # Mark as recently used
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair
        Time: O(1)
        """
        if key in self.cache:
            # Update existing
            node = self.cache[key]
            node.val = value
            self._move_to_head(node)
        else:
            # Insert new
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

            # Check capacity
            if len(self.cache) > self.capacity:
                # Evict LRU
                lru = self._remove_tail()
                del self.cache[lru.key]

# TRACE EXAMPLE:
"""
cache = LRUCache(2)

Initial state:
head <-> tail
cache = {}

put(1, 1):
head <-> [1:1] <-> tail
cache = {1: Node(1,1)}

put(2, 2):
head <-> [2:2] <-> [1:1] <-> tail
         (most recent)
cache = {1: Node(1,1), 2: Node(2,2)}

get(1):  # returns 1
Move [1:1] to head:
head <-> [1:1] <-> [2:2] <-> tail
         (most recent)

put(3, 3):  # capacity reached, evict LRU (key 2)
Remove [2:2]:
head <-> [1:1] <-> tail
Add [3:3]:
head <-> [3:3] <-> [1:1] <-> tail
cache = {1: Node(1,1), 3: Node(3,3)}

get(2):  # returns -1 (evicted)
"""
```

**How to present this in interview:**

```
STEP 1: UNDERSTAND REQUIREMENTS (1 minute)
──────────────────────────────────────────
YOU: "Let me clarify:
- LRU means least recently used, so most recently
  accessed should stay in cache
- Both get and put should be O(1)
- When capacity is full, evict the least recently used

To achieve O(1) for both operations, I need:
- O(1) lookup → Hash Map
- O(1) add/remove from middle → Doubly Linked List

I'll combine both!"

STEP 2: DRAW THE DESIGN (2 minutes)
──────────────────────────────────
[Draw on whiteboard]:

Hash Map:
{1 → Node, 2 → Node, 3 → Node}
     ↓        ↓        ↓
DLL: head ↔ [3] ↔ [1] ↔ [2] ↔ tail
            (most)      (least)

"When accessing a key:
1. Hash map gives O(1) access to node
2. Move node to head (most recent)

When adding new key:
1. Add to hash map
2. Add to head of DLL
3. If over capacity, remove tail"

STEP 3: CODE WITH EXPLANATION (5 minutes)
────────────────────────────────────────
[Write code while explaining each method]

"I'll use dummy head and tail nodes to simplify
edge cases - no need to check for null..."

STEP 4: TRACE EXAMPLE (2 minutes)
────────────────────────────────
[Walk through the example step-by-step with drawings]

STEP 5: COMPLEXITY (30 seconds)
──────────────────────────────
"Both get and put are O(1):
- Hash map lookup: O(1)
- DLL add/remove: O(1)
- Space: O(capacity) for hash map and DLL"
```

**Common mistakes:**
```
❌ Using single linked list (can't remove from middle in O(1))
❌ Forgetting to update hash map when evicting
❌ Not using dummy nodes (messy edge case handling)
❌ Not updating "recently used" on get() operation
❌ Updating value but forgetting to move to head
```

**Follow-ups:**
```
1. "What if we need LFU (Least Frequently Used) instead?"
   → Need to track frequency, use min-heap or similar

2. "How would you handle concurrent access?"
   → Add locks/mutexes around operations

3. "What if capacity is very large?"
   → This design still works, O(1) operations scale well

4. "Can you implement TTL (Time To Live) for entries?"
   → Add timestamp to nodes, background thread for cleanup
```

---

### Question 4: Merge K Sorted Lists (Hard)

**Asked at:** Google, Amazon, Apple (Onsite for senior roles)

**Question:**
```
You are given an array of k linked-lists, each sorted in
ascending order. Merge all the linked-lists into one sorted
linked-list and return it.

Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

**What they're testing:**
- Understanding of heaps/priority queues
- Ability to optimize from brute force
- Knowledge of divide-and-conquer
- Time complexity analysis

**Complete solution:**

```python
import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    APPROACH: Min Heap

    Intuition:
    - At each step, we need the SMALLEST element among
      k lists
    - Min heap gives us min element in O(log k)

    Algorithm:
    1. Add first node from each list to heap
    2. Pop smallest, add to result
    3. Add next node from that list to heap
    4. Repeat until heap empty

    Time: O(N log k) where N = total nodes, k = number of lists
    Space: O(k) for heap
    """
    # Edge case
    if not lists:
        return None

    # Min heap: (val, list_index, node)
    # We need list_index to track which list the node came from
    heap = []

    # Add first node from each list
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))

    # Dummy head for result list
    dummy = ListNode(0)
    current = dummy

    while heap:
        # Get smallest node
        val, list_idx, node = heapq.heappop(heap)

        # Add to result
        current.next = node
        current = current.next

        # Add next node from same list
        if node.next:
            heapq.heappush(heap, (node.next.val, list_idx, node.next))

    return dummy.next

# ALTERNATIVE: Divide and Conquer
def mergeKLists_divideConquer(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    APPROACH: Divide and Conquer

    Merge lists pairwise:
    [1,2,3,4,5,6,7,8] lists
           ↓
    Merge pairs: [merged1, merged2, merged3, merged4]
           ↓
    Merge pairs: [merged1, merged2]
           ↓
    Merge pairs: [final]

    Time: O(N log k)
    Space: O(1) if not counting recursion, O(log k) with recursion
    """
    if not lists:
        return None

    def merge2Lists(l1, l2):
        """Merge two sorted lists"""
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 if l1 else l2
        return dummy.next

    def mergeRange(start, end):
        """Merge lists[start:end+1]"""
        if start == end:
            return lists[start]
        if start > end:
            return None

        mid = (start + end) // 2
        left = mergeRange(start, mid)
        right = mergeRange(mid + 1, end)
        return merge2Lists(left, right)

    return mergeRange(0, len(lists) - 1)

# TRACE EXAMPLE:
"""
lists = [[1,4,5], [1,3,4], [2,6]]

HEAP APPROACH:
──────────────
Initial heap: [(1,0,node), (1,1,node), (2,2,node)]
                ↑ list 0    ↑ list 1    ↑ list 2

Step 1: Pop (1,0,node) → add to result: [1]
        Add next from list 0: (4,0,node)
        Heap: [(1,1,node), (2,2,node), (4,0,node)]

Step 2: Pop (1,1,node) → result: [1,1]
        Add next from list 1: (3,1,node)
        Heap: [(2,2,node), (3,1,node), (4,0,node)]

Step 3: Pop (2,2,node) → result: [1,1,2]
        Add next from list 2: (6,2,node)
        Heap: [(3,1,node), (4,0,node), (6,2,node)]

Step 4: Pop (3,1,node) → result: [1,1,2,3]
        Add next from list 1: (4,1,node)
        Heap: [(4,0,node), (4,1,node), (6,2,node)]

Continue until heap empty...
Final: [1,1,2,3,4,4,5,6]
"""
```

**How to present in interview:**

```
STEP 1: BRUTE FORCE (1 minute)
──────────────────────────────
YOU: "The brute force would be:
1. Collect all nodes into array
2. Sort the array
3. Rebuild linked list

Time: O(N log N) where N is total nodes
Space: O(N)

But we can do better since each list is already sorted!"

STEP 2: OPTIMIZED APPROACH (2 minutes)
─────────────────────────────────────
YOU: "Two good approaches:

Approach 1: Min Heap
- At each step, we need smallest among k lists
- Heap gives us min in O(log k)
- Total: O(N log k) time, O(k) space

Approach 2: Divide and Conquer
- Merge lists pairwise
- Similar to merge sort
- Total: O(N log k) time, O(1) space

I'll implement the heap approach as it's more intuitive."

[Draw heap visualization on whiteboard]

STEP 3: CODE (5 minutes)
────────────────────────
[Implement with clear variable names and comments]

STEP 4: TRACE (2 minutes)
────────────────────────
[Trace through example showing heap state changes]

STEP 5: COMPLEXITY (1 minute)
────────────────────────────
"Time: O(N log k)
- N total nodes
- Each push/pop is O(log k)
- We process each node once

Space: O(k) for heap

This is optimal because we must look at all N nodes."
```

**Common mistakes:**
```
❌ Trying to compare ListNode objects directly (need to use values)
❌ Losing track of which list a node came from
❌ Forgetting to handle empty lists
❌ Not handling case where lists have different lengths
❌ Memory leak by not updating pointers correctly
```

**Follow-ups:**
```
1. "What if lists are stored on disk, too large for memory?"
   → External sorting, process in chunks

2. "What if new lists are added dynamically?"
   → Keep heap, add new list's first node when it arrives

3. "Can you do it without extra space?"
   → Divide and conquer approach uses O(1) space

4. "What if some lists are much longer than others?"
   → Heap approach automatically handles this efficiently
```

---

## 💬 System Design Questions

### Question 5: Design Twitter/News Feed

**Asked at:** Meta, Twitter, Instagram, LinkedIn

**Question:**
```
Design a news feed system like Twitter. Users can:
- Post tweets
- Follow other users
- See feed of tweets from people they follow
- Like and comment on tweets

Focus on the feed generation algorithm.
```

**How to answer (45-minute format):**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1: CLARIFY REQUIREMENTS (5 minutes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOU: "Let me understand the scope..."

Functional Requirements:
□ Post tweets (text, 280 char limit?)
□ Follow/unfollow users
□ View personalized feed
□ Like and comment

Non-Functional Requirements:
□ Scale: How many users? (Let's say 300M DAU)
□ Tweets per day? (500M tweets/day)
□ Average followers? (200)
□ Feed latency? (< 2 seconds)
□ Consistency vs Availability? (AP - eventual consistency OK)

INTERVIEWER: "Yes, those numbers work. Focus on feed generation."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2: BACK-OF-ENVELOPE ESTIMATION (3 minutes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Traffic:
- 300M DAU
- Each user checks feed 5 times/day
- Total feed requests: 1.5B/day = 17,000 RPS

Storage:
- 500M tweets/day
- Each tweet: ~1KB (text + metadata)
- Daily: 500 GB
- 5 years: 500 GB × 365 × 5 ≈ 1 PB

Bandwidth:
- 17,000 RPS × 50 tweets × 1KB = 850 MB/s read

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3: HIGH-LEVEL DESIGN (15 minutes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Draw on whiteboard]:

┌─────────────┐
│   Client    │
└──────┬──────┘
       │
┌──────▼───────────┐
│  Load Balancer   │
└──────┬───────────┘
       │
       ├──→ Post Service    ──┐
       ├──→ Feed Service    ──┤
       ├──→ Follow Service  ──┤
       └──→ Like Service    ──┤
                               │
                        ┌──────▼───────┐
                        │   Database   │
                        │   Cluster    │
                        └──────────────┘
                               │
                        ┌──────▼───────┐
                        │     Cache    │
                        │    (Redis)   │
                        └──────────────┘

YOU: "I'll break this into services..."

1. POST SERVICE
   - User creates tweet
   - Store in database
   - Trigger feed generation

2. FEED SERVICE  ← FOCUS HERE
   - Generate personalized feed
   - Two approaches: Fanout on write vs Fanout on read

3. FOLLOW SERVICE
   - Manage follower relationships
   - Graph database or SQL with join table

4. LIKE SERVICE
   - Track likes/comments
   - Update counts

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4: DEEP DIVE - FEED GENERATION (15 minutes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOU: "Feed generation is the critical piece.
Let me explain two approaches..."

APPROACH 1: FANOUT ON WRITE (Push Model)
────────────────────────────────────────

When user posts:
1. Find all followers (e.g., 200 people)
2. Insert tweet into each follower's feed cache
3. User requests feed → just read from cache

┌──────────┐
│ User A   │ posts tweet
└────┬─────┘
     │
     ▼ Find followers: [B, C, D, ...]
     │
     ├──→ Insert into B's feed cache
     ├──→ Insert into C's feed cache
     └──→ Insert into D's feed cache

Read feed:
   SELECT * FROM user_B_feed_cache LIMIT 50

Pros:
✅ Fast reads (pre-computed)
✅ Simple for users

Cons:
❌ Slow writes (if user has many followers)
❌ Lots of storage (duplicate tweets)
❌ Celebrities problem (millions of followers)

APPROACH 2: FANOUT ON READ (Pull Model)
───────────────────────────────────────

When user requests feed:
1. Find all users they follow
2. Get recent tweets from those users
3. Merge and sort
4. Return top 50

Read feed:
1. SELECT following FROM user_follows WHERE user_id = 123
   → [45, 67, 89, ...]

2. SELECT * FROM tweets
   WHERE user_id IN (45, 67, 89, ...)
   ORDER BY timestamp DESC
   LIMIT 50

Pros:
✅ Fast writes
✅ No storage duplication
✅ No celebrity problem

Cons:
❌ Slow reads (compute on every request)
❌ Complex queries

APPROACH 3: HYBRID (BEST - Real Solution)
─────────────────────────────────────────

YOU: "In production, use HYBRID approach..."

For normal users (< 10k followers):
  → Fanout on write

For celebrities (> 10k followers):
  → Fanout on read

When user reads feed:
1. Fetch pre-computed feed (fanout on write)
2. Fetch latest from celebrities they follow (fanout on read)
3. Merge both
4. Cache result for 30 seconds

┌────────────────────────────────────┐
│  User B's Feed Request             │
└────────┬───────────────────────────┘
         │
         ├──→ [FAST] Pre-computed feed (Redis)
         │    From normal users
         │
         └──→ [SLOW] Query celebrity tweets
              From celebrity users

         Merge + Sort → Return

Implementation:

```python
def generateFeed(user_id, limit=50):
    # 1. Get pre-computed feed from cache
    precomputed = redis.get(f"feed:{user_id}", limit=40)

    # 2. Get followed celebrities
    celebrities = getFollowedCelebrities(user_id)

    # 3. Fetch their latest tweets
    celeb_tweets = []
    for celeb_id in celebrities:
        tweets = getTweets(celeb_id, limit=10)
        celeb_tweets.extend(tweets)

    # 4. Merge and sort by timestamp
    all_tweets = precomputed + celeb_tweets
    all_tweets.sort(key=lambda t: t.timestamp, reverse=True)

    # 5. Return top N
    return all_tweets[:limit]
```

YOU: "This hybrid approach:
- Fast for most users (pre-computed)
- Handles celebrities efficiently
- Balances write and read costs"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 5: DISCUSS TRADE-OFFS (5 minutes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YOU: "Let me discuss some trade-offs..."

Database Choice:
- SQL (PostgreSQL): Good for relations, ACID
- NoSQL (Cassandra): Better for high write throughput
- Recommendation: Hybrid
  - PostgreSQL for user/follow data
  - Cassandra for tweets (time-series)

Caching:
- Redis for feed cache
- TTL: 30 seconds for active users
- LRU eviction for inactive users

Consistency:
- Eventual consistency is OK (AP system)
- User might not see tweet immediately
- Trade-off for availability and scalability

Bottlenecks:
- Celebrity tweets (addressed with hybrid)
- Hot user feeds (cache with short TTL)
- Database writes (use message queue)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 6: MONITORING & SCALING (2 minutes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Metrics to monitor:
- Feed generation latency (p50, p99)
- Cache hit rate
- Database query time
- Queue depth (for async processing)

How to scale:
- Horizontal scaling: Add more API servers
- Database sharding: Shard by user_id
- Read replicas: For read-heavy workload
- CDN: For static content (images, videos)
```

**What interviewer looks for:**
```
✅ Clarified requirements before designing
✅ Calculated rough numbers
✅ Compared multiple approaches
✅ Chose hybrid solution with reasoning
✅ Discussed trade-offs
✅ Mentioned monitoring and scaling
✅ Drew clear diagrams
✅ Communicated thought process
```

**Common mistakes:**
```
❌ Jumping to solution without clarifying
❌ Not considering scale (designing for 100 users)
❌ Only discussing one approach
❌ Not handling celebrity/hot user problem
❌ Forgetting to cache
❌ Not discussing consistency model
```

---

## 🎭 Behavioral Questions

### Question 6: "Tell me about a time you disagreed with a teammate"

**Asked at:** All FAANG companies (Every single one!)

**What they're testing:**
- Communication skills
- Conflict resolution
- Humility
- Team collaboration
- Outcome focus

**Bad Answer (What NOT to say):**

```
❌ "I disagreed with my teammate about using React vs Vue.
We argued for a while but eventually went with React
because I was right. It worked out fine."

Why it's bad:
- Too vague
- Shows arrogance ("I was right")
- No specific actions
- No learning
- Doesn't show respect for teammate
```

**Good Answer (STAR Method):**

```
SITUATION (30 seconds)
─────────────────────
"At my previous company, I was working on a real-time
dashboard for monitoring server health. My tech lead
wanted to use WebSockets for real-time updates, while
I believed Server-Sent Events (SSE) would be sufficient
and simpler for our use case."

TASK (15 seconds)
────────────────
"As a senior engineer, it was my responsibility to voice
technical concerns while maintaining a collaborative
relationship with my tech lead."

ACTION (1.5 minutes) ← MOST IMPORTANT
────────────────────────────────────
"Here's how I handled it:

First, I scheduled a 1-on-1 with my tech lead to
understand their reasoning. I learned they chose
WebSockets because:
- Bi-directional communication
- Experience from previous project

Then I did my homework:
- Created a comparison document analyzing both options
- Benchmarked both solutions with our expected load
- Found that SSE would handle our 1000 concurrent
  connections easily
- SSE was simpler (no need for socket.io library)
- We only needed server-to-client communication

I presented this data in our architecture review meeting:
- Showed benchmarks (SSE handled 2000 connections easily)
- Demonstrated simpler code (30% less complexity)
- Acknowledged WebSockets had merit for future features
- Proposed: Start with SSE, migrate to WebSockets if needed

The team agreed this made sense. My tech lead appreciated
the data-driven approach and said they learned something
new about SSE's capabilities."

RESULT (30 seconds)
──────────────────
"We implemented SSE and:
- Launched on schedule (2 weeks)
- System handled 1500 peak connections smoothly
- Code was easier for team to maintain
- Total cost: $200/month vs $500/month for WebSocket service
- My tech lead and I maintained excellent working relationship
- This became our template for technical decision-making:
  Data over opinions"

LEARNING
───────
"I learned that disagreements are healthy when handled with:
- Respect and curiosity (understand their perspective first)
- Data and evidence (not just opinions)
- Focus on outcomes (what's best for project, not ego)
- Humility (acknowledge other viewpoints)"
```

**Why this answer works:**
```
✅ Specific situation with details
✅ Shows respect for tech lead
✅ Demonstrates research and preparation
✅ Quantifiable results (metrics!)
✅ Maintained relationship (crucial!)
✅ Shows learning and growth
✅ Focuses on "we" and "team" (not just "I")
✅ Data-driven decision making
```

**Follow-up questions:**
```
Q: "What if your tech lead had still disagreed?"
A: "I would have committed fully to their decision.
    As a team, once a decision is made, we support it 100%.
    I'd document my concerns for future reference but
    execute wholeheartedly."

Q: "Did you consider their feelings?"
A: "Yes, I made sure to:
    - Meet 1-on-1 first (not ambush in group meeting)
    - Acknowledge their experience and expertise
    - Frame it as 'what's best for project' not 'who's right'
    - Give credit publicly when we succeeded"

Q: "What would you do differently?"
A: "I might have involved them earlier in my research phase.
    Collaborative investigation could have been even better
    than presenting completed research."
```

---

## 🔍 More Questions Coming...

This file will be continuously updated with more real questions from:

**DSA Topics:**
- [ ] Binary Tree problems
- [ ] Dynamic Programming classics
- [ ] Graph algorithms
- [ ] String manipulation
- [ ] Array optimization

**System Design:**
- [ ] Design Uber/Lyft
- [ ] Design Netflix
- [ ] Design URL Shortener
- [ ] Design Rate Limiter
- [ ] Design Notification System

**Behavioral:**
- [ ] Leadership scenarios
- [ ] Failure stories
- [ ] Team conflict
- [ ] Technical decisions
- [ ] Amazon LP questions

---

## 📝 How to Practice with This Guide

**Week 1-2:** Master the 6 questions above
- Solve each coding question without looking
- Practice explaining each system design out loud
- Record yourself answering behavioral question

**Week 3-4:** Mix it up
- Random practice from all categories
- Time yourself (45 min per question)
- Practice with a friend

**Week 5-6:** Mock interviews
- Use these exact questions in mocks
- Get feedback on your answers
- Refine based on feedback

---

**Next:** See COMPANY_QUESTIONS.md for company-specific questions and what each company prioritizes!
