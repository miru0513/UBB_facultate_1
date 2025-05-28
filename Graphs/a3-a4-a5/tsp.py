
from domain import MyDirectedGraph


class UndirectedEdge:
    """Represents an undirected edge with a cost."""

    def __init__(self, u, v, cost):
        # Store vertices in sorted order to ensure uniqueness
        self.u = min(u, v)
        self.v = max(u, v)
        self.cost = cost

    def __eq__(self, other):
        return self.u == other.u and self.v == other.v

    def __hash__(self):
        return hash((self.u, self.v))

    def __str__(self):
        return f"{self.u}-{self.v} (cost: {self.cost})"


class DisjointSet:
    """Disjoint Set Union (DSU) data structure for cycle detection."""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        """Find the representative of the set containing x (with path compression)."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union the sets containing x and y (with union by rank)."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in the same set

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
            self.size[root_x] += self.size[root_y]

        return True

    def get_size(self, x):
        """Get the size of the component containing x."""
        return self.size[self.find(x)]

    def in_same_component(self, x, y):
        """Check if x and y are in the same component."""
        return self.find(x) == self.find(y)


def approximate_tsp(graph):
    """
    Approximate TSP solution using the edge sorting heuristic:
    1. Sort edges in increasing order of their costs
    2. For each edge, choose it if and only if it does not close a cycle of length lower than n

    Args:
        graph: An instance of MyDirectedGraph

    Returns:
        A tuple (cycle, total_cost) where cycle is a list of vertices and total_cost is the cost of the cycle
    """
    n = graph.get_node_count()

    # Collect all edges from the directed graph and convert to undirected
    edges = []
    edge_dict = {}

    # First, collect all edges from the directed graph
    for u in range(n):
        for v in range(n):
            if graph.has_edge(u, v):
                min_u, max_u = min(u, v), max(u, v)
                cost = graph.get_edge_cost(u, v)

                edge = UndirectedEdge(min_u, max_u, cost)
                if edge not in edge_dict or cost < edge_dict[edge].cost:
                    edge_dict[edge] = edge

    # Convert dictionary to list
    edges = list(edge_dict.values())

    # Sort edges by cost in ascending order
    edges.sort(key=lambda e: e.cost)

    print(f"Sorted {len(edges)} edges by cost")

    # Initialize solution structures
    solution_edges = []
    vertex_degree = [0] * n

    # Initialize DSU for cycle detection
    dsu = DisjointSet(n)

    # Process edges in order of increasing cost
    for edge in edges:
        u, v, cost = edge.u, edge.v, edge.cost

        # Skip if adding this edge would exceed degree 2 for any vertex
        if vertex_degree[u] >= 2 or vertex_degree[v] >= 2:
            continue

        # Check if adding this edge would create a cycle
        if dsu.in_same_component(u, v):
            # Only allow a cycle if it would include all vertices
            component_size = dsu.get_size(u)
            if component_size < n:
                continue  # Skip - would create a premature cycle

        # Add the edge to our solution
        solution_edges.append(edge)
        vertex_degree[u] += 1
        vertex_degree[v] += 1
        dsu.union(u, v)

    print(f"Selected {len(solution_edges)} edges for the solution")

    # Build adjacency list from solution edges
    adjacency = [[] for _ in range(n)]
    for edge in solution_edges:
        adjacency[edge.u].append(edge.v)
        adjacency[edge.v].append(edge.u)

    # Find vertices with degree 1 (endpoints of the path)
    endpoints = [i for i in range(n) if vertex_degree[i] == 1]

    # If we have exactly 2 endpoints, try to connect them to form a cycle
    if len(endpoints) == 2:
        u, v = endpoints
        min_u, max_u = min(u, v), max(u, v)
        edge = UndirectedEdge(min_u, max_u, 0)  # Cost doesn't matter for the check

        for e in edges:
            if e.u == min_u and e.v == max_u:
                solution_edges.append(e)
                adjacency[u].append(v)
                adjacency[v].append(u)
                vertex_degree[u] += 1
                vertex_degree[v] += 1
                break

    # Extract the cycle/path
    cycle = extract_cycle(adjacency, vertex_degree, n)

    # Calculate total cost
    total_cost = 0
    for i in range(len(cycle)):
        u = cycle[i]
        v = cycle[(i + 1) % len(cycle)]

        # Find the cost of edge (u, v) in the original edges
        min_u, max_u = min(u, v), max(u, v)
        for edge in solution_edges:
            if (edge.u == min_u and edge.v == max_u):
                total_cost += edge.cost
                break

    return cycle, total_cost


def extract_cycle(adjacency, degrees, n):
    """
    Extract a cycle or path from the adjacency list.

    Args:
        adjacency: List of lists representing the adjacency list
        degrees: List of vertex degrees
        n: Number of vertices

    Returns:
        A list of vertices representing the cycle or path
    """
    # Find a starting vertex (preferably with degree 1)
    start = 0
    for i in range(n):
        if degrees[i] == 1:
            start = i
            break

    # If no vertex with degree 1, use any vertex with non-zero degree
    if degrees[start] == 0:
        for i in range(n):
            if degrees[i] > 0:
                start = i
                break

    # If still no suitable vertex, return empty path
    if degrees[start] == 0:
        return []

    # Traverse the path/cycle
    path = [start]
    current = start
    prev = -1

    while True:
        # Find the next vertex
        next_vertex = -1
        for neighbor in adjacency[current]:
            if neighbor != prev:
                next_vertex = neighbor
                break

        if next_vertex == -1 or (next_vertex == start and len(path) > 1):
            break  # End of path or completed cycle

        path.append(next_vertex)
        prev = current
        current = next_vertex

    return path


def test_with_directed_graph(graph):
    """Test the TSP approximation algorithm with a directed graph."""
    n = graph.get_node_count()

    print(f"Testing TSP approximation on a graph with {n} vertices")

    # Run the algorithm
    cycle, total_cost = approximate_tsp(graph)

    print(f"Approximate TSP solution:")
    if cycle:
        print(f"Cycle: {' -> '.join(map(str, cycle))}" + (f" -> {cycle[0]}" if cycle else ""))
        print(f"Total cost: {total_cost}")

        # Verify the cycle
        unique_vertices = set(cycle)
        print(f"Number of unique vertices in cycle: {len(unique_vertices)}")
        print(f"Expected number of vertices: {n}")
        print(f"Is a Hamiltonian cycle: {len(unique_vertices) == n and len(cycle) == n}")
    else:
        print("Failed to find a cycle.")

    return cycle, total_cost


def create_complete_graph(n, min_cost=1, max_cost=100):
    """Create a complete directed graph with random edge costs."""
    import random
    graph = MyDirectedGraph(n)

    for i in range(n):
        for j in range(n):
            if i != j:
                cost = random.randint(min_cost, max_cost)
                graph.add_edge(i, j, cost)

    return graph


if __name__ == "__main__":
    # Test with a random complete graph
    n = 5
    graph = create_complete_graph(n)
    test_with_directed_graph(graph)