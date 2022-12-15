import numpy as np
from optimalf import *

my_trades = np.array([100, -50, 20, 87, -55])
print(my_trades)
fs = np.linspace(0.1, 1, 10)
for f in fs:
    g = geometric_mean(f, my_trades)
    print(f"{f:.0%}\t{g:.3}")

print(optimalf(my_trades))
