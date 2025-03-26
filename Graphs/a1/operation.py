# operations.py

import random
from domain import MyDirectedGraph

def random_graph(total_nodes, total_edges, max_cost=100):
    """
    Generates a random directed graph with the specified number of nodes and edges.
    Returns a MyDirectedGraph instance.
    """
    max_possible_edges = total_nodes * total_nodes
    total_edges=min(total_edges,max_possible_edges)

    graph=MyDirectedGraph(total_nodes)
    edges_added=set()
    while len (edges_added)< total_edges:
        source=random.randint(0,total_nodes-1)
        target=random.randint(0,total_nodes-1)
        cost=random.randint(1,max_cost)

        edge=(source,target)
        if edge in edges_added:
            continue

        graph.add_edge(source,target,cost)
        edges_added.add(edge)


    return graph

def save_graph(graph, filename):
    """
    Saves the graph to a file.

    The first line will contain two integers: number of vertices, number of edges.
    Each subsequent line will contain three integers: source_vertex, target_vertex, cost.
    """
    with open(filename, 'w') as file:
        file.write(f"{graph.get_node_count()} {len(graph.edge_costs)}\n")
        for (start_node, end_node), cost in graph.edge_costs.items():
            file.write(f"{start_node} {end_node} {cost}\n")

def load_graph(filename):
    """
    Loads a directed graph from a file.

    The file's first line should have: number of vertices, number of edges.
    Each subsequent line should have: source_vertex, target_vertex, cost.
    Returns a MyDirectedGraph instance.
    """
    with open(filename, 'r') as file:
        n, m = map(int, file.readline().strip().split())
        graph = MyDirectedGraph(n)
        for line in file:
            x, y, c = map(int, line.strip().split())
            graph.add_edge(x, y, c)
    return graph
