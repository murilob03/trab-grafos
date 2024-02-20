class Graph:
    def __init__(self, is_directed, is_weighted):
        self.is_directed = is_directed
        self.is_weighted = is_weighted
        self.graph = {}

    def add_edge(self, source, destination, weight=None):
        if source not in self.graph:
            self.graph[source] = []
        if destination not in self.graph[source]:
            if self.is_weighted:
                self.graph[source].append((destination, weight))
            else:
                self.graph[source].append(destination)

        if not self.is_directed:
            if destination not in self.graph:
                self.graph[destination] = []
            if source not in self.graph[destination]:
                if self.is_weighted:
                    self.graph[destination].append((source, weight))
                else:
                    self.graph[destination].append(source)

    def display(self):
        for source, destinations in self.graph.items():
            print(f"{source} -> {destinations}")


def input_graph():
    is_directed = input("Is your graph directed? (y/n): ").lower() == 'y'
    is_weighted = input("Is your graph weighted? (y/n): ").lower() == 'y'

    graph = Graph(is_directed, is_weighted)

    while True:
        if is_weighted:
            edge = input("Input your graph edge (source, destination, weight) or type 'done' to finish: ")
            if edge.lower() == 'done':
                break
            source, destination, weight = map(int, edge.split(','))
            graph.add_edge(source, destination, weight)
        else:
            edge = input("Input your graph edge (source, destination) or type 'done' to finish: ")
            if edge.lower() == 'done':
                break
            source, destination = map(int, edge.split(','))
            graph.add_edge(source, destination)

    graph.display()

input_graph()
