import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import random	
import numpy as np
import math

# Read the file
file_path = 'modified_impression_network.csv'
df = pd.read_csv(file_path)

# Create a directed graph
G = nx.DiGraph()

# Adding directed edges
for index, row in df.iterrows():
    person = row[0]  # The person who is impressed
    impressed_by = row[1:].dropna()  # The people they are impressed by
    for impressed_person in impressed_by:
        G.add_edge(person, impressed_person)  # Add an edge from person to impressed_person


# def pagerank_random_walk(G, d=0.85):
#     """
#     Finds the pagerank of a graph using random walks with teleportation and returns it as a dictionary.
#     """
#     # Create a dictionary
#     pagerank = {}
#     # Set all nodes to have a pagerank of 0
#     for node in G.nodes():
#         pagerank[node] = 0
#     # Pick a random node to start at
#     current_node = random.choice(list(G.nodes()))
#     # Do n random walks
#     n = 100000000
#     for i in range(n):
#         # Add 1 to the pagerank of the current node
#         pagerank[current_node] += 1
#         # Decide to either follow a link or teleport
#         if random.random() > d:
#             # Teleport to a random node
#             current_node = random.choice(list(G.nodes()))
#         else:
#             # Get a list of current node's neighbors
#             neighbors = list(G.neighbors(current_node))
#             # If the current node has no neighbors, pick a random node to start at
#             if len(neighbors) == 0:
#                 current_node = random.choice(list(G.nodes()))
#             # Otherwise, pick a random neighbor to move to
#             else:
#                 current_node = random.choice(neighbors)
#     # Normalize the pagerank
#     for node in pagerank:
#         pagerank[node] /= n
#     return pagerank


# # Generate pagerank using random walk and sort the dictionary
# pagerank = pagerank_random_walk(G)
# sorted_pagerank = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)


# # Create a matrix such that the i,jth element is the number of common neighbors
# # between the ith and jth nodes / the number of neighbors of the ith node
# def common_neighbors_matrix(G):
#     """
#     Creates a matrix such that the i,jth element is the number of common neighbors
#     between the ith and jth nodes / the number of neighbors of the ith node
#     """
#     # Create a dictionary
#     common_neighbors = {}
#     # Create a dictionary of the number of neighbors of each node
#     num_neighbors = {}
#     for node in G.nodes():
#         num_neighbors[node] = len(list(G.neighbors(node)))
#     print(num_neighbors)
#     # Create a matrix
#     matrix = np.zeros((len(G.nodes()), len(G.nodes())))
#     # Fill in the matrix
#     for i, node1 in enumerate(G.nodes()):
#         for j, node2 in enumerate(G.nodes()):
#             # If the nodes are the same, set the matrix element to 0
#             if node1 == node2:
#                 matrix[i][j] = 0
#             else:
#                 # Get the neighbors of the two nodes
#                 neighbors1 = set(G.neighbors(node1))
#                 neighbors2 = set(G.neighbors(node2))
#                 # Get the common neighbors
#                 common = neighbors1.intersection(neighbors2)
#                 # Set the matrix element to the number of common neighbors /
#                 # the number of neighbors of node1. If num_neighbors[node1] = 0
#                 # the set the matrix element to 0
#                 if num_neighbors[node1] == 0:
#                     matrix[i][j] = 0
#                 else:
#                     matrix[i][j] = len(common) / num_neighbors[node1]
#     return matrix

# Create a function which creates a list of all the confirmed interactions.
def confirmed_interactions(G):
    """
    Creates a list of all the confirmed interactions.
    """
    # Create a list of confirmed interactions
    confirmed_interactions = []
    # Iterate through all pairs of nodes
    for node1 in G.nodes():
        for node2 in G.nodes():
            # If there is an edge between the two nodes, add the pair to the list
            if G.has_edge(node1, node2):
                # Add it as a set so that the order of the nodes doesn't matter
                confirmed_interactions.append({ node1, node2 })
    # Remove duplicates and convert the sets back to tuples
    confirmed_interactions = list(set([tuple(sorted(x)) for x in confirmed_interactions]))
    return confirmed_interactions

# Create a function which takes a confirmed interaction and returns the
# fraction of common neighbors between the two nodes.
def fraction_common_neighbors(G, interaction):
    """
    Takes a confirmed interaction and returns the fraction of common  between the two nodes.
    """
    # Get the two nodes in the interaction
    node1, node2 = interaction
    # Get the successors of the two nodes 
    out_neighbors1 = set(G.successors(node1))
    out_neighbors2 = set(G.successors(node2))
    # Get the common successors
    common_out = out_neighbors1.intersection(out_neighbors2)
    # Get the predecessors of the two nodes
    in_neighbors1 = set(G.predecessors(node1))
    in_neighbors2 = set(G.predecessors(node2))
    # Get the common predecessors
    common_in = in_neighbors1.intersection(in_neighbors2)
    # Return the fraction of common neighbors
    return ((len(common_out)/len(out_neighbors1),
            len(common_out)/len(out_neighbors2)),
            (len(common_in)/len(in_neighbors1),
            len(common_in)/len(in_neighbors2)))

# Test fraction_common_neighbors
confirmed_interactions = confirmed_interactions(G)
interaction = random.choice(confirmed_interactions)
print(fraction_common_neighbors(G, interaction))

