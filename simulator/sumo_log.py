import os
class SUMOLog:
    logFileName = "log.txt"
    globalOptimumFitness = 0
    globalOptimumIndividual = None
    @classmethod
    def log(cls, fitness, genes):
        fileWriter = open(cls.logFileName, "a")
        fileWriter.write("fitness=" + str(fitness) + "\n")
        for gene in genes:
            fileWriter.write(str(gene) + "\n")
        fileWriter.close()
    
    @classmethod   
    def removeFileForLog(cls, fileName):
        cls.logFileName = fileName
        try:
            os.remove(fileName)
        except :
                print("No log file found!\n")