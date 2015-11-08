#!/usr/bin/python3

inputFile = open('../data/slopeMC.csv', 'r')

# header
inputFile.readline()

outputFile = open('MCslopeVar.csv', 'w')
outputFile.write('run;step;value\n')

values = list()

# 5500 not exist because there is no data
steps = list(range(5450,550,-50))
numRun = 0    

for line in inputFile:
    splitLine = line.strip().split(';')
    # first value is always NA (not previous value)
    for index in range(1,len(splitLine)-1):
        try:
            value1 = float(splitLine[index-1])-float(splitLine[index-2])
            value2 = float(splitLine[index])-float(splitLine[index-1])
            value3 = float(splitLine[index+1])-float(splitLine[index])
            finalValue = (value1+value2+value3)/3
            outputFile.write(str(numRun)+';'+str(steps[index])+';'+str(finalValue)+'\n')
        except ValueError:
            outputFile.write(str(numRun)+';'+str(steps[index])+';\n')
    numRun += 1
inputFile.close()        
outputFile.close()

