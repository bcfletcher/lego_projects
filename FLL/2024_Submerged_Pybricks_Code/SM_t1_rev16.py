#  Task 1 - M09 (“Octopus”) Part 1
#
#
# task revision number
t1_revision="16"
#
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task, hub_menu
from umath import sin, pi
from SM_robot_core_rev13 import resetAttachment, moveAttachment, moveAttachmentFC, driveRobot,turnRobot, debugL1, debugL2, driveBase,initializeRobotForTask, stopEverything

# Drive forward, turn move gripper at the same time, and drive backward.
async def T1_Run():


    print ("Task 1 - M09 (Octopus) Part 1, rev#",t1_revision)

    await initializeRobotForTask() 


    if debugL1: print ("drive to forward to Octopus")
    await driveRobot(50,250,1000)
    await turnRobot(-50,400,1000,100,300)
    await driveRobot(340,200,1000)
    await driveRobot(35,50,1000)

    if debugL1: print ("return to base")
    await driveRobot(-380,200,500)

    await stopEverything()
    print ("Task 1 - Completed")


# Runs the main program from start to finish.
# uncomment this line, if you want to run the task without main menu
#run_task(T1_Run())
