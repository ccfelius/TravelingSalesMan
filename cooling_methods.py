import numpy as np
import math


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

def geometric(factor, temp):
    return temp * factor

def lundy(Tmax, Tmin, it, temp):
    """
    Lundy and Mees (L & M) Cooling method
    :param Tmax: int. Maximum temperature
    :param Tmin: int. Minimum temperature
    :param it: int. Current iteration
    :param temp: float. Current temperature
    :return: float. New temperature
    """
    it = it + 2
    beta = (Tmax - Tmin)/((it-1)*Tmax*Tmin)
    return temp * (1/(1 + beta*temp))

def cooling(it, outer, temp):
    """
    Cooling down function

    :param temp: (float) temperature
    :return: (float) new temperature
    """
    return temp - temp * np.log(it + 1)

def cooling_cos(it, outer,  temp):
    """
    Cooling down function

    :param temp: (float) temperature
    :return: (float) new temperature
    """

    # der = temp - it/outer*temp
    return temp*(1+(((it+1)/outer)*np.cos(it)))