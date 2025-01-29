#  Task 0 - Cleanup Mat and deliver to right home
#
# task revision number
t0_revision="14"
#
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task, hub_menu
from umath import sin, pi
from SM_robot_core_rev13 import resetAttachment, moveAttachment, moveAttachmentFC, driveRobot,turnRobot, debugL1, debugL2, driveBase,initializeRobotForTask, stopEverything

async def T0_Run():


    print ("Task 0 - Clean Mat & deliver to right home, rev#",t0_revision)

    await initializeRobotForTask() 


    if debugL1: print ("Drive to collect pink coral")
    await driveRobot(500,600,1000)

    if debugL1: print ("Turn to water sample and krill")
    await turnRobot(57,200,1000,100,600)
    await driveRobot(370,600,1000)
    await turnRobot(35,200,1000,100,600)

    if debugL1: print ("Drive to water sample and krill")
    await driveRobot(980,600,1000)

    if debugL1: print ("Turn to grab krill and to face purple coral and krill")
    await turnRobot(80,100,100,100,400)

    if debugL1: print ("Drive towards home area and collect purple coral and krill")
    await driveRobot(490,300,500)

    if debugL1: print ("goto octopus")
    await turnRobot(-35,100,100,200,600)

    await driveRobot(-365,300,1000)
    await driveRobot(365,400,1000)

    await stopEverything()
    print("Task 0 - Completed")


# Runs the main program from start to finish.
# uncomment this line, if you want to run the task without main menu
#run_task(T0_Run())
