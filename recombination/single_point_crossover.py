import random

from models.individual import Individual
from models.population import Population
from recombination import Recombination


class SinglePointCrossover(Recombination):

    @classmethod
    def recombine(cls, population):
        population_size = len(population.individuals)
        fathers = population.individuals[:population_size / 2]
        mothers = population.individuals[population_size / 2:]

        children = []
        for father, mother in zip(fathers, mothers):
            children += cls.single_point_crossover(father, mother)

        return Population(children)

    @classmethod
    def single_point_crossover(cls, father, mother):
        genes_father = father.genes
        genes_mother = mother.genes
        crossover_point = random.randint(0, len(genes_father) - 2)
        genes_son = [genes_father[i] if i <= crossover_point else genes_mother[i] for i in xrange(len(genes_father))]
        genes_daughter = [genes_father[i] if i <= crossover_point else genes_mother[i] for i in xrange(len(genes_father))]
        return [Individual(genes_son), Individual(genes_daughter)]
