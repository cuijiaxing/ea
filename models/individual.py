from models.traffic_light import TrafficLight
from simulator.simulate import Simulate
from simulator.sumo import SUMO
from os.path import join


class Individual(object):

    timingCounts = [4, 2, 3, 2]
    dataDir = "./"

    def __init__(self, genes):
        self.genes = genes

    @classmethod
    def random(cls, individualSize):
        genes = [TrafficLight(cls.timingCounts[i]) for i in xrange(individualSize)]
        return Individual(genes)

    def evaluateFitness(self, portNum=8813):
        subProcess = SUMO.startSimulator(join(self.dataDir, "test.sumocfg"), portNum=portNum)
        ind = Simulate(portNum, self)
        self.fitness = ind.beginEvaluate()
        subProcess.wait()
