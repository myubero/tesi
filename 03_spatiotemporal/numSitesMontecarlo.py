#!/usr/bin/python
import os, sys, random

# this script calculates the number of active sites per time step from montecarlo simulations

def processSimulation(numSteps, simulationFile, separator, output):
	simulation = open('montecarlo/'+simulationFile, 'r')
	splittedFileLine = simulationFile.replace('.csv','').split('_')
	output.write(splittedFileLine[1]+separator)

	numSites = []
	for siteLine in simulation:
		if siteLine.startswith('id'):
			# beginning, initialize values	
			for i in range(numSteps):
				numSites.append(0)
		else:
			splittedSiteLine = siteLine.split(separator)
			for j in range(numSteps):
				value = int(splittedSiteLine[j+4])
				numSites[j] = numSites[j] + value

	simulation.close()	
	for i in range(numSteps):
		output.write(str(numSites[i])+separator)
	output.write('\n')

def main():

	iniciTotal = 5400
	fiTotal = 550
	timeStep = 50
	separator = ';'

	output = open('results_montecarlo.csv', 'w')
	output.write('numExec'+separator)

	numSteps = 0
	for step in range(iniciTotal, fiTotal, -timeStep):
		output.write(str(step)+separator)
		numSteps = numSteps+1
	
	output.write('\n')

	for root, dirs, simulationFiles in os.walk('montecarlo'):
		for simulationFile in simulationFiles:
			print 'processing simulation results in file: ' + simulationFile
			processSimulation(numSteps, simulationFile, separator, output)
	output.close()

if __name__ == "__main__":
    main()

