from models.traffic_light import TrafficLight
from simulator.simulate import Simulate
from simulator.sumo import SUMO



class Individual(object):

#    genes = None

    def __init__(self, genes):
        self.genes = genes

    @classmethod
    def random(cls, individualSize):
        genes = [TrafficLight() for _ in xrange(individualSize)]
        return Individual(genes)

    def evaluateFitness(self):
        subProcess = SUMO.startSimulator("sumo/test.sumocfg")
        ind = Simulate(8813, self)
        self.fitness = ind.beginEvaluate()
        subProcess.wait()
        
        
