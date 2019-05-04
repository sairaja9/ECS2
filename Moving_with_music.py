
# Students please note that you must include the reference Ed. before each piece of code. This is because Edison is an object. This is a bit advanced so you dont have to worry about it for now. 


#-------------Setup----------------

import Ed #This imports the Edison module

Ed.EdisonVersion = Ed.V2 #This tells the code what version Edison robot you own

Ed.DistanceUnits = Ed.CM # This specifies the units of distance (in this case centimeters)
Ed.Tempo = Ed.TEMPO_MEDIUM #This sets the music tempo to medium

#--------Your code below-----------

def music():
    #The music function plays a series of notes before driving
    Ed.PlayTone(Ed.NOTE_D_7, Ed.NOTE_QUARTER)
    #Ed.PlayTone makes the robot play a sound
        #Parameters for for this function are Ed.PlayTone(Note and pitch, speed)
    Ed.PlayTone(Ed.NOTE_E_7, Ed.NOTE_QUARTER)
    Ed.PlayTone(Ed.NOTE_F_7, Ed.NOTE_QUARTER)
    Ed.PlayTone(Ed.NOTE_E_7, Ed.NOTE_QUARTER)
    Ed.PlayTone(Ed.NOTE_D_7, Ed.NOTE_QUARTER)
    Ed.PlayTone(Ed.NOTE_C_7, Ed.NOTE_QUARTER)
    Ed.PlayTone(Ed.NOTE_B_7, Ed.NOTE_QUARTER)
    

while True:
    music() #This calls the function music

    #All of the code below makes the robot move
    Ed.Drive(Ed.FORWARD, Ed.SPEED_2, 10)
    Ed.Drive(Ed.BACKWARD, Ed.SPEED_2, 16)
    Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 6)
    Ed.Drive(Ed.BACKWARD, Ed.SPEED_5, 6)
    Ed.Drive(Ed.FORWARD_LEFT, Ed.SPEED_3, 30)
    Ed.Drive(Ed.BACKWARD_LEFT, Ed.SPEED_3, 30)
    Ed.Drive(Ed.FORWARD, Ed.SPEED_2, 10)
    Ed.Drive(Ed.BACKWARD, Ed.SPEED_2, 16)
    Ed.Drive(Ed.FORWARD_RIGHT, Ed.SPEED_5, 45)
    Ed.Drive(Ed.BACKWARD_RIGHT, Ed.SPEED_5, 45)
    Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 3)
    Ed.Drive(Ed.BACKWARD, Ed.SPEED_5, 12)