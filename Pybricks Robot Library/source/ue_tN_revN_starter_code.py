# Robot Lib Demonstration
#
# task revision number
task_number="1"     # enter the task number here 
task_revision="3"
#
import robot_library_rev33 as RL

# change # in T#_Run() to the number of the task
async def T#_Run(): 

    #   enter the list of missions
    print ("Task ",task_number," Rev ",task_revision," - Lists of missons or parts of missions done by this task")

    await RL.initializeRobotForTask()
    
    waitForPrompt=False

    await RL.wait(1000)
    if RL.debugL1: print("  description of the first step in the task")
    #await RL.driveRobot(690,750,500,"hold",waitForPrompt)
    #await RL.turnRobot(-40,200,200,"hold",waitForPrompt)
    #await RL.moveAttachment("right",-165,1000,False,"hold",False,True, waitForPrompt)

    # example of using an "if" statement to allow different robots to have slightly different settings
    #if RL.hubname == "T1PrimaryHub"   : await RL.driveRobot(690,750,500,"hold",waitForPrompt)
    #if RL.hubname == "T1SecondaryHub" : await RL.driveRobot(695,740,500,"hold",waitForPrompt)
    

    # 
    #  Syntax for the Robot Library commands (for reference) and an example
    # 
    # moveAttachment(attachmentStr,degrees,speed,waitMode,stopMode,resetAngle,stallDetect,waitForPrompt)
    # await RL.moveAttachment("right",-165,1000,False,"hold",False,True, waitForPrompt)
    #
    # driveRobot(dist,speed, accel,stopMode,waitForPrompt)
    # await RL.driveRobot(690,750,500,"hold",waitForPrompt)
    #
    # turnRobot(dir, turnAccel, turnRate, stopMode, waitForPrompt)
    # await RL.turnRobot(-40,200,200,"hold",waitForPrompt)
    #
    # driveRobotInArc(radius,mode,angleOrDist,speed,accel,turnAccel,turnRate,stopMode,waitForPrompt)
    # 
    #
    # driveRobotInArcAndLift(radius,mode,angleOrDist,attachmentStr,degrees,aSpeed,stopMode,resetAngle,stallDetect,waitForPrompt)
    #
    #
    # driveRobotAndLift(dist,dSpeed,accel,attachmentStr,degrees,aSpeed,stopMode,resetAngle,stallDetect,waitForPrompt)
    #
    #
    # turnRobotAndLift(dir,turnAccel, turnRate,attachmentStr,degrees,aSpeed,stopMode,resetAngle,stallDetect,waitForPrompt)
    #
    #
    #