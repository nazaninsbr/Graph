import matplotlib.pyplot as plt 
import networkx as nx 


def draw_graph(graph):
	G=nx.DiGraph()

	G.add_edges_from(graph)

	graph_pos = nx.shell_layout(G)

	nx.draw_networkx_nodes(G, graph_pos, node_size=1000, node_color='blue', alpha=0.3)
	nx.draw_networkx_edges(G, graph_pos, width=2, alpha=0.3, edge_color='green')
	nx.draw_networkx_labels(G, graph_pos, font_size=12, font_family='sans-serif')

	plt.show()

graph = graph = [
		(20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 20),
		(25, 21), (23, 20), (24, 22), (21, 24), (20, 21)
	]
draw_graph(graph)