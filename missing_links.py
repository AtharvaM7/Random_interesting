import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import random	
import numpy as np
from sklearn.linear_model import LinearRegression
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

# Get the adjacency matrix of the graph
adj_matrix = nx.adjacency_matrix(G).todense()

# All the entries in the adjacency matrix that are 0 are practically unknown to
# us if the same entry in the transpose of the adjacency matrix is also 0.
# We can use this information to find the missing links in the network.


def random_entry_picker(adj_matrix):
    """
    This function returns a random entry in the adjacency matrix that is definitely a missing link in the network.
    """
    # Randomly pick an entry in the adjacency matrix
    i = random.randint(0, adj_matrix.shape[0] - 1)
    j = random.randint(0, adj_matrix.shape[1] - 1)
    # If the entry is 0, check the corresponding entry in the transpose
    if adj_matrix[i, j] == 0 and adj_matrix[j, i] == 0:
        return i, j
    else:
        return random_entry_analysis(adj_matrix)

def confirmed_interactions(adj_matrix):
    """
    This function returns the list of confirmed interactions in the network.
    """
    # Return i,j if either aij or aji is 1
    confirmed_interactions = []
    for i in range(adj_matrix.shape[0]):
        for j in range(adj_matrix.shape[1]):
            if adj_matrix[i, j] == 1 or adj_matrix[j, i] == 1:
                confirmed_interactions.append((i, j))
    return confirmed_interactions

def split_train_test(confirmed_interactions, test_size=0.2):
    """
    This function splits the confirmed interactions into training and test sets.
    """
    random.shuffle(confirmed_interactions)
    split_index = math.ceil(len(confirmed_interactions) * (1 - test_size))
    train = confirmed_interactions[:split_index]
    test = confirmed_interactions[split_index:]
    return train, test
   
def check_if_lambda_works(adj_matrix, interaction, lambda_value):
    """
    This function checks if the lambda value works for the given interaction.
    """
    i, j = interaction
    # Create a copy of the adjacency matrix without the ith row.
    adj_matrix_copy = np.delete(adj_matrix, i, axis=0)
    # Get the ith row of the adjacency matrix as an array.
    row = adj_matrix[i]
    # Express the jth column as a linear combination of the other columns.
    X = np.delete(adj_matrix_copy, j, axis=1)
    y = adj_matrix_copy[:, j]
    model = LinearRegression()
    model.fit(X, y)
    # Predict aij using the model.
    prediction = model.predict(row)
    # If the prediction is greater than lambda, return True, else False.
    return prediction > lambda_value


def find_threshold(adj_matrix, confirmed_interactions):
    """
    We remove the one of the confirmed interactions from the adjacency matrix.
    Assume a threshold lambda such that if the value of the entry is greater
    than lambda, then it is 1, otherwise 0. The prediction is made using least
    squares method.

    With every confirmed interaction, we fine tune the value of lambda. Then
    test it on the test set.
    """
    train, test = split_train_test(confirmed_interactions)
    # Set lambda to 0
    lambda_value = 0
    # Iterate through the training set 1000 times
    for i in range(1000):
        for interaction in train:
            if not check_if_lambda_works(adj_matrix, interaction, lambda_value):
                lambda_value += 0.1
    # Test the lambda value on the test set
    # Create a list to store the accuracy of the model
    accuracy = []
    for interaction in test:
        i, j = interaction
        if check_if_lambda_works(adj_matrix, interaction, lambda_value):
            accuracy.append(1)
        else:
            accuracy.append(0)
    # Return the accuracy of the model
    return sum(accuracy) / len(accuracy)

print(find_threshold(adj_matrix, confirmed_interactions(adj_matrix)))




