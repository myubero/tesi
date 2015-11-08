#!/usr/bin/python
import sys


#!/usr/bin/python
import os, sys, random

def parseLine( numExec, fo, line, separator, iniciTotal, fiTotal, timeStep):
	splittedLine = line.split(separator)
	# if id already registered we need to skip this part
	idSite = splittedLine[0]
	name = splittedLine[1]
	x = splittedLine[2]
	y = splittedLine[3]
	i = 4
	print 'simulating site: ' + name + ' for execution: ' + str(numExec+1)
	fo.write(idSite+separator+name+separator+x+separator+y+separator)
	for timeStep in range (iniciTotal, fiTotal, -timeStep):
		weight = float(splittedLine[i].replace(',','.'))
		if weight > 0.0:
			#print 'site: ' + name + ' contributing with weight: ' + str(weight) + ' to time step: ' + str(timeStep)
			if random.random()<float(weight):
				fo.write('1'+separator)
			else:
				fo.write('0'+separator)
		else:
			fo.write('0'+separator)

		i = i+1
	fo.write('\n')

def main():

	executions = 1000

	iniciTotal = 5400
	fiTotal = 550
	timeStep = 50
	separator = ';'


	if not os.path.exists('montecarlo'):
	    os.makedirs('montecarlo')

	simulations = []
	print 'creating ' + str(executions) + ' simulations...'
	for numExec in range(0,executions):
		simulations.append(open('montecarlo/simulation_'+str(numExec+1)+'.csv','w'))
	print 'done'

	f = open('aoristicValues.csv', 'r')
	for line in f:
		for numExec in range(0, executions):
			fo = simulations[numExec]
			if line.startswith('id'):
				#print 'Header: ' + line
				fo.write(line)
			else:
				parseLine( numExec, fo, line, separator, iniciTotal, fiTotal, timeStep )
	f.close()
	
	print 'closing ' + str(executions) + ' simulations...'
	for numExec in range(0,executions):
		simulations[numExec].close()
	print 'done'

if __name__ == "__main__":
    main()

