from models.population import Population
from parent_selection import ParentSelection


class Rank(ParentSelection):

    @classmethod
    def select(cls, population, ratio):
        """In order to maintain a stable population size, ensure that the result of this population has the same size as the population
        """
        sortedIndividuals = sorted(population.individuals, key=lambda x: x.fitness, reverse=True)
        return Population(sortedIndividuals[:int(ratio * population.size())])
