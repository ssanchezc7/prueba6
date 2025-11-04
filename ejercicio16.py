import networkx as nx

# Definir el grafo
G = nx.Graph()
edges = [
    ('a', 'b'), ('a', 'c'), ('a', 'd'),
    ('b', 'c'), ('b', 'e'),
    ('c', 'd'), ('c', 'e'), ('c', 'f'),
    ('d', 'g'),
    ('e', 'f'), ('e', 'h'),
    ('f', 'g'), ('f', 'h'), ('f', 'i'),
    ('g', 'i'), ('g', 'j'),
    ('h', 'i'), ('h', 'k'),
    ('i', 'j'), ('i', 'k'), ('i', 'l'),
    ('j', 'l'), ('j', 'm'),
    ('k', 'l'), ('k', 'n'),
    ('l', 'm'), ('l', 'n'),
    ('m', 'n')
]
G.add_edges_from(edges)

# Verificar eulerianos
print("Ciclo Euleriano:", nx.is_eulerian(G))  # False
print("Camino Euleriano:", nx.has_eulerian_path(G))  # False

# Para hamiltonianos, no hay función directa, pero puedes dibujar para visualizar
nx.draw(G, with_labels=True)
import matplotlib.pyplot as plt
plt.show()