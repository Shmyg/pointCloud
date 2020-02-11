# This script finds if a point belongs to an ortho projection (z=0) of a polygon

import numpy as np
import pyny3d.geoms as pyny

## Polygons by their vertices (should be replaced by real vertices
vertices = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 1], [1, 1, 0]])

# Should be replaced with an array of real points
points_to_check = np.array([[1, 1, 1], [5, 5, 5]])
polygon = pyny.Polygon(vertices)

verified_points = polygon.contains(points_to_check)

for index, i in np.ndenumerate(verified_points):
   if (i) :
      print(points_to_check[index]) 
