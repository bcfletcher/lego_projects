# Robot Library
#
# Base Robot Code shared by all tasks
# 
coreLib_revision="16"
# 17 Feb 2025
#
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task, hub_menu
from umath import sin, pi

# define and set the debug levels
debugL1=True
debugL2=True
attachmentsPresent=True
# set below to false if Top/Front attachments
LeftRightAttachments=True
sensorsPresent=True

if debugL1: print("Robot Core Library Rev#",coreLib_revision)
# Initialize the hub.    
hub = PrimeHub()

# Initialize  motors and sensors. The motor on the
# left must turn counterclockwise to make the robot go forward.
if debugL2: print("DEBUG-L2 - Assigning & Configuring Motors")
leftMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE,reset_angle=True)
rightMotor = Motor(Port.B,Direction.CLOCKWISE,reset_angle=True)

#
# if the gearing for the attachment is  gear based then add gears=[gear1,gear2, etc...] values (diamter in mm)
# need to be updated
if attachmentsPresent == True and LeftRightAttachments == False:
    if debugL2: print("DEBUG-L2 - Configuring Top & Front Attachments")
    topAttachment = Motor(Port.C,Direction.CLOCKWISE,gears=[20,28],reset_angle=True)
    frontAttachment = Motor(Port.D,Direction.CLOCKWISE,reset_angle=True)
if attachmentsPresent == True and LeftRightAttachments == True: 
    if debugL2: print("DEBUG-L2 - Configuring Left & Right Attachments")
    leftAttachment = Motor(Port.D,Direction.CLOCKWISE,reset_angle=True)
    rightAttachment = Motor(Port.F,Direction.CLOCKWISE,gears=[20,28],reset_angle=True)

#
# assign sensors to ports
#
if sensorsPresent: rightColorSensor=Port.C
if sensorsPresent: leftColorSensor=Port.F


# setup drive base and default performance parameters

if debugL2: print("DEBUG-L2 - Configuring the Drive base")

#
# if wheels are changed on the robot are changed then the wheel_diameter value in MM needs to be updated
# if the distance between them of the wheels is changed the axle_track value needs to updated 
#
# secondary hub  wheel 56, axle 199
# primary hub wheel appears to be same
if debugL2: print("DEBUG-L2 - Hub Name=",hub.system.name())

if hub.system.name() == "T2PrimaryHub":
    wheel_diameter=56
    axle_track=199
elif hub.system.name() == "T2SecondHub":
    wheel_diameter=56
    axle_track=199    
elif hub.system.name() == "CoachHub":
    wheel_diameter=62.4
    axle_track=204 
else:
    if debugL2: print("DEBUG-L2 - Unknown Hub, using default values for wheel_diameter and axle_track")
    wheel_diameter=56
    axle_track=199

driveBase = DriveBase(leftMotor, rightMotor, 
                        wheel_diameter=55,  # for small Blue, 87 for Black 
                        axle_track=160)  
driveBase.settings(straight_speed=400,
                    straight_acceleration=1000,
                    turn_acceleration=100,
                    turn_rate=300)



# initialize the robot for a task. basically resets the attachments, enables the gyro, and makes sure the robot is calibrated
async def initializeRobotForTask():
    if debugL1: print("   Initializing Robot for Task")
    
    # calibrate robot
    if debugL2: print('   hub.imu ready status=',hub.imu.ready())
    while hub.imu.ready() != True:
        await wait(500)
        
    # generally you should reset the attachments to a known 0 position

    if attachmentsPresent: 
        if LeftRightAttachments: 
            await resetAttachment("left")
            await resetAttachment("right")
        else:
            await resetAttachment("top")
            await resetAttachment("front")
    # then enable the gyro, just make sure you turn it off at end of the task
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


# basic move attachment with stallDetection
async def moveAttachment(attachmentStr,degrees,speed,resetAngle,stallDetect):

    if attachmentStr == "top": 
        attachment=topAttachment
    elif attachmentStr == "front":
        attachment=frontAttachment
    elif attachmentStr == "left":
        attachment=leftAttachment
    elif attachmentStr == "right":
        attachment=rightAttachment
    else:
        print("moveAttachment() - illegal attachment name of ",attachmentStr)
        return False
    
    if debugL2: print("DEBUG-L2 - Start Moving Attachment ",attachmentStr," angle=",attachment.angle()," new angle=",degrees," speed=", speed," stallDetect=",stallDetect)

    if resetAngle == True: attachment.reset_angle(0)
    
    if stallDetect == False: 
        await attachment.run_target(speed,degrees,then=Stop.HOLD,wait=True)
    else:
        # move the attachment a specific number of degree WHILE also checking to see 
        # if the motor has stalled using the isStalled() command
        # when race=True it will run both command until one finishes then it kills
        # the other one. so it the motor stalls it will kill the run_target() function
        await multitask(attachment.run_target(speed,degrees,then=Stop.HOLD),isStalled(attachment),race=True)

    if debugL2: print("DEBUG-L2 - End moveAttachment() final angle=",attachment.angle())
    
    return True

# advacned move attachment with stall detection
async def moveAttachmentFC(attachmentStr,degrees,speed,stopMode,waitMode,resetAngle,stallDetect):

    if attachmentStr == "top": 
        attachment=topAttachment
    elif attachmentStr == "front":
        attachment=frontAttachment
    elif attachmentStr == "left":
        attachment=leftAttachment
    elif attachmentStr == "right":
        attachment=rightAttachment
    else:
        print("moveAttachmentFC() - ERROR, illegal attachment name of ",attachmentStr)
        return False

    if (waitMode == True and stallDetect == True):
        print("moveAttachmentFC() - ERROR, waitMode and stallDetect are both not allowed to be true")
        return False

    if debugL2: print("DEBUG-L2 - Start moveAttachmentFC() FC attachment=",attachmentStr," angle=",attachment.angle()," new angle=",degrees," speed=", speed, " stop mode=",stopMode," wait=",waitMode," stallDetect=",stallDetect)

    if resetAngle == True: attachment.reset_angle(0)

    if stopMode == "hold": 
        stopMode=Stop.HOLD
    elif stopMode == "brake":
        stopMode=Stop.BRAKE
    elif stopMode == "coast":
        stopMode=Stop.COAST 
    else:
        stopMode=Stop.HOLD

    if (waitMode == False and stallDetect == False):
         await attachment.run_target(speed,degrees,then=Stop.HOLD,wait=False)

    elif (waitMode == False and stallDetect == True):
           #  move the attachment a specific number of degree WHILE also checking to see 
           # if the motor has stalled using the isStalled() command
           # when race=True it will run both command until one finishes then it kills
           # the other one. so it the motor stalls it will kill the run_target() function
           await multitask(attachment.run_target(speed,degrees,then=Stop.HOLD),isStalled(attachment),race=True)

    else:
        await attachment.run_target(speed,degrees,then=stopMode,wait=True)
    
    if debugL2: print("DEBUG-L2 - End moveAttachmentFC() final angle=",topAttachment.angle())

    return True


# drive robot forward or backward (-negative dist)
async def driveRobot(dist,speed, accel) -> bool :
    if debugL2: print("DEBUG-L2 - driveRobot() dist=",dist," speed=",speed," accel=",accel)
    driveBase.settings(straight_speed=speed,
                    straight_acceleration=accel,
                    turn_acceleration=100,
                    turn_rate=300)
    driveBase.reset()
    await driveBase.straight(dist,then=Stop.HOLD,wait=True)
    if debugL2: print("DEBUG-L2 - driveRobot() done dist travelled=",driveBase.distance())
    return True

# turn robot forward or backward (use negative number for backward if robot facing forwards)
# if robot is facing backwards, forward is then the negative number
async def turnRobot(dir,turnAccel, turnRate):
    if debugL2: print("DEBUG-L2 - turnRobot() dir=",dir," turnAccel=",turnAccel," turnRate=",turnRate)
    driveBase.settings(turn_acceleration=turnAccel,
                       turn_rate=turnRate)
    await driveBase.turn(dir,then=Stop.HOLD,wait=True)
    if debugL2: print("DEBUG-L2 - turnRobot() done")
    return True

# drive robot forward or backward  while moving attachment
async def driveRobotAndLift(dist,dSpeed,accel,attachmentStr,degrees,aSpeed,resetAngle,stallDetect):
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
        
    if debugL2: print("DEBUG-L2 - driveRobotAndLift() dist=",dist," dSpeed=",dSpeed," accel=",accel," attach=",attachmentStr," degrees=",
                        degrees," aSpeed=",aSpeed," resetAngle=",resetAngle," stallDetect=",stallDetect)
    await multitask(driveRobot(dist,dSpeed,accel),
                    moveAttachment(attachmentStr,degrees,aSpeed,resetAngle,False))
    if debugL2: print("DEBUG-L2 - driveRobotAndLift() done")

# turn robot while moving attachment
async def turnRobotAndLift(dir,turnAccel, turnRate,attachmentStr,degrees,aSpeed,resetAngle,stallDetect):
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
        
    if debugL2: print("DEBUG-L2 - turnRobotAndLift() dist=",dist," dSpeed=",dSpeed," accel=",accel," attach=",attachmentStr," degrees=",
                        degrees," aSpeed=",aSpeed," resetAngle=",resetAngle," stallDetect=",stallDetect)
    await multitask(turnRobot(dir,turnAccel, turnRate),
                    moveAttachment(attachmentStr,degrees,aSpeed,resetAngle,False))
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
        if LeftRightAttachments: 
            leftAttachment.stop()
            rightAttachment.stop()
        else:
            topAttachment.stop()
            frontAttachment.stop()
    await wait(100)
    if debugL1: print("All motors should be stopped")

#
# End
#