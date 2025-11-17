"""
Trees - Code Templates
======================
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================================
# TEMPLATE 1: Inorder Traversal (Recursive)
# ============================================================================

def inorder(root):
    """Left → Root → Right"""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


# ============================================================================
# TEMPLATE 2: Inorder Traversal (Iterative)
# ============================================================================

def inorder_iterative(root):
    """Using stack"""
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result


# ============================================================================
# TEMPLATE 3: Level Order Traversal (BFS)
# ============================================================================

def level_order(root):
    """Level by level traversal"""
    if not root:
        return []

    from collections import deque
    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# ============================================================================
# TEMPLATE 4: Max Depth (DFS)
# ============================================================================

def max_depth(root):
    """Maximum depth of tree"""
    if not root:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


# ============================================================================
# TEMPLATE 5: Validate BST
# ============================================================================

def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    """Check if tree is valid BST"""
    if not root:
        return True

    if not (min_val < root.val < max_val):
        return False

    return (is_valid_bst(root.left, min_val, root.val) and
            is_valid_bst(root.right, root.val, max_val))


# ============================================================================
# TEMPLATE 6: Lowest Common Ancestor
# ============================================================================

def lowest_common_ancestor(root, p, q):
    """Find LCA of two nodes in BST"""
    if not root:
        return None

    # Both in left subtree
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)

    # Both in right subtree
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)

    # Split or found
    return root


# ============================================================================
# TEMPLATE 7: Invert Binary Tree
# ============================================================================

def invert_tree(root):
    """Mirror the tree"""
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)

    return root
