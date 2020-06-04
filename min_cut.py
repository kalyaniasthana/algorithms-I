import sys
import random

def read_graph(filename):

	graph = {}
	with open(filename) as f:
		for line in f:
			line = line.strip('\n')
			#print(line)
			line = line.split('\t')
			#print(line)
			node = int(line[0])
			graph[node] = [int(i) for i in line[1: len(line) - 1]]

	return graph

'''
def initialize_supernodes(G):

	supernodes = []
	for key in G:
		supernodes.append(key)

	return supernodes

def initialize_superedges(G):

	superedges = []
	for key in G:
		for key_ in G[key]:

			edge = list(key) + [key_]
			edge = tuple(edge)
			superedges.append(edge)

	return superedges
'''

#(a, b) is an edge and we have to merge the nodes of this edge

def merge_random_edge(G):

	#select two random nodes
	node = random.choice(list(G))
	node_ = random.choice(G[node])

	#merge edges of both nodes

	new_edges = G[node] + G[node_]
	G[node] = new_edges

	#print(node,node_)

	#print(node, G[node])

	#delete second node
	del G[node_]
	#print(len(G))

	#replace node_ with node everywhere in the damn graph. dude ik this isn't efficient ok. 
	#I suck. I should learn proper OOP.
	for _node in G:
		for j in range(len(G[_node])):
			if G[_node][j] == node_:
				G[_node][j] = node

	#remove self loops
	G[node] = [x for x in G[node] if x != node]

	return G

def karger(G):

	while len(list(G)) > 2:

		G = merge_random_edge(G)

	nodes = list(G.keys())

	return len(G[nodes[0]])	

def karger_min_loop(G):

	l = []
	for i in range(500):
		l.append(karger(G))

	return min(l)

filename = 'kargerMinCut.txt'
G = read_graph(filename)
print(karger_min_loop(G))


