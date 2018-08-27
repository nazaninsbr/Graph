import networkx as nx 
import matplotlib.pyplot as plt 
import numpy as np 

G = nx.Graph()
G.add_node(11)
G.add_nodes_from([12, 13])
G.clear()
G.add_nodes_from([1, 2, 3])
G.add_edge(1, 2)
G.remove_edge(1, 2)
G.add_edges_from([(1, 2), (1, 3)])
print(G.nodes())

adj = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
G = nx.from_numpy_matrix(adj)
nx.draw_networkx(G, with_labels=True)
plt.show()