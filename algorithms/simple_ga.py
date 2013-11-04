from random import randint

from models.population import Population

from simulator.sumo_log import SUMOLog


class SimpleGA(object):

    def __init__(self):
        pass

    def run(self, initialPopulation, rounds, parentSelection, recombination, mutation, survivorSelection):
        self.population = initialPopulation
        for currentRound in xrange(rounds):
            for individual in self.population.individuals:
                individual.evaluateFitness()

            self.evaluatePopulationMetrics(currentRound)

            parents = parentSelection.select(self.population, 0.5)
            offsprings = recombination.recombine(parents)
            for offspring in offsprings.individuals:
                if randint(0, offsprings.size()) == 0:
                    mutation.mutate(offspring)

            self.population = survivorSelection.select(self.population, offsprings)

        #write best to file
        SUMOLog.writeBestToFile("BestLog.txt")

    def evaluatePopulationMetrics(self, currentRound):
        fitnesses = [individual.fitness for individual in self.population.individuals]
        avgFitness = sum(fitnesses) / self.population.size()
        maxFitness = max(fitnesses)
        print "Round {} | avg fitness {} | max fitness {}".format(currentRound, avgFitness, maxFitness)
        
