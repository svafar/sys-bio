import matplotlib.pyplot as plt
import networkx as nx
import math, random

G = nx.Graph()

# Create a a list of 1..N, where N is what the user asked for.
i = int(input("Number of nodes: "))
nodes = [r for r in range(1, i+1)]

edges = []
for k in nodes:
    a = random.choices(nodes, k=2)
    edges += [a]
print(nodes)
print("Edges between two nodes:")
print(edges)
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