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
data = pd.read_csv("data/eil51.tsp.tsp-batch-20.txt", sep="\t")
colname = "428.87"
z = list(map(float,list(data[f'{colname}-19'])))

# optimum so far (costs = 428.87175639203394)
# r= [1.0, 32, 11, 38, 5, 37, 17, 4, 18, 47, 12, 46, 51.0, 27, 6, 48, 23, 7, 43, 24, 14, 25, 13, 41, 40, 19, 42, 44, 15, 45, 33, 39, 10, 49, 9, 30, 34, 21, 50, 16, 2, 29, 20, 35, 36, 3, 28, 31, 26, 8, 22, 1.0]

temp = []
# get coordinates of each point
for item in z:
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
ax.set_title(f"Shortest Route: {filename}, costs: {colname}", fontsize=16)
#
plt.savefig("plots/eil51-opt-route-3.png")
plt.show()



