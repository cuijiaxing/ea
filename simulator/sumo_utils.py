from models.traffic_light import TrafficLight
import os
class SUMOUtils(object):
    @classmethod
    def changeTrafficLight(cls, individuals, inputFileName, outputFileName):
        fileReader = open(inputFileName, 'r')
        fileWriter = open(outputFileName, 'w')
        trafficLightCount = 0
        for line in fileReader:
            currentStr = line
            if 'phase' in currentStr:
                index = currentStr.find("<")
                strList = currentStr.lstrip(" ").rstrip(" ").split(" ")
                trafficLight = individuals.genes[trafficLightCount / TrafficLight.StateNum]
                trafficTime = trafficLight.times[trafficLightCount % TrafficLight.StateNum]
                durationStr = """duration="%d""" % trafficTime
                fileWriter.write(currentStr[0:index] + strList[0] + " " + durationStr + " " + strList[2])
                trafficLightCount += 1
            else:
                fileWriter.write(currentStr)
        fileReader.close()
        fileWriter.close()        
        os.remove(inputFileName)
        os.rename(outputFileName,inputFileName)
                
# if __name__ == "__main__":
#     individual = Individual.random(16)
#     SUMOUtils.changeTrafficLight(individual, "../road_map/test.net.xml","../road_map/test_temp.net.xml")