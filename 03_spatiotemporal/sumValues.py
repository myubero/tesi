#!/usr/bin/python3

inputFile = open('../data/aoristicValues.csv', 'r')

# header
inputFile.readline()

values = list()

# 98 values, from 5500 to 600 in 50-year intervals 
numValues = int((5500-550)/50)
for i in range(numValues):
    values.append(0.0)

for line in inputFile:
    splitLine = line.strip().split(';')
    initialValue = 4
    i = initialValue
    while i<len(splitLine):
        values[i-initialValue] += float(splitLine[i])
        i += 1

inputFile.close()
outputFile = open('sumValues.csv', 'w')
outputFile.write('step;year;sum\n')
for i in range(numValues):
    outputFile.write(str(i)+';'+str(5500-i*50)+';'+str(values[i])+'\n')
    print(i,'/',(5500-i*50),' -> ' ,values[i])
outputFile.close()

