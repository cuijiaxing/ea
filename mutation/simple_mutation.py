
"""This mutation operator modifies exactly one gene of an individual
"""
from random import randint, gauss

from models.traffic_light import TrafficLight
from mutation import Mutation


class SimpleMutation(Mutation):

    @classmethod
    def mutate(cls, individual):
        random_position = randint(0, len(individual.genes) - 1)
        individual.genes[random_position] = TrafficLight(individual.timingCounts[random_position])
