from fitness_output_retrieve import OutputDataRetriever
from simulator_info_retriever import InfoRetriever
from simulator.sumo_command import SUMOCommandExecutor
class FitnessEvaluator:
    
    PORT = 8813
    N = 3600
    
    @classmethod
    def run(cls): 
        detectorIdList= InfoRetriever.getDetectorList("../road_map/e1.add.xml")
        return cls.evaluateFitness("../road_map/e1output.xml", detectorIdList, "flow")
        
    @classmethod   
    def evaluateFitness(cls, inputFileName, detectorIdList, targetAttrName):
        fitnessListForEachDetector = []
        summation = 0.0
        for detectorId in detectorIdList:
            fitnessListForEachDetector.append(OutputDataRetriever.getFlowFromOneDetector(inputFileName, detectorId, targetAttrName))
        for i in xrange(len(fitnessListForEachDetector)):
            summation += fitnessListForEachDetector[i]
        return summation    
            
            
if __name__ == "__main__":
#     sumoBinary = "sumo"
#     sumoProcess = subprocess.Popen([sumoBinary, "-c", "../road_map/data/cross.sumocfg", "--tripinfo-output", "../road_map/tripinfo.xml"], stdout=sys.stdout, stderr=sys.stderr)
#     sumoProcess.wait()
#     print(FitnessEvaluator.run())
    SUMOCommandExecutor.startANewRun()
    print(FitnessEvaluator.run())
    