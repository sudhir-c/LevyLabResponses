class GeneUtils:
    def __init__(self, geneExpressions: list[float]):
        self.geneExpressions = geneExpressions

    def calculateMean(self) -> float:
        return sum(self.geneExpressions) / len(self.geneExpressions)
    
    def calculateStandardDeviation(self) -> float:
        mean = self.calculateMean()
        squaredDistances = []
        for index, value in enumerate(self.geneExpressions):
            squaredDistances.append((self.geneExpressions[index] - mean)**2)
        return (sum(squaredDistances) / len(squaredDistances))**0.5 
    
    def returnDataSetLength(self) -> int:
        return len(self.geneExpressions)
    
    def calculateProportionAboveThreshold(self, threshold: int) -> float:
        atRisk = 0
        for index, value in enumerate(self.geneExpressions):
            if self.geneExpressions[index] > threshold: 
                atRisk+=1
        return 100 * atRisk / len(self.geneExpressions)        