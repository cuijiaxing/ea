import os
class SUMOLog:
    logFileName = "log.txt"
    @classmethod
    def log(cls, content):
        fileWriter = open(cls.logFileName, "a")
        fileWriter.write(content)
        fileWriter.close()
    
    @classmethod   
    def removeFileForLog(cls, fileName):
        cls.logFileName = fileName
        try:
            os.remove(fileName)
        except :
                print("No log file found!\n")