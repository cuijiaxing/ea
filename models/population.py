from models.individual import Individual


class Population(object):

    individuals = None

    def __init__(self, populationSize, individualSize):
        self.individuals = [Individual.random(individualSize) for i in xrange(populationSize)]

    def size(self):
        return len(self.individuals)
