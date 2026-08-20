"""
Problem: Linked List Cycle
Difficulty: Easy on LeetCode (filed under Medium here - the Floyd's proof
            is genuinely medium-level reasoning and worth the extra time)
Topics: Linked List, Two Pointers, Hash Table

Problem Statement:
-----------------
Given the head of a linked list, determine if the linked list has a cycle
in it.

There is a cycle if some node in the list can be reached again by
continuously following the `next` pointer. Internally, `pos` denotes the
index of the node that the tail's `next` pointer connects to. `pos` is not
passed to your function - it exists only to describe the test input.

Return True if there is a cycle. Otherwise, return False.

Examples:
---------
Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: True
    Explanation: The tail (-4) connects back to index 1 (the node with
    value 2), so the list loops forever:

        [3] → [2] → [0] → [-4]
               ↑            |
               +------------+

Example 2:
    Input: head = [1,2], pos = 0
    Output: True
    Explanation: The tail connects back to the head - a 2-node loop.

Example 3:
    Input: head = [1], pos = -1
    Output: False
    Explanation: pos = -1 means no cycle. A single node pointing at None
    terminates normally.

Constraints:
-----------
- The number of nodes in the list is in the range [0, 10^4]
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked list

Follow-up:
---------
Can you solve it using O(1) (constant) memory?

LEARNING NOTES:
--------------
Two solutions worth knowing, and the contrast between them is the whole
lesson:
    1. Hash set  - obvious, easy to explain, O(n) space
    2. Floyd's   - "tortoise and hare", O(1) space  <- the follow-up answer

Key Insight (Floyd's): Put two runners on a circular track at different
    speeds and the fast one WILL lap the slow one. On a straight track it
    just runs off the end.

    slow moves 1 step, fast moves 2 steps.
    - No cycle -> fast reaches None and we return False.
    - Cycle    -> fast enters the loop, laps around, and the gap between
                  fast and slow shrinks by exactly 1 every iteration.
                  A gap that decreases by 1 each step must eventually hit
                  0, which means they land on the SAME node.

    Why the gap shrinks by exactly 1: relative to slow, fast advances
    2 - 1 = 1 node per iteration. So fast can never "jump over" slow -
    that is why a step size of 2 is guaranteed to work.

Pattern: "Detect a cycle / find the middle / find nth from end"
         -> SLOW & FAST POINTERS (GUIDE.md pattern #1)!

Visualization:
    head = [3, 2, 0, -4] with tail linked back to index 1

        [3] → [2] → [0] → [-4]
               ↑            |
               +------------+
        idx     0     1     2     3

    Iteration  slow      fast      same?
    ---------  --------  --------  -----
    start      3 (i0)    3 (i0)    (we check AFTER moving, so no)
    1          2 (i1)    0 (i2)    no
    2          0 (i2)    2 (i1)    no      <- fast wrapped around
    3          -4 (i3)   -4 (i3)   YES ✅  -> cycle detected, return True

    And on an acyclic list [1, 2, 3, 4]:

    Iteration  slow   fast
    ---------  -----  ----------------
    1          2      3
    2          3      None -> `while fast and fast.next` fails
    -> return False ✅
"""


# ============================================================================
# SETUP: Node definition + helpers (so this file runs standalone)
# ============================================================================

class ListNode:
    """A single node of a singly linked list: [val | next]"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def build_list(values, pos=-1):
    """
    Build a linked list from a plain Python list, optionally with a cycle.

    values: the node values, in order
    pos:    index the TAIL should point back to. -1 means no cycle.

    build_list([3, 2, 0, -4], pos=1)  ->  cyclic list (tail → index 1)
    build_list([1, 2, 3], pos=-1)     ->  ordinary acyclic list
    build_list([], pos=-1)            ->  None

    Time Complexity: O(n)
    Space Complexity: O(n) - n nodes, plus an index of them for the cycle

    NOTE: this helper is why the file is self-contained - we need a way to
    manufacture cyclic inputs, which a plain list literal cannot express.
    """
    if not values:
        return None

    nodes = [ListNode(v) for v in values]

    # Link them up in order
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Optionally close the loop
    if 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]

    return nodes[0]


def to_list(head, limit=100):
    """
    Convert a linked list back to a plain Python list.

    Because a cyclic list has no end, we stop after `limit` nodes so that
    printing a cyclic list can never hang the program. Handy for demos!

    Time Complexity: O(min(n, limit))
    Space Complexity: O(min(n, limit))
    """
    values = []
    curr = head

    while curr and len(values) < limit:
        values.append(curr.val)
        curr = curr.next

    return values


def format_list(values, pos=-1):
    """Pretty-print the SHAPE of a test input (from its description)."""
    if not values:
        return "None (empty list)"

    text = " → ".join(f"[{v}]" for v in values)
    if pos == -1:
        return text + " → None"
    return text + f" → (loops back to index {pos}, value {values[pos]})"


# ============================================================================
# SOLUTION 1: Floyd's Tortoise and Hare (OPTIMAL!)
# ============================================================================

def hasCycle(head):
    """
    Approach: Two pointers at different speeds. If they ever meet, there is
    a cycle; if the fast one falls off the end, there is not.

    Algorithm:
    1. slow = head, fast = head
    2. While fast and fast.next are both non-None:
       a. slow = slow.next        (tortoise: 1 step)
       b. fast = fast.next.next   (hare: 2 steps)
       c. If slow is fast -> they met -> return True
    3. Loop exited -> fast hit the end -> return False

    Why the loop condition is `while fast and fast.next`:
    - We are about to do fast.next.next, which needs BOTH fast and
      fast.next to exist. Checking only `fast` gives AttributeError on a
      list of even length.
    - We never have to check `slow`, because slow is always behind fast.

    Why we compare with `is` and not `==`:
    - We care about the same NODE OBJECT, not the same value. A list like
      [1, 1, 1] with no cycle has equal values everywhere but no cycle.

    Time Complexity: O(n)
        No cycle: fast reaches the end in n/2 iterations.
        Cycle:    slow needs at most n steps to enter the loop, then the
                  gap closes by 1 per step over a loop of length <= n.
                  So O(n) overall.
    Space Complexity: O(1) - just two pointers! ✅ (answers the follow-up)
    """
    slow = head
    fast = head

    # fast.next.next requires both fast AND fast.next to exist
    while fast and fast.next:
        slow = slow.next          # tortoise: 1 step
        fast = fast.next.next     # hare: 2 steps

        if slow is fast:          # `is` = same node object, not same value
            return True

    # fast ran off the end -> the list terminates -> no cycle
    return False


# ============================================================================
# SOLUTION 2: Hash Set of Visited Nodes (Naive - great for explaining)
# ============================================================================

def hasCycle_hashset(head):
    """
    Approach: Remember every node you have already stood on. If you arrive
    somewhere twice, you are going in circles.

    Algorithm:
    1. visited = empty set
    2. Walk the list one node at a time
    3. If the current node is already in visited -> return True
    4. Otherwise add it and continue
    5. If we reach None -> return False

    Important detail: we store the NODE OBJECTS (via id / identity), not
    their values. Python sets hash objects by identity by default, which is
    exactly what we want - [1, 1, 1] with no cycle must return False.

    Time Complexity: O(n) - each node visited once, O(1) set operations
    Space Complexity: O(n) - the set can hold every node ❌

    Why Floyd's is better:
    - Same O(n) time, but O(1) space instead of O(n).
    - The follow-up explicitly asks for constant memory, so this one alone
      does not fully answer the question.

    When this one is still the right call:
    - It is far easier to explain and to extend (e.g. "which node repeats
      first?" falls out for free - the set version tells you immediately).
    - Lead with this in an interview, then upgrade to Floyd's. Showing the
      progression is worth more than jumping straight to the clever trick.
    """
    visited = set()
    curr = head

    while curr:
        if curr in visited:   # identity-based membership
            return True
        visited.add(curr)
        curr = curr.next

    return False


# ============================================================================
# SOLUTION 3: Step Counter / Length Cap (Naive - DON'T use! Fragile)
# ============================================================================

def hasCycle_counter(head, max_nodes=10_001):
    """
    Approach: Exploit the constraint "at most 10^4 nodes" - if you can take
    more than 10^4 steps without hitting None, you must be looping.

    Algorithm:
    1. Walk the list counting steps
    2. If the count exceeds the maximum possible length -> return True
    3. If we hit None first -> return False

    Time Complexity: O(n) - bounded by max_nodes
    Space Complexity: O(1)

    Why you should NOT use this:
    - It only works because of a problem-specific constraint. Change the
      constraint and the code silently becomes wrong.
    - An interviewer will read it as "did not actually solve the problem".
    - It is shown here to make a point: a solution that depends on magic
      limits is not a real algorithm. Floyd's needs no such assumption.
    """
    curr = head
    steps = 0

    while curr:
        if steps > max_nodes:
            return True
        curr = curr.next
        steps += 1

    return False


# ============================================================================
# BONUS: Find WHERE the cycle starts (Floyd's, phase 2)
# ============================================================================

def detectCycleStart(head):
    """
    Approach: After the tortoise and hare meet, reset one pointer to the
    head and advance BOTH one step at a time. They meet at the cycle entry.

    Algorithm:
    1. Run phase 1 (hasCycle) until slow is fast, or return None
    2. Set slow = head, keep fast at the meeting point
    3. Advance both by 1 until they are the same node
    4. That node is the start of the cycle

    Why it works (the classic proof):
        Let L = distance from head to the cycle entry
            C = length of the cycle
            k = distance from the entry to the meeting point
        When they meet, slow has walked L + k and fast has walked
        2(L + k), and the difference is a whole number of laps:
            2(L + k) - (L + k) = L + k = nC
        So L = nC - k, i.e. walking L steps from the head and L steps from
        the meeting point both land on the entry. Hence the reset trick.

    Time Complexity: O(n)
    Space Complexity: O(1)

    This is LeetCode "Linked List Cycle II" - the natural follow-up. Being
    able to sketch this proof is a strong signal in an interview.
    """
    slow = head
    fast = head

    # Phase 1: find a meeting point (if any)
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None  # loop ended normally -> no cycle

    if not (fast and fast.next):
        return None  # defensive: no cycle

    # Phase 2: reset one pointer, walk both at the same speed
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return slow  # the entry node


# ============================================================================
# TEST CASES
# ============================================================================

def test():
    """Test all solutions"""

    test_cases = [
        # (values, pos, expected_has_cycle)
        ([3, 2, 0, -4], 1, True),    # classic cyclic example
        ([1, 2], 0, True),           # 2-node loop
        ([1], 0, True),              # single node pointing at itself!
        ([1], -1, False),            # single node, acyclic (edge case)
        ([], -1, False),             # empty list (edge case!)
        ([1, 2, 3, 4, 5], -1, False),         # plain acyclic list
        ([1, 2, 3, 4], 3, True),              # tail loops to itself
        ([1, 2, 3, 4, 5, 6], 0, True),        # whole list is one big loop
        ([1, 1, 1], -1, False),      # equal VALUES but no cycle - the test
                                     # that catches `==` instead of `is`
        ([1, 2, 3, 4, 5, 6, 7], 4, True),     # cycle late in the list
    ]

    solutions = [
        ("Floyd's Tortoise & Hare (Optimal)", hasCycle),
        ("Hash Set (Naive)", hasCycle_hashset),
        ("Step Counter (Fragile)", hasCycle_counter),
    ]

    for name, solution in solutions:
        print(f"\n{'='*50}")
        print(f"Testing: {name}")
        print('='*50)

        all_passed = True
        for i, (values, pos, expected) in enumerate(test_cases, 1):
            head = build_list(values, pos)
            result = solution(head)

            is_correct = result == expected
            status = "✅" if is_correct else "❌"
            print(f"Test {i}: {status} {format_list(values, pos)}")
            print(f"         → {result} (expected {expected})")
            if not is_correct:
                all_passed = False

        if all_passed:
            print(f"\n🎉 All tests passed for {name}!")

    # ---- Bonus: cycle START detection ----
    print(f"\n{'='*50}")
    print("Testing: Bonus - detectCycleStart (Cycle II)")
    print('='*50)

    start_cases = [
        # (values, pos, expected_start_value or None)
        ([3, 2, 0, -4], 1, 2),
        ([1, 2], 0, 1),
        ([1], 0, 1),
        ([1], -1, None),
        ([], -1, None),
        ([1, 2, 3, 4, 5], -1, None),
        ([1, 2, 3, 4, 5], 4, 5),
    ]

    all_passed = True
    for i, (values, pos, expected) in enumerate(start_cases, 1):
        head = build_list(values, pos)
        node = detectCycleStart(head)
        result = node.val if node else None

        is_correct = result == expected
        status = "✅" if is_correct else "❌"
        print(f"Test {i}: {status} {format_list(values, pos)}")
        print(f"         → cycle starts at {result} (expected {expected})")
        if not is_correct:
            all_passed = False

    if all_passed:
        print("\n🎉 All tests passed for detectCycleStart!")


# ============================================================================
# VISUAL DEMO
# ============================================================================

def visual_demo(values, pos=-1):
    """
    Visual step-by-step demonstration of Floyd's tortoise and hare.
    """
    print(f"\n{'='*70}")
    print("VISUAL DEMO: Linked List Cycle (Floyd's tortoise & hare)")
    print(f"Input: {values}, pos = {pos}")
    print('='*70)

    head = build_list(values, pos)
    print(f"\nShape: {format_list(values, pos)}")

    if head is None:
        print("\nEmpty list -> fast is None, loop never runs. "
              "Return False immediately. ✅")
        return

    # Map node objects to indices so we can print positions readably
    index_of = {}
    node = head
    for i in range(len(values)):
        index_of[id(node)] = i
        node = node.next

    def where(p):
        if p is None:
            return "None"
        return f"idx {index_of[id(p)]} (val {p.val})"

    slow = head
    fast = head
    step = 0

    print(f"\nStart: slow = {where(slow)}, fast = {where(fast)}")
    print("(We compare AFTER moving, so starting together is fine.)")
    print("\nStep-by-step execution:\n")

    while fast and fast.next:
        step += 1
        slow = slow.next
        fast = fast.next.next

        print(f"Step {step}:")
        print(f"  slow moved 1 step → {where(slow)}")
        print(f"  fast moved 2 steps → {where(fast)}")

        if slow is fast:
            print("  ✅ slow IS fast - the pointers collided!")
            print("     A collision is only possible on a circular track.")
            print("     Return True (cycle detected)")

            entry = detectCycleStart(head)
            print(f"\n  Bonus (phase 2): the cycle starts at "
                  f"{where(entry)}")
            return

        print("  Not equal yet - keep running")
        print()

    print(f"Step {step + 1}:")
    print("  fast (or fast.next) is None - the hare ran off the end.")
    print("  A list you can run off the end of cannot loop.")
    print("  ❌ No collision → Return False (no cycle)")


# ============================================================================
# WHAT YOU SHOULD LEARN
# ============================================================================

"""
KEY TAKEAWAYS:
-------------
1. SLOW & FAST POINTERS detect cycles in O(1) space.
2. Fast gains exactly 1 node per iteration, so it cannot skip past slow.
3. Loop condition must be `while fast and fast.next` - both matter.
4. Compare with `is` (identity), never `==` (value).
5. The hash-set version is easier to explain; Floyd's answers the follow-up.
6. Phase 2 (reset to head, walk together) finds WHERE the cycle starts.

PATTERN RECOGNITION:
-------------------
When you see:
- "Does this list/sequence loop?"
- "Find the middle node"
- "Find the nth node from the end"
- "Find the duplicate number" (array as an implicit linked list!)

Think: SLOW & FAST POINTERS!

THE TORTOISE-AND-HARE TEMPLATE (memorize this):
----------------------------------------------
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

INTERVIEW TIPS:
--------------
1. Lead with the hash set: "the simple version is O(n) time, O(n) space"
2. Then ask/answer the follow-up: "can we do O(1) space? Yes - Floyd's"
3. Explain WHY they must meet: the gap shrinks by 1 each iteration
4. Justify the loop condition out loud - it is the #1 crash source
5. Offer Cycle II (find the entry) as a bonus if there is time

COMMON MISTAKES:
---------------
❌ `while fast` alone -> AttributeError on fast.next.next
❌ Comparing `slow.val == fast.val` instead of `slow is fast`
   (a list of identical values would report a phantom cycle)
❌ Checking `slow is fast` BEFORE the first move -> instant false positive
   (they both start at head!)
❌ Forgetting the empty-list case (head = None)
❌ Moving fast by 3 - it still works but the argument is messier; 2 is the
   step size where the gap shrinks by exactly 1
❌ Printing/traversing a cyclic list without a guard -> infinite loop

VARIATIONS:
----------
- Linked List Cycle II - return the node where the cycle begins
- Find the Duplicate Number - treat nums[i] as a next pointer, same trick
- Happy Number - cycle detection on a number sequence!
- Middle of the Linked List - slow ends at the middle when fast ends
- Palindrome Linked List - find middle with slow/fast, reverse, compare

TIME COMPLEXITY COMPARISON:
--------------------------
Step counter:   O(n) time, O(1) space (but relies on a magic constant ❌)
Hash set:       O(n) time, O(n) space
Floyd's:        O(n) time, O(1) space ← BEST!

NEXT STEPS:
----------
✅ Mastered slow & fast pointers
✅ Know both the space-heavy and space-free approaches
→ Now try: Find the Duplicate Number (same trick on an array!)
→ Or:      Reorder List (slow/fast to split, then reverse and merge)

PRACTICE MORE:
-------------
Similar problems to practice this pattern:
- Linked List Cycle II
- Middle of the Linked List
- Remove Nth Node From End of List
- Palindrome Linked List
- Find the Duplicate Number
- Happy Number
"""


if __name__ == "__main__":
    # Run tests
    test()

    # Visual demonstrations
    visual_demo([3, 2, 0, -4], 1)   # cyclic
    visual_demo([1, 2, 3, 4], -1)   # acyclic

    # Interactive practice
    print("\n" + "="*70)
    print("YOUR TURN TO TRACE!")
    print("="*70)
    print("\nTry tracing through this example yourself:")
    print("values = [1, 2, 3, 4, 5, 6], pos = 2")
    print("\nWhere are slow and fast after each step?")
    print("On which step do they collide?")
    print("Then run: visual_demo([1, 2, 3, 4, 5, 6], 2)")
