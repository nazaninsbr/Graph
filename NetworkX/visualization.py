import matplotlib.pyplot as plt 
import networkx as nx 

def draw_graph(graph):
	G = nx.Graph()

	for edge in graph:
		G.add_edge(edge[0], edge[1]) 

	graph_pos = nx.shell_layout(G)

	nx.draw_networkx_nodes(G, graph_pos, node_size=1000, node_color='blue', alpha=0.3)
	nx.draw_networkx_edges(G, graph_pos)
	nx.draw_networkx_labels(G, graph_pos, font_size=12, font_family='sans-serif')

	plt.show()

graph = [(20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 20)]
draw_graph(graph)		