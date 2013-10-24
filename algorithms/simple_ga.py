from models.population import Population


class SimpleGA(object):
  
  def __init__(self):
    pass
  
  def run(self, initial_population, rounds, parent_selection, recombination, mutation, survivor_selection):
    population = initial_population
    while rounds > 0:
      rounds -= 1
      for individual in population.individuals:
        individual.evaluate_fitness()

      parents = parent_selection(population)
      # generate off
      offsprings = Population([])
      for offspring in offsprings:
        #TODO introduce a random parameter here
        mutation(offspring)
      
      survivor_selection(offspring)
      
      
      