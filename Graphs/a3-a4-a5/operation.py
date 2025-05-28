# operations.py

import random
from domain import MyDirectedGraph

def random_graph(total_nodes, total_edges, max_cost=100):
    max_possible_edges = total_nodes * total_nodes
    total_edges = min(total_edges, max_possible_edges)

    graph = MyDirectedGraph(total_nodes)
    edges_added = set()
    while len(edges_added) < total_edges:
        source = random.randint(0, total_nodes - 1)
        target = random.randint(0, total_nodes - 1)
        cost = random.randint(1, max_cost)

        edge = (source, target)
        if edge in edges_added:
            continue

        graph.add_edge(source, target, cost)
        edges_added.add(edge)

    return graph

def save_graph(graph, filename):
    with open(filename, 'w') as file:
        file.write(f"{graph.get_node_count()} {len(graph.edge_costs)}\n")
        for (start_node, end_node), cost in graph.edge_costs.items():
            file.write(f"{start_node} {end_node} {cost}\n")

def load_graph(filename):
    with open(filename, 'r') as file:
        n, m = map(int, file.readline().strip().split())
        graph = MyDirectedGraph(n)
        for line in file:
            x, y, c = map(int, line.strip().split())
            graph.add_edge(x, y, c)
    return graph

def find_connected_components_bfs(graph):
    visited = set()
    components = []

    adjacency = {v: set() for v in graph.parse_vertices()}
    for v in graph.parse_vertices():
        for _, neighbor in graph.get_outbound_edges(v):
            adjacency[v].add(neighbor)
            adjacency[neighbor].add(v)
        for neighbor, _ in graph.get_inbound_edges(v):
            adjacency[v].add(neighbor)
            adjacency[neighbor].add(v)

    for vertex in adjacency:
        if vertex not in visited:
            component = set()
            queue = [vertex]
            visited.add(vertex)

            while queue:
                current = queue.pop(0)
                component.add(current)
                for neighbor in adjacency[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            components.append(component)

    return components


def floyd_warshall(graph):
    """
    Implements the Floyd-Warshall algorithm to find shortest paths between all pairs of nodes in a graph.
    """
    # Get the number of nodes in the graph
    n = graph.get_node_count()

    # Initialize distance matrix with infinity for all pairs
    # dist[i][j] will hold the shortest distance from node i to node j
    dist = [[float('inf')] * n for _ in range(n)]

    # Initialize next_node matrix with -1 (no path) for all pairs
    # next_node[i][j] will hold the next node on the shortest path from i to j
    next_node = [[-1] * n for _ in range(n)]

    # Fill in the direct edge costs and set next nodes for direct connections
    for (u, v), cost in graph.edge_costs.items():
        dist[u][v] = cost
        next_node[u][v] = v  # The next node after u on the path to v is v itself

    # Store snapshots of the distance matrix after considering each intermediate node
    intermediate_matrices = []

    # Core Floyd-Warshall algorithm
    # Consider each node k as a potential intermediate node in the path from i to j
    for k in range(n):
        # Take a snapshot of the current distance matrix before considering node k
        snapshot = [row[:] for row in dist]
        intermediate_matrices.append((k, snapshot))

        # For each pair of nodes (i, j), check if going through node k gives a shorter path
        for i in range(n):
            for j in range(n):
                # If the path i→k→j is shorter than the current path i→j
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    # Update the shortest distance
                    dist[i][j] = dist[i][k] + dist[k][j]
                    # Update the next node on the path from i to j to be the same as the next node from i to k
                    next_node[i][j] = next_node[i][k]

    return dist, next_node, intermediate_matrices


def reconstruct_path(u, v, next_node):
    """
    Reconstructs the shortest path from node u to node v using the next_node matrix.
    Args:
        u: The starting node
        v: The destination node
        next_node: The next_node matrix from floyd_warshall
    Returns:
        A list representing the shortest path from u to v, or an empty list if no path exists
    """
    # If there's no path between u and v
    if next_node[u][v] == -1:
        return []

    # Special case for cycles (u == v)
    if u == v:
        # Find a neighbor that's part of the cycle
        intermediate = next_node[u][v]
        if intermediate == -1:
            return [u]  # No cycle exists, just the node itself

        # First find path from u to intermediate
        first_path = [u]
        current = u
        while current != intermediate:
            current = next_node[current][intermediate]
            if current == -1:
                return [u]  # Should not happen
            first_path.append(current)

        # Then find path from intermediate back to u
        second_path = []
        current = intermediate
        visited = {intermediate}
        while current != u:
            current = next_node[current][u]
            if current == -1 or current in visited:
                break  # Avoid infinite loops
            second_path.append(current)
            visited.add(current)

        # Combine paths (first_path already includes intermediate)
        return first_path + second_path

    # Regular case (u != v)
    path = [u]  # Start with the source node
    current = u

    # Follow the next_node pointers until we reach the destination
    while current != v:
        current = next_node[current][v]
        if current == -1:
            return []  # No path exists
        path.append(current)

        # Safety check to prevent infinite loops
        if len(path) > len(next_node) * 2:
            print("Warning: Possible infinite loop detected in path reconstruction")
            return []

    return path