#ask Rohan for help 
#-------------Setup----------------

import Ed

Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.INCH
Ed.Tempo = Ed.TEMPO_MEDIUM

#--------Your code below-----------

Ed.LeftLed(Ed.ON)
Ed.PlayMyBeep(8000)
Ed.LeftLed(Ed.OFF)
Ed.PlayMyBeep(8000)

Ed.RightLed(Ed.ON)
Ed.PlayMyBeep(8000)
Ed.RightLed(Ed.OFF)
Ed.PlayMyBeep(8000)


