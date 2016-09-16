import numpy as np
import numba

@numba.jit(nopython=True)

def testNumba(nopython=True):
    for i in range(0, 100000):
        x = np.random.random(0, 2)
