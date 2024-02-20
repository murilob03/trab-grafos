class Graph:
    def __init__(self, is_directed, is_weighted):
        self.is_directed = is_directed
        self.is_weighted = is_weighted
        self.graph = {}

    def add_edge(self, source, destination, weight=None):
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

    def dfs(self, s):
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

    def display(self):
        for source, destinations in self.graph.items():
            print(f"{source} -> {destinations}")
