import xml.etree.ElementTree as ET
class InfoRetriever(object):
    
    #get all the detector ids from the id file
    @classmethod
    def getDetectorList(self, inputFileName):
        tree = ET.parse(inputFileName)
        root = tree.getroot()
        detectorIdList = []
        for child in root:
            detectorIdList.append(child.get('id'))
        return detectorIdList
    
    
    
    
# if __name__ == "__main__":
#     print len(InfoRetriever.getDetectorList("../road_map/data/e1.add.xml"))