class Vertice:
    def __init__(self, idx: int):
        self.idx = idx
        self.d = float('inf')
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

def initialize_single_source(G: Grafo, s: int):
    #s: índice do vértice na lista de vertices do grafo
    for v in G.vertices:
        v.d = float('inf')
        v.pi = None
    G.vertices[s].d = 0


def relax(u: Vertice, v: Vertice, G: Grafo):
    #Calcula distância e associa pai
    if(v.d > u.d + G.matriz_adj[u.idx][v.idx]):
        v.d = u.d + G.matriz_adj[u.idx][v.idx]
        v.pi = u


def extract_min(Q) -> Vertice:
    vertice_min = None
    distancia_min = float('inf')
    for v in Q:
        if v.d < distancia_min:
            vertice_min = v
            distancia_min = v.d
    Q.remove(vertice_min)
    return vertice_min


def menor_distancia(G: Grafo, dest:int):
    return G.vertices[dest].d

def menor_caminho(G: Grafo, source:int, dest:int) -> list[Vertice]:
    caminho = []
    vert_atual = G.vertices[dest]
    while(vert_atual != None and vert_atual != G.vertices[source]):
        # caminho.append(vert_atual.idx)
        # caminho.insert(0, vert_atual.idx)
        caminho.insert(0, vert_atual)
        vert_atual = vert_atual.pi

    return caminho


def djikstra(G: Grafo, source:int, dest:int):
    initialize_single_source(G, source)
    S = []
    Q = G.vertices.copy()
    while len(Q) > 0:
        vertice = extract_min(Q)
        S.append(vertice)
        for (idx, v) in enumerate(G.matriz_adj[vertice.idx]):
        if v != 0:
            relax(vertice, G.vertices[idx], G)

    dist = menor_distancia(G, dest)
    caminho = menor_caminho(G, source, dest)

    print(caminho, dist)
    return (caminho, dist)