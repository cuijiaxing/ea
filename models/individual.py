from random import random

from models.traffic_light import TrafficLight


class Individual(object):

    genes = None

    def __init__(self, genes):
        self.genes = genes

    @classmethod
    def random(cls, individualSize):
        genes = [TrafficLight() for i in xrange(individualSize)]
        return Individual(genes)

    def evaluate_fitness(self):
        #TODO implement by Cuijiaxing
        self.fitness = random()
