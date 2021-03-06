import pandas as pd
import math
import scipy.stats as st
import numpy as np

def conf_int(mean, var, n, p=0.95):
    """
    Calculate a confidence interval
    :param mean: mean of simulations
    :param var: variance of simulations
    :param n: amount of simulations
    :param p: certainty percentage
    :return:
    """
    pnew = (p+1)/2
    zval = st.norm.ppf(pnew)
    sigma = math.sqrt(var)
    alambda = (zval*sigma)/math.sqrt(n)
    min_lambda = mean - alambda
    plus_lambda = mean + alambda
    return f"Confidence interval: [{min_lambda:.4f} < X < {plus_lambda:.4f}] with p = {p}"

# batchlist = ["1100", "1400", "11000", "12000", "-1749", "-1999"]
batchlist = ["mkc10005000"]
mcklist = ["mkc100-2", "11000", "mkc1000", "mkc10000"]

# 1999 is 500 temp
# 1749 is 250 temp

# for batch in batchlist:
    # file = pd.read_csv(f'data/a280.tsp-batch-{batch}.txt', sep='\t')
    # m = [float(x.split("-")[0]) for x in file.columns]
    # mean = np.mean(m)
    # var = np.var(m)
    # n = len(m)
    # print(f'Batch: a280.tsp-batch-{batch}')
    # print(f'Average: {mean}, Stdev: {np.std(m)}')
    # print(conf_int(mean, var, n))
    # print()

file = pd.read_csv(f'data/a280_lun_MKC.tsp-batch-3000.txt', sep='\t')
m = [float(x.split("-")[0]) for x in file.columns]
mean = np.mean(m)
var = np.var(m)
n = len(m)
print(f'Batch: a280.tsp-batch-3000')
print(f'Average: {mean}, Stdev: {np.std(m)}')
print(conf_int(mean, var, n))
print()
