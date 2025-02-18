# 
#
# task revision number
t0_revision="1"
#
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task, hub_menu
from umath import sin, pi
from robot_core_rev16 import *

#import resetAttachment, moveAttachment, moveAttachmentFC, driveRobot,turnRobot, driveRobotAndLift, turnRobotAndLift, debugL1, debugL2, driveBase,initializeRobotForTask, stopEverything
#sensor = ColorSensor(Port.E)



async def mt_test():
    global debugL2

    print ("multtasking tests",t0_revision)

    await initializeRobotForTask() 

    await wait(2000)
    await driveRobot(110,200,500)
#    await turnRobot(360,300,300)
#    await driveRobot(-300,500,1000)

    #await moveAttachment("right",-160,100,False,True)
    #await moveAttachment("right",0,100,False,True)

    await wait(2000)
    await moveAttachment("left",-1700,900,True,True)
    #await moveAttachment("left",170,900,False,True)
    await wait(2000)
    await driveRobot(130,200,500)
    await wait(2000)
    await moveAttachment("left",-1400,900,False,True)
    await driveRobot(-130,100,200)

    # drive and lift tests
    '''
    for s in range(1,10,1):
        print ("drive forward and lower run=",s)
        await driveRobotAndLift(400,900,1000,"top",100,500,False,False)
        await wait(100)
        print ("drive backward and raise")
        await driveRobotAndLift(-400,900,1000,"top",0,500,False,False)
    '''
    debugL2=False
    
    # turn robot lifting attachment
    '''
    for s in range(1,4,1):
        print ("turn robot right and lower run=",s)
        await turnRobotAndLift(90,100,100,"top",100,75,False,False)
        await wait(100)
        print ("turn robot left and raise")
        await turnRobotAndLift(-90,100,100,"top",0,75,False,False)
    '''

    await stopEverything()
    print("Task 0 - Completed")


# Runs the main program from start to finish.
# uncomment this line, if you want to run the task without main menu
run_task(mt_test())
