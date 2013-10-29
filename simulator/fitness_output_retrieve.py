import xml.etree.ElementTree as ET


class OutputDataRetriever(object):
    
    @classmethod
    def average(cls, inputFileName, nodeId, attrName):
        tree = ET.parse(inputFileName)
        root = tree.getroot()
        summation= 0.0
        count = 0
        for child in root:
            if child.get('id') == nodeId:
                summation += float(child.get(attrName))
                count += 1
        
        if count == 0:
            return 0
        else:
            return summation / count        
    

if __name__ == "__main__":
    print(OutputDataRetriever.average("../road_map/data/e1output.xml", 'e1det_1i_0', 'flow'))