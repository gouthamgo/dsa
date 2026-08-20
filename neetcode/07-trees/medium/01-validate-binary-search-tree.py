"""
Problem: Validate Binary Search Tree
Difficulty: Medium
Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree, Recursion

Problem Statement:
-----------------
Given the root of a binary tree, determine if it is a valid binary search
tree (BST).

A valid BST is defined as follows:
    - The left subtree of a node contains ONLY nodes with keys strictly
      LESS than the node's key.
    - The right subtree of a node contains ONLY nodes with keys strictly
      GREATER than the node's key.
    - Both the left and right subtrees must themselves be valid BSTs.

Read that first bullet again: it says SUBTREE, not CHILD. That single word
is the whole problem.

Examples:
---------
Example 1:
    Input: root = [2,1,3]
    Output: True
    Explanation:
            2
           / \
          1   3      1 < 2 < 3 ✓

Example 2:
    Input: root = [5,1,4,null,null,3,6]
    Output: False
    Explanation:
            5
           / \
          1   4
             / \
            3   6
    Node 4's children look fine locally (3 < 4 < 6), but 4 is in 5's RIGHT
    subtree, so every node under it must be > 5. The 3 violates that.

Example 3:
    Input: root = [5,4,6,null,null,3,7]
    Output: False
    Explanation: The classic trap!
            5
           / \
          4   6
             / \
            3   7
    Check only parent-vs-children and everything passes:
        4 < 5 ✓, 6 > 5 ✓, 3 < 6 ✓, 7 > 6 ✓
    But 3 sits in 5's right subtree and 3 < 5. NOT a BST.

Constraints:
-----------
- The number of nodes in the tree is in the range [1, 10^4]
  (we also handle the empty tree here - it is vacuously valid)
- -2^31 <= Node.val <= 2^31 - 1

LEARNING NOTES:
--------------
This problem exists to punish one specific wrong instinct. Read the
"THE BUG" section below before anything else - understanding the wrong
answer is more valuable than memorizing the right one.

THE BUG (the naive "check children only" solution):
    if root.left and root.left.val >= root.val:  return False
    if root.right and root.right.val <= root.val: return False
    ... recurse ...

    This checks a LOCAL property. But "BST" is a GLOBAL property: a node
    constrains not just its children, but every single descendant.

    Example 3 above defeats it. Node 3 is a legal left child of 6, but it
    is an illegal descendant of 5. A local check can never see that,
    because by the time you are standing on node 3, you have forgotten
    that you turned right at 5.

Key Insight: CARRY THE VALID RANGE DOWN THE TREE.
    Every node inherits an open interval (low, high) it must live in.
    - Start at the root with (-infinity, +infinity)
    - Going LEFT tightens the ceiling:  (low, node.val)
    - Going RIGHT raises the floor:     (node.val, high)

    Now node 3 in Example 3 arrives with the range (5, 6) - because we
    went right at 5 (floor = 5) then left at 6 (ceiling = 6). 3 is not in
    (5, 6), so it is correctly rejected. The information we "forgot" in
    the buggy version is exactly what the range carries for us.

Pattern: "Validate a global tree property" -> DFS carrying STATE DOWN
         (top-down), not just returning values up (bottom-up).

    Contrast with Maximum Depth, which was purely bottom-up. This problem
    is the natural next step: information flows DOWNWARD into the calls.

Second Insight: An inorder traversal of a valid BST is strictly increasing
    (see GUIDE.md - "Result: [4, 2, 5, 1, 3] (sorted for BST!)"). So an
    equally valid approach is: traverse inorder, and check that each value
    is strictly greater than the one before it.

Visualization:
    root = [5, 4, 6, null, null, 3, 7]

            5
           / \
          4   6
             / \
            3   7

    Ranges pushed down the tree:

    validate(5, low=-inf, high=+inf)
        -inf < 5 < +inf ✓
        │
        ├── validate(4, low=-inf, high=5)      [went LEFT: ceiling = 5]
        │       -inf < 4 < 5 ✓  (leaf, both children None → True)
        │
        └── validate(6, low=5, high=+inf)      [went RIGHT: floor = 5]
                5 < 6 < +inf ✓
                │
                ├── validate(3, low=5, high=6) [LEFT of 6: ceiling = 6]
                │       is 5 < 3 ? NO ❌  → return False
                │
                └── (never reached - False short-circuits)

    Answer: False ✅ (correctly caught, unlike the naive version)

    Compare with the naive check on the SAME tree:
        5: children 4 and 6 → 4 < 5 < 6 ✓ pass
        4: no children               ✓ pass
        6: children 3 and 7 → 3 < 6 < 7 ✓ pass
        3, 7: no children            ✓ pass
        Naive answer: True ❌ WRONG!
"""

from collections import deque


# ============================================================================
# SETUP: Node definition + helpers (so this file runs standalone)
# ============================================================================

class TreeNode:
    """A binary tree node: [left | val | right]"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def build_tree(values):
    """
    Build a binary tree from a LeetCode-style level-order list.
    `None` marks a missing child.

        build_tree([5, 4, 6, None, None, 3, 7])
                5
               / \
              4   6
                 / \
                3   7

        build_tree([]) -> None

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

    return root


def to_list(root):
    """
    Convert a tree back to a level-order list (trailing Nones trimmed).

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not root:
        return []

    values = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            values.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            values.append(None)

    while values and values[-1] is None:
        values.pop()

    return values


def print_tree(root, prefix="", is_left=True):
    """
    Print the tree sideways (tilt your head left). Right subtree on top.

    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    if root is None:
        return

    print_tree(root.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(root.val))
    print_tree(root.left, prefix + ("    " if is_left else "│   "), True)


def inorder_values(root):
    """
    Collect all values via inorder traversal (Left → Root → Right).

    For a VALID BST this comes out strictly increasing. Handy for demos.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if root is None:
        return []
    return (inorder_values(root.left)
            + [root.val]
            + inorder_values(root.right))


# ============================================================================
# SOLUTION 0: The Naive "Check Children Only" BUG (WRONG! Learn from it)
# ============================================================================

def isValidBST_naive_BUGGY(root):
    """
    ⚠️  THIS SOLUTION IS WRONG ON PURPOSE. DO NOT SUBMIT IT.
    It is here because writing it is the mistake almost everyone makes,
    and seeing exactly how it fails is the fastest way to never make it.

    Approach (flawed): At each node, check only its immediate children,
    then recurse.

    Algorithm:
    1. Base case: None -> True
    2. If root.left exists and root.left.val >= root.val -> False
    3. If root.right exists and root.right.val <= root.val -> False
    4. Return naive(root.left) AND naive(root.right)

    Time Complexity: O(n)
    Space Complexity: O(h)

    WHY IT IS WRONG:
    ---------------
    It verifies a LOCAL invariant ("I am bigger than my left child") when
    the problem states a GLOBAL one ("I am bigger than EVERY node in my
    left subtree").

    Counterexample - [5, 4, 6, None, None, 3, 7]:
            5
           / \
          4   6
             / \
            3   7
    Every parent/child pair is fine, so this returns True. But 3 lives in
    5's right subtree and 3 < 5, so the tree is NOT a BST.

    The deep reason: when the recursion reaches node 3, it has LOST the
    memory that it passed through 5 on the way down. The fix is not a
    better local check - it is to carry that memory along. That is
    precisely what Solution 1's (low, high) range does.

    Watch how badly this scales, too: you could try patching it by also
    comparing against grandchildren, then great-grandchildren... that is
    an O(n^2) road to nowhere. Carry the range instead.
    """
    if root is None:
        return True

    # ❌ Only looks one level down - this is the bug!
    if root.left is not None and root.left.val >= root.val:
        return False
    if root.right is not None and root.right.val <= root.val:
        return False

    return (isValidBST_naive_BUGGY(root.left)
            and isValidBST_naive_BUGGY(root.right))


# ============================================================================
# SOLUTION 1: DFS with Min/Max Bounds (OPTIMAL! The correct fix)
# ============================================================================

def isValidBST(root, low=float('-inf'), high=float('inf')):
    """
    Approach: Carry an allowed open interval (low, high) down to every node
    and check membership. Going left lowers the ceiling; going right raises
    the floor.

    Algorithm:
    1. Base case: None -> True (an empty subtree is vacuously a valid BST)
    2. Check this node fits its inherited window: low < root.val < high
       If not -> return False
    3. Recurse left  with (low, root.val)   <- everything left must be < me
    4. Recurse right with (root.val, high)  <- everything right must be > me
    5. Return the AND of both

    Why it works:
    - The window a node receives encodes EVERY ancestor decision on the
      path from the root. Turning left at ancestor A caps you at A.val
      forever; turning right at A floors you at A.val forever.
    - So the local check `low < val < high` is actually a global check.
    - Strict inequalities (`<`, not `<=`) enforce "strictly less/greater",
      which correctly rejects duplicate values.

    Why float('-inf') / float('inf') as the starting window:
    - The root is unconstrained, so its window must be all of the reals.
    - Using them avoids the classic bug of seeding with INT_MIN/INT_MAX,
      which breaks on a tree whose root actually IS -2^31 (a legal value
      per the constraints!). In Python you could also use None sentinels.

    Time Complexity: O(n) - each node is visited exactly once
    Space Complexity: O(h) - recursion stack, h = height.
                      Balanced: O(log n). Degenerate stick: O(n).

    This is the answer to give in an interview.
    """
    # Base case: nothing here to violate anything
    if root is None:
        return True

    # Does this node fit the window every ancestor handed down?
    if not (low < root.val < high):
        return False

    # Tighten the window for each side and recurse
    return (isValidBST(root.left, low, root.val)      # ceiling drops to me
            and isValidBST(root.right, root.val, high))  # floor rises to me


# ============================================================================
# SOLUTION 2: Inorder Traversal Must Be Strictly Increasing
# ============================================================================

def isValidBST_inorder(root):
    """
    Approach: Walk the tree inorder (Left → Root → Right) and verify each
    value is strictly greater than the previous one.

    Algorithm:
    1. Keep `prev`, the last value emitted by the inorder walk
    2. Recurse into the left subtree; bail out early if it fails
    3. Check root.val > prev; if not -> False. Then set prev = root.val
    4. Recurse into the right subtree
    5. Return True if the whole walk stayed increasing

    Why it works:
    - Inorder on a BST visits keys in sorted order (GUIDE.md, Traversals).
    - "Sorted with no duplicates" is exactly "strictly increasing", so the
      two conditions are equivalent. This gives a completely different -
      and equally correct - way to see the problem.

    Time Complexity: O(n) - one traversal
    Space Complexity: O(h) - recursion stack (we do NOT store the whole
                      list of values; only `prev`)

    Trade-off vs Solution 1: this version is a nice thing to mention as an
    alternative, but the bounds version fails FASTER (it can reject a bad
    node before traversing the rest of that subtree) and reads more
    directly from the BST definition.
    """
    # Use a one-element list so the nested function can mutate it
    prev = [float('-inf')]

    def walk(node):
        if node is None:
            return True

        # 1. Left subtree first
        if not walk(node.left):
            return False

        # 2. Then this node - must beat everything already emitted
        if node.val <= prev[0]:
            return False
        prev[0] = node.val

        # 3. Then the right subtree
        return walk(node.right)

    return walk(root)


# ============================================================================
# SOLUTION 3: Iterative Inorder with an Explicit Stack (No recursion)
# ============================================================================

def isValidBST_iterative(root):
    """
    Approach: The same inorder idea, but driving the traversal yourself
    with a stack instead of the call stack.

    Algorithm:
    1. stack = []; curr = root; prev = -infinity
    2. While stack is non-empty OR curr is not None:
       a. Walk as far LEFT as possible, pushing every node
       b. Pop a node - this is the next value in sorted order
       c. If node.val <= prev -> return False; else prev = node.val
       d. curr = node.right (now do that node's right subtree)
    3. Return True

    Time Complexity: O(n) - each node is pushed and popped once
    Space Complexity: O(h) - the stack holds one path at a time

    When to prefer this:
    - The tree may be ~10^4 nodes deep in a stick shape, which would blow
      Python's default recursion limit of 1000.
    - Interviewer explicitly asks for an iterative solution.

    This "push all the way left, pop, go right" loop is THE standard
    iterative inorder template - worth memorizing on its own.
    """
    stack = []
    curr = root
    prev = float('-inf')

    while stack or curr:
        # a. Dive as far left as we can
        while curr:
            stack.append(curr)
            curr = curr.left

        # b. This pop is the next node in sorted order
        node = stack.pop()

        # c. Must be strictly greater than everything seen so far
        if node.val <= prev:
            return False
        prev = node.val

        # d. Now handle its right subtree
        curr = node.right

    return True


# ============================================================================
# SOLUTION 4: Collect Inorder Then Check Sorted (Naive - wasteful)
# ============================================================================

def isValidBST_collect(root):
    """
    Approach: Build the full inorder list, then check it is strictly
    increasing.

    Algorithm:
    1. values = inorder_values(root)
    2. Return all(values[i] < values[i+1] for each adjacent pair)

    Time Complexity: O(n)
    Space Complexity: O(n) - stores every value ❌

    Why the others are better:
    - Same time, but O(n) extra space instead of O(h).
    - No early exit: it traverses the ENTIRE tree even if the very first
      two nodes already prove the answer is False.
    - Still, it is the easiest version to explain, and it makes the
      "inorder of a BST is sorted" fact vivid. Good stepping stone, bad
      final answer.
    """
    values = inorder_values(root)

    for i in range(len(values) - 1):
        if values[i] >= values[i + 1]:  # >= catches duplicates too
            return False

    return True


# ============================================================================
# TEST CASES
# ============================================================================

def test():
    """Test all CORRECT solutions (the buggy one is tested separately)"""

    test_cases = [
        # (level_order_values, expected_is_valid)
        ([2, 1, 3], True),                          # textbook valid BST
        ([5, 1, 4, None, None, 3, 6], False),       # LeetCode example 2
        ([5, 4, 6, None, None, 3, 7], False),       # THE TRAP - naive fails
        ([], True),                                 # empty tree (edge case!)
        ([1], True),                                # single node (edge case)
        ([2, 2], False),                            # duplicate: 2 not < 2
        ([2, 1, 2], False),                         # duplicate on the right
        ([10, 5, 15, None, None, 6, 20], False),    # 6 < 10 but sits right
        ([10, 5, 15, 3, 7, 12, 20], True),          # full valid BST
        ([1, None, 2, None, 3, None, 4], True),     # right stick, increasing
        ([4, 3, None, 2, None, 1], True),           # left stick, decreasing
        ([3, 1, 5, 0, 2, 4, 6], True),              # another valid BST
        ([3, 1, 5, 0, 2, 4, 6, None, None, None, 3], False),  # 3 == root
        ([-2147483648], True),                      # INT_MIN root - breaks
                                                    # solutions that seed
                                                    # bounds with INT_MIN!
        ([2147483647], True),                       # INT_MAX root
        ([0, -1], True),                            # negatives
    ]

    solutions = [
        ("DFS + Min/Max Bounds (Optimal)", isValidBST),
        ("Recursive Inorder (prev tracking)", isValidBST_inorder),
        ("Iterative Inorder (stack)", isValidBST_iterative),
        ("Collect Inorder Then Check (Naive)", isValidBST_collect),
    ]

    for name, solution in solutions:
        print(f"\n{'='*50}")
        print(f"Testing: {name}")
        print('='*50)

        all_passed = True
        for i, (values, expected) in enumerate(test_cases, 1):
            root = build_tree(values)
            result = solution(root)

            is_correct = result == expected
            status = "✅" if is_correct else "❌"
            print(f"Test {i}: {status} {values} → {result} "
                  f"(expected {expected})")
            if not is_correct:
                all_passed = False

        if all_passed:
            print(f"\n🎉 All tests passed for {name}!")

    # ------------------------------------------------------------------
    # The teaching moment: prove the naive solution is broken
    # ------------------------------------------------------------------
    print(f"\n{'='*50}")
    print("Testing: The NAIVE 'check children only' solution")
    print("(We EXPECT this one to get some answers wrong!)")
    print('='*50)

    wrong_cases = []
    for i, (values, expected) in enumerate(test_cases, 1):
        root = build_tree(values)
        result = isValidBST_naive_BUGGY(root)

        agrees = result == expected
        marker = "agrees" if agrees else "⚠️  WRONG"
        print(f"Test {i}: {values}")
        print(f"         naive → {result}, correct → {expected}  [{marker}]")
        if not agrees:
            wrong_cases.append((values, result, expected))

    print(f"\n{'-'*50}")
    if wrong_cases:
        print(f"The naive solution got {len(wrong_cases)} case(s) WRONG:")
        for values, got, want in wrong_cases:
            print(f"  {values}: said {got}, should be {want}")
        print("\n✅ Confirmed: local parent-vs-child checks are NOT enough.")
        print("   Every one of these failures is a node that is fine")
        print("   relative to its parent but violates a distant ancestor.")
        print("   The (low, high) range in Solution 1 is what fixes it.")
    else:
        print("❌ Unexpected - the naive version should fail these cases!")


# ============================================================================
# VISUAL DEMO
# ============================================================================

def visual_demo(values):
    """
    Visual step-by-step demonstration: show the (low, high) window each
    node inherits, and contrast with what the naive check would say.
    """
    print(f"\n{'='*70}")
    print("VISUAL DEMO: Validate BST (min/max bounds carried downward)")
    print(f"Input (level order): {values}")
    print('='*70)

    root = build_tree(values)

    if root is None:
        print("\nEmpty tree -> base case fires, return True "
              "(vacuously a valid BST). ✅")
        return

    print("\nThe tree (printed sideways - tilt your head left):\n")
    print_tree(root)

    print(f"\nInorder traversal: {inorder_values(root)}")
    print("(For a VALID BST this list must be strictly increasing.)")

    print("\nStep-by-step execution (each node checks its inherited window):\n")

    def fmt(x):
        if x == float('-inf'):
            return "-inf"
        if x == float('inf'):
            return "+inf"
        return str(x)

    failure = []

    def validate_traced(node, low, high, depth, direction):
        if node is None:
            return True

        indent = "  " * depth
        window = f"({fmt(low)}, {fmt(high)})"

        print(f"{indent}{direction}node [{node.val}] must be in {window}")

        if not (low < node.val < high):
            print(f"{indent}  ❌ VIOLATION: {fmt(low)} < {node.val} < "
                  f"{fmt(high)} is FALSE")
            print(f"{indent}     → this subtree is invalid, return False")
            failure.append(node.val)
            return False

        print(f"{indent}  ✅ fits the window")

        left_ok = validate_traced(node.left, low, node.val, depth + 1,
                                  "LEFT  → ")
        if not left_ok:
            return False

        return validate_traced(node.right, node.val, high, depth + 1,
                               "RIGHT → ")

    result = validate_traced(root, float('-inf'), float('inf'), 0, "ROOT  → ")

    print(f"\n{'-'*70}")
    print(f"✅ Correct answer (bounds method): {result}")

    naive = isValidBST_naive_BUGGY(root)
    if naive != result:
        print(f"⚠️  Naive 'check children only' answer: {naive}  ← WRONG!")
        print(f"    Node {failure[0]} is legal next to its own parent, but")
        print(f"    it violates an ANCESTOR further up. A local check")
        print(f"    cannot see that; the inherited window can.")
    else:
        print(f"   Naive 'check children only' answer: {naive} "
              f"(happens to agree on this tree)")


# ============================================================================
# WHAT YOU SHOULD LEARN
# ============================================================================

"""
KEY TAKEAWAYS:
-------------
1. BST is a GLOBAL property. "Left subtree", not "left child".
2. Checking only parent-vs-child is THE classic wrong answer. It passes
   [5,4,6,null,null,3,7] which is not a BST.
3. The fix: carry a (low, high) window down the recursion.
   Go left  -> (low, node.val)
   Go right -> (node.val, high)
4. Seed with -inf / +inf, NOT INT_MIN / INT_MAX (a node may equal INT_MIN).
5. Use STRICT inequalities so duplicates are rejected.
6. Alternative view: inorder traversal of a BST is strictly increasing.

PATTERN RECOGNITION:
-------------------
When you see:
- "Validate / verify a property that involves ancestors"
- "Every node in the subtree must satisfy X"
- Any BST question at all

Think: DFS CARRYING STATE DOWNWARD (top-down), or INORDER = SORTED!

TOP-DOWN vs BOTTOM-UP RECURSION:
-------------------------------
    BOTTOM-UP (Maximum Depth):  children compute values, parent combines
        return 1 + max(solve(left), solve(right))

    TOP-DOWN (Validate BST):    parent hands constraints to children
        return solve(left, low, node.val) and solve(right, node.val, high)

Recognizing which direction information needs to flow is half of tree
problem solving. If a node's answer depends on its ANCESTORS, go top-down.

INTERVIEW TIPS:
--------------
1. Say the definition back precisely: "subtree, not child" - it signals
   immediately that you know the trap
2. Draw [5,4,6,null,null,3,7] and show why the naive check fails. Doing
   this unprompted is a very strong move
3. Then introduce the (low, high) window as the fix
4. Mention the inorder alternative as a second approach
5. Call out the INT_MIN seeding pitfall - it is a real LeetCode test case
6. Offer the iterative version if depth could reach 10^4

COMMON MISTAKES:
---------------
❌ Comparing only against immediate children (Solution 0 - the whole point
   of this problem)
❌ Using <= or >= instead of < and > (duplicates would wrongly pass)
❌ Seeding bounds with INT_MIN/INT_MAX and failing on a root of -2^31
❌ Swapping which bound tightens: going LEFT lowers the ceiling, going
   RIGHT raises the floor. Mixing them up passes some trees and fails
   others, which is a miserable bug to find
❌ In the inorder version, using a plain local `prev` variable in a nested
   function - Python rebinds it locally. Use a list, a class attribute, or
   `nonlocal`
❌ Storing the whole inorder list when only `prev` is needed (O(n) space
   for no reason)

VARIATIONS:
----------
- Kth Smallest Element in a BST - inorder, stop at the kth value
- Lowest Common Ancestor of a BST - walk down comparing against both keys
- Recover Binary Search Tree - find the two swapped nodes via inorder
- Convert Sorted Array to BST - the inverse construction
- Range Sum of BST - prune subtrees using the same bounds idea

TIME COMPLEXITY COMPARISON:
--------------------------
Naive children-only:   O(n) time, O(h) space - and WRONG ❌
Collect inorder:       O(n) time, O(n) space, no early exit
Iterative inorder:     O(n) time, O(h) space, no recursion limit
Recursive inorder:     O(n) time, O(h) space
DFS + bounds:          O(n) time, O(h) space ← BEST (early exit, reads
                       straight off the BST definition)

NEXT STEPS:
----------
✅ Understand global vs local tree properties
✅ Can carry state DOWN a recursion, not just return it up
→ Now try: Kth Smallest Element in a BST (inorder with a counter)
→ Then:    Lowest Common Ancestor of a BST (walk down using BST order)

PRACTICE MORE:
-------------
Similar problems to practice this pattern:
- Kth Smallest Element in a BST
- Lowest Common Ancestor of a BST
- Binary Tree Right Side View
- Count Good Nodes in Binary Tree (also carries state downward!)
- Range Sum of BST
- Recover Binary Search Tree
"""


if __name__ == "__main__":
    # Run tests
    test()

    # Visual demonstrations
    visual_demo([5, 4, 6, None, None, 3, 7])   # the trap - naive says True
    visual_demo([2, 1, 3])                     # a valid BST
    visual_demo([10, 5, 15, 3, 7, 12, 20])     # bigger valid BST

    # Interactive practice
    print("\n" + "="*70)
    print("YOUR TURN TO TRACE!")
    print("="*70)
    print("\nTry tracing through this example yourself:")
    print("root = [5, 1, 4, None, None, 3, 6]")
    print("\nWhat window (low, high) does node 3 inherit?")
    print("Which ancestor does it violate?")
    print("Then run: visual_demo([5, 1, 4, None, None, 3, 6])")
