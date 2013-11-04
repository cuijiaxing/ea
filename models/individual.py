from simulator.fitness_evaluator import FitnessEvaluator

from models.traffic_light import TrafficLight

from simulator.sumo_log import SUMOLog


class Individual(object):

#    genes = None

    def __init__(self, genes):
        self.genes = genes

    @classmethod
    def random(cls, individualSize):
        genes = [TrafficLight() for _ in xrange(individualSize)]
        return Individual(genes)

    def evaluateFitness(self):
        self.fitness = FitnessEvaluator.getEvaluationResult(self)

        SUMOLog.log(self.fitness, self.genes)

        #print self.fitness
