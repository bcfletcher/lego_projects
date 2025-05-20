# Box Robot Demonstration
#
# task revision number
t1_revision="22"
#
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task, hub_menu
from umath import sin, pi
from robot_library_rev29 import *

async def box_robot_task1():
    global debugL2

    #clearConsole()
    #
    # comment this out if running from menu
    #initiatizeRobot()

    print ("Box Robot Demonstration, Task 1 rev=",t1_revision)
    

    await displayRobotStats(True)
    await initializeRobotForTask() 
    
    await wait(2000)

    continuePrompt=False

    if debugL1: print("  get and place coral tree")
    await driveRobot(285,750,500,continuePrompt)
    await driveRobotAndLift(160,100,100,"left",1750,1000,False,True,continuePrompt)
    await turnRobot(5,100,100,continuePrompt)
    await driveRobotAndLift(-230,300,150,"left",1100,1000,False,True,continuePrompt)
    await turnRobotAndLift(25,200,100,"left",1850,1000,False,True,continuePrompt)

    if debugL1: print("   smash coral nursery")
    await driveRobot(580,850,500,continuePrompt)
    await turnRobot(-15,200,200,continuePrompt)
    await moveAttachment("right",-165,1000,False,True,continuePrompt)
    await moveAttachment("right",0,1000,False,True,continuePrompt)
    await driveRobot(-105,400,100,continuePrompt)
    await turnRobot(76,200,200,continuePrompt)

    if debugL1: print("   lift mast")
    await driveRobotAndLift(-80,100,100,"right",-170,300,False,True,continuePrompt)
    # drive slowly to light mast
    await turnRobot(5,100,100,continuePrompt)
    await driveRobot(260,200,400,continuePrompt)
    # drive away from ship and lift robot arm out of the way
    await driveRobot(-210,400,1000,continuePrompt)
    await moveAttachment("right",0,100,False,True,continuePrompt)
    await driveRobot(100,400,1000,continuePrompt)

    if debugL1: print("   goto shark")
    await turnRobot(-142,200,200,continuePrompt)
    await driveRobot(300,700,500,continuePrompt)

    if debugL1: print("   move away from shark")
    await driveRobot(-75,500,100,continuePrompt)

    if debugL1: print("   pickup scuba diver")
    await turnRobot(-34,100,100,continuePrompt)

    if debugL1: print("   pickup scuba diver")
    await driveRobot(-20,600,500,continuePrompt)
    await driveRobotAndLift(80,100,100,"left",1100,950,False,True,continuePrompt)
    await moveAttachment("left",1850,900,False,True,continuePrompt)
    await driveRobot(-70,600,500,continuePrompt)
    await turnRobot(45,300,300,continuePrompt)
    await driveRobot(-175,500,500,continuePrompt)

    if debugL1: print("   turn to coral reef to drop off diver")
    await turnRobot(70,300,100,continuePrompt)
    await driveRobotAndLift(-45,400,400,"left",1450,900,False,True,continuePrompt)
    await driveRobot(210,500,500,continuePrompt)
    await turnRobot(-12,100,100,continuePrompt)
    # left attachment for seabed
    #await driveRobotAndLift(-140,100,100,"left",850,900,False,True,continuePrompt)
    # right attachment for seabed
    await driveRobotAndLift(-140,100,100,"left",300,950,False,True,continuePrompt)

    if debugL1: print("   move angler fish")
    await turnRobot(40,300,300,continuePrompt)
    await driveRobot(360,400,500,continuePrompt)
    await turnRobot(70,100,100,continuePrompt)
    await driveRobot(100,100,100,continuePrompt)
    await moveAttachment("right",-175,500,False,True,continuePrompt)
    await driveRobot(-60,100,100,continuePrompt)
    await turnRobot(20,200,200,continuePrompt)
    await turnRobot(-30,200,200,continuePrompt)
    await moveAttachment("right",0,500,False,True,continuePrompt)


    if debugL1: print("   raise submersible")
    await turnRobot(-40,200,200,continuePrompt)
    await driveRobot(160,100,100,continuePrompt)
    await turnRobot(-30,200,200,continuePrompt)
    await moveAttachment("left",1150,200,False,True,continuePrompt)
    await moveAttachment("left",600,200,False,True,continuePrompt)
    await turnRobot(40,200,200,continuePrompt)

    '''
    if debugL1: print("   pick up seabed sample right attachment")
    await turnRobot(25,100,100,continuePrompt)
    await moveAttachment("right",-144,500,False,True,continuePrompt)
    await driveRobotAndLift(400,750,500,"left",1850,800,False,True,continuePrompt)
    await moveAttachment("right",-50,500,False,True,continuePrompt)
    await turnRobot(30,200,200,continuePrompt)
    await moveAttachment("right",-175,500,False,True,continuePrompt)
    await driveRobot(80,100,100,continuePrompt)
    await turnRobot(110,200,200,continuePrompt)
    
    '''

    
    await stopEverything()
    print("Task 2 - Completed")


# Runs the main program from start to finish.
# uncomment this line, if you want to run the task without main menu
#run_task(box_robot_task1())
