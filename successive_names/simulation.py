import numpy as np

SIMULATIONS=100_000_000

N=26
l=4

data = np.random.randint(1, N+1, size=(SIMULATIONS, l))
data.sort(axis=1)

print(np.mean(np.all(np.diff(data, axis=1) == 1, axis=1)))
