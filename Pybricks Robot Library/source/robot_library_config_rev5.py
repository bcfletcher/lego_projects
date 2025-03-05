# Configuration file for robot library 
# 
#
robotLibraryConfigRev="5"
#
#
from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop


#
# index values for the different robot configurations, this should not
# need to be changed
#

class RobotConfig:

    #
    # default values for the robot configuration
    #
    def __init__(self,HubName,HubNumber):
        self.HubName=HubName
        self.HubNumber=HubNumber
        # set this to the diameter of the wheel
        self.WheelDiameter=62.4
        # set this to the default Axle Track width
        self.AxleTrack=204
        # set this for the default speed
        self.DefaulStraightSpeed=500
        # set this tuple for straight acceleration and deceleration
        self.DefaultStraightAcceleration=500
        # set this tuple for turn acceleration and deceleration
        self.DefaultTurnAcceleration=[500,500]
        # set this to default turn rate for the robot
        self.DefaultTurnRate=300
        # set this to true if there are attachments
        self.AttachmentsPresent=9
        # set below to False if Top/Front attachments other set to True
        self.LeftRightAttachments=10
        # change these values depending on your sensors
        self.LightSensorsPresent=11
        # valid values are 1 or 2. 1 is assumed in center,
        # 2 is asusme left and right side of robot
        self.LightSensorsNum=2
        self.RightLightSensorPort=Port.E
        self.LeftLightSensorPort=Port.F
        self.CenterLightSensorPort=None
        # use Port.A, Port.B, etc..
        self.LeftDriveMotorPort=Port.B
        self.RightDriveMotorPort=Port.A
        #
        self.TopAttachmentPort=None
        self.TopAttachmentGearsPresent=False
        self.TopAttachmentGearsCfg=None
        #
        self.FrontAttachmentPort=None
        self.FrontAttachmentGearsPresent=False
        self.FrontAttachmentGearsCfg=None
        #
        self.LeftAttachmentPort=Port.C
        self.LeftAttachmentGearsPresent=False
        self.LeftAttachmentGearsCfg=None
        #
        self.RightAttachmentPort=Port.D
        self.RightAttachmentGearsPresent=True
        self.RightAttachmentGearsCfg=[28,36]



###########################################
#
# site specific hub configurations
#
###########################################


# number of hubs that are supported
NumberOfHubs=3

robotConfigs=[]
robotConfigs.append(RobotConfig("CoachHub",1))
robotConfigs.append(RobotConfig("T2PrimaryHub",2))
robotConfigs.append(RobotConfig("T2SecondaryHub",3))


#
# hub #1 configuration
#
robotConfigs[0].HubName="CoachHub"
robotConfigs[0].HubNumber=0
robotConfigs[0].WheelDiameter=62.4
robotConfigs[0].AxleTrack=204
robotConfigs[0].DefaultStraightSpeed=400
robotConfigs[0].DefaultStraightAcceleration=[500,500]
robotConfigs[0].DefaultTurnAcceleration=[500,500]
robotConfigs[0].DefaultTurnRate=300
robotConfigs[0].LightSensorsPresent=True
robotConfigs[0].LightSensorsNum=2
robotConfigs[0].RightLightSensorPort=Port.E
robotConfigs[0].LeftLightSensorPort=Port.F
robotConfigs[0].CenterLightSensorPort=False
robotConfigs[0].LeftDriveMotorPort=Port.B
robotConfigs[0].RightDriveMotorPort=Port.A
#
robotConfigs[0].AttachmentsPresent=True
robotConfigs[0].LeftRightAttachments=True
#
robotConfigs[0].TopAttachmentPort=None
robotConfigs[0].TopAttachmentGearsPresent=False
robotConfigs[0].TopAttachmentGearsCfg=None
#
robotConfigs[0].FrontAttachmentPort=None
robotConfigs[0].FrontAttachmentGearsPresent=False
robotConfigs[0].FrontAttachmentGearsCfg=None
#
robotConfigs[0].LeftAttachmentPort=Port.D
robotConfigs[0].LeftAttachmentGearsPresent=False
robotConfigs[0].LeftAttachmentGearsCfg=None
#
robotConfigs[0].RightAttachmentPort=Port.C
robotConfigs[0].RightAttachmentGearsPresent=True
robotConfigs[0].RightAttachmentGearsCfg=[28,36]


#
# hub #2 configuration
#

robotConfigs[1].HubName="T2PrimaryHub"
robotConfigs[1].HubNumber=1
robotConfigs[1].WheelDiameter=62.4
robotConfigs[1].AxleTrack=204
robotConfigs[1].DefaultStraightSpeed=400
robotConfigs[1].DefaultStraightAcceleration=[500,500]
robotConfigs[1].DefaultTurnAcceleration=[500,500]
robotConfigs[1].DefaultTurnRate=300
robotConfigs[1].LightSensorsPresent=True
robotConfigs[1].LightSensorsNum=2
robotConfigs[1].RightLightSensorPort=Port.E
robotConfigs[1].LeftLightSensorPort=Port.F
robotConfigs[1].CenterLightSensorPort=False
robotConfigs[1].LeftDriveMotorPort=Port.B
robotConfigs[1].RightDriveMotorPort=Port.A
#
robotConfigs[1].AttachmentsPresent=True
robotConfigs[1].LeftRightAttachments=True
#
robotConfigs[1].TopAttachmentPort=None
robotConfigs[1].TopAttachmentGearsPresent=False
robotConfigs[1].TopAttachmentGearsCfg=None
#
robotConfigs[1].FrontAttachmentPort=None
robotConfigs[1].FrontAttachmentGearsPresent=False
robotConfigs[1].FrontAttachmentGearsCfg=None
#
robotConfigs[1].LeftAttachmentPort=Port.C
robotConfigs[1].LeftAttachmentGearsPresent=False
robotConfigs[1].LeftAttachmentGearsCfg=None
#
robotConfigs[1].RightAttachmentPort=Port.D
robotConfigs[1].RightAttachmentGearsPresent=True
robotConfigs[1].RightAttachmentGearsCfg=[28,36]
#
# robot #3 congfiguration
#

robotConfigs[2].HubName="T2SecondHub"
robotConfigs[2].HubNumber=2
robotConfigs[2].WheelDiameter=56
robotConfigs[2].AxleTrack=199
robotConfigs[2].DefaultStraightSpeed=400
robotConfigs[2].DefaultStraightAcceleration=[500,500]
robotConfigs[2].DefaultTurnAcceleration=[500,500]
robotConfigs[2].DefaultTurnRate=300
robotConfigs[2].LightSensorsPresent=True
robotConfigs[2].LightSensorsNum=2
robotConfigs[2].RightLightSensorPort=Port.E
robotConfigs[2].LeftLightSensorPort=Port.F
robotConfigs[2].CenterLightSensorPort=False
robotConfigs[2].LeftDriveMotorPort=Port.B
robotConfigs[2].RightDriveMotorPort=Port.A
#
robotConfigs[2].AttachmentsPresent=True
robotConfigs[2].LeftRightAttachments=False
#
robotConfigs[2].TopAttachmentPort=Port.C
robotConfigs[2].TopAttachmentGearsPresent=True
robotConfigs[2].TopAttachmentGearsCfg=[20,28]
#
robotConfigs[2].FrontAttachmentPort=Port.D
robotConfigs[2].FrontAttachmentGearsPresent=False
robotConfigs[2].FrontAttachmentGearsCfg=None
#
robotConfigs[2].LeftAttachmentPort=None
robotConfigs[2].LeftAttachmentGearsPresent=False
robotConfigs[2].LeftAttachmentGearsCfg=None
#
robotConfigs[2].RightAttachmentPort=None
robotConfigs[2].RightAttachmentGearsPresent=False
robotConfigs[2].RightAttachmentGearsCfg=None


###########################################
#
# end robot library configuration
#
###########################################


# These are the values for our Gen3 Front Top Attachment Robot
# available https://github.com/bcfletcher/lego_projects/tree/main/BrickLink%20Studio%20Models
#
#   wheel_diameter=56
#   axle_track=199

# These are the values for our New Box Robot
# (currently not available for download)
#
#    wheel_diameter=62.4
#    axle_track=204 
