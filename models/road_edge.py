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
                    #they can reach to each other directly
                    priority = random.randint(1, 100)
                    speedLimit = random.random() * 100
                    edgeList.append(RoadEdge(edgeCount, verticalNodeList[i][j].id, verticalNodeList[i][j + 1].id, priority, 1, speedLimit))
                    edgeCount += 1
                    edgeList.append(RoadEdge(edgeCount, verticalNodeList[i][j + 1].id, verticalNodeList[i][j].id, priority, 1, speedLimit))
                    edgeCount += 1
        for i in xrange(len(verticalNodeList)):
            if i == len(verticalNodeList) - 1:
                continue
            
            #then we generate horizontal edges
            #skip the last column 
            if i == len(verticalNodeList) - 1:
                continue
            for j in xrange(len(verticalNodeList[i])):
                if j == 0 or j == len(verticalNodeList[i]) - 1:
                    continue
                else:
                    priority = random.randint(1, 100)
                    speedLimit = random.random() * 100
                    edgeList.append(RoadEdge(edgeCount, verticalNodeList[i][j].id, verticalNodeList[i + 1][j].id, priority, 1, speedLimit))
                    edgeCount += 1
                    edgeList.append(RoadEdge(edgeCount, verticalNodeList[i + 1][j].id, verticalNodeList[i][j].id, priority, 1, speedLimit))
                    edgeCount += 1
                    
        return edgeList 
    
    @classmethod
    def generateEdgesAndWrite2File(els, fileName, nodeList):
        edgeList = RoadEdge.generateEdgesFromVerticalNodeList(nodeList)
        with open(fileName, "w") as printer:
            printer.write("<edges>")
            for edge in edgeList:
                    print >> printer, """<edge id="%d" from="%d" to="%d" priority="%d" numLanes="%d" speed="%f"/>""" % (edge.id, edge.startNode, edge.endNode, edge.priority, edge.numLanes, edge.speed)
            printer.write("</edges>")
        return edgeList
            
    @classmethod
    def generateAdjacentMatrix(cls, nodeList, edgeList):
        #note that nodeList is a collection of column vectors
        adjacentMatrix = [[0 for _ in xrange(len(edgeList))] for _ in xrange(len(edgeList))]
        for i in xrange(len(edgeList)):
            for j in xrange(len(edgeList)):
                if i != j:
                    if edgeList[i].endNode == edgeList[j].startNode:
                        adjacentMatrix[i][j]
                    else:
                        if edgeList[j].endNode == edgeList[i].startNode:
                            adjacentMatrix[j][i] = 1
            
        return adjacentMatrix
        
        
                    
                