from random import uniform

from models.population import Population
from parent_selection import ParentSelection

"""An implementation of n-roulette-wheel fitness-proportional selection
"""


class FitnessProportional(ParentSelection):

    @classmethod
    def select(cls, population):
        matingPool = []
        i = 0
        currentMember = 0
        mu = population.size()
        r = uniform(0, 1.0 / mu)
        fitnessSum = 0
        for individual in population.individuals:
            fitnessSum += individual.fitness
        while currentMember < mu:
            print i, population.individuals[i].fitness / fitnessSum
            while r < population.individuals[i].fitness / fitnessSum:
                print "picking", i
                matingPool.append(population.individuals[i])
                r += 1.0 / mu
                currentMember += 1
            i += 1

        return Population(matingPool)
