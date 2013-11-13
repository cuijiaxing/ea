from fitness_output_retrieve import OutputDataRetriever
from simulator_info_retriever import InfoRetriever
from simulate import Simulate


class FitnessEvaluator:

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
        ind = Simulate()
        return ind
