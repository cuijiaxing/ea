import traci

class Simulate:
    trafficLightIdList = None
    trafficLightIdList = ["65470359", "65535917", "65531994", "65620946"]
    trafficLightPhaseNumList = [4, 2, 3, 2]
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
#                 print self.individual.genes[i].times[j]
                phaseList.append(traci.trafficlights.Phase(self.individual.genes[i].times[j], self.individual.genes[i].times[j], self.individual.genes[i].times[j], tlsLogicList._phases[j]._phaseDef))
            tlsLogicList._phases = phaseList
            traci.trafficlights.setCompleteRedYellowGreenDefinition(self.trafficLightIdList[i], tlsLogicList)

        totalNumPassed = 0
        for _ in xrange(1000):
            traci.simulationStep()
            totalNumPassed = totalNumPassed + traci.simulation.getArrivedNumber()
        traci.close()
        self.fitness = totalNumPassed
        return totalNumPassed 



