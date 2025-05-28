# dag_operations.py

def is_dag(graph):
    """
    Check if the graph is a Directed Acyclic Graph (DAG) using DFS to detect cycles.

    Args:
        graph: MyDirectedGraph instance

    Returns:
        bool: True if the graph is a DAG, False otherwise
    """
    visited = set()
    temp = set()  # temporary set for cycle detection

    def dfs_check_cycle(vertex):
        if vertex in temp:
            return False  # Cycle detected
        if vertex in visited:
            return True

        temp.add(vertex)

        # Check outbound neighbors
        for _, neighbor in graph.get_outbound_edges(vertex):
            if not dfs_check_cycle(neighbor):
                return False

        temp.remove(vertex)
        visited.add(vertex)
        return True

    # Check all vertices
    for vertex in graph.parse_vertices():
        if vertex not in visited:
            if not dfs_check_cycle(vertex):
                return False

    return True


def topological_sort(graph):
    """
    Perform topological sorting using predecessor counters (in-degree method).

    Args:
        graph: MyDirectedGraph instance

    Returns:
        list: Topologically sorted vertices or None if not a DAG
    """
    if not is_dag(graph):
        return None  # Not a DAG, can't perform topological sort

    # Calculate in-degree (predecessor count) for each vertex
    in_degree = {v: graph.get_in_degree(v) for v in graph.parse_vertices()}

    # Queue of vertices with no predecessors
    queue = [v for v in graph.parse_vertices() if in_degree[v] == 0]
    result = []

    while queue:
        u = queue.pop(0)
        result.append(u)

        # Decrease in-degree of adjacent vertices
        for _, v in graph.get_outbound_edges(u):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # If topological sort doesn't include all vertices, there's a cycle
    if len(result) != graph.get_node_count():
        return None

    return result


def highest_cost_path(graph, start, end):
    """
    Find the highest cost path from start to end vertex in a DAG.

    Args:
        graph: MyDirectedGraph instance
        start: Starting vertex
        end: Ending vertex

    Returns:
        tuple: (highest_cost, path) or (None, None) if no path exists or not a DAG
    """
    if not is_dag(graph):
        return None, None  # Not a DAG

    # Get topological order
    topo_order = topological_sort(graph)
    if not topo_order:
        return None, None

    # Initialize distances
    dist = {v: float('-inf') for v in graph.parse_vertices()}
    dist[start] = 0

    # Initialize predecessor tracking for path reconstruction
    pred = {v: None for v in graph.parse_vertices()}

    # Process vertices in topological order
    for u in topo_order:
        if u == end:
            break

        if dist[u] != float('-inf'):
            for _, v in graph.get_outbound_edges(u):
                cost = graph.get_edge_cost(u, v)
                if dist[u] + cost > dist[v]:
                    dist[v] = dist[u] + cost
                    pred[v] = u

    # If end is not reachable
    if dist[end] == float('-inf'):
        return None, None

    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = pred[current]

    path.reverse()

    return dist[end], path