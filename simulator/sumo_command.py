import subprocess
import sys
class SUMOCommandExecutor(object):
    
    @classmethod
    def generateNetworkFile(cls, nodeFileName, edgeFileName, outputFileName):
        netconvertCommand = "netconvert"
        sumoProcess = subprocess.Popen([netconvertCommand,"--node-files", nodeFileName, "--edge-files", edgeFileName, "--output-file", outputFileName], stdout=sys.stdout, stderr=sys.stderr)
        sumoProcess.wait() 
        print("network file generated successfully")
    
    @classmethod
    def generateE1Detector(cls, networkFileName, detectorLength):
        pythonCommand = "python"
        targetDetectorFile = "../simulator/generateTLSE1Detectors.py"
        sumoProcess = subprocess.Popen([pythonCommand, targetDetectorFile, "--net-file" , networkFileName, "--detector-length", str(detectorLength)], stdout=sys.stdout, stderr=sys.stderr)
        sumoProcess.wait() 
        print("network file generated successfully")
        
        
    
    