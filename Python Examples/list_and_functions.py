
Done=False
Course=[['fwd',360,1000],
       ['back',360,500],
       ['turn',-90,200]]


CourseStep=0
while CourseStep < len(Course):
    print("CourseStep=",CourseStep)
    Cmd=Course[CourseStep][0]
    Angle=Course[CourseStep][1]
    Speed=Course[CourseStep][2]
    if (Cmd == 'fwd'):
        print("forward ",Angle,"@",Speed)
        MoveFwd(Angle,Speed)
    elif (Cmd == 'back'):
            print("back ",Angle,"@",Speed)
            MoveBack(Angle,Speed)
    elif (Cmd == 'turn'):
            print("turn ",Angle,"@",Speed)
            Turn(Angle,Speed)
    CourseStep = CourseStep + 1
print("done")
