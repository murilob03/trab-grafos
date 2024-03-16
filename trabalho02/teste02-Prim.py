from prim import Grafo, Prim;

grafo = Grafo(9)

#A
grafo.add_aresta(0, 1, 4)
grafo.add_aresta(1, 0, 4)

grafo.add_aresta(0, 7, 8) 
grafo.add_aresta(7, 0, 8) 


#B
grafo.add_aresta(1, 7, 11)
grafo.add_aresta(7, 1, 11)

grafo.add_aresta(1, 2, 8)
grafo.add_aresta(2, 1, 8)

#C
grafo.add_aresta(2, 3, 7)
grafo.add_aresta(3, 2, 7)

grafo.add_aresta(2, 8, 2)
grafo.add_aresta(8, 2, 2)

grafo.add_aresta(2, 5, 4)
grafo.add_aresta(5, 2, 4)

#D
grafo.add_aresta(3, 5, 14)
grafo.add_aresta(5, 3, 14)

grafo.add_aresta(3, 4, 9)
grafo.add_aresta(4, 3, 9)


#E
grafo.add_aresta(4, 5, 10)
grafo.add_aresta(5, 4, 10)

#F
grafo.add_aresta(5, 6, 2)
grafo.add_aresta(6, 5, 2)

#G
grafo.add_aresta(6, 8, 6)
grafo.add_aresta(8, 6, 6)

grafo.add_aresta(6, 7, 1)
grafo.add_aresta(7, 6, 1)

#H
grafo.add_aresta(7, 8, 7)
grafo.add_aresta(8, 7, 7)

raiz = 0  # Vértice de partida
Prim(grafo, raiz)

grafo.prim_result()