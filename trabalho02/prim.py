class Vertice:
    def __init__(self, idx: int):
        self.idx = idx
        self.chave = float('inf')
        self.pi = None

class Grafo:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.vertices = [Vertice(idx) for idx in range(n_vertices)]
        self.matriz_adj = [[0] * n_vertices for k in range(n_vertices)]

    def add_aresta(self, i, j, w):
        self.matriz_adj[i][j] = w

    def print(self):
        for l in self.matriz_adj:
            print(l)

    def prim_result(self):
        for v in self.vertices:
            print(f'vertice: {v.idx} - pai:{v.pi.idx if v.pi else None}')

def extract_min(Q) -> Vertice:
    vertice_min = None
    chave_min = float('inf')
    for v in Q:
        if v.chave < chave_min:
            vertice_min = v
            chave_min = v.chave
    Q.remove(vertice_min)
    return vertice_min


def Prim(G: Grafo, raiz: int):

    for v in G.vertices: #inicializacao
        v.chave = float('inf')
        v.pi = None
    G.vertices[raiz].chave = 0
    Q = G.vertices.copy()

    while len(Q) != 0:
        #vertice de menor chave
        u = extract_min(Q)

        for (idx, w) in enumerate(G.matriz_adj[u.idx]): #w é o peso, idx é o índice do vertice em G.vertices
            current_vertex = G.vertices[idx]
            if(current_vertex in Q and w < current_vertex.chave and w != 0):
                current_vertex.pi, current_vertex.chave = u, w