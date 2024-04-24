cmd=0
dir=1
speed=2

Route = []
Route[0] = ['f',30,400]
Route[1] = ['r',90,300]
Route[2] = ['f',10,400]
Route[3] = ['r',90,300]
Route[4] = ['b',20,200]

for routeStep in range(0,len(Route)):
    print("command dir=",Route[routeStep][cmd], " dir=",Route[routeStep][dir], "  speed=", Route[routeStep][speed])

    