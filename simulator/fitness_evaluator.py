from fitness_output_retrieve import OutputDataRetriever
from simulator_info_retriever import InfoRetriever
from simulator.sumo_command import SUMOCommandExecutor
from simulator.sumo_utils import SUMOUtils
class FitnessEvaluator:
    
    PORT = 8813
    N = 3600
    
    @classmethod
    def run(cls): 
        detectorIdList= InfoRetriever.getDetectorList("road_map/e1.add.xml")
        return cls.evaluateFitness("road_map/e1output.xml", detectorIdList, "flow")
        
    @classmethod   
    def evaluateFitness(cls, inputFileName, detectorIdList, targetAttrName):
        fitnessListForEachDetector = []
        summation = 0.0
        for detectorId in detectorIdList:
            fitnessListForEachDetector.append(OutputDataRetriever.getFlowFromOneDetector(inputFileName, detectorId, targetAttrName))
        for i in xrange(len(fitnessListForEachDetector)):
            summation += fitnessListForEachDetector[i]
        return summation    
    
    @classmethod
    def getEvaluationResult(cls, inputTrafficLights):
        SUMOUtils.changeTrafficLight(inputTrafficLights, "road_map/test.net.xml", "road_map/testtemp.net.xml")
        SUMOCommandExecutor.startANewRun(False)
        return FitnessEvaluator.run()
    
            
#     sumoBinary = "sumo"
#     sumoProcess = subprocess.Popen([sumoBinary, "-c", "../road_map/data/cross.sumocfg", "--tripinfo-output", "../road_map/tripinfo.xml"], stdout=sys.stdout, stderr=sys.stderr)
#     sumoProcess.wait()
#     print(FitnessEvaluator.run())
    #start a new run and do not generate new newwork
    
# if __name__ == "__main__":
#     SUMOCommandExecutor.startANewRun(True)
#     print(FitnessEvaluator.run())