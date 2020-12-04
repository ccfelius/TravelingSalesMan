""" TSP SIMULATED ANNEALING """

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

# optimum so far (costs = 2866.7391789280546)
r= [1.0, 280.0, 2, 242, 243, 241, 244, 245, 240, 239, 238, 231, 246, 251, 250, 247, 248, 249, 256, 255, 254, 253, 252, 230, 229, 232, 237, 236, 235, 234, 233, 228, 227, 226, 225, 224, 223, 219, 222, 221, 220, 217, 218, 215, 216, 213, 214, 211, 212, 210, 209, 208, 207, 206, 205, 204, 203, 202, 200, 201, 196, 195, 194, 192, 191, 193, 197, 198, 199, 145, 144, 143, 146, 147, 142, 141, 148, 149, 139, 140, 265, 266, 138, 137, 267, 268, 136, 135, 269, 270, 134, 133, 132, 19, 20, 131, 130, 21, 128, 129, 154, 155, 153, 156, 122, 121, 120, 119, 157, 158, 159, 160, 174, 163, 162, 161, 175, 176, 177, 151, 152, 178, 150, 179, 180, 181, 182, 183, 184, 185, 187, 186, 190, 189, 188, 164, 165, 166, 167, 168, 171, 172, 170, 169, 101, 100, 99, 92, 102, 103, 105, 106, 173, 107, 108, 104, 91, 90, 109, 89, 88, 112, 110, 111, 114, 115, 117, 116, 113, 87, 86, 85, 84, 83, 82, 81, 79, 80, 94, 93, 98, 97, 96, 95, 78, 77, 75, 76, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 118, 61, 60, 59, 58, 57, 44, 43, 42, 41, 40, 46, 45, 56, 55, 54, 47, 48, 53, 52, 51, 50, 49, 37, 38, 39, 35, 36, 34, 33, 32, 31, 30, 125, 124, 123, 126, 127, 29, 28, 27, 26, 22, 25, 23, 24, 18, 17, 16, 271, 272, 15, 14, 13, 12, 11, 10, 8, 7, 9, 276, 275, 274, 273, 261, 262, 263, 264, 257, 258, 259, 260, 278, 279, 3, 4, 277, 6, 5.0, 1.0]
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

# for i, txt in enumerate(nodes.keys()):
#     ax.annotate(txt, (x[i], y[i]))

ax.plot(*temp.T, color="deeppink", alpha=0.5)
ax.set_title(f"Shortest Route: {filename}, costs: 2866.73", fontsize=16)
#
plt.savefig("plots/a280-test2.png", dpi=300)
plt.show()