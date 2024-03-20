# Integrantes: Murilo Boccardo (RA124160), Reidner Adnan Maniezo de Melo (RA110582)

from floyd import Grafo, floyd

grafo: Grafo = Grafo(5)

# A (0)
grafo.add_vertice(0, 3, 5)
grafo.add_vertice(0, 1, 4)

# B (1)
grafo.add_vertice(1, 4, 6)
grafo.add_vertice(1, 2, 1)

# C (2)
grafo.add_vertice(2, 0, 2)
grafo.add_vertice(2, 3, 3)

# D (3)
grafo.add_vertice(3, 2, 1)
grafo.add_vertice(3, 4, 2)

# E (4)
grafo.add_vertice(4, 3, 4)
grafo.add_vertice(4, 0, 1)

floyd(grafo)
