import random
from models.vehicle_type import VehicleType
class RouteGenerator:
    random.seed(42) #make sure that the experiment is recurrent
    
    #demand per second from different directions
    pEW = 1. / 30
    pEW = 1. /31
    pNS = 1. / 5
    CarTypeNum = 10
    CarNum = 30000
    TotalTimeStep = 36000
    
    
    carTypeList = VehicleType.getARandomCarTypeList(CarTypeNum)
    with open("data/cross.rou.xml", "w") as routes:
        routes.write("<routes>")
        for item in carTypeList:
            print>>routes, """<vType id="{0:d} accel="{1:f}" decel="{2:f}" sigma="{3:f}" length="{4:f}" width="{5:f}" minGap="{6:f}" maxSpeed="{7:f}" guiShape="{8:s}"/>""", format(item.id, item.accel, item.decel, item.sigma, item.length, item.width, item.minGap, item.maxSpeed, item.guiShape)
        
        for i in xrange(CarNum):
            currentCarType = carTypeList[random.randint(len(carTypeList))]
            print >> routes, """<vehicle id="{0:d}" type="{1:d}" route="{2:s}" depart="{0:d}"/>""", format(i, currentCarType.id, "not know", random.randint(TotalTimeStep) )
            
       
    