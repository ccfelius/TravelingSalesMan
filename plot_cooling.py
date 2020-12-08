import matplotlib.pyplot as plt
from TravelingSalesMan.cooling_methods import *
import numpy as np

i = np.arange(0, 2000, 1)
print(len(i))
Tmax = 1000
Tmin = 1
factor = 0.99

geo = []
lundy = []
logcooling = []

for j in i:
    if j == 0:
        ltemp = Tmax
        gtemp = Tmax
        logtemp = Tmax

    ltemp = lundy_var(Tmax, Tmin, j, ltemp)
    if ltemp <= 0:
        lundy.append(0)
    else:
        lundy.append(ltemp)
    gtemp = geometric(gtemp, factor)
    if gtemp <= 0:
        geo.append(0)
    else:
        geo.append(gtemp)
    logtemp = cooling(j, logtemp)
    if logtemp <= 0:
        logcooling.append(0)
    else:
        logcooling.append(logtemp)

# Plot the temperature decrease
plt.plot(i, lundy, color="deeppink", label="Lundy & Mees")
plt.plot(i, geo, color="indianred", label="geometric")
plt.plot(i, logcooling, color="springgreen", label="Logarithmic addition")
plt.title(f"Temperature decrease", fontsize=16)
plt.ylabel("Temperature")
plt.xlabel("Iterations")
plt.legend()
plt.savefig("plots/temp-decrease-test.png", dpi=300)
plt.show()