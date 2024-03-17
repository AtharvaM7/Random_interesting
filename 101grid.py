import random
import math
import matplotlib.pyplot as plt
import numpy

# We imagine a nxn grid bounded by x = 0, x = n, y = 0, y = n

def throw_darts(n, k):
    """
    This function simulates throwing k darts at the grid and returns the list
    of coordinates of the darts.

    Args:
    n (int): the size of the grid
    k (int): the number of darts to throw

    Returns:
    List of tuples, the coordinates of the darts
    """
    darts = []
    for i in range(k):
        x = random.uniform(0, n)
        y = random.uniform(0, n)
        darts.append((x, y))
    return darts

# Write a function which takes a tuple as input and returns the least of the
# distances of the point from the diagonals.
def measure_distance(p):
    """
    This function takes a tuple as input and returns the least of the distances
    of the point from the diagonals.

    Args:
    p (tuple): the coordinates of the point

    Returns:
    float: the least of the distances of the point from the diagonals
    """
    x, y = p
    # Calculate distance from diagonal 1
    d1 = abs(x - y)/math.sqrt(2)
    # Calculate distance from diagonal 2
    d2 = abs(x + y)/math.sqrt(2)
    return min(d1, d2)

# Write a function which takes a list of tuples as input and returns the least
# distance of the points from the diagonals.
def least_distance(darts):
    """
    This function takes a list of tuples as input and returns the least distance
    of the points from the diagonals.

    Args:
    darts (list): the list of coordinates of the darts

    Returns:
    float: the least distance of the points from the diagonals
    """
    distances = [measure_distance(p) for p in darts]
    return min(distances)

def main():
    observations = []
    for i in range(1000):
        n = 101
        k = 20
        darts = throw_darts(n, k)
        observations.append(least_distance(darts))
   



if __name__ == "__main__":
    main()



