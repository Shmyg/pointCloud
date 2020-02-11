import numpy as np

def calc_plane(x, y, z):
    a = np.column_stack((x, y, np.ones_like(x)))
    return np.linalg.lstsq(a, z)[0]

>>> x = np.random.rand(1000)
>>> y = np.random.rand(1000)
>>> z = 4*x + 5*y + 7 + np.random.rand(1000)*.1
>>> calc_plane(x, y, z)
array([ 3.99795126,  5.00233364,  7.05007326])
