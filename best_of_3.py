# Imports
import copy as cp
import pandas as pd
from TravelingSalesMan.cooling_methods import *
from TravelingSalesMan.sampling_methods import *
import matplotlib.pyplot as plt

# begin met best guess (2600.4?) And start with initial guess, at lower temperature etc. Maybe also do iggy's thing as it seems to perform good.

""" TSP SIMULATED ANNEALING """
""" Hybrid Sampling and L&M Cooling Scheme"""

# read data from file
# uncomment the file you'd like to work with

# f = open("TSP-configurations/eil51.tsp.txt", "r")
f = open("TSP-configurations/a280.tsp.txt", "r")
# f = open("TSP-configurations/pcb442.tsp.txt", "r")

network = f.readlines()[6:-1]

# create dictionary to store coordinates
nodes = dict()

# split data and put in dict
for node in network:
    node = list(map(float, (list(filter(None, node.rstrip().rsplit(' '))))))
    nodes[node[0]] = node[1:]


good = pd.read_csv("data/a280.tsp-batch-mkc10k2.txt")
print(good['2600.4-0'])


def SA(coordinates, tour, Tmax, Tmin, coolingdown, outer, mlength, best_guess=False, start_end=True):
    """

    :param coordinates: Dictionary. Dict with nodes as keys, coordinates as values
    :param tour: List. initial path.
    :param Tmax: Int. Maximum Temperature
    :param Tmin: Int. Maximum Temperature
    :param coolingdown: Func. Cooling down method
    :param outer: Int. # Iterations in outer loop
    :param mlength: Int. Markov Chain length
    :param best_guess: List. Best guess as start.
    :param start_end: Bool. Indicate whether start and end node are fixed
    :return: List, Float. Optimal path, Optimal path length respectively
    """

    # initial temp is Tmax
    temp = Tmax
    templist = []

    # set begin and end node (city)

    if not best_guess:
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
    total_costs = cp.deepcopy(costs)
    shortest_route = []

    for i in range(outer):  # Parameter

        print(i, 'cost=', costs, temp)

        temp = coolingdown(Tmax, Tmin, i, temp)
        templist.append(temp)

        for j in range(mlength):  # Parameter

            ## Hybrid Approach
            ## Take best value of swap, insert or invert

            ## SWAP
            stour = swap(tour)
            scosts = total_distance(stour, coordinates)

            # Insert
            instour = insert(tour)
            inscosts = total_distance(instour, coordinates)

            # Invert
            itour = invert(tour)
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
                p0 = math.exp(-(cost_n - costs) / temp)
                if x < min(1, p0):
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

    return shortest_route, total_costs, templist


# Most optimal parameters found so far for eil51.tsp
# Tmax = 400  # Parameter
# Tmin = 5
# outer = 1000
# MCL = 1000  # Markov Chain Length (inner loop)

# random params, test
# Tmax = 100  # Parameter
# Tmin = 1
# outer = 1000
# MCL = 1000  # Markov Chain Length (inner loop)

# Most optimal parameters found so far for a280.tsp
Tmax = 1.5 # Parameter #1000
Tmin = 1 # 1
outer = 1000
MCL = 1000  # Markov Chain Length (inner loop)

# Get node names
bestguess = pd.read_csv("data/a280.tsp-batch-mkc10k2.txt")
# print(good['2600.4-0'])
initial_tour = list(bestguess['2600.4-0'])
# initial_tour = [i for i in nodes.keys()]
# print(initial_tour)
# # #
# ans = SA(nodes, initial_tour, Tmax, Tmin, lundy_var(), outer, MCL)


def simulate(i, save="a280", batch="1"):
    data = pd.DataFrame()

    for j in range(i):
        print(f"Simulation {j+1}")
        sim = SA(nodes, initial_tour, Tmax, Tmin, lundy_var, outer, MCL, best_guess=True)
        print(sim[0], sim[1])
        tlist = sim[2]
        colname = str(round(sim[1], 2)) + "-" + str(j)
        plt.plot([i for i in range(outer)], tlist, color='deeppink')
        plt.title("Temperature decreasing per iteration")
        plt.xlabel("Iteration")
        plt.ylabel("Temperature")
        plt.savefig(f"plots/lundy_plot-1-{j}")
        data[colname] = sim[0]

    data.to_csv(f'data/{save}.tsp-batch-{batch}.txt', sep='\t', index=False)

    return data
#
print(simulate(1, save="a280", batch="bestguess"))



