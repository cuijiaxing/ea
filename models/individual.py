from simulator.fitness_evaluator import FitnessEvaluator

from models.traffic_light import TrafficLight


class Individual(object):

#    genes = None

    def __init__(self, genes):
        self.genes = genes

    @classmethod
    def random(cls, individualSize):
        genes = [TrafficLight() for _ in xrange(individualSize)]
        return Individual(genes)

    def evaluateFitness(self):
        #TODO implement by Cuijiaxing
        self.fitness = FitnessEvaluator.getEvaluationResult(self)
        
if __name__ == "__main__":
    ind = Individual.random(16)
    print ind.evaluateFitness()
    

