from random import randint


class TrafficLight(object):

    times = None

    #denote the number of states
    StateNum = 8

    def __init__(self):
        self.times = [randint(1, 100) * 1000 for _ in xrange(self.StateNum)]

    def __str__(self):
        return str(self.times)
