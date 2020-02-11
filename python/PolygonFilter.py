# This script should be used a PDAL filter.python  
# The idea is to check if a point belongs to a projected polygon
# and, in case it is inside the polygon with the specified coordinates,
# it should be marked in any way (at the moment PointSourceId is set
# to some arbitrary value

# Created by Serge Shmygelskyy aka Shmyg

import numpy
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

def apply_filter(ins,outs):

    xCoordinate = ins['X'].astype('float64')
    yCoordinate = ins['Y'].astype('float64')
    
    point = Point([[xCoordinate],[yCoordinate]])
    polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])

    if polygon.contains(point) :
         point_source_id = ins['PointSourceId'] + 66

    outs['PointSourceId'] = point_source_id
	
    return True
