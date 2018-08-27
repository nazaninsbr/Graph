import networkx as nx 

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([3, 8])
G.add_edge(1, 3)
G.add_edge(1, 8)
G[1][8]['color'] = "blue"
G.add_edge(1, 5)
G.add_edge(4, 6)
print('number of nodes: ', G.number_of_nodes())
print(list(G.nodes))
print('number of edges: ', G.number_of_edges())
print(list(G.adj[1]))
G.remove_node(8)
print('number of nodes: ', G.number_of_nodes())
print(list(G.nodes))