import random
class Vehicle(object):
    
    def __init__(self, v_id, v_type, routeId, depart):
        self.id = v_id
        self.type = v_type
        self.routeId = routeId
        self.depart = depart
        
    
    
    @classmethod
    def generateCarList(cls, carNum, routesList, carTypeList, endTime):
        carList = []
        carTypeNum = len(carTypeList)
        routeNum = len(routesList)
        for i in xrange(carNum):
            carList.append(Vehicle(i, carTypeList[random.randint(1, carTypeNum - 1)].id, routesList[random.randint(1, routeNum - 1)].routeId, endTime * random.random()))
            
        #sort the car list
        carList = sorted(carList, key = lambda car:car.depart)
        return carList
            
    def __str__(self): 
        return """<vehicle id="%d" type="%d" route="%d" depart="%f"/>""" % (self.id, self.type, self.routeId, self.depart)
    