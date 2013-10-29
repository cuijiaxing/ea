import os, sys
import optparse
import subprocess
import random
import traci
from fitness_output_retrieve import OutputDataRetriever
class FitnessEvaluator:
    
    PORT = 8813
    N = 3600
    
    @classmethod
    def run(cls): 
        detectorIdList= ["e1det_1i_0", "e1det_2i_0", "e1det_3i_0", "e1det_4i_0"]
        return cls.evaluateFitness("../road_map/data/e1output.xml", detectorIdList, "flow")
        
    @classmethod   
    def evaluateFitness(cls, inputFileName, detectorIdList, targetAttrName):
        fitnessListForEachDetector = []
        summation = 0.0
        for detectorId in detectorIdList:
            fitnessListForEachDetector.append(OutputDataRetriever.average(inputFileName, detectorId, targetAttrName))
        for i in xrange(len(fitnessListForEachDetector)):
            summation += fitnessListForEachDetector[i]
        
        return summation    
            
            
if __name__ == "__main__":
    sumoBinary = "sumo"
    sumoProcess = subprocess.Popen([sumoBinary, "-c", "../road_map/data/cross.sumocfg", "--tripinfo-output", "../road_map/tripinfo.xml"], stdout=sys.stdout, stderr=sys.stderr)
    sumoProcess.wait()
    print(FitnessEvaluator.run())
    