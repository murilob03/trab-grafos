from grafo import Graph


def input_graph() -> Graph:
    is_directed = input("Is your graph directed? (y/N): ").lower() == "y"
    is_weighted = input("Is your graph weighted? (y/N): ").lower() == "y"

    graph = Graph(is_directed, is_weighted)

    while True:
        if is_weighted:
            edge = input(
                "Input your graph edge (source, destination, weight) or type 'done' to finish: "
            )
            if edge.lower() == "done":
                break
            source, destination, weight = map(str, edge.split(","))
            graph.add_edge(source, destination, weight)
        else:
            edge = input(
                "Input your graph edge (source, destination) or type 'done' to finish: "
            )
            if edge.lower() == "done":
                break
            source, destination = map(str, edge.split(","))
            graph.add_edge(source, destination)
        
    return graph

def main():
    graph = input_graph()

    while True:
        operation = input("Choose an operation - [1]Print, [2]BFS, [3]DFS, [4]Dijkstra, or [5]Exit: ").lower()
        if operation == '5':
            break
        elif operation == '1':
            graph.display()
            continue

        start_vertex = input("Enter the start vertex: ")

        if operation == '2':
            graph.bfs(start_vertex)
        elif operation == '3':
            graph.dfs(start_vertex)
        elif operation == '4':
            if not graph.is_weighted:
                print("Dijkstra's algorithm requires a weighted graph!")
                continue
            graph.dijkstra(start_vertex)
        else:
            print("Invalid operation. Please choose BFS, DFS, Dijkstra, or Exit.")


if __name__ == "__main__":
    main()
