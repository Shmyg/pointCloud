import numpy as np

def calc_plane_bis(x, y, z):
    a = np.column_stack((x, y, z))
    return np.linalg.lstsq(a, np.ones_like(x))[0]

x = np.random.rand(1000)
y = np.random.rand(1000)
z = np.random.rand(1000)
print(calc_plane_bis(x, y, z))
