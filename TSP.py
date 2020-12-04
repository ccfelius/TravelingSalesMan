""" TSP SIMULATED ANNEALING """

# Imports
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# read data from file
filename = "eil51.tsp"
f = open(f"TSP-configurations/{filename}.txt", "r")
network = f.readlines()[6:-1]

# create dictionary to store coordinates
nodes = dict()

# split data and put in dict
for node in network:
    node = [int(x) for x in node.rstrip().split(' ')]
    nodes[node[0]] = node[1:]

x = [x[0] for x in nodes.values()]
y = [y[1] for y in nodes.values()]

# load in data of optimal path
data = pd.read_csv("data/eil51.tsp-batch-1.txt", sep="\t")
z = list(map(float,list(data['429-10'])))

# optimum so far
r = [1.0, 32, 11, 38, 5, 49, 10, 39, 33, 45, 15, 37, 17, 44, 42, 19, 40, 41, 13, 25, 14, 18, 4, 47, 12, 46, 51.0, 27, 6, 48, 23, 24, 43, 7, 26, 8, 31, 28, 3, 36, 35, 20, 29, 21, 34, 30, 9, 50, 16, 2, 22, 1.0]

temp = []
# get coordinates of each point
for item in r:
    temp.append(nodes[item])

temp = np.array(temp)
# path = [temp[i:i+2] for i in range(len(temp)-2+1)]
# print(path)

# Plot the nodes and coordinates
fig, ax = plt.subplots()
ax.scatter(x, y, color="deeppink")

for i, txt in enumerate(nodes.keys()):
    ax.annotate(txt, (x[i], y[i]))

ax.plot(*temp.T, color="deeppink", alpha=0.5)
ax.set_title(f"Shortest Route: {filename}, costs: 428.98", fontsize=16)
#
plt.savefig("plots/eil51-opt-route.png")
plt.show()



