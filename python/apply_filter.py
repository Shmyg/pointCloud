# This script should be used a PDAL filter.python  
# The idea is to check each and every point in a .las file
# and, in case it is inside a cuboid with the specified coordinates,
# it should be marked in any way (at the moment PointSourceId is set
# to some arbitrary value
# The logics is built on the vector geometry, description can be found here:
# https://math.stackexchange.com/questions/1472049/check-if-a-point-is-inside-a-rectangular-shaped-area-3d
# and here:
# https://stackoverflow.com/questions/59828533/python-code-to-check-if-a-point-is-inside-or-outside-a-cuboid
#
# Should be used a function for PDAL filter.python:
# pdal pipeline $PROJECT_DIR/json/pipeline_filter.json

# Created by Serge Shmygelskyy aka Shmyg

import numpy

def apply_filter(ins,outs):

    vertex_1 = [-10,-10,-10]
    vertex_2 = [-10, -10, 10]
    vertex_3 = [-10, 10, -10]
    vertex_4 = [10, -10, -10]

    vector_1 = numpy.subtract(vertex_1, vertex_2)
    vector_2 = numpy.subtract(vertex_1, vertex_3)
    vector_3 = numpy.subtract(vertex_1, vertex_4)
    
    xCoordinate = ins['X'].astype('float64')
    yCoordinate = ins['Y'].astype('float64')
    zCoordinate = ins['Z'].astype('float64')
    
    point = numpy.array([[xCoordinate],[yCoordinate],[zCoordinate]])

    point_source_id = ins['PointSourceId'] + 66

#    if min(numpy.dot(vector_1, vertex_1), numpy.dot(vector_1, vertex_2)) <= \
#        numpy.dot(vector_1, point) <= max(numpy.dot(vector_1, vertex_1), numpy.dot(vector_1, vertex_2)) \
#    and min(numpy.dot(vector_2, vertex_1), numpy.dot(vector_2, vertex_3)) <= \
#        numpy.dot(vector_2, point) <= max(numpy.dot(vector_2, vertex_1), numpy.dot(vector_1, vertex_3)) \
#    and min(numpy.dot(vector_3, vertex_1), numpy.dot(vector_3, vertex_4)) <= \
#        numpy.dot(vector_3, point) <= max(numpy.dot(vector_3, vertex_1), numpy.dot(vector_3, vertex_4)) :
#
    outs['PointSourceId'] = point_source_id
	
    return True
