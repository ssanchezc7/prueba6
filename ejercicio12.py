import networkx as nx

# Grafo A: 5 vértices, casi completo
G_A = nx.Graph()
G_A.add_edges_from([(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5)])  # falta 4-5?

# Grafo B: C7 + 3 cuerdas (ej. 1-3, 3-5, 5-7)
G_B = nx.cycle_graph(7)
G_B.add_edges_from([(0,2),(2,4),(4,6)])  # cuerdas

# Grafo C: C7 + vértice central conectado a 3
G_C = nx.cycle_graph(7)
G_C.add_node(7)
G_C.add_edges_from([(7,0),(7,2),(7,4)])  # centro a 3 vértices

# Función para comparar
def son_isomorfos(G1, G2):
    return nx.is_isomorphic(G1, G2)

print("A y B isomorfos:", son_isomorfos(G_A, G_B))  # False
print("A y C isomorfos:", son_isomorfos(G_A, G_C))  # False
print("B y C isomorfos:", son_isomorfos(G_B, G_C))  # True