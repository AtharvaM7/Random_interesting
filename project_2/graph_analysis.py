import random
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
file_path = 'modified_impression_network.csv'  # Change to your file path
df = pd.read_csv(file_path)

# Step 2: Create a directed graph
G = nx.DiGraph()

# Step 3: Add edges
for index, row in df.iterrows():
    person = row[0]  # The person who is impressed
    impressed_by = row[1:].dropna()  # The people they are impressed by
    for impressed_person in impressed_by:
        G.add_edge(person, impressed_person)  # Add an edge from person to impressed_person

import random

def pagerank_random_walk(G, d=0.85):
    """
    Finds the pagerank of a graph using random walks with teleportation and returns it as a dictionary.
    """
    # Create a dictionary
    pagerank = {}
    # Set all nodes to have a pagerank of 0
    for node in G.nodes():
        pagerank[node] = 0
    # Pick a random node to start at
    current_node = random.choice(list(G.nodes()))
    # Do n random walks
    n = 10000000
    for i in range(n):
        # Add 1 to the pagerank of the current node
        pagerank[current_node] += 1
        # Decide to either follow a link or teleport
        if random.random() > d:
            # Teleport to a random node
            current_node = random.choice(list(G.nodes()))
        else:
            # Get a list of current node's neighbors
            neighbors = list(G.neighbors(current_node))
            # If the current node has no neighbors, pick a random node to start at
            if len(neighbors) == 0:
                current_node = random.choice(list(G.nodes()))
            # Otherwise, pick a random neighbor to move to
            else:
                current_node = random.choice(neighbors)
    # Normalize the pagerank
    for node in pagerank:
        pagerank[node] /= n
    return pagerank

pagerank = pagerank_random_walk(G)

# Sort the pagerank dictionary by value
sorted_pagerank = dict(sorted(pagerank.items(), key=lambda item: item[1], reverse=True))

# Print the top 10 nodes by pagerank
l1 = []
for i, (node, value) in enumerate(sorted_pagerank.items()):
    l1.append(node)

pagerank = nx.pagerank(G, alpha=0.85)
# Sort and print
l2 = []
sorted_pagerank = dict(sorted(pagerank.items(), key=lambda item: item[1], reverse=True))
for i, (node, value) in enumerate(sorted_pagerank.items()):
    l2.append(node)

print(l1 == l2)


