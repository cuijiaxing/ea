from random import random

class RoadNode(object):
    pos_x = 0
    pos_y = 0
    
    def __init__(self, minX, maxX, minY, maxY):
        self.pos_x = minX + random() * (maxX - minX)
        self.pos_y = minY + random() * (maxY - minY)
       
    #generate a list of node with the number of numOfNodes    
    @classmethod
    def generateRoadNodeList(cls, numOfNodes, minX, maxX, minY, maxY):
        return [cls(minX, maxX, minY, maxY) for _ in xrange(numOfNodes)]