

class Population(object):

    individuals = None

    def __init__(self, individuals):
        self.individuals = individuals

    def size(self):
        return len(self.individuals)
