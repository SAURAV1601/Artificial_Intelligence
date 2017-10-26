import math
import random
import matplotlib.pyplot as plt
#In this algorithm, a new point is generated using the formula newpoint = (r-0.5)*0.1 + oldpoint , where r is a random number between 0 and 1

globalmin=10000
localMinX=0
localMinY=0
globalMinX=0
globalMinY=0
runMinVal=[]
runs=[]
noRuns=100 #number of runs

#returns ackleys function value for given x,y
def ackleysufunction(x,y):
	firstvalue = -20*(math.exp(-0.2*math.sqrt(0.5*(x*x+y*y))))
	secondvalue = math.exp(0.5*(math.cos(2*math.pi*x)+math.cos(2*math.pi*y)))
	return firstvalue-secondvalue

#returns next number on the hill for the given number
def nextValue(val):
	randomNumber=random.uniform(0,1)
	return ((randomNumber-0.5)*0.1)+val

#loop to run the algorithm for given runs
for i in range(1,noRuns+1):
	localmin=10000
	#initializing x and y with random numbers in given domain of ackley's function
	x=random.uniform(-5,5)
	y=random.uniform(-5,5)
	localcount=1
	#this loop breaks when a minimum value is not found in last 100 iterations
	while(1):
		value=ackleysufunction(x,y)
		#checks if the given x,y have minimum ackley's value than the existing value, if so this value is made as minimum for the run
		if value<localmin:
			localmin=value
			localMinX=x
			localMinY=y
			localcount=0
		#incrementing the counter to check if last 100 iterations don't have minimum than exisiting, if they do then counter is set to 0
		localcount+=1
		if localcount==100:
			break
		#gets x and y for next iteration
		x=nextValue(x)
		y=nextValue(y)
	#adds minimum ackley's value to a list on each run
	runMinVal.append(localmin)
	runs.append(i)
	if localmin<globalmin:
		globalmin=localmin
		globalMinX=localMinX
		globalMinY=localMinY
#uncomment below line to display minima of ackley's functions in all the runs
# print globalMinX,globalMinY,globalmin

#Displaying the line chart for minimum in each run
fig = plt.figure(figsize=(11,8))
ax1 = fig.add_subplot(111)

ax1.plot(runs, runMinVal, label='Component 1', color='c', marker='o')
plt.xticks(runs)
plt.xticks(rotation=90)
plt.xlabel('Runs')
plt.show()
plt.savefig('hill_climb.png')
