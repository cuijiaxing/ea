import random


class TrafficLight(object):

    times = None

    def __init__(self):
        self.times = [random.uniform(1, 10) for _ in xrange(4)]
