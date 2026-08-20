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

## 🔍 Trigger Phrases

If a problem statement says any of these, reach for graphs:

| Phrase in the problem | What it means |
|-----------------------|---------------|
| "connected", "network", "islands", "regions" | Connected components → DFS/BFS/union-find |
| "prerequisite", "depends on", "order of tasks" | Topological sort on a DAG |
| "shortest path", "fewest steps", "minimum moves" | BFS if unweighted, Dijkstra if weighted |
| "can you reach", "is there a path" | Any traversal — DFS is fine |
| "cycle", "deadlock", "is it a valid tree" | Cycle detection |
| "grid", "maze", "matrix of 0s and 1s" | Implicit graph — cells are nodes, 4 neighbours are edges |
| "cheapest way to connect all" | Minimum spanning tree (Kruskal/Prim) |
| "friend circles", "accounts merge", "groups" | Union-find |

**The sneaky ones:** a 2D grid, a word list where words differ by one letter,
a list of equations, and a set of string prefixes are all graphs in disguise.
If you can define "node" and "edge", it is a graph problem.

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

### Which representation?

| | Adjacency List | Adjacency Matrix |
|---|---|---|
| Space | O(V + E) | O(V²) |
| Is u→v an edge? | O(degree(u)) | O(1) |
| Iterate u's neighbours | O(degree(u)) | O(V) |
| Best for | Sparse graphs (almost always) | Dense graphs, or lots of edge lookups |

In interviews you are handed an edge list ~90% of the time and your first line
is building an adjacency list:

```python
from collections import defaultdict

graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)   # drop this line if the graph is directed
```

Use `defaultdict(list)` so isolated nodes don't need a `if node in graph` guard.

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

### 3. Grid traversal (implicit graph)
```python
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

for dr, dc in DIRECTIONS:
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
        ...
```

Always bounds-check **before** indexing. In Python `grid[-1]` is the last row,
not an error, so a missing check silently wraps around the grid.

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

## 🧭 Decision Guide: DFS vs BFS vs Union-Find vs Dijkstra

```
Do edges have weights?
├── YES ──> Are any weights negative?
│           ├── YES ──> Bellman-Ford
│           └── NO  ──> Dijkstra (heap)
└── NO ───> Do you need the SHORTEST path / FEWEST steps?
            ├── YES ──> BFS  (first time you reach a node IS optimal)
            └── NO ───> Do you only need "are these two connected?"
                        ├── YES, and edges arrive one at a time ──> Union-Find
                        └── otherwise ──> DFS (simplest to write)

Is it a DAG and the question is about ordering?  ──> Topological sort
Is the question "cheapest way to connect everything"?  ──> Kruskal + Union-Find
```

**Key tiebreakers:**
- **BFS over DFS** whenever the word "shortest" or "minimum number of steps"
  appears in an *unweighted* setting. DFS finds *a* path, not the *short* one.
- **Union-Find over DFS** when edges are added incrementally, or when you must
  answer many connectivity queries. Union-Find can't give you paths though.
- **DFS over BFS** for cycle detection in directed graphs, topological sort,
  and anything needing backtracking (all paths, colouring).
- **Dijkstra is just BFS with a priority queue.** If all weights equal 1, it
  degenerates into plain BFS — so don't reach for a heap unless weights differ.

## ⚡ Complexity Analysis

| Algorithm | Time | Space | Notes |
|-----------|------|-------|-------|
| Build adjacency list | O(V + E) | O(V + E) | |
| DFS / BFS | O(V + E) | O(V) | recursion stack is O(V) worst case |
| Grid DFS / BFS | O(R·C) | O(R·C) | every cell visited once |
| Cycle detection | O(V + E) | O(V) | directed and undirected alike |
| Topological sort | O(V + E) | O(V) | Kahn's or DFS post-order |
| Union-Find `find`/`union` | O(α(V)) ≈ O(1) | O(V) | α = inverse Ackermann, < 5 always |
| Kruskal MST | O(E log E) | O(V) | sorting dominates |
| Dijkstra (binary heap) | O(E log V) | O(V + E) | lazy deletion, no decrease-key |

For a grid, V = R·C and E ≈ 4·R·C, so O(V + E) collapses to O(R·C).

## 🔬 Worked Example: Course Schedule II, Traced

```
numCourses = 4
prerequisites = [[1,0], [2,0], [3,1], [3,2]]     # [course, prereq]
```

**Step 1 — build the DAG** (edge points prereq → course):
```
0 → 1
0 → 2
1 → 3
2 → 3

        ┌─→ 1 ─┐
   0 ───┤      ├─→ 3
        └─→ 2 ─┘
```

**Step 2 — count in-degrees** (how many prerequisites each course still has):
```
in_degree = [0, 1, 1, 2]
             ^  ^  ^  ^
             0  1  2  3      course 3 needs both 1 and 2
```

**Step 3 — seed the queue with everything at in-degree 0:**
```
queue = [0]        order = []
```

**Step 4 — drain the queue:**
```
pop 0  → order = [0]
         edge 0→1: in_degree[1] 1→0  → enqueue 1
         edge 0→2: in_degree[2] 1→0  → enqueue 2
         queue = [1, 2]      in_degree = [0, 0, 0, 2]

pop 1  → order = [0, 1]
         edge 1→3: in_degree[3] 2→1  → still blocked, do NOT enqueue
         queue = [2]         in_degree = [0, 0, 0, 1]

pop 2  → order = [0, 1, 2]
         edge 2→3: in_degree[3] 1→0  → enqueue 3
         queue = [3]         in_degree = [0, 0, 0, 0]

pop 3  → order = [0, 1, 2, 3]
         queue = []
```

**Step 5 — validate:** `len(order) == numCourses` → **[0, 1, 2, 3]** ✓

If instead the graph had a cycle (say `3 → 0`), then `in_degree[0]` would
start at 1, the queue would be empty from the very first line, and `order`
would come back short — that's how Kahn's detects cycles for free.

## 🚨 Common Pitfalls

1. **Marking visited at dequeue instead of enqueue (BFS).**
   ```python
   # ❌ node gets queued once per incoming edge — blows up to O(V²)
   while queue:
       node = queue.popleft()
       visited.add(node)
   # ✅ mark the moment you enqueue
   if neighbor not in visited:
       visited.add(neighbor)
       queue.append(neighbor)
   ```

2. **Using `visited` alone to detect cycles in a directed graph.** Re-reaching
   a *finished* node is fine (a diamond `0→1→3`, `0→2→3` has no cycle). You
   need to know whether the node is on the **current** DFS path — that's the
   grey/on-stack set. And you must **remove it on the way out**.

3. **Forgetting the parent in undirected cycle detection.** Every undirected
   edge `u-v` sits in both adjacency lists, so `v` always sees `u` again.
   Skip exactly the edge you arrived on, no more.

4. **Recursion depth.** Python caps at ~1000 frames. A 200×200 grid of all-land
   cells is a 40,000-deep DFS → `RecursionError`. Switch to the iterative
   stack version, or `sys.setrecursionlimit`.

5. **Not handling disconnected graphs.** One DFS from node 0 does not visit
   everything. Loop over all nodes and start a fresh traversal from each
   unvisited one.

6. **Dijkstra without the stale check.** Python's `heapq` has no decrease-key,
   so you push duplicates. If you skip `if d > dist[node]: continue`, you
   re-expand nodes and the complexity degrades.

7. **Dijkstra with negative weights.** It is simply wrong — once a node is
   popped, Dijkstra considers it settled. Use Bellman-Ford instead.

8. **Union-Find without path compression *or* union by rank.** You get O(n)
   finds and a TLE. Use both; they're 4 extra lines.

9. **Mutating the grid as your visited marker without telling anyone.** It's a
   legitimate O(1)-space trick (`grid[r][c] = '0'`), but say so out loud — some
   interviewers require the input be left intact.

10. **Off-by-one in in-degree bookkeeping.** Enqueue exactly when the count
    *hits* zero (`== 0`), not when it's `<= 0`, or a node lands in the queue
    multiple times.

## ⚡ Key Problems

**Medium:**
- Number of Islands ⭐ — grid DFS/BFS, the archetype
- Clone Graph ⭐ — DFS + a `old → new` hash map to avoid infinite recursion
- Max Area of Island — grid DFS returning a size
- Pacific Atlantic Water Flow — reverse thinking: BFS *inward* from each ocean
- Surrounded Regions — mark border-connected regions first, flip the rest
- Rotting Oranges ⭐ — multi-source BFS, count the levels
- Course Schedule ⭐ — cycle detection in a directed graph
- Course Schedule II ⭐ — topological sort, return the order
- Graph Valid Tree — n-1 edges **and** connected
- Number of Connected Components ⭐ — union-find or repeated DFS

**Hard:**
- Word Ladder — BFS on an implicit graph; build the `*o*` wildcard buckets
- Alien Dictionary — derive edges from adjacent word pairs, then topo sort
- Minimum Cost to Connect All Points — MST (Kruskal + union-find, or Prim)

⭐ = must-know. Number of Islands, Course Schedule II, and Rotting Oranges
between them cover grid traversal, topological sort, and multi-source BFS —
the three ideas most graph interview questions are built from.

## 💡 Graph Types

- **Undirected**: Edges have no direction
- **Directed**: Edges have direction
- **Weighted**: Edges have weights
- **Cyclic/Acyclic**: Contains cycles or not
- **Connected**: All nodes reachable

Time: O(V + E) for DFS/BFS
Space: O(V) for visited set

## 🚀 Next Steps

1. Study the `template.py` file — build-graph, DFS, BFS, topo sort, union-find, Dijkstra
2. Start with **Number of Islands** (grid DFS, the gentlest entry point)
3. Then **Course Schedule** → **Course Schedule II** (cycle detection → ordering)
4. Then **Rotting Oranges** (multi-source BFS) and **Number of Connected
   Components** (union-find)
5. Finish with **Word Ladder** — it forces you to *construct* the graph yourself

---
**Graphs model real-world relationships - very common in interviews!** 🕸️
