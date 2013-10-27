from models.population import Population
from survivor_selection import SurvivorSelection
from utils import stochastic_universal_sampling


class FitnessProportional(SurvivorSelection):

    @classmethod
    def select(cls, population, offspring):
        """In order to maintain a stable population size, ensure that the result of this population has the same size as the population
        """
        for individual in offspring.individuals:
            individual.evaluateFitness()

        largerPopulation = Population(population.individuals + offspring.individuals)

        return stochastic_universal_sampling.sample(largerPopulation, population.size())
