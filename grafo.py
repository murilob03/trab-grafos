class Graph:
    def __init__(self, is_directed, is_weighted):
        self.is_directed = is_directed
        self.is_weighted = is_weighted
        self.graph = {}

    def add_edge(self, source: int, destination: int, weight: int = 0):
        if source not in self.graph:
            self.graph[source] = []
        if destination not in self.graph:
            self.graph[destination] = []
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

    # Procedimento de busca em largura
    def bfs(self, s):
        print("BFS: ", end="")

        # Marca todos os vértices como não visitados
        visited = {key: False for key in self.graph}

        # Cria uma fila para o BFS
        queue = []
        queue.append(s)

        visited[s] = True

        while queue:
            # Remove um vértice da fila e imprime
            s = queue.pop(0)
            print(s, end=" ")

            # Pega todos os vértices adjacentes do vértice desenfileirado
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        print()

    def dfs(self, s):
        print("DFS: ", end="")

        visited = {}
        for vertex in self.graph.keys():
            visited[vertex] = False

        def dfs_recursive(i, visited_rec):
            visited_rec[i] = True
            print(i, end=" ")
            for i in self.graph[i]:
                if visited_rec[i] == False:
                    dfs_recursive(i, visited_rec)

        dfs_recursive(s, visited)
        print()

    # Implement Dijkstra's Algorithm
    def dijkstra(self, start_vertex, end_vertex):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start_vertex] = 0
        predecessors = {vertex: None for vertex in self.graph}
        visited = {vertex: False for vertex in self.graph}

        while True:
            # Find the unvisited vertex with the smallest distance
            min_vertex = None
            for vertex in self.graph:
                if not visited[vertex] and (min_vertex is None or distances[vertex] < distances[min_vertex]):
                    min_vertex = vertex

            if min_vertex is None or min_vertex == end_vertex:
                break

            visited[min_vertex] = True
            for neighbor, weight in self.graph[min_vertex]:
                if not visited[neighbor]:
                    new_distance = distances[min_vertex] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        predecessors[neighbor] = min_vertex

        # Build the path from start_vertex to end_vertex
        path = self.build_path(predecessors, end_vertex)

        print(f"Shortest path from {start_vertex} to {end_vertex}: {path}")
        print(f"Total distance: {distances[end_vertex]}")
        print()

    def build_path(self, predecessors, vertex):
        path = []
        while vertex is not None:
            path.insert(0, vertex)
            vertex = predecessors[vertex]
        return path

    def display(self):
        for source, destinations in self.graph.items():
            print(f"{source} -> {destinations}")
