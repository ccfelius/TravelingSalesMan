""" TSP SIMULATED ANNEALING """
""" Plotting a graph with shortest route """

# Imports
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# read data from file
filename = "a280.tsp"
f = open(f"TSP-configurations/{filename}.txt", "r")
network = f.readlines()[6:-1]

# create dictionary to store coordinates
nodes = dict()

# split data and put in dict
for node in network:
    node = list(map(float, (list(filter(None, node.rstrip().rsplit(' '))))))
    nodes[node[0]] = node[1:]

x = [x[0] for x in nodes.values()]
y = [y[1] for y in nodes.values()]

# load in data of optimal path iff necessary
# data = pd.read_csv(f"data/{filename}-batch-1.txt", sep="\t")
# z = list(map(float,list(data['429-10'])))

# optimum so far (costs = 2600.4), read from file
opt = open(f"data/a280.tsp-batch-mkc10k2.txt", "r")
opt2 = opt.readlines()[1:]
r = [float(x.split('\n')[0]) for x in opt2]

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

ax.plot(*temp.T, color="deeppink", alpha=0.3)
ax.set_title(f"Shortest Route: {filename}, costs: 2600.4", fontsize=16)
#
plt.savefig("plots/a280-optimum.png", dpi=300)
plt.show()