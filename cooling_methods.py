import numpy as np
import math


def geometric(factor, temp):
    return temp * factor

def lundy2(Tmax, Tmin, it, temp):
    """
    Lundy and Mees (L & M) Cooling method
    :param Tmax: int. Maximum temperature
    :param Tmin: int. Minimum temperature
    :param it: int. Total iterations (markov chain length)
    :param temp: float. Current temperature
    :return: float. New temperature
    """
    beta = (Tmax - Tmin)/((it-1)*Tmax*Tmin)
    return temp * (1/(1 + beta*temp))

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

def lundy_var(Tmax, Tmin, it, temp):
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
    return (temp * (1/(1 + beta)))

def cooling(it, temp):
    """
    Cooling down function

    :param temp: (float) temperature
    :return: (float) new temperature
    """
    return temp - np.log(it + 2)

def cooling_cos(it, outer,  temp):
    """
    Cooling down function

    :param temp: (float) temperature
    :return: (float) new temperature
    """

    # der = temp - it/outer*temp
    return temp*(1+(((it+1)/outer)*np.cos(it)))