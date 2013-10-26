
"""This mutation operator modifies exactly one gene of an individual
"""
from random import randint, gauss

from mutation import Mutation


class SimpleMutation(Mutation):

    @classmethod
    def mutate(cls, individual):
        random_position = randint(0, len(individual.genes) - 1)
        random_timing = randint(0, 3)
        individual.genes[random_position].times[random_timing] += gauss(0, 1)
