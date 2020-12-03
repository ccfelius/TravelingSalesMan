""" TSP SIMULATED ANNEALING """

# Imports
import math
import numpy as np

# read data from file
f = open("TSP-configurations/eil51.tsp.txt", "r")
network = f.readlines()[6:-1]

# create dictionary to store coordinates
nodes = dict()

# split data and put in dict
for node in network:
    node = [int(x) for x in node.rstrip().split(' ')]
    nodes[node[0]] = node[1:]


# calculate distance between 2 nodes
def get_distance(dictionary, city1, city2):
    x = dictionary[city1][0] - dictionary[city2][0]
    y = dictionary[city1][1] - dictionary[city2][1]
    return math.sqrt(x**2 + y**2)


# calculate the total distance
def total_distance(tour, dictionary):

    distance = 0
    for i in range(len(tour)-1):
        distance += get_distance(dictionary, tour[i], tour[i+1])

    return distance


def SA(coordinates, tour, temp, factor, mlength, start_node=True):

    if start_node == True:
        a, c = [tour[0]], [tour[0]]
        b = tour[1:]
        np.random.shuffle(b)
        tour = a + b + c
    else:
        np.random.shuffle(tour)

    print(f'\nInitial solution: {tour}\n')
    
    # Initial costs
    costs = total_distance(tour, coordinates)

    for i in range(1000): # Parameter
        print(i, 'cost=', costs)

        temp = temp*factor
        for j in range(mlength): # Parameter

            # Exchange two coordinates and get a candidate solution solution
            c1, c2 = np.random.randint(1, len(tour)-1, size = 2)

            # Swap coordinates
            tour[c1], tour[c2] = tour[c2], tour[c1]

            # get the new costs
            cost_n = total_distance(tour, coordinates)

            if cost_n < costs:
                costs = cost_n
            else:
                # generate random probability
                x = np.random.uniform()

                # if prob < formula
                if x < math.exp((costs-cost_n)/temp):
                    costs = cost_n
                else:
                    # Swap coordinates
                    tour[c1], tour[c2] = tour[c2], tour[c1]

    return tour, costs


Temperature = 1000 # Parameter
factor = 0.99 # Parameter
MCL = 500 # Markov Chain Length (inner loop)

# Get node names
initial_tour = [i for i in nodes.keys()]

print(SA(nodes, initial_tour, Temperature, factor, MCL))