"""
Problem: Reverse Linked List
Difficulty: Easy
Topics: Linked List, Recursion, Two Pointers

Problem Statement:
-----------------
Given the head of a singly linked list, reverse the list, and return the
head of the reversed list.

The list must be reversed IN PLACE - you rewire the existing nodes by
flipping every `next` pointer. You do NOT build a brand new list.

Examples:
---------
Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
    Explanation: Every arrow flips direction.
        Before: 1 → 2 → 3 → 4 → 5 → None
        After:  None ← 1 ← 2 ← 3 ← 4 ← 5
        The old tail (5) becomes the new head.

Example 2:
    Input: head = [1,2]
    Output: [2,1]
    Explanation: Only one arrow to flip.

Example 3:
    Input: head = []
    Output: []
    Explanation: Empty list reversed is still empty (edge case!).

Constraints:
-----------
- The number of nodes in the list is in the range [0, 5000]
- -5000 <= Node.val <= 5000

Follow-up:
---------
A linked list can be reversed either iteratively or recursively.
Could you implement both?

LEARNING NOTES:
--------------
This is THE fundamental linked list problem. Every harder linked list
problem (Reorder List, Palindrome Linked List, Reverse Nodes in k-Group)
uses this as a sub-routine. Learn it until it is muscle memory!

Key Insight: You need THREE pointers, not two!
    prev  - the part already reversed (grows behind you)
    curr  - the node you are flipping right now
    next  - a SAVED copy of the rest of the list

    The whole trick is: the moment you do `curr.next = prev`, you have
    DESTROYED your only link to the rest of the list. So you must save
    `curr.next` into a temp variable BEFORE you overwrite it.

Pattern: "Reverse pointers in place" -> prev / curr / next_temp three-pointer walk!

Visualization:
    head = [1, 2, 3]

    Start:
        prev=None   curr=[1] → [2] → [3] → None

    Step 1: (curr = 1)
        next_temp = [2]            (SAVE the rest!)
        curr.next = prev           1 → None
        prev = curr                prev = [1]
        curr = next_temp           curr = [2]
        State: None ← [1]     [2] → [3] → None
                       ^prev   ^curr

    Step 2: (curr = 2)
        next_temp = [3]
        curr.next = prev           2 → 1
        prev = [2], curr = [3]
        State: None ← [1] ← [2]     [3] → None
                             ^prev   ^curr

    Step 3: (curr = 3)
        next_temp = None
        curr.next = prev           3 → 2
        prev = [3], curr = None
        State: None ← [1] ← [2] ← [3]
                                   ^prev

    curr is None -> loop ends. Return prev = [3].
    Reversed list: [3, 2, 1] ✅

    NOTE: prev always ends up on the LAST node, which is the new head.
          That is why we `return prev`, never `return curr` (curr is None!).
"""


# ============================================================================
# SETUP: Node definition + helpers (so this file runs standalone)
# ============================================================================

class ListNode:
    """
    A single node of a singly linked list: [val | next]

    This is the exact definition LeetCode gives you, so practicing with it
    here builds the right habits.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def build_list(values):
    """
    Build a linked list from a plain Python list.

    build_list([1, 2, 3])  ->  [1] → [2] → [3] → None
    build_list([])         ->  None

    We use a DUMMY HEAD here (see GUIDE.md pattern #2) so we do not need a
    special case for "the very first node".

    Time Complexity: O(n)
    Space Complexity: O(n) - we allocate n nodes
    """
    dummy = ListNode(0)
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next  # skip the dummy


def to_list(head):
    """
    Convert a linked list back to a plain Python list.

    Needed so our tests can assert on ordinary values like [3, 2, 1]
    instead of comparing node objects.

    Time Complexity: O(n)
    Space Complexity: O(n) - for the output list
    """
    values = []
    curr = head

    while curr:
        values.append(curr.val)
        curr = curr.next

    return values


def format_list(head):
    """Pretty-print a linked list as: [1] → [2] → [3] → None"""
    values = to_list(head)
    if not values:
        return "None (empty list)"
    return " → ".join(f"[{v}]" for v in values) + " → None"


# ============================================================================
# SOLUTION 1: Iterative Three-Pointer Walk (OPTIMAL!)
# ============================================================================

def reverseList(head):
    """
    Approach: Walk the list once, flipping each `next` pointer backwards.

    Algorithm:
    1. prev = None (nothing is reversed yet; the new tail points to None)
    2. curr = head (the node we are about to flip)
    3. While curr is not None:
       a. next_temp = curr.next   <- SAVE the rest of the list FIRST!
       b. curr.next = prev        <- flip the arrow backwards
       c. prev = curr             <- prev advances onto the flipped node
       d. curr = next_temp        <- curr advances into the saved rest
    4. Return prev (the last node we flipped = the new head)

    Why it works:
    - `prev` is the head of the growing reversed portion.
    - `curr` is the head of the shrinking un-reversed portion.
    - Each iteration moves exactly one node from "un-reversed" to "reversed".
    - When curr falls off the end (None), everything has moved over.

    Time Complexity: O(n) - one pass, each node visited exactly once
    Space Complexity: O(1) - only three pointer variables, no extra structures

    This is the answer to give in an interview: optimal time AND space.
    """
    prev = None
    curr = head

    while curr:
        next_temp = curr.next  # 1. SAVE (or we lose the rest forever!)
        curr.next = prev       # 2. FLIP the arrow
        prev = curr            # 3. ADVANCE prev
        curr = next_temp       # 4. ADVANCE curr

    return prev  # prev is the new head (curr is None here!)


# ============================================================================
# SOLUTION 2: Recursive (Elegant, but uses stack space)
# ============================================================================

def reverseList_recursive(head):
    """
    Approach: Reverse the rest of the list, then attach the current node
    onto the back of it.

    Algorithm:
    1. Base case: empty list or single node -> already reversed, return head
    2. Recurse on head.next -> returns the new head of the reversed tail
    3. head.next.next = head  <- make our successor point BACK at us
    4. head.next = None       <- we are the new tail, so cut our old arrow
    5. Return new_head (unchanged all the way back up the stack)

    The magic line explained (head = 1, list = 1 → 2 → 3):
        After recursion:  1 → 2 ← 3     (2 still points forward to 3!)
        head.next is 2, so head.next.next = head means: 2 → 1
        Now:              1 ← 2 ← 3
        head.next = None cuts 1's stale forward arrow.

    Time Complexity: O(n) - one recursive call per node
    Space Complexity: O(n) - the call stack goes n frames deep!

    Interview note: mention this is elegant but risks stack overflow on a
    very long list. The iterative version is strictly better in practice.
    """
    # Base case: nothing to reverse
    if head is None or head.next is None:
        return head

    # Reverse everything after us; new_head bubbles up unchanged
    new_head = reverseList_recursive(head.next)

    # Our successor should now point back at us
    head.next.next = head
    head.next = None  # we become the new tail

    return new_head


# ============================================================================
# SOLUTION 3: Stack (Naive - DON'T use! Just for learning contrast)
# ============================================================================

def reverseList_stack(head):
    """
    Approach: Push every node onto a stack, then pop them off (LIFO gives
    us reverse order) and re-link.

    Algorithm:
    1. Push all nodes onto a stack
    2. Pop the first node -> that is the new head
    3. Keep popping, linking each popped node after the previous one
    4. Set the final node's next to None (critical - or you get a cycle!)

    Time Complexity: O(n) - two passes
    Space Complexity: O(n) - the stack holds every node ❌

    Why the three-pointer version is better:
    - Same O(n) time, but O(1) space instead of O(n)
    - This version exists only to show that "reverse" and "stack" are
      related ideas. Never submit this one.
    """
    if head is None:
        return None

    # Pass 1: push everything
    stack = []
    curr = head
    while curr:
        stack.append(curr)
        curr = curr.next

    # Pass 2: pop and re-link
    new_head = stack.pop()
    curr = new_head
    while stack:
        curr.next = stack.pop()
        curr = curr.next

    curr.next = None  # MUST cut the old head's arrow, else infinite loop!
    return new_head


# ============================================================================
# SOLUTION 4: Rebuild With New Nodes (Cheating - not "in place")
# ============================================================================

def reverseList_rebuild(head):
    """
    Approach: Read all values out, then build a fresh list backwards.

    Algorithm:
    1. Walk the list collecting values into a Python list
    2. Build a brand new linked list from the reversed values

    Time Complexity: O(n)
    Space Complexity: O(n) - values array + n brand new nodes

    Why this is NOT acceptable in an interview:
    - The problem says reverse the list, meaning rewire existing nodes.
    - Any other code holding a reference to an original node would not
      see the reversal. That is a real bug in real systems.
    - Shown here so you can articulate WHY in-place matters.
    """
    values = to_list(head)
    return build_list(values[::-1])


# ============================================================================
# TEST CASES
# ============================================================================

def test():
    """Test all solutions"""

    test_cases = [
        # (input_values, expected_output)
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),   # standard case
        ([1, 2], [2, 1]),                      # two nodes
        ([1], [1]),                            # single node (edge case)
        ([], []),                              # empty list (edge case!)
        ([1, 1, 1], [1, 1, 1]),                # duplicates
        ([-5, 0, 5000], [5000, 0, -5]),        # negatives + bounds
        ([7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7]),  # longer list
    ]

    solutions = [
        ("Iterative Three-Pointer (Optimal)", reverseList),
        ("Recursive", reverseList_recursive),
        ("Stack (Naive)", reverseList_stack),
        ("Rebuild (Cheating)", reverseList_rebuild),
    ]

    for name, solution in solutions:
        print(f"\n{'='*50}")
        print(f"Testing: {name}")
        print('='*50)

        all_passed = True
        for i, (values, expected) in enumerate(test_cases, 1):
            # Build a FRESH list per solution (reversing mutates it!)
            head = build_list(values)
            result = to_list(solution(head))

            is_correct = result == expected
            status = "✅" if is_correct else "❌"
            print(f"Test {i}: {status} {values} → {result} (expected {expected})")
            if not is_correct:
                all_passed = False

        if all_passed:
            print(f"\n🎉 All tests passed for {name}!")


# ============================================================================
# VISUAL DEMO
# ============================================================================

def visual_demo(values):
    """
    Visual step-by-step demonstration of the three-pointer reversal.
    """
    print(f"\n{'='*70}")
    print("VISUAL DEMO: Reverse Linked List (three-pointer walk)")
    print(f"Input: {values}")
    print('='*70)

    head = build_list(values)
    print(f"\nStarting list: {format_list(head)}")

    if head is None:
        print("\nEmpty list -> nothing to flip. Return None immediately. ✅")
        return

    prev = None
    curr = head
    step = 0

    print("\nStep-by-step execution:\n")

    while curr:
        step += 1
        next_temp = curr.next

        print(f"Step {step}:")
        print(f"  curr = [{curr.val}]")
        print(f"  prev = {'[' + str(prev.val) + ']' if prev else 'None'}")
        print(f"  1. SAVE next_temp = "
              f"{'[' + str(next_temp.val) + ']' if next_temp else 'None'}")
        print(f"  2. FLIP  [{curr.val}].next = "
              f"{'[' + str(prev.val) + ']' if prev else 'None'}")

        curr.next = prev
        prev = curr
        curr = next_temp

        print(f"  3. ADVANCE prev = [{prev.val}], curr = "
              f"{'[' + str(curr.val) + ']' if curr else 'None'}")
        print(f"     Reversed so far: {format_list(prev)}")
        print(f"     Still to do:     {format_list(curr)}")
        print()

    print(f"curr is None -> loop ends. Return prev.")
    print(f"✅ Final reversed list: {format_list(prev)}")
    print(f"   As a Python list: {to_list(prev)}")


# ============================================================================
# WHAT YOU SHOULD LEARN
# ============================================================================

"""
KEY TAKEAWAYS:
-------------
1. THREE POINTERS: prev, curr, next_temp. Two is not enough!
2. SAVE BEFORE YOU OVERWRITE - `next_temp = curr.next` must come first.
3. Return `prev`, not `curr`. When the loop ends curr is None.
4. Iterative is O(1) space; recursive is O(n) stack space.
5. "In place" means rewire existing nodes, not build new ones.

PATTERN RECOGNITION:
-------------------
When you see:
- "Reverse the list / a sublist / groups of k"
- "Check if a linked list is a palindrome" (reverse the second half!)
- "Reorder list" (reverse the back half, then weave)

Think: PREV / CURR / NEXT_TEMP THREE-POINTER WALK!

THE FOUR-LINE LOOP BODY (memorize this rhythm):
----------------------------------------------
    next_temp = curr.next   # SAVE
    curr.next = prev        # FLIP
    prev = curr             # ADVANCE prev
    curr = next_temp        # ADVANCE curr

Say it out loud while you write it: "save, flip, advance, advance."

INTERVIEW TIPS:
--------------
1. DRAW THE ARROWS on the whiteboard - this problem is visual (GUIDE tip #1)
2. State the invariant: "prev heads the reversed part, curr heads the rest"
3. Give the iterative solution first, then offer the recursive one
4. Call out the edge cases yourself: empty list and single node
5. Mention the O(n) stack depth risk of recursion - interviewers love that

COMMON MISTAKES:
---------------
❌ Forgetting next_temp -> you orphan the rest of the list instantly
❌ Returning `curr` or `head` instead of `prev`
❌ Writing `while curr.next` instead of `while curr` (drops the last node)
❌ In the recursive version, forgetting `head.next = None` -> creates a
   2-node cycle between the last two nodes and hangs any later traversal
❌ Assuming head is non-None - always handle the empty list

VARIATIONS:
----------
- Reverse Linked List II - reverse only positions left..right
- Reverse Nodes in k-Group (Hard) - reverse chunks of k
- Palindrome Linked List - find middle, reverse half, compare
- Reorder List - split, reverse, merge

TIME COMPLEXITY COMPARISON:
--------------------------
Rebuild new list:  O(n) time, O(n) space  (and not in place!)
Stack:             O(n) time, O(n) space
Recursive:         O(n) time, O(n) space  (call stack)
Iterative:         O(n) time, O(1) space ← BEST!

NEXT STEPS:
----------
✅ Mastered pointer rewiring
✅ Know the save/flip/advance rhythm
→ Now try: Merge Two Sorted Lists (dummy head pattern!)
→ Then:    Linked List Cycle (slow & fast pointers)

PRACTICE MORE:
-------------
Similar problems to practice this pattern:
- Merge Two Sorted Lists
- Palindrome Linked List
- Reorder List
- Reverse Linked List II
- Reverse Nodes in k-Group
"""


if __name__ == "__main__":
    # Run tests
    test()

    # Visual demonstrations
    visual_demo([1, 2, 3])
    visual_demo([1, 2, 3, 4, 5])
    visual_demo([])

    # Interactive practice
    print("\n" + "="*70)
    print("YOUR TURN TO TRACE!")
    print("="*70)
    print("\nTry tracing through this example yourself:")
    print("head = [10, 20, 30, 40]")
    print("\nAt each step, write down prev, curr, and next_temp.")
    print("Then run: visual_demo([10, 20, 30, 40])")
