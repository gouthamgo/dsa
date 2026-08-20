"""
Problem: Invert Binary Tree
Difficulty: Easy
Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree, Recursion

Problem Statement:
-----------------
Given the root of a binary tree, invert the tree (mirror it left-to-right),
and return its root.

Inverting means: at EVERY node, swap its left and right children.

Fun fact: this is the problem that famously got a developer rejected from
Google. It is now the single most recognizable "can you do recursion?"
question in existence.

Examples:
---------
Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]
    Explanation:
            4                    4
          /   \                /   \
         2     7      ->      7     2
        / \   / \            / \   / \
       1   3 6   9          9   6 3   1

Example 2:
    Input: root = [2,1,3]
    Output: [2,3,1]
    Explanation:
          2            2
         / \    ->    / \
        1   3        3   1

Example 3:
    Input: root = []
    Output: []
    Explanation: An empty tree inverted is still empty (edge case!).

Constraints:
-----------
- The number of nodes in the tree is in the range [0, 100]
- -100 <= Node.val <= 100

LEARNING NOTES:
--------------
This is the perfect first tree problem. It teaches the shape that almost
every tree solution has:

    if not root: return <base case>
    do something with root
    recurse left
    recurse right

Key Insight: SWAP AT EVERY NODE, then let recursion handle the rest.
    You do NOT need to think about grandchildren. If you trust that the
    recursive call correctly inverts an entire subtree, then all you have
    to do at the current node is swap two pointers.

    This "trust the recursion" mindset is the single most important habit
    for tree problems. Do not trace 4 levels deep in your head - define
    what the function promises, then use that promise.

Pattern: "Transform every node the same way" -> DFS recursion (GUIDE.md
         pattern #1), one line of real work per node!

Visualization:
    Input tree (as a level-order list): [4, 2, 7, 1, 3, 6, 9]

            4
          /   \
         2     7
        / \   / \
       1   3 6   9

    invert(4):
        swap children of 4  ->  left=7, right=2
                4
              /   \
             7     2
            / \   / \
           6   9 1   3     (grandchildren not touched YET)

        invert(7):  swap -> left=9, right=6
        invert(2):  swap -> left=3, right=1

            4
          /   \
         7     2
        / \   / \
       9   6 3   1

        invert(9), invert(6), invert(3), invert(1):
            leaves - both children are None, swapping None with None
            is a harmless no-op. This is why leaves need no special case!

    Result (level order): [4, 7, 2, 9, 6, 3, 1] ✅
"""

from collections import deque


# ============================================================================
# SETUP: Node definition + helpers (so this file runs standalone)
# ============================================================================

class TreeNode:
    """
    A binary tree node: [left | val | right]

    This is the exact definition LeetCode hands you.
    """

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
        build_tree([4, 2, 7, 1, 3, 6, 9])
                4
              /   \
             2     7
            / \   / \
           1   3 6   9

        build_tree([1, None, 2])
                1
                 \
                  2

        build_tree([]) -> None

    Algorithm:
    1. Make the root from values[0]
    2. Keep a queue of nodes still waiting for children
    3. Pop a node, consume the next two values as its left/right children
    4. Push any real (non-None) children onto the queue

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

        # Left child
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

        # Right child
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1

    return root


def to_list(root):
    """
    Convert a binary tree back to a level-order list, with trailing Nones
    trimmed - matching how LeetCode prints trees.

    Needed so our tests can assert on plain Python values.

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

    # Trim trailing Nones (they carry no information)
    while values and values[-1] is None:
        values.pop()

    return values


def print_tree(root, prefix="", is_left=True):
    """
    Print the tree sideways so you can SEE the shape. Read it with your
    head tilted left: the root is on the far left, and the right subtree
    prints above the left one.

    Time Complexity: O(n)
    Space Complexity: O(h) - recursion depth
    """
    if root is None:
        return

    print_tree(root.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(root.val))
    print_tree(root.left, prefix + ("    " if is_left else "│   "), True)


# ============================================================================
# SOLUTION 1: Recursive DFS (OPTIMAL!)
# ============================================================================

def invertTree(root):
    """
    Approach: At each node, swap its two children, then recursively invert
    each subtree.

    Algorithm:
    1. Base case: if root is None, return None (nothing to invert)
    2. Swap root.left and root.right
    3. Recursively invert root.left (which is the OLD right subtree)
    4. Recursively invert root.right
    5. Return root

    Why it works:
    - Mirroring a tree = mirroring the top level AND mirroring both halves.
    - Every node is visited exactly once and does exactly one swap.
    - Leaves swap None with None, so they need no special case.

    Note: the order of steps 2 and 3-4 does not matter! You can swap first
    and then recurse, or recurse first and then swap. Both produce the same
    mirrored tree, because the swap at a node and the swaps inside its
    subtrees are independent.

    Time Complexity: O(n) - every node is visited once
    Space Complexity: O(h) - the recursion stack, h = height of the tree.
                      Balanced: O(log n). Degenerate (a "stick"): O(n).
    """
    # Base case: empty tree / past a leaf
    if root is None:
        return None

    # Do the one piece of real work at this node
    root.left, root.right = root.right, root.left

    # Trust the recursion to handle everything below
    invertTree(root.left)
    invertTree(root.right)

    return root


# ============================================================================
# SOLUTION 2: Recursive DFS, Rebuilding Style (Same idea, different phrasing)
# ============================================================================

def invertTree_rebuild_links(root):
    """
    Approach: Compute the inverted subtrees FIRST, then assign them across.

    Algorithm:
    1. Base case: None -> None
    2. left = invert(root.left), right = invert(root.right)
    3. root.left = right; root.right = left   (the crossover!)
    4. Return root

    Time Complexity: O(n)
    Space Complexity: O(h) - recursion stack

    Why show this variant:
    - Some people find "invert both sides, then cross-assign" clearer than
      "swap, then invert both sides". They are the same algorithm.
    - It also makes the point that you can post-order (children first) just
      as validly as pre-order (node first) here.
    """
    if root is None:
        return None

    left_inverted = invertTree_rebuild_links(root.left)
    right_inverted = invertTree_rebuild_links(root.right)

    # The crossover: old right goes left, old left goes right
    root.left = right_inverted
    root.right = left_inverted

    return root


# ============================================================================
# SOLUTION 3: Iterative BFS with a Queue (No recursion!)
# ============================================================================

def invertTree_bfs(root):
    """
    Approach: Level order traversal (GUIDE.md pattern #2). Visit every node
    with a queue and swap its children as you go.

    Algorithm:
    1. If root is None, return None
    2. queue = deque([root])
    3. While the queue is non-empty:
       a. node = queue.popleft()
       b. Swap node.left and node.right
       c. Enqueue any non-None children
    4. Return root

    Time Complexity: O(n) - each node enters and leaves the queue once
    Space Complexity: O(w) - w = maximum width of the tree. For a complete
                      binary tree the last level holds ~n/2 nodes, so this
                      is O(n) in the worst case.

    When to prefer this:
    - The tree might be extremely deep (recursion would blow the stack).
    - The interviewer explicitly asks for an iterative solution.

    Note the space trade-off: recursion costs O(height), BFS costs O(width).
    Neither is universally smaller - it depends on the tree's shape!
    """
    if root is None:
        return None

    queue = deque([root])

    while queue:
        node = queue.popleft()

        # Swap this node's children
        node.left, node.right = node.right, node.left

        # Enqueue children to process later
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root


# ============================================================================
# SOLUTION 4: Iterative DFS with an Explicit Stack
# ============================================================================

def invertTree_dfs_stack(root):
    """
    Approach: Exactly the recursive solution, but with a stack you manage
    yourself instead of the call stack Python manages for you.

    Algorithm:
    1. If root is None, return None
    2. stack = [root]
    3. While the stack is non-empty:
       a. node = stack.pop()
       b. Swap node.left and node.right
       c. Push any non-None children
    4. Return root

    Time Complexity: O(n)
    Space Complexity: O(h) on a balanced tree, O(n) worst case

    Notice this is the SAME code as the BFS version with one character
    changed: `popleft()` becomes `pop()`. That one change turns a queue
    into a stack, and breadth-first into depth-first. Great thing to point
    out in an interview - it shows you understand the traversals, not just
    memorized them.
    """
    if root is None:
        return None

    stack = [root]

    while stack:
        node = stack.pop()  # <- pop() = LIFO = DFS (popleft() = FIFO = BFS)

        node.left, node.right = node.right, node.left

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return root


# ============================================================================
# TEST CASES
# ============================================================================

def test():
    """Test all solutions"""

    test_cases = [
        # (input_level_order, expected_level_order)
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),  # classic example
        ([2, 1, 3], [2, 3, 1]),                           # small tree
        ([1], [1]),                                       # single node (edge)
        ([], []),                                         # empty tree (edge!)
        ([1, 2], [1, None, 2]),                           # left child only
        ([1, None, 2], [1, 2]),                           # right child only
        ([1, 2, 3, 4, None, None, 5], [1, 3, 2, 5, None, None, 4]),  # sparse
        ([1, 2, None, 3, None, 4], [1, None, 2, None, 3, None, 4]),  # left stick
        ([-100, -50, 100], [-100, 100, -50]),             # negatives
        ([1, 1, 1, 1, 1], [1, 1, 1, None, None, 1, 1]),   # duplicate values
    ]

    solutions = [
        ("Recursive DFS (Optimal)", invertTree),
        ("Recursive DFS (Rebuild Links)", invertTree_rebuild_links),
        ("Iterative BFS (Queue)", invertTree_bfs),
        ("Iterative DFS (Stack)", invertTree_dfs_stack),
    ]

    for name, solution in solutions:
        print(f"\n{'='*50}")
        print(f"Testing: {name}")
        print('='*50)

        all_passed = True
        for i, (values, expected) in enumerate(test_cases, 1):
            # Build a FRESH tree per solution - inverting mutates it!
            root = build_tree(values)
            result = to_list(solution(root))

            is_correct = result == expected
            status = "✅" if is_correct else "❌"
            print(f"Test {i}: {status} {values} → {result}")
            if not is_correct:
                print(f"         expected {expected}")
                all_passed = False

        if all_passed:
            print(f"\n🎉 All tests passed for {name}!")

    # Sanity check: inverting twice must give back the original tree
    print(f"\n{'='*50}")
    print("Testing: Invert twice == identity")
    print('='*50)

    all_passed = True
    for i, (values, _) in enumerate(test_cases, 1):
        root = build_tree(values)
        result = to_list(invertTree(invertTree(root)))

        is_correct = result == to_list(build_tree(values))
        status = "✅" if is_correct else "❌"
        print(f"Test {i}: {status} invert(invert({values})) → {result}")
        if not is_correct:
            all_passed = False

    if all_passed:
        print("\n🎉 Inverting twice always restores the original! "
              "(invert is its own inverse)")


# ============================================================================
# VISUAL DEMO
# ============================================================================

def visual_demo(values):
    """
    Visual step-by-step demonstration of the recursive inversion.
    """
    print(f"\n{'='*70}")
    print("VISUAL DEMO: Invert Binary Tree (recursive DFS)")
    print(f"Input (level order): {values}")
    print('='*70)

    root = build_tree(values)

    if root is None:
        print("\nEmpty tree -> base case fires immediately, return None. ✅")
        return

    print("\nBEFORE (printed sideways - tilt your head left):\n")
    print_tree(root)

    print("\nStep-by-step execution (pre-order: swap, then recurse):\n")

    step = [0]

    def invert_traced(node, depth):
        if node is None:
            print(f"{'  ' * depth}None → base case, return")
            return None

        step[0] += 1
        left_val = node.left.val if node.left else None
        right_val = node.right.val if node.right else None

        print(f"{'  ' * depth}Step {step[0]}: at node [{node.val}]")
        print(f"{'  ' * depth}  before: left={left_val}, right={right_val}")

        node.left, node.right = node.right, node.left

        new_left = node.left.val if node.left else None
        new_right = node.right.val if node.right else None
        print(f"{'  ' * depth}  SWAP  → left={new_left}, right={new_right}")

        invert_traced(node.left, depth + 1)
        invert_traced(node.right, depth + 1)

        return node

    invert_traced(root, 0)

    print("\nAFTER (mirrored):\n")
    print_tree(root)

    print(f"\n✅ Result (level order): {to_list(root)}")
    print(f"   Nodes visited: {step[0]} (exactly one swap per node → O(n))")


# ============================================================================
# WHAT YOU SHOULD LEARN
# ============================================================================

"""
KEY TAKEAWAYS:
-------------
1. TRUST THE RECURSION. Do one node's worth of work, delegate the rest.
2. The base case `if not root: return None` handles empty trees AND leaves.
3. Swapping None with None is harmless - no leaf special case needed.
4. Recursion costs O(height) space; BFS costs O(width). Different, not
   strictly better or worse.
5. Queue + popleft() = BFS. Stack + pop() = DFS. One character apart!

PATTERN RECOGNITION:
-------------------
When you see:
- "Mirror / invert / reflect a tree"
- "Apply the same transformation to every node"
- "Symmetric tree" (compare a tree with its own mirror)

Think: DFS RECURSION - base case, work, recurse left, recurse right!

THE UNIVERSAL TREE RECURSION SHAPE:
----------------------------------
    def solve(root):
        if not root:
            return <base case value>
        <do work at this node>
        solve(root.left)
        solve(root.right)
        return <result>

Nine out of ten easy tree problems are this template with different work.

INTERVIEW TIPS:
--------------
1. Draw the before/after tree - it makes the swap obvious in 5 seconds
2. Say the recursive contract: "invert(x) returns x's subtree, mirrored"
3. Mention that pre-order and post-order both work here, and why
4. Offer the iterative version unprompted - it shows range
5. Great closer: "inverting twice returns the original tree"

COMMON MISTAKES:
---------------
❌ Forgetting the None base case -> AttributeError on root.left
❌ Writing `root.left = root.right` then `root.right = root.left`
   without a temp - you just cloned the right subtree onto both sides!
   (Python's tuple assignment `a, b = b, a` avoids this. In other
   languages you MUST use a temp variable.)
❌ Only swapping at the root and forgetting to recurse
❌ Returning None instead of root at the end
❌ Assuming the tree is balanced when reasoning about space

VARIATIONS:
----------
- Symmetric Tree - is a tree its own mirror?
- Same Tree - are two trees identical?
- Subtree of Another Tree - does t appear inside s?
- Flip Equivalent Binary Trees - invert only SOME nodes to match

TIME COMPLEXITY COMPARISON:
--------------------------
Recursive DFS:  O(n) time, O(h) space ← BEST (simplest, and h <= n)
Iterative DFS:  O(n) time, O(h) space (no stack-overflow risk)
Iterative BFS:  O(n) time, O(w) space (w can be ~n/2 at the bottom level)

NEXT STEPS:
----------
✅ Mastered the tree recursion template
✅ Know DFS and BFS iteratively too
→ Now try: Maximum Depth of Binary Tree (same shape, returns a number!)
→ Then:    Validate Binary Search Tree (recursion that carries state down)

PRACTICE MORE:
-------------
Similar problems to practice this pattern:
- Maximum Depth of Binary Tree
- Same Tree
- Symmetric Tree
- Subtree of Another Tree
- Diameter of Binary Tree
- Balanced Binary Tree
"""


if __name__ == "__main__":
    # Run tests
    test()

    # Visual demonstrations
    visual_demo([4, 2, 7, 1, 3, 6, 9])
    visual_demo([2, 1, 3])
    visual_demo([])

    # Interactive practice
    print("\n" + "="*70)
    print("YOUR TURN TO TRACE!")
    print("="*70)
    print("\nTry tracing through this example yourself:")
    print("root = [1, 2, 3, 4, 5, 6, 7]")
    print("\nDraw the tree, swap each node's children, then draw it again.")
    print("Then run: visual_demo([1, 2, 3, 4, 5, 6, 7])")
