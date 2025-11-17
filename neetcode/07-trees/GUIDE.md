# Trees - Complete Guide

## 🎯 What is a Tree?

Hierarchical data structure with nodes connected by edges. A binary tree has at most 2 children per node.

**Visual:**
```
        1
       / \
      2   3
     / \
    4   5

Root: 1
Leaves: 4, 5, 3
Height: 2
```

## 🧠 Binary Tree Node

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## 🎨 Tree Traversals

### 1. Inorder (Left → Root → Right)
```python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
# Result: [4, 2, 5, 1, 3]  (sorted for BST!)
```

### 2. Preorder (Root → Left → Right)
```python
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)
# Result: [1, 2, 4, 5, 3]
```

### 3. Postorder (Left → Right → Root)
```python
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
# Result: [4, 5, 2, 3, 1]
```

### 4. Level Order (BFS)
```python
from collections import deque

def levelOrder(root):
    if not root:
        return []

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
# Result: [[1], [2, 3], [4, 5]]
```

## 🔑 Common Patterns

### 1. Recursion (DFS)
Most tree problems use recursion!

### 2. Level Order (BFS)
Use queue for level-by-level processing

### 3. BST Properties
Left < Root < Right (allows binary search!)

## ⚡ Key Problems

**Easy:**
- Maximum Depth of Binary Tree ⭐
- Invert Binary Tree
- Same Tree

**Medium:**
- Validate BST
- Lowest Common Ancestor
- Binary Tree Level Order Traversal
- Kth Smallest Element in BST

**Hard:**
- Binary Tree Maximum Path Sum
- Serialize and Deserialize Binary Tree

## 💡 Types of Trees

- **Binary Tree**: At most 2 children
- **BST**: Left < Root < Right
- **Balanced**: Height difference ≤ 1
- **Complete**: All levels filled except possibly last
- **Full**: Every node has 0 or 2 children

Time: O(n) for most traversals
Space: O(h) for recursion stack, h = height

---
**Trees are everywhere in interviews - master recursion!** 🌳
