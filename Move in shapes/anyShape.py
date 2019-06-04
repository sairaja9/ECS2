#-------------Setup----------------

import Ed

Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

#--------Your code below-----------
def find_internal_angle_measure(number_of_sides):
    internal_angle_measure = (180*(number_of_sides -2))/number_of_sides
    return internal_angle_measure

number_of_sides = 4

internal_angle_measure = find_internal_angle_measure(number_of_sides)
side = 1
while side <= number_of_sides:
    Ed.Drive(Ed.Foreward,Ed.Speen_5, 20)
    Ed.Drive(Ed.Forward_Left, Ed.Speed_5, internal_angle_measure)
    side += 1
    