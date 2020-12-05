import numpy as np
import copy as cp
import math


def get_distance(dictionary, city1, city2):
    """
    Calculate distance between 2 nodes
    :param dictionary: Dictionary. Dict with node names as keys, coordinates as values
    :param city1: int. Name of city
    :param city2: int. Name of city
    :return: float. Distance from one node to another.
    """
    x = dictionary[city1][0] - dictionary[city2][0]
    y = dictionary[city1][1] - dictionary[city2][1]
    return math.sqrt(x ** 2 + y ** 2)


# calculate the total distance
def total_distance(tour, dictionary):
    """
    Calculate total distance of path
    :param tour: list. Current path
    :param dictionary: Dictionary. Dict with node names as keys, coordinates as value
    :return: float. Current length of path
    """
    distance = 0
    for i in range(len(tour) - 1):
        distance += get_distance(dictionary, tour[i], tour[i + 1])

    return distance

def swap(tour):
    """
    Exchange two coordinates and get a candidate solution solution
    :param tour: list. List with current path
    :return: list. List with new path
    """
    c1, c2 = np.random.randint(1, len(tour) - 1, size=2)
    # Swap coordinates, make deepcopy of list
    stour = cp.deepcopy(tour)
    stour[c1], stour[c2] = stour[c2], stour[c1]
    return stour


# inserting
def insert(tour):
    """
    Randomly insert node in random place of path
    :param tour: list. List with current path
    :return: list. List with new path
    """
    randindex = np.random.randint(1, len(tour) - 2)
    randcity = np.random.randint(2, len(tour) - 1)
    instour = cp.deepcopy(tour)
    instour.remove(randcity)
    instour.insert(randindex, randcity)
    return instour


# invert
def invert(tour):
    """
    Invert part of path
    :param tour: list. List with current path
    :return: list. List with new path
    """
    c1, c2 = np.random.randint(1, len(tour) - 1, size=2)
    if c2 < c1:
        a = c2
        b = c1
    else:
        a = c1
        b = c2

    itour = cp.deepcopy(tour)
    itour = itour[:a] + itour[b:a - 1:-1] + itour[b + 1:]
    return itour

def calc_nn(nodes):
    """
    Calculate Euclidean distance to all other nodes in path
    :param nodes:  Dictionary. Dict with node names as keys, coordinates as values
    :return: Dictionary. Dict containing coords and an individual dict for each node,
    containing distances to other neighbor sorted in ascending order.
    """
    for node in range(1, len(nodes) + 1):
        t_dict = dict()
        tour = [i for i in nodes.keys()]
        tour.remove(node)

        for j in tour:
            t_dict[j] = get_distance(nodes, node, j)

        nodes[node].append(sorted(t_dict.items(), key=lambda x: x[1]))

    return nodes
