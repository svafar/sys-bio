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
# We also grab the number of self-arrows.
edges = []
self_arrows = 0
for unused in range(edge_count):
    # k=2 means we want two nodes, describing an edge, i.e. a node from which
    # the edge is connected, and the node to which it is connected.
    #
    # Note that we purposely allow for selecting two nodes that are
    # identical, because a node may connect to itself.
    a = random.choices(nodes, k=2)
    while [a] in edges:
        # Make sure that we don't get a duplicate edge expressing the same
        # nodes in the same direction. (No duplicate arrows.)
        a = random.choices(nodes, k=2)
    edges += [a]

    # Count the self-arrows.
    if a[0] == a[1]:
        self_arrows += 1

# Print some statistics.
print()
print('### GLORIOUS STATISTICS ###')
print()
print('Number of nodes       : %d' % len(nodes))
print('Number of arrows      : %d' % edge_count)
print('Number of self-arrows : %d' % self_arrows)

# Add nodes and edges.
G.add_nodes_from(nodes)
G.add_edges_from(edges)

seed = random.randint(0,100)
pos = nx.spring_layout(G, seed=seed)  # Seed for reproducible layout
nx.draw(G,pos=pos)
plt.show()