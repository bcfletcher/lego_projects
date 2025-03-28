# Team 2 Submerged Main menu
#
# menu revision number
menu_revision="26"
#
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task, hub_menu
from umath import sin, pi
#he name of the task file minus the .py file extension
#
from box_robot_task1_rev16 import box_robot_task1
#from t0_rev1 import *

# update robot config and library rev # as needed
from robot_library_config_rev7 import *
from robot_library_rev23 import *
#
# this is the list of tasks and the main function for each task
# add more as needed. tasks usually consist of 1 or more missions
#
# the "from" is trt T0_Run
#from t1_rev1 import T1_Run
#from t2_rev1 import T3_Run
#from t3_rev1 import T3_Run
#from t4_rev1 import T4_Run

clearConsole()

print("Robot Menu, rev#",menu_revision)

# uncomment following if you want to enter the hub number manually
#hubNum=input("Enter Hub Number: ")
#initiatizeRobot(int(hubNum))

initiatizeRobot(-1)


# Based on the selection, run a task .
print("    Running Menu")

while True:
    selected = hub_menu("M","1","2","3","4","5","X")

    try:
        if selected == "M":
            # does nothing. used to show menu is active
            break
        if selected == "1":
            #hub.speaker.beep()
            wait(1000)
            run_task(box_robot_task1())
            run_task(stopEverything())
        elif selected == "2":
            wait(1000)
            #run_task(box_robot_task2())  
            run_task(stopEverything())
        elif selected == "3":
            wait(1000)
            #run_task(T2_Run())  
            run_task(stopEverything())
        elif selected == "4":
            wait(1000)
            #run_task(T3_Run())  
            run_task(stopEverything())
        elif selected == "5":
            wait(1000)
            #run_task(T4_Run())  
            run_task(stopEverything())            
        elif selected == "X":
            # does not nothing used to show end of menu
            run_task(stopEverything())
            break

    except BaseException as menuException:
        print("Stop was Pressed or a Critical Error Occured. Stopping all motors.")
        print(menuException)
        run_task(stopEverything())
        break
    print("    Back to Menu")

print ("End of Menu - if you see this, there might be a problem.")