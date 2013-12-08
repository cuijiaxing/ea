from models.population import Population
from survivor_selection import SurvivorSelection


class Rank(SurvivorSelection):

    @classmethod
    def select(cls, population, offspring):
        """In order to maintain a stable population size, ensure that the result of this population has the same size as the population
        """
        largerPopulation = Population(population.individuals + offspring.individuals)
        sortedIndividuals = sorted(largerPopulation.individuals, key=lambda x: x.fitness, reverse=True)
        return Population(sortedIndividuals[1:population.size()] + [sortedIndividuals[-1]])
