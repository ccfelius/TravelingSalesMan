""" TSP SIMULATED ANNEALING """

# Imports
import numpy as np
import matplotlib.pyplot as plt


# read data from file
f = open("TSP-configurations/eil51.tsp.txt", "r")
network = f.readlines()[6:-1]

# create dictionary to store coordinates
nodes = dict()

# split data and put in dict
for node in network:
    node = [int(x) for x in node.rstrip().split(' ')]
    nodes[node[0]] = node[1:]

x = [x[0] for x in nodes.values()]
y = [y[1] for y in nodes.values()]

# Plot the nodes and coordinates
fig, ax = plt.subplots()
ax.scatter(x, y)

for i, txt in enumerate(nodes.keys()):
    ax.annotate(txt, (x[i], y[i]))

plt.savefig("plots/example.png")
plt.show()



