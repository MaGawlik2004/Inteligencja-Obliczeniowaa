import numpy as np
import pyswarms as ps
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt


def endurance(X):
    x = X[:, 0]
    y = X[:, 1]
    z = X[:, 2]
    u = X[:, 3]
    v = X[:, 4]
    w = X[:, 5]
    return -(np.exp(-2 * (y - np.sin(x))**2) + np.sin(z * u) + np.cos(v * w))

options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
dimension = 6

x_min = np.zeros(dimension)
x_max = np.ones(dimension)
bounds = (x_min, x_max)

optimizer = ps.single.GlobalBestPSO(
    n_particles=20,
    dimensions=dimension,
    options=options,
    bounds=bounds
)

cost, pos = optimizer.optimize(endurance, iters=1000)

print("Najlepszy wynik endurance:", -cost)
print("Najlepsze proporcje metali:", pos)

plot_cost_history(optimizer.cost_history)
plt.title("Historia kosztu (endurance)")
plt.xlabel("Iteracje")
plt.ylabel("Koszt (ujemna wytrzymałość)")
plt.grid()
plt.show()