from models.individual import Individual


class Population(object):
  
  individuals = None
  
  def __init__(self, populationSize, individualSize):
    #TODO implement this
    self.individuals = [Individual.random(individualSize) for i in xrange(populationSize)]
