import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import random	
import numpy as np
from sklearn.linear_model import LinearRegression
import math

# read the file
file_path = 'modified_impression_network.csv'
df = pd.read_csv(file_path)

# create a directed graph
G = nx.DiGraph()

# adding directed edges
for index, row in df.iterrows():
    person = row[0]  # The person who is impressed
    impressed_by = row[1:].dropna()  # The people they are impressed by
    for impressed_person in impressed_by:
        G.add_edge(person, impressed_person)  # Add an edge from person to impressed_person

# get the adjacency matrix of the graph
adj_matrix = nx.adjacency_matrix(G).todense()

# Modify the adjacency matrix on the basis of percentage of common successors
def common_successors_of_interaction(i, j, adj_matrix, G):
    """
    This function returns the number of common successors of i and j in the graph G.
    """
    # Get the node corresponding to the index i in the adjacency matrix
    i = list(G.nodes())[i]
    # Get the node corresponding to the index j in the adjacency matrix
    j = list(G.nodes())[j]
    i_successors = set(G.successors(i))
    j_successors = set(G.successors(j))
    if len(i_successors) == 0:
        return 0
    else:
        return len(i_successors.intersection(j_successors)) / len(i_successors)

def feature_matrix(G, adj_matrix):
    """
    This function returns the feature matrix of the graph G.
    """
    n = len(G.nodes())
    feature_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            feature_matrix[i, j] = common_successors_of_interaction(i, j, adj_matrix, G)
    return feature_matrix
feature_matrix = feature_matrix(G, adj_matrix)

# all the entries in the adjacency matrix that are 0 are practically unknown to
# us if the same entry in the transpose of the adjacency matrix is also 0.
# we can use this information to find the missing links in the network.


def random_entry_picker(adj_matrix):
    """
    this function returns a random entry in the adjacency matrix that is definitely a missing link in the network.
    """
    # randomly pick an entry in the adjacency matrix
    i = random.randint(0, adj_matrix.shape[0] - 1)
    j = random.randint(0, adj_matrix.shape[1] - 1)
    # if the entry is 0, check the corresponding entry in the transpose
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
    # Delete the ith row and jth column from the adjacency matrix
    A = np.delete(np.delete(feature_matrix, i, 0), j, 1)
    # Make A as a float matrix
    A = A.astype(float)
    # Add small random noise to the matrix to make it invertible
    A += np.random.normal(0, 0.01, A.shape)
    # Get the ith row and delete the jth element
    y = np.delete(feature_matrix[i], j)
    # Get the jth column and delete the ith element
    b = np.delete(feature_matrix[:, j], i)
    # Now we get the linear combination coefficients using the least squares
    # method using numpy
    x = np.linalg.inv((A.T @ A )) @ A.T @ b
    # Predicted value is the dot product of the ith row and coefficients
    predicted_value = y @ x
    # If the predicted value is greater than lambda, then the entry is 1
    predicted_result = 0
    if predicted_value > lambda_value:
        predicted_result = 1
    # Compare predicted result with the actual entry
    if adj_matrix[i, j] == predicted_result:
        return True
    else:
        return False



def find_threshold(adj_matrix, feature_matrix, confirmed_interactions):
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
    lambda_value = -3
    # Iterate through the training set 1000 times
    train_accuracy = []
    corresponding_lambda = []
    # Run a while loop until the training accuracy is 60%
    for i in range(120):
        # Create a list to store the accuracy of the model
        accuracy = []
        for interaction in train:
            i, j = interaction
            if check_if_lambda_works(feature_matrix, interaction, lambda_value):
                accuracy.append(1)
            else:
                accuracy.append(0)
        # Calculate the accuracy of the model
        train_accuracy.append(sum(accuracy) / len(accuracy))
        corresponding_lambda.append(lambda_value)
        # Increment the lambda value
        lambda_value += 0.05 
        print(lambda_value, max(train_accuracy))
    # Get the lambda value with the highest accuracy
    lambda_value = corresponding_lambda[train_accuracy.index(max(train_accuracy))]
    # Test the lambda value on the test set
    # Create a list to store the accuracy of the model
    accuracy = []
    for interaction in test:
        i, j = interaction
        if check_if_lambda_works(feature_matrix, interaction, lambda_value):
            accuracy.append(1)
        else:
            accuracy.append(0)
    # Return the accuracy of the model
    return sum(accuracy) / len(accuracy), lambda_value

accuracy, lambda_value = find_threshold(adj_matrix, feature_matrix, confirmed_interactions(feature_matrix))
print("Accuracy: ", accuracy)
print("Lambda value: ", lambda_value)

