#  Task 4 - M13 - Changing Shipping Lanes (sailboat), M08 Artificial Habitat (crabs), Drive to Left Home 
#
# task revision number
task_revision="1"
#
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task, hub_menu
from umath import sin, pi
from robot_library_rev29 import *

async def box_robot_task2():
    global debugL2

    debugL2=False
    #clearConsole()
    #
    # comment this out if running from menu
    #initiatizeRobot()
    continuePrompt=False

    print ("Box Robot Demonstration, Task 2 r6v=",task_revision)    
    print ("    Changing Shipping Lanes, M08 6rtificial Habitat (crabs), Drive to Left Home")

    await displayRobotStats(True)
    await initializeRobotForTask() 
    
    await wait(2000)

    await initializeRobotForTask() 

    if debugL1: print("  drive to sailboat")
    await driveRobot(785,700,950,continuePrompt)
    await turnRobot(135,200,600,continuePrompt)

    if debugL1: print("  lift sailboat")
    await moveAttachment("right",-190,200,False,True,continuePrompt)
    await driveRobot(110,500,950,continuePrompt)
    await moveAttachment("right",0,700,False,True,continuePrompt)
    await driveRobot(-90,350,950,continuePrompt)

    if debugL1: print("  move to crabs")
    await turnRobot(45,200,200,continuePrompt)
    await driveRobot(420,800,950,continuePrompt)
    await turnRobot(38,200,200,continuePrompt)
    await driveRobot(265,850,950,continuePrompt)

    if debugL1: print("  move first 2 crab cages to the right")
    await turnRobot(100,800,600,continuePrompt)

    if debugL1: print("  reposition to lift crab cages")
    await turnRobotAndLift(-72,600,600,"left",1400,900,False,True,continuePrompt)

    if debugL1: print("  lift crab cages")
    await moveAttachment("right",-190,400,False,True,continuePrompt)
    await driveRobot(110,900,950,continuePrompt)
    await turnRobot(-10,800,600,continuePrompt)
    await moveAttachment("right",10,950,False,True,continuePrompt)

    if debugL1: print("  drive to right home base")
    #await turnRobot(59,200,600,continuePrompt)
    await driveRobot(-160,900,950,continuePrompt)

    await stopEverything()
    print("Task 2 - Completed")


# Runs the main program from start to finish.
# uncomment these lines, if you want to run the task without main menu
initiatizeRobot(1)
run_task(box_robot_task2())
