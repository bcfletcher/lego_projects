# Box Robot Demonstration
#
# task revision number
t1_revision="16"
#
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task, hub_menu
from umath import sin, pi
from robot_library_rev22 import *

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

    if debugL1: print("  get and place coral tree")
    await driveRobot(285,750,500)
    await driveRobotAndLift(175,100,100,"left",1860,1000,True,True)
    await turnRobot(9,100,100)
    await driveRobotAndLift(-200,100,100,"left",1100,1000,False,True)
    await turnRobotAndLift(25,200,100,"left",1850,1000,False,True)

    if debugL1: print("  smash coral nursery")
    await driveRobot(565,850,500)
    await turnRobot(-27,200,200)
    await moveAttachment("right",-165,1000,False,True)
    await moveAttachment("right",0,1000,False,True)
    await driveRobot(-120,400,100)
    await turnRobot(76,200,200)

    if debugL1: print("  lift mast")
    await driveRobotAndLift(-100,100,100,"right",-170,300,False,True)
    # drive slowly to light mast
    await turnRobot(4,100,100)
    await driveRobot(260,200,400)
    # drive away from ship and lift robot arm out of the way
    await driveRobot(-225,900,1000)
    await moveAttachment("right",0,100,False,True)
    await driveRobot(100,900,1000)

    if debugL1: print("   goto shark")
    await turnRobot(-90,200,200)
    await driveRobot(10,100,100)
    await turnRobot(-44,200,200)
    await driveRobot(285,700,500)

    if debugL1: print("   move away from shark")
    await driveRobot(-80,500,100)

    if debugL1: print("   pickup scuba diver")
    await turnRobot(-35,100,100)

    if debugL1: print("   pickup scuba diver")
    await driveRobotAndLift(70,100,100,"left",1100,950,False,True)
    await moveAttachment("left",1850,900,False,True)
    await driveRobot(-70,600,500)
    await turnRobot(45,300,300)
    await driveRobot(-175,500,500)
    await wait(4000)

    if debugL1: print("   turn to coral reef to drop off diver")
    await turnRobot(65,300,100)
    await wait(1500)
    await driveRobot(-50,400,400)
    await moveAttachment("left",1450,900,False,True)
    await wait(1500)
    await driveRobot(230,500,500)
    await turnRobot(-5,100,100)
    await wait(1500)
    await moveAttachment("left",850,900,False,True)
    await wait(1500)
    await driveRobot(-145,100,100)
    await wait(4000)

    if debugL1: print("   pick up seabed sample")
    await wait(2000)
    await turnRobot(34,100,100)
    await wait(2000)
    await driveRobotAndLift(380,750,500,"left",600,950,False,True)
    await turnRobot(-2,100,100)
    await wait(2000)
    await moveAttachment("left",1600,500,False,True)
    await wait(2000)
    await driveRobot(-30,100,100)
    await wait(2000)
    await turnRobot(75,200,200)
    await wait(2000)
    await driveRobot(170,300,100)

    #await turnRobotAndLift(80,200,200,"left",1800,500,False,True)

    if debugL1: print("   move angler fish")
    await driveRobot(30,100,100)
    await moveAttachment("right",-175,500,False,True)
    await driveRobot(-60,100,100)
    await turnRobot(20,200,200)
    await wait(2000)

    if debugL1: print("   raise submersible")
    await turnRobot(-60,200,200)
    await driveRobot(150,100,100)

    await stopEverything()
    print("Task 2 - Completed")


# Runs the main program from start to finish.
# uncomment this line, if you want to run the task without main menu
#run_task(box_robot_task1())
