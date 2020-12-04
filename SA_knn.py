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


# add nearest neighbors in order of nearest to most far
for node in range(1, len(nodes) + 1):
    t_dict = dict()
    tour_ = [i for i in nodes.keys()]
    tour_.remove(node)


    for j in tour_:

        # because we want to keep 1 here
        if j != 1:
            t_dict[j] = get_distance(nodes, node, j)

    # add sorted dict to values of nodes dictionary
    nodes[node].append(sorted(t_dict.items(), key=lambda x: x[1]))


def SA(coordinates, tour, temp, coolingdown, outer, mlength, knn, start_end=True):

    if start_end == True:
        a, c = [tour[0]], [tour[0]]
        b = tour[1:]
        np.random.shuffle(b)
        tour = a + b + c
    else:
        np.random.shuffle(tour)

    print(f'\nInitial solution: {tour}\n')

    # Initial costs
    costs = total_distance(tour, coordinates)

    for i in range(outer):  # Parameter
        print(i, 'cost=', costs)

        temp = coolingdown(temp)
        if temp == 0:
            print("Temperature of 0 reached")
            return tour, costs

        knn = max(knn, round((i/outer * (len(tour)-3))))
        # print(f'new knn {knn}')

        for j in range(mlength):  # Parameter

            # Exchange two coordinates and get a candidate solution
            # c1 represents an index
            c1 = np.random.randint(1, len(tour) - 2)

            # get 1 of the nearest neighbors
            # knn increases as the iterations decrease (to get out of loc minima)
            
            # c2 represents an actual city if replaced
            c2 = coordinates[c1][2][np.random.randint(0, knn)][0]

            # c2 represents an index if swapped, in that case use:
            # c2 = coordinates[c1][2][np.random.randint(0, knn)][0] - 1


            # Insert on c1 instead of swap
            c2_i = tour.index(c2)
            tour.remove(c2)
            # print(f'city {c2} removed out of index {c2_i}')
            tour.insert(c1, c2)
            # print(f'city {c2} inserted in index {c1}')

            # tour[c1], tour[c2] = tour[c2], tour[c1]


            # get the new costs
            cost_n = total_distance(tour, coordinates)

            # replace old costs if new costs is less
            if cost_n < costs:
                costs = cost_n
            else:
                # Generate random probability
                x = np.random.uniform()

                # If prob < formula accept candidate solution
                if x < min(1, math.exp(-(cost_n - costs) / temp)):
                    costs = cost_n
                else:
                    # Insert/Swap back to prior solution
                    tour.remove(c2)
                    # print(f'city {c2} removed out of index {c2_i}')
                    tour.insert(c2_i, c2)
                    # print(f'city {c2}inserted in index {c2_i}')
                    # tour[c1], tour[c2] = tour[c2], tour[c1]

    return tour, costs, temp


def candidate_solution():
    return


def cooling(temp):
    """
    Cooling down function

    :param temp: (float) temperature
    :return: (float) new temperature
    """
    return temp * 0.99


Temperature = 500  # Parameter
outer = 1000
MCL = 500  # Markov Chain Length (inner loop)
# Get node names
initial_tour = [i for i in nodes.keys()]
# print(initial_tour)
#
print(SA(nodes, initial_tour, Temperature, cooling, outer, MCL, 3))