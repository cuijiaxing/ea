import random
class Vehicle(object):
    
    def __init__(self, v_id, v_type, route, depart):
        self.id = v_id
        self.type = v_type
        self.routeList = route
        self.depart = depart
        
    
    
    @classmethod
    def generateCarList(cls, carNum, routesList, carTypeList, endTime):
        carList = []
        carNum = len(carTypeList)
        routeNum = len(routesList)
        for i in xrange(carNum):
            carList.append(Vehicle(i, carTypeList[random.randint(carNum)], routesList[random.randint(routeNum)]), endTime * random.random())
        
        return carList 
            
    
    