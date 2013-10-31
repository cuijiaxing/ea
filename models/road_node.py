class RoadNode(object):
#     def __init__(self, r_id, r_type, minX, maxX, minY, maxY):
#         self.pos_x = minX + random() * (maxX - minX)
#         self.pos_y = minY + random() * (maxY - minY)
#         self.id = r_id
#         self.type = r_type
       
    #generate a list of node with the number of numOfNodes    
#     @classmethod
#     def generateRoadNodeList(cls, numOfNodes, minX, maxX, minY, maxY):
#         return [cls(i, "priority", minX, maxX, minY, maxY) for i in xrange(numOfNodes)]

    def __init__(self, r_id, r_type, pos_x, pos_y):
        self.id = r_id
        self.type = r_type
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    @classmethod
    def generateGridRoadNodeList(self, minX, maxX, minY, maxY, hNum, vNum):
        length = maxX - minX
        height = maxY - minY
        hStepLength = length / (hNum + 1)
        vStepLength = height/ (vNum + 1)
        roadNodeList = []
        count = 0
        for i in xrange(hNum + 2):
            #vertical node list
            verticalNodeList = []
            pos_x = minX + hStepLength * i
            
            for j in xrange(vNum + 2):
                pos_y = minY + vStepLength * j
                if(pos_x == minX or pos_x == maxX or pos_y == minY or pos_y == maxY):
                    verticalNodeList.append(RoadNode(count, "priority", pos_x, pos_y))
                else:
                    verticalNodeList.append(RoadNode(count, "traffic_light", pos_x, pos_y))
                count += 1
            roadNodeList.append(verticalNodeList)
        return roadNodeList 
    
    