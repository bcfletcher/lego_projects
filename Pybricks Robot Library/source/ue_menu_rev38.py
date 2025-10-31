# Team 1 Robot menu
#
# menu revision number
menu_revision="38"
#
from pybricks.tools import wait, run_task, hub_menu
import robot_library_rev33 as RL

#
# this is the list of tasks and the main function for each task
# add more as needed. tasks usually consist of 1 or more missions
#
# The name of the task file minus the .py file extension

from ue_t1_rev7 import T1_Run
from ue_t2_rev12 import T2_Run
from ue_t3_rev13 import T3_Run
from ue_t4_rev4 import T4_Run
from ue_t5_rev8 import T5_Run


RL.clearConsole()

print("Robot Menu, rev#",menu_revision)

# uncomment following if you want to enter the hub number manually
#hubNum=input("Enter Hub Number: ")
#initiatizeRobot(int(hubNum))

# 0 = CoachHub
# 1 = T1PrimaryHub
# 2 = T1SecondaryHub
#
# Set your hub number!
HubNum=-1
if HubNum == -1:
    print("ERROR, hub number=",HubNum," is not valid, pick a valid hub number in the menu!")
RL.initiatizeRobot(HubNum)


# Based on the selection, run a task .
print("Running Menu")

while True:
    selected = hub_menu("M","1","2","3","4","5","X")

    try:
        if selected == "M":
            # does nothing. used to show menu is active
            break
        if selected == "1":
            wait(1000)
            run_task(T1_Run())
            run_task(RL.stopEverything())
        elif selected == "2":
            wait(1000)
            run_task(T2_Run())  
            run_task(RL.stopEverything())
        elif selected == "3":
            wait(1000)
            run_task(T3_Run())  
            run_task(RL.stopEverything())
        elif selected == "4":
            wait(1000)
            run_task(T4_Run())  
            run_task(RL.stopEverything())
        elif selected == "5":
            wait(1000)
            run_task(T5_Run())  
            run_task(RL.stopEverything())            
        elif selected == "X":
            # does not nothing used to show end of menu
            run_task(RL.stopEverything())
            break

    except BaseException as menuException:
        print("Stop was Pressed or a Critical Error Occured. Stopping all motors.")
        print(menuException)
        run_task(RL.stopEverything())
        break
    print("    Back to Menu")
