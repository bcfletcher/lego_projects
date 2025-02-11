# Team 2 Submerged Main menu
#
# menu revision number
menu_revision="18"
#
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task, hub_menu
from umath import sin, pi
from SM_robot_core_rev13 import stopEverything
from SM_t0_rev14 import T0_Run
from SM_t2_rev30 import T2_Run
from SM_t4_rev18 import T4_Run
from SM_t5_rev40 import T5_Run
from SM_t7_rev9 import T7_Run

print("OMMS South FLL Team 2 Submerged Menu, rev#",menu_revision)
print("    Setting Up...")
# Initialize the hub.
hub = PrimeHub()

hub.system.set_stop_button(Button.CENTER)

# Make a menu to choose a letter. You can also use numbers.

# Based on the selection, run a program.
print("    Running Menu")
hub.light.on(Color.BLUE)

while True:
    selected = hub_menu("M","0","2","4","5","7","X")

    try:
        if selected == "M":
            break
        if selected == "0":
            wait(1000)
            run_task(T0_Run())
            run_task(stopEverything())
        elif selected == "2":
            wait(1000)
            run_task(T2_Run())  
            run_task(stopEverything())
        elif selected == "4":
            wait(1000)
            run_task(T4_Run())  
            run_task(stopEverything())
        elif selected == "5":
            wait(1000)
            run_task(T5_Run())  
            run_task(stopEverything())
        elif selected == "7":
            wait(1000)
            run_task(T7_Run())  
            run_task(stopEverything())            
        elif selected == "X":
            run_task(stopEverything())
            break

    except BaseException as menuException:
        print("Stop was Pressed or a Critical Error Occured. Stopping all motors.")
        print(menuException)
        run_task(stopEverything())
        break
    print("    Back to Menu")

print ("End of Menu - if you see this, there might be a problem.")