import random

from models.individual import Individual
from recombination.recombination import Recombination


class SinglePointCrossover(Recombination):
  
  @classmethod
  def recombine(cls, individuals):
    if len(individuals) != 2:
      raise Exception("Specify exactly two parents")
    genes_0 = individuals[0].genes
    genes_1 = individuals[1].genes
    crossover_point = random.randint(0, len(genes_0) - 2)
    genes_child_0 = [genes_0[i] if i <= crossover_point else genes_1[i] for i in xrange(len(genes_0))]
    genes_child_1 = [genes_1[i] if i <= crossover_point else genes_0[i] for i in xrange(len(genes_0))]
    return [Individual(genes_child_0), Individual(genes_child_1)]
    