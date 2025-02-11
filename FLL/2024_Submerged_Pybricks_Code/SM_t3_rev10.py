#  Task 3 -  M03 – Drop off Reef Segments
#
# task revision number
t3_revision="10"
#
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task, hub_menu
from umath import sin, pi
from SM_robot_core_rev13 import resetAttachment, moveAttachment, moveAttachmentFC, driveRobot,turnRobot, debugL1, debugL2, driveBase,initializeRobotForTask, stopEverything

# Drive forward, turn move gripper at the same time, and drive backward.
async def T3_Run():

    print ("Task 3 -  M03 - Reef Segments, rev#",t3_revision)

    await initializeRobotForTask() 

    if debugL1: print(" drop off samples")
    await driveRobot(56,58,85)
    await driveRobot(-56,650,100)

    await stopEverything()
    print("Task 3 - Completed")
    
# Runs the main program from start to finish.
# uncomment this line, if you want to run the task without main menu
#run_task(T3_Run())

