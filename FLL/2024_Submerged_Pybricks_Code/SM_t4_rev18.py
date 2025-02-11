#  Task 4 - M13 - Changing Shipping Lanes (sailboat), M08 Artificial Habitat (crabs), Drive to Left Home 
#
# task revision number
t4_revision="17"
#
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task, hub_menu
from umath import sin, pi
from SM_robot_core_rev13 import resetAttachment, moveAttachment, moveAttachmentFC, driveRobot,turnRobot, debugL1, debugL2, driveBase,initializeRobotForTask, stopEverything

# Drive forward, turn move gripper at the same time, and drive backward.
async def T4_Run():

    print("Task 4 - M13 - Changing Shipping Lanes, M08 Artificial Habitat (crabs), Drive to Left Home, rev#",t4_revision)

    await initializeRobotForTask() 
    debugL2=False

    if debugL1: print("  drive to sailboat")
    await driveRobot(240,700,1000)
    await turnRobot(-20,415,1000,300,300)
    await driveRobot(450,800,1000)
    await turnRobot(-27,415,1000,300,300)

    if debugL1: print("  lift sailboat")
    await moveAttachment("top",154,150,False,True)
    await driveRobot(-80,500,1000)
    await moveAttachment("top",-10,700,False,True)
    await driveRobot(80,350,1000)

    await resetAttachment("top")

    if debugL1: print("  return to base area")
    await turnRobot(39,415,1000,300,300)
    await driveRobot(-480,800,1000)

    if debugL1: print("  move to crabs")
    await turnRobot(54,415,1000,300,300)
    await driveRobot(-210,850,1000)

    if debugL1: print("  move first 2 crab cages to the right")
    await moveAttachment("top",147,200,False,True)
    await turnRobot(120,600,1000,500,500)
    await moveAttachment("top",-5,500,False,True)

    resetAttachment("top")

    if debugL1: print("  reposition to lift crab cages")
    await turnRobot(-73,500,1000,300,300)
    await driveRobot(20,250,1000)

    if debugL1: print("  lift crab cages")
    await moveAttachment("top",160,100,False,True)
    await driveRobot(-97,800,1000)
    await turnRobot(-12,500,1000,300,300)
    await moveAttachment("top",-10,1000,False,True)

    if debugL1: print("  drift to left home base")
    await turnRobot(59,500,1000,300,300)
    await driveRobot(-135,900,1000)
    await turnRobot(-45,500,1000,300,300)
    await driveRobot(-400,900,1000)
    await turnRobot(-18,500,1000,300,300)
    await driveRobot(-700,900,1000)

    await stopEverything()
    print("Task 4 - Completed")


# Runs the main program from start to finish.
# uncomment this line, if you want to run the task without main menu
#run_task(T4_Run())
