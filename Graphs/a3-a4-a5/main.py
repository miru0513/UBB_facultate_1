from domain import MyDirectedGraph
from operation import random_graph, save_graph, load_graph, find_connected_components_bfs, floyd_warshall, \
    reconstruct_path
from dag_operations import is_dag, topological_sort, highest_cost_path
from tsp import test_with_directed_graph


def main():
    start_option = input("Would you like to generate a random graph (R) or load from a file (L)? ").strip().upper()

    if start_option == 'R':
        num_vertices = int(input("Enter the number of vertices: "))
        num_edges = int(input("Enter the number of edges: "))
        my_graph = random_graph(num_vertices, num_edges)
    elif start_option == 'L':
        filename = input("Enter the filename to load from: ")
        my_graph = load_graph(filename)
    else:
        print("Please enter a valid option (R or L). Exiting...")
        return

    while True:
        print("\n=== Directed Graph Operations Menu ===")
        print("1.  Get the total number of vertices")
        print("2.  List all vertices")
        print("3.  Check if an edge exists (source → target)")
        print("4.  Retrieve the edge ID (if present)")
        print("5.  Get a vertex's in-degree")
        print("6.  Get a vertex's out-degree")
        print("7.  List a vertex's outbound edges")
        print("8.  List a vertex's inbound edges")
        print("9.  Add a new vertex to the graph")
        print("10. Remove an existing vertex from the graph")
        print("11. Add a new edge (source → target)")
        print("12. Remove an existing edge (source → target)")
        print("13. Save the current graph to a file")
        print("14. Load a graph from a file")
        print("15. Create an entirely new random graph")
        print("16. Exit the program")
        print("17. Find connected components (undirected, BFS)")
        print("18. Display the minimum cost path between two vertices and the corresponding cost")
        print("19. Display the intermediate matrices (Floyd-Warshall)")
        print("20. Check if the graph is a DAG (Directed Acyclic Graph)")
        print("21. Perform topological sorting (if graph is a DAG)")
        print("22. Find highest cost path between two vertices (if graph is a DAG)")
        print("23. Find approximate TSP solution (Hamiltonian cycle of low cost)")

        menu_choice = input("Choose an option (1–22): ").strip()

        if menu_choice == "1":
            print("Number of vertices:", my_graph.get_node_count())

        elif menu_choice == "2":
            print("All vertices in the graph:")
            for vertex in my_graph.parse_vertices():
                print(vertex)

        elif menu_choice == "3":
            start_node = int(input("Enter the source vertex: "))
            end_node = int(input("Enter the destination vertex: "))
            print("Edge exists:", my_graph.has_edge(start_node, end_node))

        elif menu_choice == "4":
            start_node = int(input("Enter the source vertex: "))
            end_node = int(input("Enter the destination vertex: "))
            print("Edge ID:", my_graph.get_edge_id(start_node, end_node))

        elif menu_choice == "5":
            chosen_vertex = int(input("Enter the vertex: "))
            print("In-degree:", my_graph.get_in_degree(chosen_vertex))

        elif menu_choice == "6":
            chosen_vertex = int(input("Enter the vertex: "))
            print("Out-degree:", my_graph.get_out_degree(chosen_vertex))

        elif menu_choice == "7":
            chosen_vertex = int(input("Enter the vertex: "))
            print("Outbound edges:", list(my_graph.get_outbound_edges(chosen_vertex)))

        elif menu_choice == "8":
            chosen_vertex = int(input("Enter the vertex: "))
            print("Inbound edges:", list(my_graph.get_inbound_edges(chosen_vertex)))

        elif menu_choice == "9":
            new_vertex_id = int(input("Enter the new vertex ID to add: "))
            my_graph.add_vertex(new_vertex_id)

        elif menu_choice == "10":
            chosen_vertex = int(input("Enter the vertex to remove: "))
            my_graph.remove_vertex(chosen_vertex)

        elif menu_choice == "11":
            start_node = int(input("Enter the source vertex: "))
            end_node = int(input("Enter the destination vertex: "))
            edge_cost = int(input("Enter the edge cost: "))
            my_graph.add_edge(start_node, end_node, edge_cost)

        elif menu_choice == "12":
            start_node = int(input("Enter the source vertex: "))
            end_node = int(input("Enter the destination vertex: "))
            my_graph.remove_edge(start_node, end_node)

        elif menu_choice == "13":
            filename = input("Enter a filename to save the current graph: ")
            save_graph(my_graph, filename)
            print(f"Graph saved to {filename}.")

        elif menu_choice == "14":
            filename = input("Enter a filename to load a graph from: ")
            my_graph = load_graph(filename)
            print(f"Graph loaded from {filename}.")

        elif menu_choice == "15":
            num_vertices = int(input("Enter the number of vertices: "))
            num_edges = int(input("Enter the number of edges: "))
            my_graph = random_graph(num_vertices, num_edges)
            print("A new random graph was generated.")

        elif menu_choice == "16":
            print("Exiting the program...")
            break

        elif menu_choice == "17":
            components = find_connected_components_bfs(my_graph)
            print(f"Found {len(components)} connected component(s):")
            for i, comp in enumerate(components, 1):
                print(f"Component {i}: {sorted(comp)}")

        elif menu_choice == "18":
            dist, next_node, _ = floyd_warshall(my_graph)
            u = int(input("Enter start vertex: "))
            v = int(input("Enter end vertex: "))
            path = reconstruct_path(u, v, next_node)
            if not path:
                print(f"No path from {u} to {v}.")
            else:
                print(f"Minimum cost from {u} to {v}: {dist[u][v]}")
                print("Path:", " -> ".join(map(str, path)))

        elif menu_choice == "19":
            dist, _, intermediate_matrices = floyd_warshall(my_graph)
            for k, matrix in intermediate_matrices:
                print(f"\n--- After including vertex {k} ---")
                for row in matrix:
                    formatted_row = ["∞" if val == float('inf') else str(val) for val in row]
                    print(" ".join(formatted_row))

        elif menu_choice == "20":
            if is_dag(my_graph):
                print("The graph is a DAG (Directed Acyclic Graph).")
            else:
                print("The graph is NOT a DAG (contains cycles).")

        elif menu_choice == "21":
            topo_order = topological_sort(my_graph)
            if topo_order:
                print("Topological order:", " -> ".join(map(str, topo_order)))
            else:
                print("Cannot perform topological sorting. Graph is not a DAG.")

        elif menu_choice == "22":
            u = int(input("Enter start vertex: "))
            v = int(input("Enter end vertex: "))
            cost, path = highest_cost_path(my_graph, u, v)
            if cost is None:
                print(f"No path exists from {u} to {v} or graph is not a DAG.")
            else:
                print(f"Highest cost path from {u} to {v}:")
                print(f"Cost: {cost}")
                print(f"Path: {' -> '.join(map(str, path))}")
        elif menu_choice == "23":

            test_with_directed_graph(my_graph)

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()