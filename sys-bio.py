import matplotlib.pyplot as plt
import networkx as nx
import math, random

G = nx.Graph()

# Create a a list of 1..N, where N is what the user asked for.
# If user selects 400, we'll get a list with the numbers 1 up to 400.
# Example, if 6 is provided:
#     [1, 2, 3, 4, 5, 6]
i = int(input("Number of nodes: "))
nodes = [r for r in range(1, i+1)]

# Ask how many edges we want in total.
edge_count = int(input("Number of edges: "))

# Generate random links (edges) between nodes.
# This will become a list of two-instance lists.
edges = []
for unused in range(edge_count):
    # k=2 means we want two nodes, describing an edge, i.e. a node from which
    # the edge is connected, and the node to which it is connected.
    #
    # Note that we purposely allow for selecting two nodes that are
    # identical, because a node may connect to itself.
    a = random.choices(nodes, k=2)
    edges += [a]

#print(nodes)
print("Edges between two nodes:")
#print(edges)

G.add_nodes_from(nodes)
edge_list = []
while len(edge_list)<len(edges):
    nodeA=random.sample(nodes,1)[0]
    nodeB=random.sample(nodes,1)[0]
    if (nodeA, nodeB) not in edge_list:
        if (nodeB, nodeA) not in edge_list:
            edge_list.append((nodeA, nodeB))
G.add_edges_from(edge_list)
seed = random.randint(0,100)
pos = nx.spring_layout(G, seed=seed)  # Seed for reproducible layout
nx.draw(G,pos=pos)
plt.show()