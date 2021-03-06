from stat import ST_DEV
import matplotlib.pyplot as plt
import networkx as nx
import math, random
from statistics import stdev
from statistics import mean

# A function that takes only the number of nodes and edges desired, returning three values:
# 1. nodes: The generated nodes, a list from 1 to `note_count`, like [1, 2, 3].
# 2. edges: The randomly generated edges (arrows).
# 3. self_arrow_count: The number of self-referencing arrows.
def run(node_count, edge_count):
    # Create a a list of 1..N, where N is what the user asked for.
    # If user selects 400, we'll get a list with the numbers 1 up to 400.
    # Example, if 6 is provided:
    #     [1, 2, 3, 4, 5, 6]
    nodes = [r for r in range(1, node_count+1)]

    # Generate random links (edges) between nodes.
    # This will become a list of two-instance lists.
    # We also grab the number of self-arrows.
    edges = []
    self_arrow_count = 0.0
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
            self_arrow_count += 1.0
    return nodes, edges, self_arrow_count

# Ask how many nodes we want in each run.
node_count = int(input("Number of nodes: "))

# Ask how many edges we want in total for each run.
edge_count = int(input("Number of edges: "))

# Ask how many runs we want, given the aforementioned variables.
run_count = int(input('Number of runs: '))

# Iterate as often as requested ("runs"), and collect the number of
# self-arrows each run, compiling them in a list ingeniously named
# self_arrow_counts.
self_arrow_counts = []
for r in range(0, run_count):
    nodes, edges, self_arrow_count = run(node_count, edge_count)
    self_arrow_counts.append(self_arrow_count)

# Print some statistics.
print()
print('### GLORIOUS STATISTICS ###')
print()
print('Number of nodes       : %d' % node_count)
print('Number of arrows      : %d' % edge_count)
print('Number of runs        : %d' % run_count)
print('----------------------')
if run_count == 1:
    print('Number of self-arrows : %d' % self_arrow_counts[0])
elif run_count > 1:
    print('Mean of self-arrows   : %.2f' % mean(self_arrow_counts))
    print('Standard deviation    : %.2f' % stdev(self_arrow_counts))

def create_graph(nodes, edges):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    seed = random.randint(0,100)
    pos = nx.spring_layout(G, seed=seed)  # Seed for reproducible layout
    nx.draw(G,pos=pos)
    plt.show()

# Graph creation seems broken but is left here in case someone wants to fix it.
#create_graph(nodes, edges)