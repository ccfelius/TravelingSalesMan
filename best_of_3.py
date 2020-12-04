""" TSP SIMULATED ANNEALING """

# Imports
import math
import numpy as np
import copy as cp
import pandas as pd
from TravelingSalesMan.cooling_methods import *

# read data from file
f = open("TSP-configurations/eil51.tsp.txt", "r")
# f = open("TSP-configurations/a280.tsp.txt", "r")
# f = open("TSP-configurations/pcb442.tsp.txt", "r")

network = f.readlines()[6:-1]

# create dictionary to store coordinates
nodes = dict()

# split data and put in dict
for node in network:
    node = list(map(float, (list(filter(None, node.rstrip().rsplit(' '))))))
    nodes[node[0]] = node[1:]


# add nearest neighbors in order of nearest to most far
for node in range(1, len(nodes) + 1):
    t_dict = dict()
    tour = [i for i in nodes.keys()]
    tour.remove(node)

    for j in tour:
        t_dict[j] = get_distance(nodes, node, j)

    nodes[node].append(sorted(t_dict.items(), key=lambda x: x[1]))

print(nodes)


def SA(coordinates, tour, temp, coolingdown, outer, mlength, method="bo3", start_node=True):

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
    total_costs = cp.deepcopy(costs)
    shortest_route = []

    for i in range(outer):  # Parameter

        print(i, 'cost=', costs)

        temp = coolingdown(i, outer, temp)
        if temp == 0:
            print("Temperature of 0 reached")
            return tour, costs

        for j in range(mlength):  # Parameter

            ## Take best value of swap, insert or invert

            ## SWAP
            # Exchange two coordinates and get a candidate solution solution
            c1, c2 = np.random.randint(1, len(tour) - 1, size=2)
            # Swap coordinates, make deepcopy of list
            stour = cp.deepcopy(tour)
            stour[c1], stour[c2] = stour[c2], stour[c1]
            scosts = total_distance(stour, coordinates)

            # inserting
            randindex = np.random.randint(1, len(tour) - 2)
            randcity = np.random.randint(2, len(tour) - 1)
            instour = cp.deepcopy(tour)
            instour.remove(randcity)
            instour.insert(randindex, randcity)
            inscosts = total_distance(instour, coordinates)

            # invert
            c1, c2 = np.random.randint(1, len(tour) - 1, size=2)
            if c2 < c1:
                a = c2
                b = c1
            else:
                a = c1
                b = c2

            itour = cp.deepcopy(tour)
            itour = itour[:a] + itour[b:a - 1:-1] + itour[b + 1:]
            icosts = total_distance(itour, coordinates)

            # put all calculated costs in list
            opts = [scosts, inscosts, icosts]
            # get the new costs by taking minimum
            cost_n = min(opts)
            cost_ind = opts.index(cost_n)


            # replace old costs if new costs is less
            if cost_n < costs:
                costs = cost_n
                if cost_ind == 0:
                    tour = stour
                elif cost_ind == 1:
                    tour = instour
                else:
                    tour = itour

            else:
                # Generate random probability
                x = np.random.uniform()
                # If prob < formula accept candidate solution
                if x < min(1, math.exp(-(cost_n - costs) / temp)):
                    costs = cost_n
                    if cost_ind == 0:
                        tour = stour
                    elif cost_ind == 1:
                        tour = instour
                    else:
                        tour = itour

        if costs < total_costs:
            total_costs = costs
            shortest_route = tour

    return shortest_route, total_costs, temp


Temperature = 500  # Parameter
MCL = 1000  # Markov Chain Length (inner loop)
outer = 250
# Get node names
initial_tour = [i for i in nodes.keys()]

def simulate(i, save="eil51", batch="1"):
    data = pd.DataFrame()

    for j in range(i):
        sim = SA(nodes, initial_tour, Temperature, cooling_cos, outer, MCL)
        print(sim)
        colname = str(round(sim[1])) + "-" + str(i)
        data[colname] = sim[0]

    data.to_csv(f'data/{save}.tsp-batch-{batch}.txt', sep='\t', index=False)

    return data

print(simulate(10))



