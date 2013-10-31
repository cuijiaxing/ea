import random
from models.vehicle import Vehicle
from models.road_route import RoadRoute
from models.vehicle_type import VehicleType
from models.road_edge import RoadEdge


class RouteGenerator:
    random.seed(42) #make sure that the experiment is recurrent
    
    #demand per second from different directions
    CarTypeNum = 10
    CarNum = 30000
    TotalTimeStep = 36000
    
    
    #This is a facade method
    #take nodelist and edgelist as input
    @classmethod
    def generateRouteFile(cls, nodeList, edgeList, carNum, carTypeNum, fileName):
        adjacentMatrix = RoadEdge.generateAdjacentMatrix(nodeList, edgeList)
        routesList = RoadRoute.generateRoutes(adjacentMatrix)
        vehicleTypeList = VehicleType.getARandomCarTypeList(carTypeNum)
        Vehicle.generateCarList(carNum, routesList, vehicleTypeList, cls.TotalTimeStep)
        carTypeList = VehicleType.getARandomCarTypeList(cls.CarTypeNum)
        carList= Vehicle.generateCarList(carNum, routesList, carTypeList, cls.TotalTimeStep)
        
        
        with open(fileName, "w") as routes:
            routes.write("<routes>\n")
            for item in carTypeList:
                routes.write(str(item) + "\n")
            
            for item in routesList:
                routes.write(str(item) + "\n")
            
            for item in carList:
                routes.write(str(item) + "\n")
            routes.write("</routes>")
        
        print("Route File generated successfully")
            
       
    