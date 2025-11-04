import networkx as nx
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Subgrafos del Grafo Original", fontsize=16, fontweight='bold')

# SUBGRAFO 1: Árbol (camino)
G1 = nx.Graph()
G1.add_edges_from([(7, 2), (2, 10)])  # Aristas: 7-2, 2-10
pos1 = {7: (0, 2), 2: (0, 1), 10: (0, 0)}  # Disposición vertical

nx.draw(G1, pos1, ax=axes[0], with_labels=True, node_color='lightgreen', 
        node_size=800, font_size=12, font_weight='bold', edge_color='gray')
axes[0].set_title("Subgrafo 1: Árbol (Camino 7→2→10)")
axes[0].axis('off')

# SUBGRAFO 2: Ciclo (cuadrilátero)
G2 = nx.Graph()
G2.add_edges_from([(1, 12), (12, 3), (3, 14), (14, 1)])  # Ciclo 1-12-3-14-1
pos2 = {1: (-1, 0), 12: (-1, 1), 3: (1, 1), 14: (1, 0)}  # Forma de rombo

nx.draw(G2, pos2, ax=axes[1], with_labels=True, node_color='lightcoral', 
        node_size=800, font_size=12, font_weight='bold', edge_color='red', width=2)
axes[1].set_title("Subgrafo 2: Ciclo (1-12-3-14-1)")
axes[1].axis('off')

# SUBGRAFO 3: Estrella
G3 = nx.Graph()
G3.add_edges_from([(1, 13), (1, 12), (1, 14)])  # Centro 1, hojas 13,12,14
pos3 = {1: (0, 0), 13: (-1, 1), 12: (0, 1), 14: (1, 1)}  # Hojas arriba

nx.draw(G3, pos3, ax=axes[2], with_labels=True, node_color='lightyellow', 
        node_size=800, font_size=12, font_weight='bold', edge_color='blue', width=2)
axes[2].set_title("Subgrafo 3: Estrella (Centro 1)")
axes[2].axis('off')

# Ajustar layout
plt.tight_layout()
plt.show()