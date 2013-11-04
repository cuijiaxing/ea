import os
class SUMOLog:
    logFileName = "log.txt"
    globalOptimumFitness = 0
    globalOptimumIndividual = None
    
    
    @classmethod
    def recordBest(cls, fitness, genes):
        outputFile = open("kkk.txt", "a")
        outputFile.write(str(fitness) + "\n")
        if fitness > cls.globalOptimumFitness:
            cls.globalOptimumIndividual = genes
            cls.globalOptimumFitness = fitness
        outputFile.close();
    
    
    @classmethod
    def convertGenesToStr(cls, genes):
        geneStr = ""
        for light in genes:
            geneStr += str(light) + "\r\n"
        return geneStr
    
    @classmethod
    def writeBestToFile(cls, fileName):
        outputFile = open(fileName, "w")
        outputFile.write("BestFitness" + "\r\n")
        outputFile.write(str(cls.globalOptimumFitness) + "\r\n")
        outputFile.write("BestGene" + "\r\n")
        outputFile.write(cls.convertGenesToStr(cls.globalOptimumIndividual))
        outputFile.close()
        
            
    @classmethod
    def log(cls, fitness, genes):
        
        #record best individual
        cls.recordBest(fitness, genes)
        
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
    