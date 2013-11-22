from random import randint


class TrafficLight(object):

    times = None

    #denote the number of states
    # StateNum = 8

    def __init__(self, numStates):
        self.times = [randint(1, 150) * 1000 for _ in xrange(numStates)]

    def __str__(self):
        return str(self.times)
