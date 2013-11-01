import subprocess
import sys
from models.road_node import RoadNode
from models.road_edge import RoadEdge
from simulator.route_generator import RouteGenerator
class SUMOCommandExecutor(object):
    
    @classmethod
    def generateNetworkFile(cls, nodeFileName, edgeFileName, outputFileName):
        netconvertCommand = "netconvert"
        sumoProcess = subprocess.Popen([netconvertCommand,"--node-files", nodeFileName, "--edge-files", edgeFileName, "--output-file", outputFileName], stdout=sys.stdout, stderr=sys.stderr)
        sumoProcess.wait() 
        print("network file generated successfully")
    
    @classmethod
    def generateE1Detector(cls, networkFileName, detectorLength):
        pythonCommand = "python"
        targetDetectorFile = "../simulator/generateTLSE1Detectors.py"
        sumoProcess = subprocess.Popen([pythonCommand, targetDetectorFile, "--net-file" , networkFileName, "--detector-length", str(detectorLength)], stdout=sys.stdout, stderr=sys.stderr)
        sumoProcess.wait() 
        print("network file generated successfully")
    
    @classmethod
    def startSimulator(cls, configFileName, outputFileName):
        pythonCommand = "sumo"
        sumoProcess = subprocess.Popen([pythonCommand, "-c", configFileName, "--tripinfo-output", outputFileName], stdout = sys.stdout, stderr = sys.stderr)
        sumoProcess.wait()
        print("simulator generated output file succefully")
        
        
        
    
    
    @classmethod
    def generateNodeEdgeAndRoutes(cls):
        nodeList = RoadNode.generateGridRoadNodeList(-500, 500, -500, 500, 4, 4)
        with open("road_map/test.nod.xml", "w") as printer:
            printer.write("<nodes>\n")
            for items in nodeList:
                for j in xrange(len(items)):
                    print >> printer, """<node id="%d" x="%f" y="%f" type="%s"/>""" % (items[j].id, items[j].pos_x, items[j].pos_y, items[j].type)
            printer.write("</nodes>")
        edgeList = RoadEdge.generateEdgesAndWrite2File("road_map/test.edg.xml", nodeList)
        RouteGenerator.generateRouteFile(nodeList, edgeList, 1000, 10, "road_map/test.rou.xml")
        SUMOCommandExecutor.generateNetworkFile("road_map/test.nod.xml", "road_map/test.edg.xml", "road_map/test.net.xml")
        SUMOCommandExecutor.generateE1Detector("road_map/test.net.xml", 100)
    
        
    @classmethod
    def startANewRun(cls, changeNetwork = False): 
        #if there is a need to change the network
        if changeNetwork:
            cls.generateNodeEdgeAndRoutes()
        cls.startSimulator("road_map/test.sumocfg", "road_map/tripinfo.xml")
       
# if __name__ == "__main__":
#     SUMOCommandExecutor.startANewRun(True)