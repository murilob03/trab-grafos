from grafo import Graph


def main():
    is_directed = input("Is your graph directed? (y/n): ").lower() == "y"
    is_weighted = input("Is your graph weighted? (y/n): ").lower() == "y"

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

    graph.display()

    # start = input("Where to start the bfs procedure?")
    # graph.bfs(start)

    start = input("Where to start the dfs procedure?")
    graph.dfs(start)


if __name__ == "__main__":
    main()
