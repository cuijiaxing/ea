"""
@package simulator
"""
import traci
from models.individual import Individual
class SUMOOnline:
    
    def __init__(self, portNum, individual):
        """
        @param portNum the port that this class can use to evaluate the individuals, also the port num is used to identify a connection to the sumo server
        @param genes the traffic timeing for each traffic light
        """
        
        self.portNum = portNum
        #timing for each traffic light
        self.individual = individual 
    def beginEvaluate(self):
        """
        Given the parameters during initialization, we run the simulator to get the fitness
        using port num to identify a connection
        """
        traci.init(self.portNum, 10, "localhost", str(self.portNum))
        #get all the traffic lights id in the network
        self.trafficLightIdList = traci.trafficlights.getIDList()
        
        #traverse all the traffic lights
        for i in xrange(len(self.trafficLightIdList)):
            #traverse all the traffic lights
            tlsLogicList = traci.trafficlights.getCompleteRedYellowGreenDefinition(self.trafficLightIdList[i])
            #One traffic light has only one phase list now
            tlsLogicList = tlsLogicList[0]
            #each traffic light has several phases
            phaseList = []
            #traverse all the phase
            for j in xrange(len(tlsLogicList._phases)):
                phaseList.append(traci.trafficlights.Phase(self.individual.genes[i].times[j], self.individual.genes[i].times[j], self.individual.genes[i].times[j], tlsLogicList._phases[j]._phaseDef))
            tlsLogicList._phases = phaseList
            traci.trafficlights.setCompleteRedYellowGreenDefinition(self.trafficLightIdList[i], tlsLogicList)
        #close connection
        
        oriLogic =  traci.trafficlights.getCompleteRedYellowGreenDefinition(self.trafficLightIdList[0])
        print(oriLogic[0]._phases[1]._duration)
        
        traci.close()   

if __name__ == "__main__":
    instance = SUMOOnline(8813, Individual.random(16)) 
    instance.beginEvaluate()