#  Task 6 - M15 Research Vessel - Part 1 - drop off samples into vessel
#
#
# task revision number
t6_revision="6"
#
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task, hub_menu
from umath import sin, pi
from SM_robot_core_rev13 import resetAttachment, moveAttachment, moveAttachmentFC, driveRobot,turnRobot, debugL1, debugL2, driveBase,initializeRobotForTask, stopEverything

async def T6_Run():

#
# the samples need to be in the following order from front of the attachment
# watersample (yellow bands), plakton (white cone), seabed (gray scissor thing)
#
    print ("Task 6 -  Task 6 - M15 Research Vessel - Part 1, rev#",t6_revision)
    await initializeRobotForTask() 

    await driveRobot(-220,400,1000)
    # lower attachment to boat and wiggle to release samnples
    await turnRobot(27,100,100,100,100)
    await moveAttachment("top",125,100,False,False)
    await wait (1000)
    #await moveAttachment("top",90,300,False,False)
    await moveAttachment("top",120,200,False,False)
    await driveRobot(-20,400,1000)
    # return to home
    await driveRobot(220,400,200)
    
    await stopEverything()
    print ("Task 6 - Completed") 
    
# Runs the main program from start to finish.
# uncomment this line, if you want to run the task without main menu
#run_task(T6_Run())
