from lxml import etree

class OutputDataRetriever(object):
    def __init__(self, detectorId, attributeId):
        self.summation = 0.0
        self.detectorId = detectorId
        self.attributeId = attributeId
    
    def start(self, tag, attrib):
        if tag == "interval" and attrib["id"] == self.detectorId:
            self.summation += float(attrib[self.attributeId])
    def data(self, data):
        pass 
        
    def end(self, tag):
        pass
        
    def close(self):
        return self.summation
    
    #calculate the flow for one single detector
    @classmethod
    def getFlowFromOneDetector(cls, inputFileName, detectorId, targetAttributeName):
        parser = etree.XMLParser(target = OutputDataRetriever(detectorId, targetAttributeName))
        return etree.parse(inputFileName, parser)