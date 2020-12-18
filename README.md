## Traveling Salesman Problem

Amber den Hollander (10910441), Lotte Felius (12368032). <br>
Course: Stochastic Simulation @ University of Amsterdam.<br><br>

#### Required Packages:
- numpy<br>
- scipy.stats<br>
- math<br>
- pandas<br>
- matplotlib

#### Instructions:
Clone everything on your local machine. Make sure all required packages are installed and everything is in the right place. If that is the case, you can directly run best_of_3.py if you want to simulate.<br>

#### Directories
- <b>TSP-configurations and TSP</b><br>
These directories contain information about TSP problems of different sizes, and contains data from the TSP problem we aim to solve (a280.tsp).
- <b>data</b><br>
This is the folder that contains all simulated data used in our report<br>
- <b>plots</b><br>
In this folder all plots for the assignments are stated<br>

#### Python files
- <b> best_of_3.py</b><br>
This file is used for the simulations, it makes use of hybrid sampling and is therefore called 'best of 3'. If you want to run simulations you should run this file.<br>
- <b> cooling_methods.py</b><br>
In this file different cooling methods are implemented. This is file is required for running best_of_3.py <br>
- <b> sampling_methods.py</b><br>
In this file different sampling methods (swap, insert and invert) as well as the methods to calculate the total distances are implemented. This is file is required for running best_of_3.py <br>
- <b> statistics.py</b><br>
This file reads simulated data from the data folder. It subsequently prints the mean, standard deviation and confidence interval of simulations. In order to derive statistics from different batches of simulations, one should change the filename(s) in the script.<br>
- <b>read.py</b><br>
This file reads the data from the given optimal path and calculates its corresponding.
- <b>plot_cooling.py</b><br>
In this file the plot for cooling schemes and decreasing temperature is generated. <br>
- <b> SA.py and SA_knn.py</b><br>
These files can be experimented with if one wants to sample from its K-nearest-neighbor. However, for the assignments, we did not ended up using these files and therefore they can be neglected. <br>
- <b> TSP.py and TSP_a280.py</b><br>
Both these files are used to plot the graph that shows how the optimal paths are visualized
