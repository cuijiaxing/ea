from random import uniform

from models.population import Population


# from http://stackoverflow.com/questions/13221896/python-partial-sum-of-numbers
def partial_sums(iterable):
    total = 0
    for i in iterable:
        total += i
        yield total


def sample(population, sampleSize):
    pool = []
    i = 0
    currentMember = 0
    mu = sampleSize
    r = uniform(0, 1.0 / mu)
    individuals = population.individuals
    fitnessSum = 0
    for individual in individuals:
        fitnessSum += individual.fitness
    fitnessProbabilities = [individual.fitness / fitnessSum for individual in individuals]
    cumulativeProbabilities = list(partial_sums(fitnessProbabilities))
    while currentMember < mu:
        while r < cumulativeProbabilities[i]:
            pool.append(individuals[i])
            r += 1.0 / mu
            currentMember += 1
        i += 1

    return Population(pool)
