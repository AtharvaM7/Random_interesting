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



