"""in order to read the optimal path length"""

import math
import numpy as np

# read data from file

# file to experiment with
f = open("TSP-configurations/a280.tsp.txt", "r")
f2 = open("TSP-configurations/a280.opt.tour.txt", "r")
# f = open("TSP-configurations/pcb442.tsp.txt", "r")

# file to perform tests on
# f = open("TSP-configurations/a280.tsp.txt", "r")

network = f.readlines()[6:-1]

# create dictionary to store coordinates
nodes = dict()

# split data and put in dict
for node in network:
    node = list(map(int, (list(filter(None, node.rstrip().rsplit(' '))))))
    nodes[node[0]] = node[1:]


# calculate distance between 2 nodes
def get_distance(dictionary, city1, city2):
    x = dictionary[city1][0] - dictionary[city2][0]
    y = dictionary[city1][1] - dictionary[city2][1]
    return math.sqrt(x ** 2 + y ** 2)


# calculate the total distance
def total_distance(tour, dictionary):
    distance = 0
    for i in range(len(tour) - 1):
        distance += get_distance(dictionary, tour[i], tour[i + 1])

    return distance


network2 = f2.readlines()[5:-1]

# create dictionary to store coordinates
nodes2 = []

# split data and put in dict
for node in network2:
    node = list(map(int, (list(filter(None, node.rstrip().rsplit(' '))))))
    nodes2.append(node[0])

nodes2 = nodes2[:-1]
# print(nodes2[:-1])
print(total_distance(nodes2, nodes))

