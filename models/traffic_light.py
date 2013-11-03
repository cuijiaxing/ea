import random


class TrafficLight(object):

    times = None
    
    #denote the number of states
    StateNum = 8

    def __init__(self):
        self.times = [random.randint(1, 100) for _ in xrange(self.StateNum)]
    
    def __str__(self):
        return str(self.times)
#         strLight = ""
#         for light in self.times:
#             strLight += str(light)
#         return strLight
