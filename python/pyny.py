import numpy as np
import pyny3d.geoms as pyny
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from mpl_toolkits.mplot3d import Axes3D

## Polygons by their vertices
vertices = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 1], [1, 1, 0]])
print (vertices)

points_to_check = np.array([[1, 1, 1]])
polygon = pyny.Polygon(vertices)


x=polygon.get_plotable3d()
print(polygon.get_area())

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.add_collection3d(x)

#plt.show()
