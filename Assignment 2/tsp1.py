import numpy as np
import math
import random
from copy import deepcopy

# This program is to solve a TSP(Travelling Salesman Problem). It includes the following steps
# 1. Selection (roulette wheel method)
# 2. Crossover (cyclic cross over method)
# 3. Mutation (Swap 2 positions at random method)
# The above 3 steps are repeated untill optimum solution is found or till a condition is satisfied

# I have added 2 optimizations for this algorithm, described as follows.
# While selecting paths for population using roulette method, 
# the path with global minimum cost and local minimum cost is automatically added without checking probabilities.
# This would help in reaching the optimum path faster.

cities=0
cityCoord=[]
populationSize=30 # population size
count=0

# Function to calculate the round trip cost of the given path
def calculateCost(list):
	cost=0
	for i in range(0,len(list)):
		for j in range(0,cities):
			if list[i]==cityCoord[j][0]:
				currentCity=j
			if i+1 <len(list):
				if list[i+1]==cityCoord[j][0]:
					nextCity=j
			else:
				nextCity=0
		newcost = distance(cityCoord[currentCity][1],cityCoord[currentCity][2],cityCoord[nextCity][1],cityCoord[nextCity][2])
		cost=cost+newcost
	return cost

# Function to calculate distance between 2 points which has x,y coordinates
def distance(x1,y1,x2,y2):
	return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# taking the input and parsing it to store in 2D array named cityCoord
row=[]
while 1:
	row=raw_input()
	if row=="EOF":
		break
	else:
		cityCoord.append(row.split(" "))
		cities+=1
for i in range(0,cities):
	cityCoord[i][0]=int(cityCoord[i][0])
	cityCoord[i][1]=float(cityCoord[i][1])
	cityCoord[i][2]=float(cityCoord[i][2])

# initializing all variables
population=[]
allPathCost=0
flag=1
globalImpPath=[]
importantPath=[]
minDistance=100000000000000

# constructing initial population with random paths
for i in range(0,populationSize):
	path=random.sample(range(1,cities+1),cities)
	population.append(path)
roundDistance=0

# searching for minimum distance path from initial population and storing the path
for i in range(0,populationSize):
	roundDistance=calculateCost(population[i])
	if(minDistance>roundDistance):
		minDistance=roundDistance
		importantPath=deepcopy(population[i])
globalImpPath=deepcopy(importantPath)

# This loop breaks when there is no minimum cost than the exisiting in the last 1000 iterations
while flag:
	pathCost=[]
	allPathCost=0
	probabilities=[]
	totalProb=0

	# calculating costs of each path in population and cost of all paths in the population
	for i in range(0,populationSize):
		dist=calculateCost(population[i])
		pathCost.append(1/dist)
		allPathCost+=1/dist

	# calculating probabilties of each path for the roulette
	for i in range(0,populationSize):
		totalProb=totalProb+(pathCost[i]/allPathCost)
		probabilities.append(totalProb)

	#adding global minimum path and local minimum path to the population
	newPopulation=[]
	newPopulation.append(globalImpPath)
	newPopulation.append(importantPath)

	#selection of population based on roulette probabilities
	for i in range(0,populationSize-2):
		rouletteRandom=random.uniform(0,1)
		for j in range(0,populationSize):
			if rouletteRandom<probabilities[j]:
				newPopulation.append(population[j])
				break
	population=deepcopy(newPopulation)

	crossoverlist=[]
	# Generating list of cross over agents in the population, whose probability of cross over is less than 0.8
	for i in range(0,populationSize):
		randomNumber=random.uniform(0,1)
		if randomNumber<0.8:
			crossoverlist.append(i)
	#shuffling the generated list
	random.shuffle(crossoverlist)
	crosslen=len(crossoverlist)

	# performing cross over for every first and last agent in the cross over list
	for i in range(0,crosslen/2):
		parent1=population[crossoverlist[i]]
		parent2=population[crossoverlist[crosslen-i-1]]
	
		#generating random positions for crossover
		randCrossOverDivision=(random.sample(range(0,cities),2))
		randCrossOverDivision.sort()

		child1=[0]*cities
		#storing part of parent agent in yet to be generated child agent
		for k in range(randCrossOverDivision[0],randCrossOverDivision[1]):
			child1[k]=parent1[k]

		# Following is the cyclic cross over method where elements of other parent are inherited to child in cyclic order
		j=randCrossOverDivision[1]-1
		for k in range(randCrossOverDivision[1],cities):
			if not parent2[k] in child1:
				j+=1
				if j==cities:
					j=0
				child1[j]=parent2[k]

		for k in range(0,randCrossOverDivision[1]):
			if not parent2[k] in child1:
				j+=1
				if j==cities:
					j=0
				child1[j]=parent2[k]

		#generating another agent from same parents as above
		randCrossOverDivision=(random.sample(range(0,cities),2))
		randCrossOverDivision.sort()

		child2=[0]*cities
		for k in range(randCrossOverDivision[0],randCrossOverDivision[1]):
			child2[k]=parent2[k]
		j=randCrossOverDivision[1]-1

		for k in range(randCrossOverDivision[1],cities):
			if not parent1[k] in child2:
				j+=1
				if j==cities:
					j=0
				child2[j]=parent1[k]

		for k in range(0,randCrossOverDivision[1]):
			if not parent1[k] in child2:
				j+=1
				if j==cities:
					j=0
				child2[j]=parent1[k]
		# comparing cost of parent and child and which ever has a low cost is added to the population
		if calculateCost(parent1) > calculateCost(child1):
			population[crossoverlist[i]]=child1

		if calculateCost(parent2) > calculateCost(child2):
			population[crossoverlist[crosslen-i-1]]=child2

	# performing mutation on each agent of population, if mutation probability is less than 0.8
	# mutation is performed by selecting 2 elements in the agent at random and swapping the 2 elements
	for i in range(0,populationSize):
		randomNumber=random.uniform(0,1)
		if randomNumber<0.8:
			mutRand=random.sample(range(0,cities),2)
			tmp = population[i][mutRand[1]]
			population[i][mutRand[1]] = population[i][mutRand[0]]
			population[i][mutRand[0]] = tmp

	importantPath=[]
	minlocalDistance=100000000

	# calculating local minimum cost and storing its path for next selection
	for i in range(0,populationSize):
		roundDistance=calculateCost(population[i])
		if(minlocalDistance>roundDistance):
			minlocalDistance=roundDistance
			importantPath=deepcopy(population[i])

	# checking if the local minimum cost is less than global minimum cost and if so , updating global minimum cost
	if minlocalDistance<minDistance:
		minDistance=minlocalDistance
		globalImpPath=deepcopy(importantPath)
		count=0

	# incrementing counter to check number of iterations with no new minimum cost and breaking loop if minimum not found in last 1000 iterations
	count+=1
	if count==1000:
		flag=0


print "Minimum Distance for TSP is"
print minDistance











