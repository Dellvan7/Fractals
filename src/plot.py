import matplotlib.pyplot as plt
import networkx as nx

def matrix_graph_to_networkx(graph, width, height):
	nodes, adj_matrix = graph

	G = nx.Graph()
	pos = {}
	for i in range(nodes.__len__()):
		G.add_node( nodes[i] )
		pos[nodes[i]] = (width-nodes[i][0], height-nodes[i][1])
	for i in range(nodes.__len__()):
		for j in range(nodes.__len__()):
			if adj_matrix[i][j] != -1:
				G.add_edge(nodes[i], nodes[j])
	return G, pos

def list_graph_to_networkx(graph):
	G = nx.Graph()
	pos = {}
	for i, node in enumerate(graph):
		G.add_node(node)
		pos[node] = (node[0], node[1])
		for node2 in graph[node]:
			G.add_edge(node, node2)
	return G, pos

def segments_to_graph(segments):
	G = {}
	for segment in segments:
		p0, p1 = segment

		if p0 not in G:
			G[p0] = [p1]
		else:
			G[p0].append(p1)
		if p1 not in G:
			G[p1] = [p0]
		else:
			G[p1].append(p0)
	return G

def save_graph(G, pos, name, basewidth):
	plt.clf()
	nx.draw_networkx_edges(G, pos=pos, node_color='k', edge_color='b', node_shape='.', node_size=10, with_labels=True, ax=None, fontsize=8)
	plt.axis('off')
	plt.savefig('fractals/' + name + basewidth.__str__() + ".png",format="PNG", dpi=500)
