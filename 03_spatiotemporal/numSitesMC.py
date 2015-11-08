#!/usr/bin/python3

inputFile = open('../data/numSitesMC.csv', 'r')

# header
inputFile.readline()

outputFile = open('MCsites.csv', 'w')
outputFile.write('run;step;value\n')

values = list()

steps = list(range(5500,550,-50))
numRun = 0    

for line in inputFile:
    splitLine = line.strip().split(';')
    for index,value in enumerate(splitLine):
        outputFile.write(str(numRun)+';'+str(steps[index])+';'+value+'\n')
    outputFile.write(str(numRun)+';'+str(550)+';'+splitLine[len(splitLine)-1]+'\n')
    numRun += 1
inputFile.close()        
outputFile.close()

