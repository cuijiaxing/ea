import random


class TrafficLight(object):

    times = None

    def __init__(self):
        self.times = [random.uniform(1, 10) for i in xrange(4)]
