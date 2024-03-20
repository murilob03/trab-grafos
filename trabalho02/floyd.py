class Grafo:
    def __init__(self, n_vertices: int):
        self.n_vertices: int = n_vertices
        self.matriz_adj: list[list[float]] = [
            [float("inf")] * n_vertices for k in range(n_vertices)
        ]
        for i in range(n_vertices):
            self.matriz_adj[i][i] = 0

    def add_vertice(self, src: int, dest: int, weight: int):
        self.matriz_adj[src][dest] = weight

    def print_grafo(self):
        for row in range(len(self.matriz_adj)):
            print(self.matriz_adj[row])


def floyd(G: Grafo):
    dist_matrix: list[list[float]] = G.matriz_adj.copy()

    for k in range(G.n_vertices):
        for i in range(G.n_vertices):
            for j in range(G.n_vertices):
                dist_matrix[i][j] = min(dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j])

    for row in range(len(dist_matrix)):
        print(dist_matrix[row])
