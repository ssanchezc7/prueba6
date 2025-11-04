import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo
G = nx.Graph()

# Agregar vértices
G.add_nodes_from(['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8'])

# Agregar aristas desde la matriz
G.add_edges_from([
    ('V1', 'V2'), ('V1', 'V3'), ('V1', 'V4'), ('V1', 'V7'), ('V1', 'V8'),
    ('V2', 'V3'), ('V2', 'V5'), ('V2', 'V6'), ('V2', 'V8'),
    ('V3', 'V4'), ('V3', 'V5'), ('V3', 'V6'), ('V3', 'V7'),
    ('V4', 'V5'), ('V4', 'V7'),
    ('V5', 'V6'), ('V5', 'V7'), ('V5', 'V8'),
    ('V6', 'V8'),
    ('V7', 'V8')
])

nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
plt.title('Dibujo del Grafo')
plt.show()