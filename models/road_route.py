import random
class RoadRoute(object):
    
    def __init__(self, routeId, edgeList):
        self.routeId = routeId
        self.edgeList = edgeList
        
    
    
    @classmethod
    def generateRoutes(cls, adjacentMatrix):
        numOfNodes = len(adjacentMatrix)
        routesList = []
        for i in xrange(numOfNodes):
            routesList.append(RoadRoute(i, cls.generateARoute(adjacentMatrix, i, random.randint(1, numOfNodes))))
        
        return routesList    
    
    
    
    @classmethod
    def generateARoute(cls, adjacentMatrix, startNode, numOfSteps):
        routeNodeList = []
        routeNodeList.append(startNode)
        stepCount = 0
        numOfNodes = len(adjacentMatrix)
        while(stepCount < numOfSteps):
            foundAdjacent = False
            for i in xrange(numOfNodes):
                if adjacentMatrix[startNode][i] ==1 :
                    stepCount += 1
                    startNode = i
                    foundAdjacent = True
                    routeNodeList.append(i)
            if foundAdjacent == False:
                break;
        return routeNodeList   
    
    def __str__(self): 
        edgeStr = ""
        edgeNum = len(self.edgeList)
        for i in xrange(edgeNum):
            edgeStr += str(self.edgeList[i])
            if i != edgeNum - 1:
                edgeStr += " "
        return """<route id="%d" edges="%s"/>""" % (self.routeId, edgeStr)
        
        