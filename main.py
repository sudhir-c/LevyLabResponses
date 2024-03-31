from geneutils import GeneUtils

cancerGene = GeneUtils([5.99342831, 4.7234714 , 6.29537708, 8.04605971, 4.53169325, 4.53172609, 8.15842563, 6.53486946, 4.06105123, 6.08512009])
print("Average gene expression: " +  str(cancerGene.calculateMean()))
print("Standard deviation of gene expression: " + str(cancerGene.calculateStandardDeviation()))
print("Number of elements: " + str(cancerGene.returnDataSetLength())) 
print("Proportion of patients to follow up with: " + str(cancerGene.calculateProportionAboveThreshold(4)) + "%")               

