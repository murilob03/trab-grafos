from prim import Grafo, Prim;

grafo = Grafo(7)
#A
grafo.add_aresta(0, 2, 8)
grafo.add_aresta(0, 3, 1) 
grafo.add_aresta(0, 4, 6)
grafo.add_aresta(0, 5, 2)
grafo.add_aresta(0, 6, 8)

#B
grafo.add_aresta(1, 3, 5)
grafo.add_aresta(1, 6, 1)

#C
grafo.add_aresta(2, 0, 8)
grafo.add_aresta(2, 4, 2)

#D
grafo.add_aresta(3, 0, 1)
grafo.add_aresta(3, 1, 5)
grafo.add_aresta(3, 5, 9)

#E
grafo.add_aresta(4, 5, 4)
grafo.add_aresta(4, 0, 6)
grafo.add_aresta(4, 2, 2)

#F
grafo.add_aresta(5, 3, 9)
grafo.add_aresta(5, 0, 2)
grafo.add_aresta(5, 4, 4)

#G
grafo.add_aresta(6, 1, 1)
grafo.add_aresta(6, 0, 8)

raiz = 0  # indice do vértice de origem
Prim(grafo, raiz)
grafo.prim_result()