import networkx as nx
import pandas as pd
G = nx.MultiGraph()
edges = [
    ('A','C',5), ('A','H',10),
    ('B','C',9), ('B','D',2), ('B','E',4), ('B','G',3), ('B','H',6),
    ('C','F',7),
    ('D','G',12), ('D','H',8), ('D','H',14),  # dos aristas entre D y H
    ('E','F',1), ('E','G',15)
]
G.add_weighted_edges_from(edges)

adj_matrix = nx.to_pandas_adjacency(G)
print("Matriz de Adyacencia:")
print(adj_matrix)

inc_matrix = nx.incidence_matrix(G, oriented=False).todense()
inc_df = pd.DataFrame(inc_matrix, index=G.nodes(), columns=[f"e{i+1}" for i in range(13)])
print("\nMatriz de Incidencia:")
print(inc_df)