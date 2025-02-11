#  Task 7 -  M02 – Shark (p2), M14 – Trident, M15 Research Vessel – Part 2
#
# task revision number
t7_revision="9"
#
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task, hub_menu
from umath import sin, pi
from SM_robot_core_rev13 import resetAttachment, moveAttachment, moveAttachmentFC, driveRobot,turnRobot, debugL1, debugL2, driveBase,initializeRobotForTask, stopEverything

async def T7_Run():

    print ("Task 7 -  M02 - Shark (p2), M14 - Trident, M15 Research Vessel - Part 2, rev#",t7_revision)
    await initializeRobotForTask() 

    
    if debugL1: print ("M02 - Drive to Shark Habit ")
    await driveRobot(-130,600,1000)
    if debugL2: print ("   ?")
    await turnRobot(-22,100,100,100,100)
    await driveRobot(-480,600,1000)
    await moveAttachment("top",145,50,True,True)
    await wait(1000)
    await driveRobot(20,600,1000)
    if debugL2: print (" move to trident?")
    await moveAttachment("top",-40,800,True,False)
    await turnRobot(-50,900,750,900,500)
    await driveRobot(50,900,1000)
    await turnRobot(50,900,500,900,500)
    #await moveAttachment("top",14,800,True,False)
    #await driveRobot(20,400,1000)
    #await moveAttachment("top",-5,800,True,False)
    #await driveRobot(100,900,1000)
    await driveRobot(500,200,1000)
    print ("Task 7 - Completed") 

# Runs the main program from start to finish.
# uncomment this line, if you want to run the task without main menu
#run_task(T7_Run())
