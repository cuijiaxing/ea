from random import randint

from models.population import Population


class SimpleGA(object):
  
  def __init__(self):
    pass
  
  def run(self, initialPopulation, rounds, parentSelection, recombination, mutation, survivorSelection):
    population = initialPopulation
    while rounds > 0:
      rounds -= 1
      for individual in population.individuals:
        individual.evaluate_fitness()

      parents = parentSelection.select(population)
      offsprings = recombination.recombine(population)
      for offspring in offsprings.individuals:
        if randint(0, offsprings.size()) == 0:
          mutation.mutate(offspring)
      
      population = survivorSelection.select(population, offsprings)
      