import numpy

def dot(v1, v2):
    return numpy.dot(v1, v2)

def InCuboid (vertex_list, point):

    vertex_1 = vertex_list[0]
    vertex_2 = vertex_list[1]
    vertex_3 = vertex_list[2]
    vertex_4 = vertex_list[3]

    vector_1 = numpy.subtract(vertex_1, vertex_2)
    vector_2 = numpy.subtract(vertex_1, vertex_3)
    vector_3 = numpy.subtract(vertex_1, vertex_4)

    if min(dot(vector_1, vertex_1), dot(vector_1, vertex_2)) <= dot(vector_1, point) <= max(dot(vector_1, vertex_1), dot(vector_1, vertex_2)) \
    and min(dot(vector_2, vertex_1), dot(vector_2, vertex_3)) <= dot(vector_2, point) <= max(dot(vector_2, vertex_1), dot(vector_1, vertex_3)) \
    and min(dot(vector_3, vertex_1), dot(vector_3, vertex_4)) <= dot(vector_3, point) <= max(dot(vector_3, vertex_1), dot(vector_3, vertex_4)) :
        return "In"
    else :
        return "Out"

vertex_1 = [-10,-10,-10]
vertex_2 = [-10, -10, 10]
vertex_3 = [-10, 10, -10]
vertex_4 = [10, -10, -10]

vertex_list = [vertex_1,vertex_2,vertex_3,vertex_4]

points_to_verify = [[0,0,0],[100,1000,1000],[-80,2,0],[-80,2,1]]

for point in points_to_verify :
    print (InCuboid(vertex_list, point))
