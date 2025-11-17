# Graphs - Complete Guide

## 🎯 What is a Graph?

A collection of nodes (vertices) connected by edges. Represents relationships between entities.

**Visual:**
```
    1 --- 2
    |     |
    3 --- 4

Undirected Graph

    1 → 2
    ↑   ↓
    3 ← 4

Directed Graph
```

## 🧠 Graph Representations

### 1. Adjacency List (Most Common)
```python
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3]
}
```

### 2. Adjacency Matrix
```python
graph = [
    [0, 1, 1, 0],  # Node 1
    [1, 0, 0, 1],  # Node 2
    [1, 0, 0, 1],  # Node 3
    [0, 1, 1, 0]   # Node 4
]
```

## 🎨 Graph Traversals

### 1. DFS (Depth-First Search)
```python
def dfs(graph, node, visited):
    if node in visited:
        return

    visited.add(node)
    print(node)  # Process node

    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)
```

### 2. BFS (Breadth-First Search)
```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node)  # Process node

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

## 🔑 Common Algorithms

### 1. Detect Cycle
### 2. Topological Sort (DAG)
### 3. Shortest Path (BFS, Dijkstra)
### 4. Union-Find (Disjoint Set)
### 5. Minimum Spanning Tree (Kruskal, Prim)

## 💡 When to Use DFS vs BFS

**DFS:**
- Finding paths
- Detecting cycles
- Topological sort
- Recursion-friendly

**BFS:**
- Shortest path (unweighted)
- Level-order traversal
- Minimum steps problems

## ⚡ Key Problems

**Medium:**
- Number of Islands ⭐
- Clone Graph
- Course Schedule
- Pacific Atlantic Water Flow
- Graph Valid Tree

**Hard:**
- Alien Dictionary
- Word Ladder
- Minimum Cost to Connect All Points

## 💡 Graph Types

- **Undirected**: Edges have no direction
- **Directed**: Edges have direction
- **Weighted**: Edges have weights
- **Cyclic/Acyclic**: Contains cycles or not
- **Connected**: All nodes reachable

Time: O(V + E) for DFS/BFS
Space: O(V) for visited set

---
**Graphs model real-world relationships - very common in interviews!** 🕸️
