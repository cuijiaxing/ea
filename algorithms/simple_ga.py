from random import randint

from models.population import Population

from simulator.sumo_log import SUMOLog


class SimpleGA(object):

    def __init__(self):
        pass

    def run(self, initialPopulation, rounds, parentSelection, recombination, mutation, survivorSelection):
        self.population = initialPopulation
        for currentRound in xrange(rounds):
            self.population.evaluate()

            self.evaluatePopulationMetrics(currentRound)

            parents = parentSelection.select(self.population, 6)
            offsprings = recombination.recombine(parents)
            offsprings.evaluate()

            for offspring in offsprings.individuals:
                if randint(0, offsprings.size()) == 0:
                    mutation.mutate(offspring)

            self.population = survivorSelection.select(self.population, offsprings)

    def evaluatePopulationMetrics(self, currentRound):
        fitnesses = [individual.fitness for individual in self.population.individuals]
        avgFitness = int(sum(fitnesses) / self.population.size())
        maxFitness = int(max(fitnesses))
        print "Round {} | avg fitness {} | max fitness {}\n".format(currentRound, avgFitness, maxFitness)
        champion = self.population.individuals[0]
        print champion.fitness
        print [light.times for light in champion.genes]
