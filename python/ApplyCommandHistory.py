# This script should be used a PDAL filter.python  
# It reads a command history file in JSON format and then applies a command
# to a corresponding point in the .las file
#
# Should be used a function for PDAL filter.python:
# pdal pipeline $PROJECT_DIR/json/CommandHistoryPipeline.json

# Created by Serge Shmygelskyy aka Shmyg

import json
import numpy

def apply_command_history(ins,outs):

    xCoordinate = ins['X'].astype('float64')
    yCoordinate = ins['Y'].astype('float64')
    zCoordinate = ins['Z'].astype('float64')
    #pointSourceId = ins['PointSourceId'].astype('float64')
    
    point = numpy.array([[xCoordinate],[yCoordinate],[zCoordinate]])

    with open('../json/command_history.json') as f:
       data = json.load(f)

    for command in data:
        #if command['entity'] == "pointSourceId":
        outs['PointSourceId'] = ins['PointSourceId'] + int(command['new_value'])
	
    return True
