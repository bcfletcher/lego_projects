#  Task 5 - M06 – Raise the Mask, M01 – Coral Nursery, M02 Shark (p1), M03 – Scuba Diver, M14 – Seabed Sample
#
# task revision number
t5_revision="40"
#
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task, hub_menu
from umath import sin, pi
from SM_robot_core_rev13 import resetAttachment, moveAttachment, moveAttachmentFC, driveRobot,turnRobot, debugL1, debugL2, driveBase,initializeRobotForTask, stopEverything

async def T5_Run():

    print ("Task 5 -  M06 - Raise the Mask, M01 - Coral Nursery, M02 Shark (p1), M03 - Scuba Diver, M14 - Seabed Sample, rev#",t5_revision)

    await initializeRobotForTask()
    debugL2=False 

    await wait(250)
    if debugL1: print ("M06 - Drive shipwreck and raise the mast ")
    await driveRobot(412,400,1000)
    if debugL2: print ("    turn towards shipwreck")
    await turnRobot(-90,400,1000,100,300)
    if debugL2: print ("    lower attachment")
    await moveAttachment("top",134,150,False,False)
    if debugL2: print ("    move forward to lift mast")
    await driveRobot(-180,300,1000)
    if debugL2: print ("    drive away from shipwreck")
    await driveRobot(170,500,1000)
    await moveAttachment("top",-10,150,False,False)

    await resetAttachment("top")
 
    if debugL1: print ("M01 - Drive to and flip to coral nursery buds")
    await turnRobot(88,400,1000,200,500)
    await driveRobot(205,500,1000)
    await turnRobot(-88,400,1000,200,500)
    await driveRobot(90,350,1000)
     
    if debugL1: print ("M03 - Drive to coral reef and flip coral reef ")
    await driveRobot(-230,200,1000)
    await turnRobot(-90,400,1000,100,300)
    await driveRobot(-25,150,1000)
    
    await moveAttachmentFC("top", 143,1500,"coast",False,True,True)
    await moveAttachmentFC("top",-134,500,"hold",False,True,True)
    await resetAttachment("top")

    if debugL1: print ("M02 - Drive to and complete shark")
    await turnRobot(-63,400,1000,100,300)
    await driveRobot(-105,150,1000)
    await moveAttachment("top",147,1000,True,True)
    await driveRobot(2,150,1000)
    await moveAttachment("top",-147,1000,True,False)

    
    if debugL1: print ("M04 - Deliver SCUBA Diver to Coral Nursery")
    if debugL2: print ("    Pick up diver")
    await turnRobot(-31,400,1000,100,300)
    await driveRobot(50,150,1000)
    if debugL2: print ("    Lift arm to get diver")
    await moveAttachment("top",105,900,True,False)
    await driveRobot(-85,150,1000)
    await moveAttachment("top",80,100,False,False)
    await driveRobot(50,150,1000)

    if debugL2: print ("   Lower attachment to move diver to end of attachment")
    await turnRobot(10,400,1000,100,300)
    await moveAttachment("top",115,100,False,False)
    if debugL2: await wait(1000)
    await moveAttachment("top",100,50,False,False)

    if debugL2: print ("   Turn away from coral nursery")
    await turnRobot(35,400,1000,100,300)

    # back up so the attachment can be lowered
    if debugL1: print ("M03 - Backup and move to scuba diver destination")
    await driveRobot(100,300,1000)
    await turnRobot(50,400,1000,100,300)

    if debugL2: print ("    drive to coral reef")
    if debugL2: await wait(3000)
    await driveRobot(80,250,1000)

    if debugL2: print ("    lift diver to to yellow arm")
    await moveAttachment("top",94,30,False,True)  
    
    if debugL2: print ("    move to coral nursery")
    if debugL2: await wait(3000)
    await turnRobot(3,100,100,200,300)
    await driveRobot(-92,50,1000)
    await turnRobot(9,100,100,200,300)
    
    if debugL2: print ("    lower arm and back away from yellow arm")
    if debugL2: await wait(3000)
    await moveAttachment("top",107,50,False,True)
    await turnRobot(-6,100,100,100,100)
    await driveRobot(92,250,1000)

    if debugL1: print ("M03 - Grab the seabed sample")
    await moveAttachment("top",120,50,False,True)
    await turnRobot(38,400,1000,100,300)
    await driveRobot(-290,500,1000)
    await moveAttachment("top",85,50,False,True)
    await driveRobot(720,600,1000)

    await stopEverything()
    print ("Task 5 - Completed") 

# Runs the main program from start to finish.
# uncomment this line, if you want to run the task without main menu
#run_task(T5_Run())
