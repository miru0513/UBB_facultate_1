# domain.py

import random

class MyDirectedGraph:
    """
    Represents a directed graph with adjacency structures for inbound and outbound edges.
    """

    def __init__(self, node_count):
        self.node_count = node_count
        self.outbound_adjacency = {v: [] for v in range(node_count)}
        self.inbound_adjacency = {v: [] for v in range(node_count)}
        self.edge_costs = {}

    def get_node_count(self):
        return self.node_count

    def parse_vertices(self):
        return iter(self.outbound_adjacency.keys())

    def has_edge(self, start_node, end_node):
        return end_node in self.outbound_adjacency[start_node]

    def get_edge_id(self, start_node, end_node):
        return (start_node, end_node) if self.has_edge(start_node, end_node) else None

    def get_in_degree(self, vertex):
        return len(self.inbound_adjacency[vertex])

    def get_out_degree(self, vertex):
        return len(self.outbound_adjacency[vertex])

    def get_outbound_edges(self, vertex):
        return iter((vertex, dest) for dest in self.outbound_adjacency[vertex])

    def get_inbound_edges(self, vertex):
        return iter((source, vertex) for source in self.inbound_adjacency[vertex]
)
    def get_edge_endpoints(self, edge_id):
        return edge_id if edge_id in self.edge_costs else None

    def get_edge_cost(self, start_node, end_node):
        return self.edge_costs.get((start_node, end_node), float('inf'))

    def set_edge_cost(self, start_node, end_node, cost):
        if self.has_edge(start_node, end_node):
            self.edge_costs[(start_node, end_node)] = cost

    def add_edge(self, start_node, end_node, cost):
        if self.has_edge(start_node, end_node):
            print(f"Edge from {start_node} to {end_node} already exists!")
            return

        self.outbound_adjacency[start_node].append(end_node)
        self.inbound_adjacency[end_node].append(start_node)
        self.edge_costs[(start_node, end_node)] = cost
        print(f"Edge from {start_node} to {end_node} added successfully.")

    def remove_edge(self, start_node, end_node):
        if start_node not in self.outbound_adjacency or end_node not in self.inbound_adjacency:
            print(f"Invalid vertices: {start_node}, {end_node}")
            return

        if end_node in self.outbound_adjacency[start_node]:
            self.outbound_adjacency[start_node].remove(end_node)
            self.inbound_adjacency[end_node].remove(start_node)
            del self.edge_costs[(start_node, end_node)]
            print(f"Edge from {start_node} to {end_node} removed.")
        else:
            print(f"No edge exists from {start_node} to {end_node}.")

    def add_vertex(self, vertex_id):
        if vertex_id in self.outbound_adjacency:
            print(f"Vertex {vertex_id} already exists!")
            return

        self.outbound_adjacency[vertex_id] = []
        self.inbound_adjacency[vertex_id] = []
        if vertex_id >= self.node_count:
            self.node_count = vertex_id + 1
        print(f"Vertex {vertex_id} added successfully.")

    def remove_vertex(self, vertex):
        if vertex not in self.outbound_adjacency:
            print(f"Vertex {vertex} does not exist.")
            return

        for dest in list(self.outbound_adjacency[vertex]):
            self.remove_edge(vertex, dest)
        for src in list(self.inbound_adjacency[vertex]):
            self.remove_edge(src, vertex)

        del self.outbound_adjacency[vertex]
        del self.inbound_adjacency[vertex]
        self.node_count -= 1
        print(f"Vertex {vertex} removed.")

    def copy(self):
        new_graph = MyDirectedGraph(self.node_count)
        new_graph.outbound_adjacency = {
            v: list(edges) for v, edges in self.outbound_adjacency.items()
        }
        new_graph.inbound_adjacency = {
            v: list(edges) for v, edges in self.inbound_adjacency.items()
        }
        new_graph.edge_costs = self.edge_costs.copy()
        return new_graph

    def __str__(self):
        lines = []
        for source in self.outbound_adjacency:
            for target in self.outbound_adjacency[source]:
                cost = self.edge_costs[(source, target)]
                lines.append(f"{source} -> {target} [cost: {cost}]")
        return "\n".join(lines)
