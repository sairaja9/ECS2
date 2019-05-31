
#-------------Setup----------------

import Ed

Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.INCH
Ed.Tempo = Ed.TEMPO_MEDIUM

#--------Your code below-----------

Ed.LeftLed(Ed.ON)
Ed.PlayBeep()
Ed.LeftLed(Ed.OFF)
Ed.PlayBeep()

Ed.RightLed(Ed.ON)
Ed.PlayBeep()
Ed.RightLed(Ed.OFF)
Ed.PlayBeep()


