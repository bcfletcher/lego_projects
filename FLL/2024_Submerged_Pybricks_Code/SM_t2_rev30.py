#  Task 2 - M09 (“Octopus”) Part 2, M05 (“Angler Fish), M10 Send over the Submersible (lift only),M11 – Sonar Discovery, M14 - Plankton Sample Part
#
# task revision number
t2_revision="30"
#
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task, hub_menu
from umath import sin, pi
from SM_robot_core_rev13 import resetAttachment, moveAttachment, moveAttachmentFC, driveRobot,turnRobot, debugL1, debugL2, driveBase,initializeRobotForTask, stopEverything


# Drive forward, turn move gripper at the same time, and drive backward.
async def T2_Run():

    print ("Task 2 - M09 (Octopus) Part 2, M05 (Angler Fish), M10 Send over the Submersible (lift only),M11 - Sonar Discovery, M14 - Plankton Sample Part, rev#",t2_revision)

    await initializeRobotForTask() 
    debugL2=False
    debugL1=True

    if debugL1: print ("   drive to octopus dropoff")
    await driveRobot(150,650,700)
    await turnRobot(-90,100,500,200,600)
    await driveRobot(570,800,500)
    await turnRobot(93,300,500,200,600)
    await driveRobot(270,450,500)

    if debugL1: print ("   anglerfish hideout")
    await driveRobot(-107,600,500)
    await turnRobot(-51,200,500,100,300)
    await driveRobot(250,650,500) 
    #await turnRobot(-19,100,500,100,100) # turn to knock in anglerfish
    await driveRobot(5,100,100) 
    #await turnRobot(19,100,500,100,100) # turn to straighten back out
    
    if debugL1: print ("   submarine battle")
    await driveRobot(190,700,1000)
    await turnRobot(131,400,1000,100,300)
    await driveRobot(403,900,1000) # go towards submarine
    await turnRobot(47,400,1000,100,300) # getting ready to pick up submarine
    await driveRobot(80,500,500)

    if debugL1: print ("   lift submarine yellow bar")
    await moveAttachment("top",100,200,False,True)
    await driveRobot(-93,400,500)
    if debugL2: await wait(3000)
    await moveAttachment("top",30,1000,False,True)
    #await moveAttachment("top",150,100,False,True)
    await wait(500)
    await driveRobot(65,400,500)
    await moveAttachment("top",-5,100,False,True)
    if debugL2: await wait (3000)
    
    resetAttachment("top")

    if debugL1: print ("   go to left side of whales")
    await driveRobot(-120,500,500)
    await turnRobot(121,100,100,100,100)
    await driveRobot(20,400,500)
    if debugL2: await wait (3000)

    if debugL1: print ("   flip left side of whales")
    await moveAttachment("top",106,300,False,True)
    if debugL2: await wait (3000)
    await turnRobot(-20,50,100,150,200)
    await driveRobot(10,400,500)
    if debugL2: await wait(2000)
    await moveAttachment("top",-10,300,False,True)
    if debugL2: await wait (2000)

    resetAttachment("top")

    if debugL1: print ("   drive to right side of whales")
    await driveRobot(-80,500,500)
    await turnRobot(-100,200,900,100,300)
    if debugL2: await wait(2000)
    await driveRobot(430,500,1000)
    if debugL2: await wait(2000)

    if debugL1: print ("   rotate and back up to right side of whales")
    await turnRobot(45,400,900,100,300)
    await driveRobot(-170,400,500)
    await turnRobot(-11,94,500,100,100)
    await moveAttachment("top",111,300,False,True)
    await turnRobot(-2,100,500,100,100)
    await driveRobot(130,100,200)

    if debugL2: await wait(2000)

    ''' print ("    Pick up attachment and turn to plankton")
    await moveAttachment("top",-10,100,False,True)
    resetAttachment("top")
    await turnRobot(80,400,1000,100,300)
    if debugL2: await wait(2000)

    if debugL1: print ("   pull the plankton")
    await driveRobot(-55,300,100)
    await moveAttachment("top",115,100,False,True)
    if debugL2: await wait(3000)
    await driveRobot(50,400,1000)
    await turnRobot(-70,400,1000,100,300)
    if debugL2:await wait(3000)

    '''
    if debugL1: print ("   drive to right side base")
    await driveRobot(420,700,1000)
    '''
    await driveRobot(140,700,1000)
    await turnRobot(-30,400,1000,100,300)
    await driveRobot(330,900,1000)
    #await turnRobot(-60,400,1000,100,300)
    #await driveRobot(130,500,1000)
    #wait turnRobot(-30,200,1000,100,300)
    '''
    await stopEverything()
    print ("Task 2 - Completed")
 

# Runs the main program from start to finish.
# uncomment this line, if you want to run the task without main menu
#run_task(T2_Run())

