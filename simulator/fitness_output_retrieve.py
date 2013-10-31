import xml.etree.ElementTree as ET


class OutputDataRetriever(object):
    
    #It uses too much memory, we have to change the parsing method
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