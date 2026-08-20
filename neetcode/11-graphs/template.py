"""
Graphs - Code Templates
=======================

Reusable building blocks for graph problems: representation, traversal,
cycle detection, topological sort, union-find and Dijkstra.

Copy a template, rename the variables, and plug in the problem's logic.
Notation used throughout: V = number of vertices, E = number of edges.
"""

import heapq
from collections import defaultdict, deque


# ============================================================================
# TEMPLATE 1: Build an Adjacency List from an Edge List
# ============================================================================

def build_graph(n, edges, directed=False):
    """
    Turn an edge list into an adjacency list (the default representation).

    n:        number of nodes, labelled 0..n-1
    edges:    list of [u, v] pairs
    directed: if False, every edge is added in both directions

    Time: O(V + E)
    Space: O(V + E)
    """
    # defaultdict(list) means graph[node] is [] for isolated nodes too,
    # so you never need a `if node in graph` guard while traversing.
    graph = defaultdict(list)

    # Pre-seed every node so isolated vertices still show up in the keys.
    for node in range(n):
        graph[node] = []

    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)  # undirected == two directed edges

    return graph


def build_weighted_graph(n, edges, directed=False):
    """
    Same as above, but each edge is [u, v, w] and neighbours are (node, weight).

    Time: O(V + E)
    Space: O(V + E)
    """
    graph = defaultdict(list)
    for node in range(n):
        graph[node] = []

    for u, v, w in edges:
        graph[u].append((v, w))
        if not directed:
            graph[v].append((u, w))

    return graph


# ============================================================================
# TEMPLATE 2: DFS - Recursive
# ============================================================================

def dfs_recursive(graph, start):
    """
    Visit every node reachable from `start`, depth-first.

    Time: O(V + E)
    Space: O(V) for the visited set + O(V) recursion stack
    """
    visited = set()
    order = []

    def dfs(node):
        # Guard at the TOP of the function: simplest correct placement.
        if node in visited:
            return
        visited.add(node)     # mark BEFORE recursing, or cycles loop forever
        order.append(node)    # pre-order: process on the way down

        for neighbor in graph[node]:
            dfs(neighbor)

        # post-order work (e.g. topological sort) would go here

    dfs(start)
    return order


def dfs_all_components(n, graph):
    """
    Count connected components by starting a fresh DFS from every unvisited node.

    This is the skeleton behind "Number of Connected Components" and
    "Number of Islands" style problems.

    Time: O(V + E)
    Space: O(V)
    """
    visited = set()
    components = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in range(n):
        if node not in visited:
            components += 1  # every new DFS root == one new component
            dfs(node)

    return components


# ============================================================================
# TEMPLATE 3: DFS - Iterative (Explicit Stack)
# ============================================================================

def dfs_iterative(graph, start):
    """
    Same traversal as Template 2 but with an explicit stack.

    Use this when recursion depth could blow the Python limit (~1000 frames),
    e.g. a 10^5-node path graph.

    Time: O(V + E)
    Space: O(V)
    """
    visited = set()
    order = []
    stack = [start]

    while stack:
        node = stack.pop()  # pop() from the END == depth-first

        # A node can be pushed several times before it is popped, so the
        # dedupe check has to happen on POP, not only on push.
        if node in visited:
            continue
        visited.add(node)
        order.append(node)

        # Reversed so the first neighbour is popped first, matching the
        # recursive version's visit order. Drop it if order doesn't matter.
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

    return order


# ============================================================================
# TEMPLATE 4: BFS with a deque
# ============================================================================

def bfs(graph, start):
    """
    Visit nodes in order of increasing edge-distance from `start`.

    Time: O(V + E)
    Space: O(V)
    """
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()  # popleft() == FIFO == breadth-first
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                # Mark visited at ENQUEUE time, not dequeue time. Otherwise a
                # node reachable by two edges gets queued twice.
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def bfs_shortest_path_length(graph, start, target):
    """
    Fewest edges from start to target in an UNWEIGHTED graph.

    BFS is correct here precisely because every edge costs the same, so the
    first time we reach a node is via a shortest path. Returns -1 if
    unreachable.

    Time: O(V + E)
    Space: O(V)
    """
    if start == target:
        return 0

    visited = {start}
    queue = deque([(start, 0)])  # (node, distance so far)

    while queue:
        node, dist = queue.popleft()

        for neighbor in graph[node]:
            if neighbor == target:
                return dist + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1


def bfs_level_order(graph, start):
    """
    BFS that keeps each "ring" separate — one list per distance from start.

    Pattern: snapshot len(queue) BEFORE the inner loop so you drain exactly
    the current level while appending the next one.

    Time: O(V + E)
    Space: O(V)
    """
    visited = {start}
    queue = deque([start])
    levels = []

    while queue:
        level_size = len(queue)  # freeze the count for THIS level
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        levels.append(level)

    return levels


def bfs_multi_source(graph, sources):
    """
    Multi-source BFS: seed the queue with every source at distance 0.

    This is the trick behind "Rotting Oranges" and "Walls and Gates" — the
    result is the distance to the NEAREST source, computed in one pass
    instead of one BFS per source.

    Time: O(V + E)
    Space: O(V)
    """
    dist = {}
    queue = deque()

    for s in sources:
        dist[s] = 0
        queue.append(s)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return dist


# ============================================================================
# TEMPLATE 5: Grid Traversal (4-Direction Pattern)
# ============================================================================

# The canonical direction vectors: up, down, left, right.
# Add (1,1), (1,-1), (-1,1), (-1,-1) for 8-directional problems.
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def grid_dfs(grid, r, c, visited):
    """
    Flood-fill one region of a grid, depth-first. Returns the region's size.

    A grid IS a graph: cell (r,c) is a node, adjacency is the 4 neighbours.

    Time: O(rows * cols)
    Space: O(rows * cols) worst-case recursion depth
    """
    rows, cols = len(grid), len(grid[0])

    # Single combined base case: out of bounds, already seen, or not land.
    if (r < 0 or r >= rows or c < 0 or c >= cols
            or (r, c) in visited or grid[r][c] != 1):
        return 0

    visited.add((r, c))
    size = 1

    for dr, dc in DIRECTIONS:
        size += grid_dfs(grid, r + dr, c + dc, visited)

    return size


def count_islands(grid):
    """
    Count connected regions of 1s — the "Number of Islands" skeleton.

    Time: O(rows * cols)
    Space: O(rows * cols)
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                count += 1
                grid_dfs(grid, r, c, visited)

    return count


def grid_bfs(grid, start_r, start_c):
    """
    Flood-fill one grid region breadth-first (no recursion limit worries).

    Time: O(rows * cols)
    Space: O(rows * cols)
    """
    rows, cols = len(grid), len(grid[0])
    visited = {(start_r, start_c)}
    queue = deque([(start_r, start_c)])
    cells = []

    while queue:
        r, c = queue.popleft()
        cells.append((r, c))

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            # Bounds check FIRST — Python's negative indexing means r == -1
            # silently wraps to the last row instead of raising.
            if (0 <= nr < rows and 0 <= nc < cols
                    and (nr, nc) not in visited and grid[nr][nc] == 1):
                visited.add((nr, nc))
                queue.append((nr, nc))

    return cells


# ============================================================================
# TEMPLATE 6: Cycle Detection - Directed Graph (White/Grey/Black)
# ============================================================================

WHITE, GREY, BLACK = 0, 1, 2  # unvisited / on current DFS path / fully done


def has_cycle_directed(n, graph):
    """
    Detect a cycle in a DIRECTED graph with 3-colour DFS.

    The key insight: seeing an already-visited node is NOT enough. A GREY node
    is on the current recursion stack, so an edge back to it closes a cycle.
    A BLACK node is a finished subtree we merely re-reached — that's fine.

    Time: O(V + E)
    Space: O(V)
    """
    color = [WHITE] * n

    def dfs(node):
        color[node] = GREY  # entering: node is now on the current path

        for neighbor in graph[node]:
            if color[neighbor] == GREY:
                return True                      # back edge → cycle
            if color[neighbor] == WHITE and dfs(neighbor):
                return True

        color[node] = BLACK  # leaving: node is done, no longer on the path
        return False

    for node in range(n):
        if color[node] == WHITE and dfs(node):
            return True

    return False


def has_cycle_directed_recursion_stack(n, graph):
    """
    Same result as above, phrased with two sets instead of colours.

    visited   == BLACK ∪ GREY (ever entered)
    on_stack  == GREY         (on the current DFS path)

    Time: O(V + E)
    Space: O(V)
    """
    visited = set()
    on_stack = set()

    def dfs(node):
        visited.add(node)
        on_stack.add(node)

        for neighbor in graph[node]:
            if neighbor in on_stack:
                return True
            if neighbor not in visited and dfs(neighbor):
                return True

        on_stack.remove(node)  # BACKTRACK — forgetting this is the classic bug
        return False

    for node in range(n):
        if node not in visited and dfs(node):
            return True

    return False


# ============================================================================
# TEMPLATE 7: Cycle Detection - Undirected Graph
# ============================================================================

def has_cycle_undirected(n, graph):
    """
    Detect a cycle in an UNDIRECTED graph via parent-tracking DFS.

    Every undirected edge u-v appears in both adjacency lists, so v will
    always see u again. We skip exactly that one edge (the parent) — any
    OTHER visited neighbour is a genuine cycle.

    Assumes no multi-edges; with parallel edges, track the edge id instead.

    Time: O(V + E)
    Space: O(V)
    """
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor == parent:
                continue  # the edge we just came in on — not a cycle
            if neighbor in visited:
                return True
            if dfs(neighbor, node):
                return True

        return False

    for node in range(n):
        if node not in visited and dfs(node, -1):
            return True

    return False


def is_valid_tree(n, edges):
    """
    "Graph Valid Tree": a tree is a connected acyclic graph.

    Shortcut: with exactly n-1 edges, connected ⟺ acyclic, so you only need
    to check the edge count and connectivity.

    Time: O(V + E)
    Space: O(V + E)
    """
    if len(edges) != n - 1:
        return False  # too few → disconnected, too many → must contain a cycle

    graph = build_graph(n, edges)
    visited = set()
    stack = [0]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    return len(visited) == n  # every node reached → connected


# ============================================================================
# TEMPLATE 8: Topological Sort - Kahn's Algorithm (BFS)
# ============================================================================

def topological_sort_bfs(n, graph):
    """
    Order a DAG's nodes so every edge u→v puts u before v. Kahn's algorithm.

    Returns [] if a cycle exists (the standard "Course Schedule II" contract).

    Time: O(V + E)
    Space: O(V)
    """
    # in_degree[v] = how many prerequisites v still has.
    in_degree = [0] * n
    for u in range(n):
        for v in graph[u]:
            in_degree[v] += 1  # count INCOMING edges, one per u→v edge

    # Start from everything with no prerequisites.
    queue = deque(node for node in range(n) if in_degree[node] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            # `node` is now placed, so this prerequisite is satisfied.
            in_degree[neighbor] -= 1
            # Enqueue exactly when the count hits 0 — using <= 0 or checking
            # before decrementing would enqueue a node multiple times.
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Any node still holding in_degree > 0 sits in a cycle and never enqueued.
    return order if len(order) == n else []


def can_finish_courses(num_courses, prerequisites):
    """
    "Course Schedule": can every course be taken? == is the graph a DAG?

    prerequisites[i] = [course, prereq] meaning prereq → course.

    Time: O(V + E)
    Space: O(V + E)
    """
    graph = defaultdict(list)
    for node in range(num_courses):
        graph[node] = []
    for course, prereq in prerequisites:
        graph[prereq].append(course)  # edge points prereq → course

    return len(topological_sort_bfs(num_courses, graph)) == num_courses


# ============================================================================
# TEMPLATE 9: Topological Sort - DFS (Post-Order Reversed)
# ============================================================================

def topological_sort_dfs(n, graph):
    """
    Topological order via DFS: append on the way OUT, then reverse.

    A node is appended only after all its descendants are, so reversing the
    post-order list puts every node before everything it points to.

    Returns [] on a cycle (detected with the same GREY/on-stack idea).

    Time: O(V + E)
    Space: O(V)
    """
    color = [WHITE] * n
    post_order = []

    def dfs(node):
        color[node] = GREY

        for neighbor in graph[node]:
            if color[neighbor] == GREY:
                return False  # cycle → no valid ordering exists
            if color[neighbor] == WHITE and not dfs(neighbor):
                return False

        color[node] = BLACK
        post_order.append(node)  # post-order: all descendants already appended
        return True

    for node in range(n):
        if color[node] == WHITE and not dfs(node):
            return []

    post_order.reverse()  # reversed post-order == topological order
    return post_order


# ============================================================================
# TEMPLATE 10: Union-Find / Disjoint Set Union (DSU)
# ============================================================================

class UnionFind:
    """
    Disjoint sets with path compression + union by rank.

    Near-O(1) amortised per operation — formally O(α(n)), the inverse
    Ackermann function, which is < 5 for any n you will ever see.
    """

    def __init__(self, n):
        self.parent = list(range(n))  # each node starts as its own root
        self.rank = [0] * n           # upper bound on tree height
        self.count = n                # number of disjoint components

    def find(self, x):
        """Return x's root, flattening the path to it (path compression)."""
        root = x
        while self.parent[root] != root:  # walk up to the root
            root = self.parent[root]

        # Second pass: re-point every node on the path directly at the root,
        # so the next find() on any of them is O(1).
        while self.parent[x] != root:
            self.parent[x], x = root, self.parent[x]

        return root

    def union(self, x, y):
        """Merge the sets containing x and y. False if already merged."""
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            return False  # already connected — in Kruskal, this edge is a cycle

        # Union by rank: hang the SHORTER tree under the taller one so the
        # combined height doesn't grow unnecessarily.
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            # Equal heights: the winner gets exactly one level taller.
            self.rank[root_x] += 1

        self.count -= 1
        return True

    def connected(self, x, y):
        """Are x and y in the same set?"""
        return self.find(x) == self.find(y)


def count_components_union_find(n, edges):
    """
    "Number of Connected Components": start at n sets, one union per edge.

    Time: O(V + E * α(V))
    Space: O(V)
    """
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.count


def kruskal_mst(n, edges):
    """
    Minimum spanning tree cost: sort edges by weight, keep any that connects
    two different components. edges = [(u, v, w), ...]

    Returns -1 if the graph is disconnected (no spanning tree exists).

    Time: O(E log E)
    Space: O(V)
    """
    uf = UnionFind(n)
    total = 0
    used = 0

    for u, v, w in sorted(edges, key=lambda e: e[2]):  # cheapest edge first
        if uf.union(u, v):  # union() returns False if it would form a cycle
            total += w
            used += 1
            if used == n - 1:  # a spanning tree has exactly n-1 edges
                break

    return total if used == n - 1 else -1


# ============================================================================
# TEMPLATE 11: Dijkstra's Shortest Path (Weighted, Non-Negative)
# ============================================================================

def dijkstra(graph, start, n):
    """
    Shortest distance from `start` to every node, non-negative weights only.

    graph[u] = [(v, weight), ...]

    Uses the "lazy deletion" heap: instead of decrease-key (which Python's
    heapq lacks) we push a new entry and skip stale ones on pop.

    Time: O(E log V)
    Space: O(V + E)
    """
    dist = {node: float('inf') for node in range(n)}
    dist[start] = 0
    heap = [(0, start)]  # (distance, node) — distance FIRST so heapq sorts on it

    while heap:
        d, node = heapq.heappop(heap)

        # Stale entry: we already popped this node with a smaller distance.
        # Skipping here is what keeps the algorithm O(E log V).
        if d > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = d + weight
            # Only push when we strictly improve — otherwise the heap fills
            # with useless entries and can even loop on zero-weight edges.
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return dist


def dijkstra_with_path(graph, start, target, n):
    """
    Dijkstra that also reconstructs the actual route via a parent map.

    Returns (distance, [start, ..., target]) or (inf, []) if unreachable.

    Time: O(E log V)
    Space: O(V + E)
    """
    dist = {node: float('inf') for node in range(n)}
    dist[start] = 0
    parent = {start: None}
    heap = [(0, start)]

    while heap:
        d, node = heapq.heappop(heap)

        if node == target:
            break  # first pop of target is final — its distance is settled
        if d > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = node  # remember who relaxed us
                heapq.heappush(heap, (new_dist, neighbor))

    if dist[target] == float('inf'):
        return float('inf'), []

    # Walk parents backwards from target, then flip.
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    return dist[target], path


# ============================================================================
# QUICK DEMO
# ============================================================================

if __name__ == "__main__":
    g = build_graph(5, [[0, 1], [0, 2], [1, 3], [3, 4]])
    print("DFS recursive:  ", dfs_recursive(g, 0))          # [0, 1, 3, 4, 2]
    print("DFS iterative:  ", dfs_iterative(g, 0))          # [0, 1, 3, 4, 2]
    print("BFS:            ", bfs(g, 0))                    # [0, 1, 2, 3, 4]
    print("BFS levels:     ", bfs_level_order(g, 0))        # [[0],[1,2],[3],[4]]
    print("Dist 0→4:       ", bfs_shortest_path_length(g, 0, 4))  # 3

    dag = build_graph(4, [[0, 1], [0, 2], [1, 3], [2, 3]], directed=True)
    print("Topo (Kahn):    ", topological_sort_bfs(4, dag))  # [0, 1, 2, 3]
    print("Topo (DFS):     ", topological_sort_dfs(4, dag))  # [0, 2, 1, 3]
    print("Cycle?          ", has_cycle_directed(4, dag))    # False

    print("Components:     ", count_components_union_find(5, [[0, 1], [3, 4]]))  # 3
    print("Valid tree?     ", is_valid_tree(5, [[0, 1], [0, 2], [1, 3], [1, 4]]))  # True

    grid = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
    print("Islands:        ", count_islands(grid))           # 2

    wg = build_weighted_graph(4, [[0, 1, 1], [1, 2, 2], [0, 2, 5], [2, 3, 1]])
    print("Dijkstra:       ", dijkstra(wg, 0, 4))            # 0:0 1:1 2:3 3:4
    print("Dijkstra path:  ", dijkstra_with_path(wg, 0, 3, 4))  # (4, [0,1,2,3])
    print("MST cost:       ", kruskal_mst(4, [(0, 1, 1), (1, 2, 2), (0, 2, 5), (2, 3, 1)]))  # 4
