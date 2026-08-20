"""
Problem: Maximum Depth of Binary Tree
Difficulty: Easy
Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree, Recursion

Problem Statement:
-----------------
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest
path from the root node down to the farthest leaf node.

Careful with the vocabulary - the GUIDE draws a tree of "height 2" while
this problem calls the same tree "depth 3":
    DEPTH (this problem) counts NODES:  root alone = 1
    HEIGHT (common usage) counts EDGES: root alone = 0
    depth = height + 1
Always ask the interviewer which one they mean.

Examples:
---------
Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3
    Explanation:
            3          <- level 1
          /   \
         9     20      <- level 2
              /  \
            15    7    <- level 3
    Longest root-to-leaf path is 3 → 20 → 15 (or 3 → 20 → 7): 3 nodes.

Example 2:
    Input: root = [1,null,2]
    Output: 2
    Explanation:
            1
             \
              2
    Path 1 → 2 has 2 nodes.

Example 3:
    Input: root = []
    Output: 0
    Explanation: An empty tree has depth 0 (edge case!).

Constraints:
-----------
- The number of nodes in the tree is in the range [0, 10^4]
- -100 <= Node.val <= 100

LEARNING NOTES:
--------------
This is the "hello world" of tree recursion, and it is the sub-routine
inside Balanced Binary Tree, Diameter of Binary Tree, and more.

Key Insight: THE DEPTH OF A TREE IS DEFINED IN TERMS OF ITSELF.

    depth(node) = 1 + max(depth(node.left), depth(node.right))
                  ^                  ^
                  |                  |
            count yourself      the deeper of your two subtrees

    And the base case: depth(None) = 0.

    That is the entire algorithm. Two lines. The hard part is BELIEVING
    that you do not have to trace it - you just have to trust that the
    recursive call returns the right number for a smaller tree.

    Notice the base case does double duty: it handles the empty tree AND
    it terminates every leaf (whose children are both None), so leaves
    correctly report 1 + max(0, 0) = 1.

Pattern: "How tall / how far / how many levels" -> DFS returning a number
         up the call stack. Or: BFS counting levels.

Visualization:
    root = [3, 9, 20, null, null, 15, 7]

            3
          /   \
         9     20
              /  \
            15    7

    Recursion unwinds from the BOTTOM UP:

    depth(9)  = 1 + max(depth(None), depth(None)) = 1 + max(0, 0) = 1
    depth(15) = 1 + max(0, 0) = 1
    depth(7)  = 1 + max(0, 0) = 1
    depth(20) = 1 + max(depth(15), depth(7)) = 1 + max(1, 1) = 2
    depth(3)  = 1 + max(depth(9), depth(20)) = 1 + max(1, 2) = 3 ✅

    Call tree (each node returns its number up to its parent):

            3 ────────► returns 3
           / \
     ►1◄  9   20 ────► returns 2
              / \
        ►1◄ 15   7 ►1◄

    The BFS view instead counts the LEVELS of the queue:
        Level 1: [3]        -> depth so far 1
        Level 2: [9, 20]    -> depth so far 2
        Level 3: [15, 7]    -> depth so far 3
        Queue empty -> answer 3 ✅
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

        build_tree([3, 9, 20, None, None, 15, 7])
                3
              /   \
             9     20
                  /  \
                15    7

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
    Convert a tree back to a level-order list (trailing Nones trimmed), so
    tests and demos can talk in plain Python values.

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


# ============================================================================
# SOLUTION 1: Recursive DFS (OPTIMAL!)
# ============================================================================

def maxDepth(root):
    """
    Approach: A tree's depth is 1 (for the root) plus the depth of its
    deeper subtree. Write that sentence as code.

    Algorithm:
    1. Base case: if root is None, return 0
    2. left_depth  = maxDepth(root.left)
    3. right_depth = maxDepth(root.right)
    4. Return 1 + max(left_depth, right_depth)

    Why it works:
    - The longest root-to-leaf path must go through exactly one of the two
      children, so we take whichever subtree is deeper and add ourselves.
    - Leaves get 1 + max(0, 0) = 1 for free from the base case.

    Time Complexity: O(n) - every node is visited exactly once
    Space Complexity: O(h) - recursion stack, h = height.
                      Balanced tree: O(log n). Degenerate stick: O(n).

    This is the answer to give first. It is 4 lines and impossible to beat
    on time; the only concern is stack depth on a pathological tree.
    """
    # Base case: an empty tree contributes no levels
    if root is None:
        return 0

    # Trust the recursion for both halves
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    # Count this node (+1), keep only the deeper side
    return 1 + max(left_depth, right_depth)


# ============================================================================
# SOLUTION 2: Iterative BFS - Count the Levels (Great for very deep trees)
# ============================================================================

def maxDepth_bfs(root):
    """
    Approach: Level order traversal (GUIDE.md pattern #2). Process the tree
    one LEVEL at a time and count how many levels you got through.

    Algorithm:
    1. If root is None, return 0
    2. queue = deque([root]); depth = 0
    3. While the queue is non-empty:
       a. depth += 1  (we are starting a brand new level)
       b. Snapshot len(queue) - that is exactly this level's node count
       c. Pop that many nodes, enqueueing each one's real children
    4. Return depth

    The critical trick is step (b): `for _ in range(len(queue))`. You must
    capture the length BEFORE the loop, because you are appending to the
    same queue while draining it. Capturing it up front is what separates
    one level from the next.

    Time Complexity: O(n) - each node is enqueued and dequeued once
    Space Complexity: O(w) - w = maximum level width. For a complete tree
                      the bottom level holds ~n/2 nodes, so O(n) worst case.

    When to prefer this:
    - The tree may be 10,000 nodes deep in a stick shape - recursion would
      exceed Python's default recursion limit (1000). This will not.
    - You also need the level structure for something else (level order
      traversal, right side view, etc.).
    """
    if root is None:
        return 0

    queue = deque([root])
    depth = 0

    while queue:
        depth += 1  # we are about to consume one full level

        # Snapshot the size FIRST - the queue grows while we drain it!
        for _ in range(len(queue)):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth


# ============================================================================
# SOLUTION 3: Iterative DFS with an Explicit Stack (No recursion, no levels)
# ============================================================================

def maxDepth_dfs_iterative(root):
    """
    Approach: Depth-first traversal with your own stack, carrying each
    node's depth alongside it, and tracking the maximum seen.

    Algorithm:
    1. If root is None, return 0
    2. stack = [(root, 1)]; max_depth = 0
    3. While the stack is non-empty:
       a. node, depth = stack.pop()
       b. max_depth = max(max_depth, depth)
       c. Push (child, depth + 1) for each real child
    4. Return max_depth

    The key idea: since there is no call stack to remember "how deep am I",
    we PAIR each node with its depth in the stack itself. This "carry extra
    state in the stack tuple" trick generalizes to tons of problems.

    Time Complexity: O(n)
    Space Complexity: O(h) on a balanced tree, O(n) worst case

    Compared to BFS: this also avoids recursion, but its memory is bounded
    by the tree's HEIGHT rather than its WIDTH. For a wide, shallow tree
    this wins; for a narrow, deep tree BFS wins. Know both.
    """
    if root is None:
        return 0

    stack = [(root, 1)]  # (node, depth_of_that_node)
    max_depth = 0

    while stack:
        node, depth = stack.pop()

        max_depth = max(max_depth, depth)

        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))

    return max_depth


# ============================================================================
# SOLUTION 4: One-Liner Recursion (Cute, but harder to read)
# ============================================================================

def maxDepth_oneliner(root):
    """
    Approach: The same recursion, compressed into a single expression.

    Time Complexity: O(n)
    Space Complexity: O(h)

    Why NOT to write this in an interview:
    - Identical performance to Solution 1 with strictly worse readability.
    - If the interviewer asks you to modify it (e.g. "now return the
      diameter"), the compact form fights you.
    - Shown here so you recognize it in other people's code.
    """
    return 1 + max(maxDepth_oneliner(root.left),
                   maxDepth_oneliner(root.right)) if root else 0


# ============================================================================
# TEST CASES
# ============================================================================

def test():
    """Test all solutions"""

    test_cases = [
        # (level_order_values, expected_depth)
        ([3, 9, 20, None, None, 15, 7], 3),   # classic example
        ([1, None, 2], 2),                     # right child only
        ([], 0),                               # empty tree (edge case!)
        ([1], 1),                              # single node (edge case)
        ([1, 2], 2),                           # left child only
        ([1, 2, 3, 4, 5, 6, 7], 3),            # perfect tree
        ([1, 2, None, 3, None, 4], 4),         # left stick - unbalanced!
        ([1, None, 2, None, 3, None, 4], 4),   # right stick
        ([1, 2, 3, 4, None, None, 5, 6], 4),   # deep on one side only
        ([-100, -50, 100, -25], 3),            # negatives
    ]

    solutions = [
        ("Recursive DFS (Optimal)", maxDepth),
        ("Iterative BFS (Level Count)", maxDepth_bfs),
        ("Iterative DFS (Stack + Depth)", maxDepth_dfs_iterative),
        ("One-Liner Recursion", maxDepth_oneliner),
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
            print(f"Test {i}: {status} {values} → depth {result} "
                  f"(expected {expected})")
            if not is_correct:
                all_passed = False

        if all_passed:
            print(f"\n🎉 All tests passed for {name}!")

    # Cross-check: all four solutions must always agree with each other
    print(f"\n{'='*50}")
    print("Testing: All solutions agree")
    print('='*50)

    all_passed = True
    for i, (values, _) in enumerate(test_cases, 1):
        results = [sol(build_tree(values)) for _, sol in solutions]
        is_correct = len(set(results)) == 1
        status = "✅" if is_correct else "❌"
        print(f"Test {i}: {status} {values} → all returned {results[0]}"
              if is_correct else
              f"Test {i}: {status} {values} → DISAGREEMENT {results}")
        if not is_correct:
            all_passed = False

    if all_passed:
        print("\n🎉 DFS and BFS always agree - as they must!")


# ============================================================================
# VISUAL DEMO
# ============================================================================

def visual_demo(values):
    """
    Visual step-by-step demonstration of BOTH the recursive DFS unwind and
    the BFS level count, so you can see the two mental models side by side.
    """
    print(f"\n{'='*70}")
    print("VISUAL DEMO: Maximum Depth of Binary Tree")
    print(f"Input (level order): {values}")
    print('='*70)

    root = build_tree(values)

    if root is None:
        print("\nEmpty tree -> base case fires immediately, return 0. ✅")
        return

    print("\nThe tree (printed sideways - tilt your head left):\n")
    print_tree(root)

    # ---- View 1: recursive DFS, bottom-up ----
    print("\n" + "-"*70)
    print("VIEW 1: Recursive DFS - each node returns a number to its parent")
    print("-"*70 + "\n")

    def depth_traced(node, depth):
        indent = "  " * depth

        if node is None:
            print(f"{indent}maxDepth(None) → 0   [base case]")
            return 0

        print(f"{indent}maxDepth([{node.val}]) → recursing...")
        left = depth_traced(node.left, depth + 1)
        right = depth_traced(node.right, depth + 1)
        result = 1 + max(left, right)
        print(f"{indent}maxDepth([{node.val}]) = 1 + max({left}, {right}) "
              f"= {result}")
        return result

    dfs_answer = depth_traced(root, 0)

    # ---- View 2: BFS, level by level ----
    print("\n" + "-"*70)
    print("VIEW 2: Iterative BFS - count how many levels the queue produces")
    print("-"*70 + "\n")

    queue = deque([root])
    level = 0

    while queue:
        level += 1
        level_values = [n.val for n in queue]
        print(f"Level {level}: {level_values}  "
              f"({len(level_values)} node(s) in the queue)")

        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    print(f"\nQueue is empty after {level} levels.")

    print(f"\n✅ DFS says {dfs_answer}, BFS says {level} - they agree!")


# ============================================================================
# WHAT YOU SHOULD LEARN
# ============================================================================

"""
KEY TAKEAWAYS:
-------------
1. depth(node) = 1 + max(depth(left), depth(right)), with depth(None) = 0.
2. The None base case also terminates leaves - no leaf special case needed.
3. BFS counts LEVELS; the `for _ in range(len(queue))` snapshot is what
   keeps levels separate.
4. Iterative DFS carries (node, depth) tuples on the stack.
5. Recursion costs O(height); BFS costs O(width). Choose by tree shape.
6. "Depth" counts nodes, "height" counts edges. Clarify before you code.

PATTERN RECOGNITION:
-------------------
When you see:
- "How deep / how tall / how many levels"
- "Longest path from the root"
- "Is this tree balanced?" (compare subtree depths)
- "Diameter" (left depth + right depth at each node)

Think: DFS THAT RETURNS A NUMBER UP THE STACK!

THE BOTTOM-UP RECURSION SHAPE:
-----------------------------
    def solve(root):
        if not root:
            return <identity value>          # 0 here
        left = solve(root.left)
        right = solve(root.right)
        return <combine(left, right, root)>  # 1 + max(...) here

Change only the last line and you get: depth, node count, sum of values,
minimum depth, diameter, "is balanced", and many more.

THE BFS LEVEL TEMPLATE:
----------------------
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):   # <- snapshot the level size!
            node = queue.popleft()
            ... enqueue children ...
        # one full level just finished here

INTERVIEW TIPS:
--------------
1. State the recurrence in English before writing any code
2. Say the base case out loud: "an empty tree has depth 0"
3. Offer BFS as the follow-up: "if the tree could be 10^4 deep, recursion
   hits Python's recursion limit - here is the iterative version"
4. Mention the O(height) vs O(width) space trade-off - it shows depth
5. Note that this function is the core of Balanced Tree and Diameter

COMMON MISTAKES:
---------------
❌ Returning `max(left, right)` and forgetting the `1 +`
❌ Base case returning 1 instead of 0 (off by one on every answer)
❌ In BFS, calling len(queue) INSIDE the loop instead of snapshotting it
   -> levels bleed into each other and the count is wrong
❌ In BFS, incrementing depth per NODE instead of per LEVEL
❌ Forgetting the empty tree returns 0, not 1
❌ Confusing depth (nodes) with height (edges)

VARIATIONS:
----------
- Minimum Depth of Binary Tree - careful! min() is WRONG for a node with
  only one child; you must ignore the missing side
- Balanced Binary Tree - is |left depth - right depth| <= 1 everywhere?
- Diameter of Binary Tree - max over nodes of (left depth + right depth)
- Binary Tree Level Order Traversal - the BFS template, collecting values
- Maximum Depth of N-ary Tree - max over a list of children

TIME COMPLEXITY COMPARISON:
--------------------------
Recursive DFS:  O(n) time, O(h) space ← BEST for readability
Iterative DFS:  O(n) time, O(h) space (no recursion-limit risk)
Iterative BFS:  O(n) time, O(w) space (best on very deep, narrow trees)

NEXT STEPS:
----------
✅ Mastered bottom-up tree recursion
✅ Know DFS and BFS, recursive and iterative
→ Now try: Diameter of Binary Tree (same recursion, different combine)
→ Then:    Validate Binary Search Tree (top-down state instead!)

PRACTICE MORE:
-------------
Similar problems to practice this pattern:
- Invert Binary Tree
- Balanced Binary Tree
- Diameter of Binary Tree
- Minimum Depth of Binary Tree
- Binary Tree Level Order Traversal
- Same Tree
"""


if __name__ == "__main__":
    # Run tests
    test()

    # Visual demonstrations
    visual_demo([3, 9, 20, None, None, 15, 7])
    visual_demo([1, 2, None, 3, None, 4])
    visual_demo([])

    # Interactive practice
    print("\n" + "="*70)
    print("YOUR TURN TO TRACE!")
    print("="*70)
    print("\nTry tracing through this example yourself:")
    print("root = [1, 2, 3, 4, 5, None, None, 6]")
    print("\nWhat does each node return to its parent?")
    print("How many levels does BFS see?")
    print("Then run: visual_demo([1, 2, 3, 4, 5, None, None, 6])")
