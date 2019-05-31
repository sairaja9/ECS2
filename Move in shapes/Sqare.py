
#-------------Setup----------------

import Ed

Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

#--------Your code below-----------

def one_side_and_turn():
    Ed.Drive(Ed.Foreward,Ed.Speen_5, 20)
    Ed.Drive(Ed.Forward_Left, Ed.Speed_5, 90) # you may need to change the turning angle based on your encoders (we had to make ours 95)

#This while loop is not needed but we added it for fun
side = 1
while side <= 4:
    one_side_and_turn()
    side += 1


