""" TSP SIMULATED ANNEALING """

# Imports
import math
import numpy as np

# read data from file
f = open("TSP-configurations/eil51.tsp.txt", "r")
# f = open("TSP-configurations/a280.tsp.txt", "r")
# f = open("TSP-configurations/pcb442.tsp.txt", "r")

network = f.readlines()[6:-1]

# create dictionary to store coordinates
nodes = dict()

# split data and put in dict
for node in network:
    node = list(map(int, (list(filter(None, node.rstrip().rsplit(' '))))))
    nodes[node[0]] = node[1:]

# calculate distance between 2 nodes
def initial_distance(dictionary, city1, city2):
    x = dictionary[city1][0] - dictionary[city2][0]
    y = dictionary[city1][1] - dictionary[city2][1]
    return math.sqrt(x**2 + y**2)

def get_distance(dictionary, city1, city2):
    x = dictionary[city1][0][0] - dictionary[city2][0][0]
    y = dictionary[city1][0][1] - dictionary[city2][0][1]
    return math.sqrt(x**2 + y**2)

# calculate the total distance
def total_distance(tour, dictionary):

    distance = 0
    for i in range(len(tour)-1):
        distance += get_distance(dictionary, tour[i], tour[i+1])

    return distance


# add nearest neighbors in order of nearest to most far
for node in range(1,len(nodes)+1):
    t_dict = dict()
    tour = [i for i in nodes.keys()]
    tour.remove(node)

    for j in tour:
        t_dict[j] = initial_distance(nodes, node, j)

    nodes[node].append(sorted(t_dict.items(), key=lambda x: x[1]))

print(nodes)



def SA(coordinates, tour, temp, coolingdown, mlength, start_node=True):

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

        temp = coolingdown(temp)
        if temp == 0:
            print("Temperature of 0 reached")
            return tour, costs

        for j in range(mlength): # Parameter

            # Exchange two coordinates and get a candidate solution solution
            c1, c2 = np.random.randint(1, len(tour)-1, size = 2)

            # Swap coordinates
            tour[c1], tour[c2] = tour[c2], tour[c1]

            # get the new costs
            cost_n = total_distance(tour, coordinates)

            # replace old costs if new costs is less
            if cost_n < costs:
                costs = cost_n
            else:
                # Generate random probability
                x = np.random.uniform()

                # If prob < formula accept candidate solution
                if x < min(1, math.exp(-(cost_n-costs)/temp)):
                    costs = cost_n
                else:
                    # Swap back to prior solution
                    tour[c1], tour[c2] = tour[c2], tour[c1]

    return tour, costs, temp

def candidate_solution():
    return

def cooling(temp):
    """
    Cooling down function

    :param temp: (float) temperature
    :return: (float) new temperature
    """
    return temp - np.log(temp)

Temperature = 1000 # Parameter
MCL = 500 # Markov Chain Length (inner loop)
# Get node names
initial_tour = [i for i in nodes.keys()]

# print(SA(nodes, initial_tour, Temperature, cooling, MCL))