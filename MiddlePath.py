
#-------------Setup----------------

import Ed

Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

#--------Your code below-----------

def middle_path():
    if Ed.ReadLineState() == Ed.LINE_ON_BLACK:
        Ed.Drive(Ed.BACKWARD_LEFT, Ed.SPEED_5, 2)
    elif Ed.ReadLineState() == Ed.Ed.LINE_ON_BLACK:
        Ed.Drive(Ed.BACKWARD_RIGHT, Ed.SPEED_5, 2)
    else:
        Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 5)
        
middle_path()