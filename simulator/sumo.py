import subprocess
import sys
class SUMO:

    @classmethod
    def startSimulator(cls, configFileName, portNum=8813):
        pythonCommand = "sumo"
        fh = open("NUL", "w")
        sumoProcess = subprocess.Popen([pythonCommand, "-c", configFileName,"--remote-port", str(portNum)], stdout = fh,stderr = fh)
        return sumoProcess
