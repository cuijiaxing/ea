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
        #print(traci.simulation.getCurrentTime())
        #get all the traffic lights id in the network
        self.trafficLightIdList = traci.trafficlights.getIDList()
        #traverse all the traffic lights
        for i in xrange(len(self.trafficLightIdList)):
            #traverse all the traffic lights
            tlsLogicList = traci.trafficlights.getCompleteRedYellowGreenDefinition(self.trafficLightIdList[i])
            print len(tlsLogicList)
            #One traffic light has only one phase list now
            tlsLogicList = tlsLogicList[0]
            print tlsLogicList._phases[0]._duration
            #each traffic light has several phases
            phaseList = []
            #traverse all the phase
            for j in xrange(len(tlsLogicList._phases)):
#                 print self.individual.genes[i].times[j]
                phaseList.append(traci.trafficlights.Phase(self.individual.genes[i].times[j], self.individual.genes[i].times[j], self.individual.genes[i].times[j], tlsLogicList._phases[j]._phaseDef))
            tlsLogicList._phases = phaseList
            traci.trafficlights.setCompleteRedYellowGreenDefinition(self.trafficLightIdList[i], tlsLogicList)
        #close connection
        
#         oriLogic =  traci.trafficlights.getCompleteRedYellowGreenDefinition(self.trafficLightIdList[0])
#         print(oriLogic[0]._phases[1]._duration)
        #inductionLoopIdList = traci.inductionloop.getIDList()
        #print(inductionLoopIdList)
        for _ in xrange(100):
            #print traci.simulation.getCurrentTime()
            traci.simulationStep()
            print traci.inductionloop.getLastStepMeanSpeed('e1det_left0to0/0_1')
            #print traci.inductionloop.getLastStepVehicleNumber('e1det_left0to0/0_1')
        traci.close()   
        

if __name__ == "__main__":
    instance = SUMOOnline(8813, Individual.random(16)) 
    instance.beginEvaluate()