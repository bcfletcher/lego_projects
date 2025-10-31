# OMMS FLL Team Robot Library
#
# This code is released unde the Apache License v2.0
# https://www.apache.org/licenses/LICENSE-2.0.txt
#
#
# Developed against Pybricks 3.6.1 Beta
#
# This code is designed for robots with either two side by side attachment motors which
# can be in different orientations or robots with a front and top attachment motors 
# (usually on either end of the robots though technically the code does not care) 
#
#  TODO List:
#   add speed, angle, acceleration, etc.. input validation
#   add some easier mechanism or setting to determine forward/backward for a robot and attachments
#
#
# Update this if you change the code
coreLib_revision="33"
coreLib_date="30 Oct 2025"
#
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.iodevices import XboxController
from pybricks.tools import wait, StopWatch, multitask, run_task, hub_menu
from umath import sin, pi

#
# change this for your configuration file
#
from robot_library_config_rev8 import *

# define and set the debug levels
debugL1=True
debugL2=False

# if this is set to True it prompt to "Continue [y/n]" for every motion 
# command. this let's robot programmers step through a task one command
# at a time by prompting the user to enter 'y' or 'n' in the pybricks GUI
continuePrompt=True
#
# this defines a global on how many prompts to skip. this value should not 
# be changed as its done through the continue prompt
#
continuePromptSkipCount=0

#
# create some globals used by robot library functions
#
attachmentsPresent=True
leftRightAttachments=True
lightSensorsPresent=False
centerColorSensor=None
rightColorSensor=None
leftColorSensor=None
driveBase=None
lightSensorsNum=0
hub=None
hubName="hubname_changeme"
topAttachment=None
topAttachmentName="top"
frontAttachment=None
frontAttachmentName="front"
leftAttachment=True
leftAttachmentName="left"
rightAttachment=True
rightAttachmentName="right"
leftMotor=None
LeftDriveMotorPort=None
LeftAttachmentMotorPort=None
rightMotor=None
RightDriveMotorPort=None
RightAttachmentMotorPort=None


def initiatizeRobot(hubNum):

    global hub
    global hubName
    global topAttachment
    global frontAttachment
    global leftAttachment
    global rightAttachment
    global centerColorSensor
    global rightColorSensor
    global leftColorSensor
    global attachmentsPresent
    global leftRightAttachments
    global lightSensorsPresent
    global lightSensorsNum
    global driveBase
    global leftMotor
    global rightMotor

    if debugL1: print("Robot Library Rev#",coreLib_revision,"Release Date: ",coreLib_date)
    if debugL2: print("   Initializing Robot")
    tempHubNum="0"
    hubName="hub"
    hub = PrimeHub(top_side=robotConfigs[hubNum].topSide,
                   front_side=robotConfigs[hubNum].frontSide)
    if debugL1: print("   Reported Hub Name: ",hub.system.name())

    # the reason for this convoluted logic is that you can't not run PrimeHub() more than once and there is no way to get 
    # the hubname without calling PrimeHub()
    for x in range(0,NumberOfHubs,1):
        if debugL2: print("   Finding Hub in Config:",hub.system.name()," robotConfig=",robotConfigs[x].HubName)    
        if hub.system.name() ==  robotConfigs[x].HubName:
            hubName = robotConfigs[x].HubName
            tempHubNum = x
    if hubNum != tempHubNum:
        print("ERROR, requested hub number (",hubNum,") and actual hub name/number (",hubName,"/",tempHubNum,") do NOT match!. Powering Off Hub!")
        print("Verify in the robot menu python file that RL.initiatizeRobot() is set to the right hub number (found in the library config file).")
        wait(2000)
        hub.system.shutdown()

    hub.system.set_stop_button(Button.CENTER)

    if debugL1: print("   Verified hub #",hubNum," named: ",hubName)


    #
    #****************


    # add code for correcting  rotation and heading
    # imu.settings for heading 
    
    ##*****************


    # set the hub LED display to the correct orientation
    hub.display.orientation(robotConfigs[hubNum].displayOrientation)
    # set this to true if there are attachments
    attachmentsPresent=robotConfigs[hubNum].AttachmentsPresent
    # set below to false if Top/Front attachments
    leftRightAttachments=robotConfigs[hubNum].LeftRightAttachments
    # change these values depending on your sensors
    lightSensorsPresent=robotConfigs[hubNum].LightSensorsPresent
    # valid values are 1 or 2. 1 is assumed in center,
    # 2 is asusme left and right side of robot
    lightSensorsNum=robotConfigs[hubNum].LightSensorsNum

    # Initialize  motors and sensors. The motor on the
    # left must turn counterclockwise to make the robot go forward.
    if debugL2: print("DEBUG-L2 - Assigning & Configuring Motors")

    leftMotor = Motor(robotConfigs[hubNum].LeftDriveMotorPort, Direction.COUNTERCLOCKWISE,reset_angle=True)
    rightMotor = Motor(robotConfigs[hubNum].RightDriveMotorPort,Direction.CLOCKWISE,reset_angle=True)
   # setup drive base and default performance parameters
    if debugL2: print("DEBUG-L2 - Configuring the Drive base")

    wheelDiameter=robotConfigs[hubNum].WheelDiameter
    axleTrack=robotConfigs[hubNum].AxleTrack
    driveBase = DriveBase(leftMotor,rightMotor, 
                            wheel_diameter=wheelDiameter,
                            axle_track=axleTrack) 
    #
    # set some default motor settings for your drive motors
    # 
    driveBase.settings(straight_speed=robotConfigs[hubNum].DefaultStraightSpeed,
                        straight_acceleration=robotConfigs[hubNum].DefaultStraightAcceleration,
                        turn_acceleration=robotConfigs[hubNum].DefaultTurnAcceleration,
                        turn_rate=robotConfigs[hubNum].DefaultTurnRate)
    #
    # if the gearing for the attachment is  gear based then add gears=[gear1,gear2, etc...] values (diamter in mm)
    # need to be updated

    if attachmentsPresent == True and leftRightAttachments == False:
        if debugL2: print("DEBUG-L2 - Configuring Top & Front Attachments")
        if robotConfigs[hubNum].TopAttachmentGearsPresent==False:
            topAttachment = Motor(robotConfigs[hubNum].TopAttachmentPort,Direction.CLOCKWISE,reset_angle=True)
        else:
            topAttachment = Motor(robotConfigs[hubNum].TopAttachmentPort,Direction.CLOCKWISE,
                                gears=robotConfigs[hubNum].TopAttachmentGearsCfg,reset_angle=True)

        if robotConfigs[hubNum].FrontAttachmentGearsPresent==False:
            frontAttachment = Motor(robotConfigs[hubNum].FrontAttachmentPort,Direction.CLOCKWISE,reset_angle=True)
        else:
            frontAttachment = Motor(robotConfigs[hubNum].FrontAttachmentPort,Direction.CLOCKWISE,
                                gears=robotConfigs[hubNum].FrontAttachmentGearsCfg,reset_angle=True)

    if attachmentsPresent == True and leftRightAttachments == True: 
        if debugL2: print("DEBUG-L2 - Configuring Left & Right Attachments")
        if robotConfigs[hubNum].LeftAttachmentGearsPresent==False:
            leftAttachment = Motor(robotConfigs[hubNum].LeftAttachmentPort,Direction.CLOCKWISE,reset_angle=True)

        else:    
            leftAttachment = Motor(robotConfigs[hubNum].LeftAttachmentPort,Direction.CLOCKWISE,
                                gears=robotConfigs[hubNum].LeftAttachmentGearsCfg,reset_angle=True)

        if robotConfigs[hubNum].RightAttachmentGearsPresent==False:
            rightAttachment = Motor(robotConfigs[hubNum].RightAttachmentPort,Direction.CLOCKWISE,reset_angle=True)
        else:
            rightAttachment = Motor(robotConfigs[hubNum].RightAttachmentPort,Direction.CLOCKWISE,
                                gears=robotConfigs[hubNum].RightAttachmentGearsCfg,reset_angle=True)
    #
    # assign sensors to ports
    #
    if lightSensorsPresent: 
        if lightSensorsNum == robotConfigs[hubNum].LightSensorsNum: 
            centerColorSensor=robotConfigs[hubNum].CenterLightSensorPort
        if lightSensorsNum == robotConfigs[hubNum].LightSensorsNum:
            rightColorSensor=robotConfigs[hubNum].RightLightSensorPort
            leftColorSensor=robotConfigs[hubNum].LeftLightSensorPort
    
 
# clear the console
def clearConsole():
    print("\x1b[H\x1b[3J", end="")
    print("\x1b[H\x1b[2J", end="")

# Display Robot statistics
async def displayRobotStats(resetStats):
    print("*************************************")
    print("* Robot Stats:")
    if attachmentsPresent == True:
        if leftRightAttachments == True:
            print("* Attachments Present: Left/Right Mode")
        else:
            print("* Attachments Present: Top/Front Mode") 
    print("* Distance Driven (est)=",driveBase.distance())
    print("* Rotation Angle (est)=",driveBase.angle())
    print("* Hub Ready=",hub.imu.ready()," Stationary=",hub.imu.stationary())
    print("* Hub Up=",hub.imu.up())
    if resetStats:
        driveBase.reset()
    print("*************************************")

# initialize the robot for a task. basically resets the attachments, enables the gyro, and makes sure the robot is calibrated
async def initializeRobotForTask():
    if debugL1: print("   Initializing Robot (",hubName,") for Task")
    
    # calibrate robot
    if debugL2: print('   hub.imu ready status=',hub.imu.ready())
    while hub.imu.ready() != True:
        await wait(250)
        
    # generally you should reset the attachments to a known 0 position

    if attachmentsPresent: 
        if leftRightAttachments: 
            await resetAttachment("left")
            await resetAttachment("right")
        else:
            await resetAttachment("top")
            await resetAttachment("front")
    # then enable the gyro, just make sure you turn it off at end of the task
    driveBase.use_gyro(False)
    driveBase.reset(angle=0,distance=0)
    hub.imu.reset_heading(0)
    driveBase.use_gyro(True)
    if debugL1: print("   Completed Robot Initialization")
    

# detect if a specific attachment is stalled, used with multitask() in moveAttachment functions
async def isStalled(attachment) -> bool :

    if debugL2: print("isStalled()",attachment.stalled())
    while attachment.stalled() == False: 
        await wait(1)
    if debugL1: print("stalled")
    return attachment.stalled()

# display current angle of an attachment
async def displayAngleForAttachment(attachmentStr):
    if attachmentStr == "top": 
        attachment=topAttachment
    elif attachmentStr == "front":
        attachment=frontAttachment
    elif attachmentStr == "left":
        attachment=leftAttachment
    elif attachmentStr == "right":
        attachment=rightAttachment
    else:
        print("displayAngleForAttachment() - illegal attachment name of ",attachmentStr)
        return False 
    print("displayAngleForAttachment() attachment=",attachmentStr," angle=",attachment.angle())
   
# used to reset and attachment to a new "zero" position
async def resetAttachment(attachmentStr):

    if attachmentsPresent == False: return

    if attachmentStr == "top": 
        attachment=topAttachment
    elif attachmentStr == "front":
        attachment=frontAttachment
    elif attachmentStr == "left":
        attachment=leftAttachment
    elif attachmentStr == "right":
        attachment=rightAttachment
    else:
        print("resetAttachment() - illegal attachment name of ",attachmentStr)
        return False
    
    if debugL2: print("DEBUG-L2 - Start Reset Attachment ",attachmentStr," previous angle=",attachment.angle())

    attachment.reset_angle(0)
    if debugL2: print("DEBUG-L2 - Reset Attachment ",attachmentStr," previous angle=",attachment.angle())

    if debugL2: print("DEBUG-L2 - End resetAttachment() final angle=",attachment.angle())



# advacned move attachment with stall detection
async def moveAttachment(attachmentStr,degrees,speed,waitMode,stopMode,resetAngle,stallDetect,waitForPrompt):

    await promptToContinue(waitForPrompt)

    if stopMode == "hold": 
        stopModeVal=Stop.HOLD
    elif stopMode == "brake":
        stopModeVal=Stop.BRAKE
    elif stopMode == "coast":
        stopModeVal=Stop.COAST 
    else:
        stopModeVal=Stop.HOLD

    if attachmentStr == "top": 
        attachment=topAttachment
    elif attachmentStr == "front":
        attachment=frontAttachment
    elif attachmentStr == "left":
        attachment=leftAttachment
    elif attachmentStr == "right":
        attachment=rightAttachment
    else:
        print("moveAttachment() - ERROR, illegal attachment name of ",attachmentStr)
        return False

    if (waitMode == True and stallDetect == True):
        print("moveAttachment() - ERROR, waitMode and stallDetect are both not allowed to be true")
        return False

    if debugL2: print("DEBUG-L2 - Start moveAttachment() attachment=",attachmentStr," angle=",
                      attachment.angle()," new angle=",degrees," speed=", speed, " stop mode=",
                      stopModeVal," wait=",waitMode," stallDetect=",stallDetect)

    if resetAngle == True: attachment.reset_angle(0)


    if (waitMode == False and stallDetect == False):
         await attachment.run_target(speed,degrees,then=stopModeVal,wait=False)

    elif (waitMode == False and stallDetect == True):
           #  move the attachment a specific number of degree WHILE also checking to see 
           # if the motor has stalled using the isStalled() command
           # when race=True it will run both command until one finishes then it kills
           # the other one. so it the motor stalls it will kill the run_target() function
           await multitask(attachment.run_target(speed,degrees,then=stopModeVal),isStalled(attachment),race=True)

    else:
        await attachment.run_target(speed,degrees,then=stopModeVal,wait=True)
    
    if debugL2: print("DEBUG-L2 - End moveAttachment() final angle=",attachment.angle())

    return True


# drive robot forward or backward (-negative dist)
async def driveRobot(dist,speed, accel,stopMode,waitForPrompt) -> bool :

    await promptToContinue(waitForPrompt)
    
    if stopMode == "hold": 
        stopModeVal=Stop.HOLD
    elif stopMode == "brake":
        stopModeVal=Stop.BRAKE
    elif stopMode == "coast":
        stopModeVal=Stop.COAST 
    else:
        stopModeVal=Stop.HOLD

    if debugL2: print("DEBUG-L2 - driveRobot() dist=",dist," speed=",speed," accel=",accel)
    driveBase.settings(straight_speed=speed,
                    straight_acceleration=accel,
                    turn_acceleration=100,
                    turn_rate=300)
    driveBase.reset()
    await driveBase.straight(dist,then=stopModeVal,wait=True)
    if debugL2: print("DEBUG-L2 - driveRobot() done dist travelled=",driveBase.distance())
    return True

# turn robot forward or backward (use negative number for backward if robot facing forwards)
# if robot is facing backwards, forward is then the negative number
async def turnRobot(dir, turnAccel, turnRate, stopMode, waitForPrompt):

    await promptToContinue(waitForPrompt)

    if stopMode == "hold": 
        stopModeVal=Stop.HOLD
    elif stopMode == "brake":
        stopModeVal=Stop.BRAKE
    elif stopMode == "coast":
        stopModeVal=Stop.COAST 
    else:
        stopModeVal=Stop.HOLD

    if debugL2: print("DEBUG-L2 - turnRobot() dir=",dir," turnAccel=",turnAccel," turnRate=",turnRate)
    driveBase.settings(turn_acceleration=turnAccel,
                       turn_rate=turnRate)
    await driveBase.turn(dir,then=stopModeVal,wait=True)
    if debugL2: print("DEBUG-L2 - turnRobot() done")
    return True

#
# drive robot in arc
#
async def driveRobotInArc(radius,mode,angleOrDist,speed,accel,turnAccel,turnRate,stopMode,waitForPrompt):

    await promptToContinue(waitForPrompt)

    if stopMode == "hold": 
        stopModeVal=Stop.HOLD
    elif stopMode == "brake":
        stopModeVal=Stop.BRAKE
    elif stopMode == "coast":
        stopModeVal=Stop.COAST 
    else:
        stopModeVal=Stop.HOLD


    driveBase.settings(straight_speed=speed,
                    straight_acceleration=accel,
                    turn_acceleration=turnAccel,
                    turn_rate=turnRate)
                          
    if mode == "arc": 
        if debugL2: print("DEBUG-L2 - turnRobotInArc() radius=",radius," mode=arc degrees=",angleOrDist)
        await driveBase.arc(radius,angle=angleOrDist,then=stopModeVal,wait=True)

    if mode == "distance": 
        if debugL2: print("DEBUG-L2 - turnRobotInArc() radius=",radius," mode=distance distance=",angleOrDist)
        await driveBase.arc(radius,distance=angleOrDist,then=stopModeVal,wait=True)

    if debugL2: print("DEBUG-L2 - turnRobotInArc() done")
    return True

# drive robot in an arc while moving attachment
async def driveRobotInArcAndLift(radius,mode,angleOrDist,attachmentStr,degrees,aSpeed,stopMode,resetAngle,stallDetect,waitForPrompt):

    if stopMode == "hold": 
        stopModeVal=Stop.HOLD
    elif stopMode == "brake":
        stopModeVal=Stop.BRAKE
    elif stopMode == "coast":
        stopModeVal=Stop.COAST 
    else:
        stopModeVal=Stop.HOLD

    if attachmentStr == "top": 
        attachment=topAttachment
    elif attachmentStr == "front":
        attachment=frontAttachment
    elif attachmentStr == "left":
        attachment=leftAttachment
    elif attachmentStr == "right":
        attachment=rightAttachment
    else:
        print("driveRobotInArcAndLift() - illegal attachment name of ",attachmentStr)
        return False
        
    await promptToContinue(waitForPrompt)
                       
    if mode == "arc": 
        if debugL2: print("DEBUG-L2 - driveRobotInArcAndLift() radius=",radius," mode=arc degrees=",angleOrDist,
                          " attach=",attachmentStr," degrees=",degrees," aSpeed=",aSpeed,
                          " resetAngle=",resetAngle," stallDetect=",stallDetect)
        await multitask(driveBase.arc(radius,angle=angleOrDist,then=stopMode,wait=True),
                        moveAttachment(attachmentStr,degrees,aSpeed,False, stopModeVal,resetAngle,stallDetect, False))
    
    if mode == "distance": 
        if debugL2: print("DEBUG-L2 - driveRobotInArcAndLift() radius=",radius," mode=distance distance=",angleOrDist,
                          " attach=",attachmentStr," degrees=",degrees," aSpeed=",aSpeed,
                          " resetAngle=",resetAngle," stallDetect=",stallDetect)
        await multitask(driveBase.arc(radius,distance=angleOrDist,then=stopMode,wait=True),
                        moveAttachment(attachmentStr,degrees,aSpeed,False,stopModeVal,resetAngle,stallDetect, False)) 
    
    if debugL2: print("DEBUG-L2 - driveRobotInArcAndLift() done")



# drive robot forward or backward  while moving attachment
async def driveRobotAndLift(dist,dSpeed,accel,attachmentStr,degrees,aSpeed,stopMode,resetAngle,stallDetect,waitForPrompt):

    await promptToContinue(waitForPrompt)

    if stopMode == "hold": 
        stopModeVal=Stop.HOLD
    elif stopMode == "brake":
        stopModeVal=Stop.BRAKE
    elif stopMode == "coast":
        stopModeVal=Stop.COAST 
    else:
        stopModeVal=Stop.HOLD

    if attachmentStr == "top": 
        attachment=topAttachment
    elif attachmentStr == "front":
        attachment=frontAttachment
    elif attachmentStr == "left":
        attachment=leftAttachment
    elif attachmentStr == "right":
        attachment=rightAttachment
    else:
        print("driveRobotAndLift() - illegal attachment name of ",attachmentStr)
        return False
        
    if debugL2: print("DEBUG-L2 - driveRobotAndLift() dist=",dist," dSpeed=",dSpeed," accel=",accel,
                        " attach=",attachmentStr," degrees=",degrees," aSpeed=",aSpeed," resetAngle=",
                        resetAngle," stallDetect=",stallDetect)
    await multitask(driveRobot(dist,dSpeed,accel,"hold",False),
                    moveAttachment(attachmentStr,degrees,aSpeed,False,stopModeVal,resetAngle,stallDetect, False))
    if debugL2: print("DEBUG-L2 - driveRobotAndLift() done")


# moveAttachment(attachmentStr,degrees,speed,waitMode,stopMode,resetAngle,stallDetect,waitForPrompt):


# turn robot while moving attachment
async def turnRobotAndLift(dir,turnAccel, turnRate,attachmentStr,degrees,aSpeed,stopMode,resetAngle,stallDetect,waitForPrompt):

    await promptToContinue(waitForPrompt)

    if stopMode == "hold": 
        stopModeVal=Stop.HOLD
    elif stopMode == "brake":
        stopModeVal=Stop.BRAKE
    elif stopMode == "coast":
        stopModeVal=Stop.COAST 
    else:
        stopModeVal=Stop.HOLD

    if attachmentStr == "top": 
        attachment=topAttachment
    elif attachmentStr == "front":
        attachment=frontAttachment
    elif attachmentStr == "left":
        attachment=leftAttachment
    elif attachmentStr == "right":
        attachment=rightAttachment
    else:
        print("turnRobotAndLift() - illegal attachment name of ",attachmentStr)
        return False
        
    if debugL2: print("DEBUG-L2 - turnRobotAndLift() dir=",dir," turnAccel=",turnAccel," turnRate=",turnRate," attach=",attachmentStr," degrees=",
                        degrees," aSpeed=",aSpeed," resetAngle=",resetAngle," stallDetect=",stallDetect)
    await multitask(turnRobot(dir,turnAccel, turnRate,stopModeVal,False),
                    moveAttachment(attachmentStr,degrees,aSpeed,False,stopModeVal,resetAngle,stallDetect, False))
    if debugL2: print("DEBUG-L2 - turnRobotAndLift() done")


# stops the motors and disables the gyroscope (if you lift it off the table)
# this should be run at the end of every task in the task and in menu after each task
async def stopEverything():
    if debugL1: print("Stop All Motors")
    driveBase.use_gyro(False)
    await wait(100)
    leftMotor.stop()
    await wait(100)
    rightMotor.stop()
    await wait(100)
    if attachmentsPresent: 
        if leftRightAttachments: 
            leftAttachment.stop()
            rightAttachment.stop()
        else:
            topAttachment.stop()
            frontAttachment.stop()
    await wait(100)
    if debugL1: print("All motors should be stopped")



#
# wait for a prompt, intended to use used to step through the execution of task 
# command by command
# if 's' is provided on the input, you can enter the number of Continue prompts to skip. 
# this is kinda like a fastforward
#
async def promptToContinue(waitForPrompt):
    global continuePromptSkipCount

    if debugL2: print("DEBUG-L2 - prompToContinue: wait=",waitForPrompt," count=",continuePromptSkipCount)

    if (waitForPrompt == True and continuePromptSkipCount <= 0):
        driveBase.use_gyro(False)
        prompt=''
        while (prompt not in {'n','y','s'}):
            prompt=input("Continue? (y/n/s) ")
        if prompt == 'n':
            await stopEverything()
            await hub.system.shutdown()
        if prompt == 's':
            count=-1
            while (count < 0) :
                skipCount = input("How many Countinue steps to Skip? (#/0): ")
                if skipCount.isdigit() == True:
                    count = int(skipCount)
            continuePromptSkipCount = count-1
        driveBase.use_gyro(True)
    else:
        if (waitForPrompt == True):
            continuePromptSkipCount -= 1


#
# End
#