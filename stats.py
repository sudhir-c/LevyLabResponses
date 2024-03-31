geneExpressions = [5.99342831, 4.7234714 , 6.29537708, 8.04605971, 4.53169325, 4.53172609, 8.15842563, 6.53486946, 4.06105123, 6.08512009]

# Calculate the mean
mean = sum(geneExpressions) / len(geneExpressions)
print("Average gene expression: " +  str(mean))

# Calculate the standard deviation
squaredDistances = []
for index, value in enumerate(geneExpressions):
    squaredDistances.append((geneExpressions[index] - mean)**2)
standardDev = sum(squaredDistances) / len(squaredDistances)
print("Standard deviation of gene expression: " + str(standardDev))

# Return number of elements
print("Number of elements: " + str(len(geneExpressions))) 
    
# Figure out what proportion of values pass 4
atRisk = 0
for index, value in enumerate(geneExpressions):
    if geneExpressions[index] > 4: 
        atRisk+=1
print("Proportion of patients to follow up with: " + str(100 * atRisk / len(geneExpressions)) + "%")               