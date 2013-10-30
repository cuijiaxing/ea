import random
class VehicleType(object):
    id= 0 #the id of the vehicle type
    accel = 0 # the accelerate rate of the vehicle
    decel= 0 # the decelerate rate of the vehicle
    sigma = 0 # the intervention of the driver
    length = 0 # the length of the car
    width = 0 # the width of the vehicle
    minGap = 0 # the minimum gap of cars between cars when they park
    maxSpeed = 0 # the max speed the car can get to 
    guiShapeArray = ["private",
                     "public_transport",
                     "public_emergency",
                     "public_authority",
                      "public_army",
                      "vip",
                      "ignoring",
                      "passenger",
                      "hov",
                      "taxi",
                      "bus",
                      "delivery",
                      "transport",
                      "lightrail",
                      "cityrail",
                      "rail_slow",
                      "rail_fast",
                      "motorcycle",
                      "bicycle",
                      "pedestrian",
                      "custom1",
                      "custom2"];
                      
    guiShape = guiShapeArray[0]
    
    def __init__(self, v_id):
        self.generateAVehicleTypeRandomly(v_id, 0, 10, 0, 10, -1, 1, 10, 1, 10, 1, 10, 1, 10, None)
    
    def generateAVehicleTypeRandomly(self, v_id, minAccel, maxAccel, minDecel, maxDecel, sigma, minLength, maxLength, minWidth, maxWidth, minMinGap, maxMinGap, minMaxSpeed, maxMaxSpeed, carGUI):
        if minAccel > maxAccel:
            raise Exception("minAccel should be less than maxAccel")
        if minDecel > maxDecel:
            raise Exception("minDecel shoudld be less than maxAccel")
        if minLength > maxLength:
            raise Exception("minLength should be less than maxLength")
        if minWidth > maxLength:
            raise Exception("minWidth should be less than maxLength")
        if minMinGap > maxMinGap:
            raise Exception("minMinGap should be less than maxMinGap")
        if minMaxSpeed > maxMaxSpeed:
            raise Exception("minmaxSpeed should be less than maxMaxSPeed")
        
        self.id= v_id #the id of the vehicle type
        self.accel = random.uniform(minAccel, maxAccel) # the accelerate rate of the vehicle
        self.decel= random.uniform(minDecel, maxDecel) # the decelerate rate of the vehicle
        if sigma == -1:
            self.sigma = random.random() # the intervention of the driver
        elif sigma < 0 or sigma > 1:
                raise Exception("sigma should be less 1 and positive")
        else:
                self.sigma = sigma
        self.length = random.uniform(minLength, maxLength) # the length of the car
        self.width = random.uniform(minWidth, maxWidth) # the width of the vehicle
        self.minGap = random.uniform(minMinGap, maxMinGap) # the minimum gap of cars between cars when they park
        self.maxSpeed = random.uniform(minMaxSpeed, maxMaxSpeed) # the max speed the car can get to
        

        if carGUI == None or carGUI not in self.guiShapeArray:
            self.guiShape = self.guiShapeArray[random.randint(0, len(self.guiShapeArray))]
        else:
            self.guiShape = carGUI
       
    @classmethod   
    def getARandomCarTypeList(cls, num):
        return [VehicleType(i) for i in xrange(num)]
    
# if __name__ == "__main__":
#     carTypeList = VehicleType.getARandomCarTypeList(10)
#     for item in carTypeList:
#         print item.guiShape

    
    
        
        
        