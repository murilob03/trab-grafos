# Integrantes: Murilo Boccardo (RA124160), Reidner Adnan Maniezo de Melo (RA110582)

from floyd import Grafo, floyd

grafo: Grafo = Grafo(4)

# A (0)
grafo.add_vertice(0, 3, 5)
grafo.add_vertice(0, 1, 3)

# B (1)
grafo.add_vertice(1, 3, 4)
grafo.add_vertice(1, 0, 2)

# C (2)
grafo.add_vertice(2, 1, 1)

# D (3)
grafo.add_vertice(3, 2, 2)

floyd(grafo)
