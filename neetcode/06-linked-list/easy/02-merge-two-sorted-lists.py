"""
Problem: Merge Two Sorted Lists
Difficulty: Easy
Topics: Linked List, Recursion, Two Pointers

Problem Statement:
-----------------
You are given the heads of two sorted linked lists, list1 and list2.

Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists (reuse the existing
nodes - do not allocate new ones).

Return the head of the merged linked list.

Examples:
---------
Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    Explanation: Repeatedly take the smaller head:
        1(l1), 1(l2), 2(l1), 3(l2), 4(l1), 4(l2)

Example 2:
    Input: list1 = [], list2 = []
    Output: []
    Explanation: Both empty -> merged is empty (edge case!).

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]
    Explanation: One empty -> just return the other list untouched.

Constraints:
-----------
- The number of nodes in both lists is in the range [0, 50]
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in NON-DECREASING order

LEARNING NOTES:
--------------
This is the merge step of merge sort, written for linked lists. It is also
the building block of "Merge K Sorted Lists" (Hard). Learn it well!

Key Insight: Use a DUMMY HEAD!
    Without a dummy you need an ugly special case:
        "is this the first node? then set head, else append"
    With a dummy node sitting in front, EVERY node is appended the same
    way, and at the end you just `return dummy.next`.

    This is GUIDE.md pattern #2 and it shows up everywhere in linked list
    problems. Whenever the head of your result might change (or might not
    exist yet), reach for a dummy head.

Second Insight: Because both inputs are already sorted, the next node of
    the answer is ALWAYS the smaller of the two current heads. You never
    have to look further ahead than one node on each list.

Pattern: "Merge two sorted sequences" -> Dummy head + compare-and-advance!

Visualization:
    list1 = [1, 2, 4]      list2 = [1, 3, 4]

    dummy → ?
    tail = dummy

    Compare 1 vs 1  -> tie, take list1 (keeps the merge STABLE)
        dummy → [1]                    l1=[2,4]  l2=[1,3,4]
    Compare 2 vs 1  -> take list2
        dummy → [1] → [1]              l1=[2,4]  l2=[3,4]
    Compare 2 vs 3  -> take list1
        dummy → [1] → [1] → [2]        l1=[4]    l2=[3,4]
    Compare 4 vs 3  -> take list2
        dummy → [1] → [1] → [2] → [3]  l1=[4]    l2=[4]
    Compare 4 vs 4  -> tie, take list1
        dummy → [1] → [1] → [2] → [3] → [4]      l1=None  l2=[4]

    list1 is exhausted -> ATTACH the whole leftover of list2 at once:
        dummy → [1] → [1] → [2] → [3] → [4] → [4] → None

    return dummy.next = [1,1,2,3,4,4] ✅

    NOTE the last move: you do NOT need to walk the leftover node by node.
    It is already sorted and already linked, so one pointer assignment
    splices the entire remainder on.
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


def build_list(values):
    """
    Build a linked list from a plain Python list.

    build_list([1, 2, 4])  ->  [1] → [2] → [4] → None
    build_list([])         ->  None

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    dummy = ListNode(0)  # the same dummy-head trick we use in the solution!
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def to_list(head):
    """
    Convert a linked list back to a plain Python list so tests can assert
    on ordinary values.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    values = []
    curr = head

    while curr:
        values.append(curr.val)
        curr = curr.next

    return values


def format_list(head):
    """Pretty-print a linked list as: [1] → [2] → [4] → None"""
    values = to_list(head)
    if not values:
        return "None (empty list)"
    return " → ".join(f"[{v}]" for v in values) + " → None"


# ============================================================================
# SOLUTION 1: Iterative with Dummy Head (OPTIMAL!)
# ============================================================================

def mergeTwoLists(list1, list2):
    """
    Approach: Walk both lists at once, always splicing the smaller head
    onto the tail of the result. Use a dummy head so appending is uniform.

    Algorithm:
    1. Create dummy = ListNode(0); tail = dummy
    2. While BOTH lists still have nodes:
       a. If list1.val <= list2.val: tail.next = list1; list1 = list1.next
       b. Else:                      tail.next = list2; list2 = list2.next
       c. tail = tail.next
    3. One list is now empty. Attach the OTHER list wholesale:
       tail.next = list1 if list1 else list2
    4. Return dummy.next (the real head; dummy itself is discarded)

    Why it works:
    - Both inputs are sorted, so the global minimum of what remains is
      always one of the two current heads.
    - Step 3 is safe because whatever remains is already sorted and is
      already >= everything we have placed.

    Why `<=` and not `<`:
    - On ties we take from list1, which makes the merge STABLE (equal
      elements keep their relative order). It also avoids an infinite
      loop-style bug if you ever adapt this code and forget to advance.

    Time Complexity: O(n + m) - each node is visited and spliced once
    Space Complexity: O(1) - only the dummy and a couple of pointers; we
                      reuse the input nodes rather than allocating new ones
    """
    dummy = ListNode(0)  # sacrificial node so we never special-case "first"
    tail = dummy

    # Compare-and-advance while both lists have something left
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Exactly one list may still have nodes - splice the whole thing on.
    # (If both are None this harmlessly sets tail.next = None.)
    tail.next = list1 if list1 else list2

    return dummy.next


# ============================================================================
# SOLUTION 2: Recursive (Elegant, mirrors the definition of "merge")
# ============================================================================

def mergeTwoLists_recursive(list1, list2):
    """
    Approach: The merge of two lists is "the smaller head, followed by the
    merge of what's left". Write that sentence as code.

    Algorithm:
    1. Base case: if list1 is None -> return list2
    2. Base case: if list2 is None -> return list1
    3. If list1.val <= list2.val:
         list1.next = merge(list1.next, list2); return list1
       Else:
         list2.next = merge(list1, list2.next); return list2

    Time Complexity: O(n + m) - one call per node consumed
    Space Complexity: O(n + m) - call stack depth ❌

    Interview note: beautiful and short, but the stack grows with the total
    number of nodes. Prefer the iterative version for large inputs.
    """
    # Base cases: an empty list merged with X is just X
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val <= list2.val:
        list1.next = mergeTwoLists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists_recursive(list1, list2.next)
        return list2


# ============================================================================
# SOLUTION 3: No Dummy Head (Works, but see how much uglier it is!)
# ============================================================================

def mergeTwoLists_nodummy(list1, list2):
    """
    Approach: Same compare-and-advance, but without a dummy node - so we
    must hand-pick the head first and guard every append.

    Algorithm:
    1. Handle the empty-input cases up front
    2. Pick the smaller head manually and advance that list
    3. Then run the normal compare-and-advance loop
    4. Attach the leftover

    Time Complexity: O(n + m)
    Space Complexity: O(1)

    Why the dummy version is better:
    - Identical complexity, but ~8 fewer lines and no head special case.
    - Fewer branches = fewer places to introduce a bug under pressure.
    - This variant is here purely so you can FEEL why the dummy exists.
    """
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    # Manually choose the head (the part the dummy would have handled)
    if list1.val <= list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    tail = head

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2

    return head


# ============================================================================
# SOLUTION 4: Collect and Sort (Naive - DON'T use! Just for contrast)
# ============================================================================

def mergeTwoLists_sort(list1, list2):
    """
    Approach: Dump every value into a Python list, sort it, rebuild.

    Algorithm:
    1. Walk both lists collecting values
    2. Sort the combined values
    3. Build a fresh linked list

    Time Complexity: O((n + m) log(n + m)) - the sort dominates ❌
    Space Complexity: O(n + m) - values array + brand new nodes ❌

    Why this is wrong for this problem:
    - It THROWS AWAY the fact that the inputs are already sorted. That
      free information is exactly what makes the O(n + m) merge possible.
    - It allocates new nodes instead of splicing existing ones, which the
      problem statement explicitly asks you not to do.
    - If an interviewer sees this first, they will assume you did not
      notice "sorted" in the problem statement.
    """
    values = to_list(list1) + to_list(list2)
    values.sort()
    return build_list(values)


# ============================================================================
# TEST CASES
# ============================================================================

def test():
    """Test all solutions"""

    test_cases = [
        # (list1_values, list2_values, expected)
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),  # classic example
        ([], [], []),                                 # both empty (edge!)
        ([], [0], [0]),                               # one empty (edge!)
        ([5], [], [5]),                               # other empty (edge!)
        ([1], [2], [1, 2]),                           # single vs single
        ([2], [1], [1, 2]),                           # order swapped
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),   # no interleaving
        ([4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5, 6]),   # fully front-loaded
        ([1, 1, 1], [1, 1], [1, 1, 1, 1, 1]),         # all duplicates
        ([-100, 0, 100], [-50, 50], [-100, -50, 0, 50, 100]),  # negatives
    ]

    solutions = [
        ("Iterative + Dummy Head (Optimal)", mergeTwoLists),
        ("Recursive", mergeTwoLists_recursive),
        ("Iterative, No Dummy", mergeTwoLists_nodummy),
        ("Collect and Sort (Naive)", mergeTwoLists_sort),
    ]

    for name, solution in solutions:
        print(f"\n{'='*50}")
        print(f"Testing: {name}")
        print('='*50)

        all_passed = True
        for i, (v1, v2, expected) in enumerate(test_cases, 1):
            # Rebuild fresh lists each time - merging consumes the inputs!
            l1 = build_list(v1)
            l2 = build_list(v2)
            result = to_list(solution(l1, l2))

            is_correct = result == expected
            status = "✅" if is_correct else "❌"
            print(f"Test {i}: {status} {v1} + {v2} → {result} "
                  f"(expected {expected})")
            if not is_correct:
                all_passed = False

        if all_passed:
            print(f"\n🎉 All tests passed for {name}!")


# ============================================================================
# VISUAL DEMO
# ============================================================================

def visual_demo(values1, values2):
    """
    Visual step-by-step demonstration of the dummy-head merge.
    """
    print(f"\n{'='*70}")
    print("VISUAL DEMO: Merge Two Sorted Lists (dummy head)")
    print(f"Input: list1 = {values1}, list2 = {values2}")
    print('='*70)

    list1 = build_list(values1)
    list2 = build_list(values2)

    print(f"\nlist1: {format_list(list1)}")
    print(f"list2: {format_list(list2)}")

    dummy = ListNode(0)
    tail = dummy
    step = 0

    print("\nStep-by-step execution:\n")

    while list1 and list2:
        step += 1
        print(f"Step {step}:")
        print(f"  list1 head = [{list1.val}], list2 head = [{list2.val}]")

        if list1.val <= list2.val:
            print(f"  {list1.val} <= {list2.val} → take from list1 "
                  f"(ties go to list1, keeping the merge stable)")
            tail.next = list1
            list1 = list1.next
        else:
            print(f"  {list2.val} <  {list1.val} → take from list2")
            tail.next = list2
            list2 = list2.next

        tail = tail.next
        tail.next = None  # display-only: keeps the partial print clean
        print(f"  Merged so far: {format_list(dummy.next)}")
        print()

    step += 1
    leftover = list1 if list1 else list2
    print(f"Step {step} (cleanup):")
    if leftover:
        which = "list1" if list1 else "list2"
        print(f"  One list is empty; {which} still has "
              f"{format_list(leftover)}")
        print(f"  ✅ Splice the ENTIRE remainder on with one assignment "
              f"(it is already sorted!)")
    else:
        print("  Both lists are empty - nothing left to attach.")

    tail.next = leftover

    print(f"\n✅ Final merged list: {format_list(dummy.next)}")
    print(f"   As a Python list: {to_list(dummy.next)}")
    print("   (We return dummy.next - the dummy node itself is thrown away.)")


# ============================================================================
# WHAT YOU SHOULD LEARN
# ============================================================================

"""
KEY TAKEAWAYS:
-------------
1. DUMMY HEAD removes the "is this the first node?" special case.
2. Return dummy.next, NEVER dummy itself.
3. Because both inputs are sorted, one comparison per step is enough.
4. Attach the leftover in ONE assignment - do not loop over it.
5. Splice existing nodes; allocating new ones is a different (worse) answer.

PATTERN RECOGNITION:
-------------------
When you see:
- "Merge two sorted ..." / "combine sorted sequences"
- "Build a new list whose head may change"
- "Remove nodes from a list" (dummy protects you if the head is removed)

Think: DUMMY HEAD + COMPARE-AND-ADVANCE!

THE DUMMY HEAD TRICK:
--------------------
    dummy = ListNode(0)
    tail = dummy
    ... tail.next = something; tail = tail.next ...
    return dummy.next

`dummy` never moves, so it always remembers where the answer starts.
`tail` walks forward as the answer grows.

INTERVIEW TIPS:
--------------
1. Say "both lists are sorted, so I only ever compare the two heads"
2. Introduce the dummy explicitly: "this saves me a head special case"
3. Call out the leftover splice - it shows you noticed it is already sorted
4. Handle empty inputs out loud; they are 2 of the 3 LeetCode examples
5. Follow up with: "this same routine, in a heap, solves Merge K Sorted Lists"

COMMON MISTAKES:
---------------
❌ Returning `dummy` instead of `dummy.next` (extra leading 0 in output)
❌ Forgetting the leftover splice -> merged list is silently truncated
❌ Walking the leftover node-by-node (works, but wasteful and error-prone)
❌ Using `<` instead of `<=` -> merge is no longer stable
❌ Forgetting to advance `tail` -> you keep overwriting the same link
❌ Not handling one or both lists being empty

VARIATIONS:
----------
- Merge K Sorted Lists (Hard) - this routine + a min-heap
- Sort List - merge sort on a linked list, uses this as the merge step
- Merge Sorted Array - the array version, merged from the back
- Intersection / union of two sorted lists

TIME COMPLEXITY COMPARISON:
--------------------------
Collect and sort:   O((n+m) log(n+m)) time, O(n+m) space
Recursive merge:    O(n+m) time, O(n+m) space (call stack)
Iterative, no dummy:O(n+m) time, O(1) space (but messier)
Iterative + dummy:  O(n+m) time, O(1) space ← BEST!

NEXT STEPS:
----------
✅ Mastered the dummy head pattern
✅ Know the merge step of merge sort
→ Now try: Linked List Cycle (slow & fast pointers)
→ Then:    Remove Nth Node From End (dummy head + two pointers)

PRACTICE MORE:
-------------
Similar problems to practice this pattern:
- Reverse Linked List
- Remove Nth Node From End of List
- Add Two Numbers
- Merge K Sorted Lists
- Sort List
"""


if __name__ == "__main__":
    # Run tests
    test()

    # Visual demonstrations
    visual_demo([1, 2, 4], [1, 3, 4])
    visual_demo([], [0])

    # Interactive practice
    print("\n" + "="*70)
    print("YOUR TURN TO TRACE!")
    print("="*70)
    print("\nTry tracing through this example yourself:")
    print("list1 = [1, 3, 5, 7], list2 = [2, 4]")
    print("\nWhich list does each step take from?")
    print("Where does the leftover splice happen?")
    print("Then run: visual_demo([1, 3, 5, 7], [2, 4])")
