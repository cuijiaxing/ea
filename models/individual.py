from models.traffic_light import TrafficLight
from simulator.simulate import Simulate
from simulator.sumo import SUMO


class Individual(object):
    
    dataDir = "."
    def __init__(self, genes):
        self.genes = genes

    @classmethod
    def random(cls, individualSize):
        genes = [TrafficLight() for _ in xrange(individualSize)]
        return Individual(genes)

    def evaluateFitness(self, portNum=8813):
        subProcess = SUMO.startSimulator(self.dataDir + "test.sumocfg", portNum=portNum)
        ind = Simulate(portNum, self)
        self.fitness = ind.beginEvaluate()
        subProcess.wait()
