import random
class RoadEdge(object):
    
    def __init__(self, e_id, startNode, endNode, priority, numLanes, speed):
        self.id = e_id 
        self.startNode = startNode 
        self.endNode= endNode 
        self.priority = priority 
        self.numLanes = numLanes 
        self.speed = speed
        
    #generate edges from vertical nodes
    @classmethod    
    def generateEdgesFromVerticalNodeList(self, verticalNodeList):
        edgeList = []
        edgeCount = 0
        #first of all generate vertical edges
        for i in xrange(len(verticalNodeList)):
            #and we don't generate vertical edges at the beginning and end of horizontal lines
            if i == 0 or i == len(verticalNodeList) - 1:
                continue
            for j in xrange(len(verticalNodeList[i])):
                if j == len(verticalNodeList[i]) - 1:
                    continue
                else:
                    edgeList.append(RoadEdge(edgeCount, verticalNodeList[i][j].id, verticalNodeList[i][j + 1].id, random.random(1, 100), 1, random.random(1, 10) ))
                edgeCount += 1
            
            #then we generate horizontal edges
            #skip the last colomn 
            if i == len(verticalNodeList) - 1:
                continue
            for j in xrange(len(verticalNodeList[i])):
                if j == 0 or j == len(vetticalNodeList[i]) - 1
            
                
                
                    
                    
                    
                