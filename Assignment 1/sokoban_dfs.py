from collections import deque
from copy import deepcopy

row=[]
board=[]
rowCount=0
columnCount=0
state=[]
uniquestate=[]
countBlocks=0
isSolutionAvailable=0
moves=[[-1,0],[0,1],[1,0],[0,-1]]
path=['N','E','S','W']

# function to display board
def display_board():
	for i in range(0,rowCount):
		print board[i]
# function to check if board is in goal state or not
def check_solution(sol):
	
	storage_blockCount=0
	
	for i in range(1,len(sol)-1):
		
		if(empty_board[sol[i][0]][sol[i][1]]=='S'):
			
			storage_blockCount+=1
		else:
			return 0
	if(storage_blockCount==countBlocks):
		print 'Solution found, Path to reach goal is  '
		print ', '.join(sol[-1])
		return 1;


#function to check if board is in new state or already visited state
def check_unique_state(state):
	
	new_state=deepcopy(state)
	new_state=new_state[:-1]
	# if the state is not in visited state, it is added to visited states list 
	if new_state not in uniquestate:
		
		uniquestate.append(new_state)
		d.append(state)

# taking input board

while(1):
	row=raw_input()
	if row=="":
		break
	else:
		board.append([])
		for i in range(0,len(row)):
			board[-1].append(row[i])
		
		rowCount+=1
		if(len(row)>columnCount):
			columnCount=len(row)


# Uncomment following 2 lines to view input board  
# print 'Input board is '
# display_board()

# parsing the input board 
empty_board=deepcopy(board)
for i in range(0,rowCount):
	for j in range(0,columnCount):
		if(board[i][j]=='R'):
			state.append([i,j])
			empty_board[i][j]=' '
		if board[i][j]=='#':
			state.append([i,j])
			empty_board[i][j]='S'

for i in range(0,rowCount):
	for j in range(0,columnCount):
		if(board[i][j]=='B'):
			state.append([i,j])
			empty_board[i][j]=' '
			countBlocks+=1
		if board[i][j]=='@':
			state.append([i,j])
			empty_board[i][j]='S'
			countBlocks+=1

state.append([])

d=deque()

check_unique_state(state)

print 'Finding solution for the board using Depth First Search'

# loop for each state in the queue
while(len(d)>0):
	# popping the first state in the queue
	currentstate=d.pop()
	
	changed_board=deepcopy(empty_board)
	changed_board[currentstate[0][0]][currentstate[0][1]]='R'
	for i in range(1,len(currentstate)-1):
		changed_board[currentstate[i][0]][currentstate[i][1]]='B'

	#  Uncomment the below 2 lines to print the board state after robo made a move
	# for i in range(0,rowCount):
	# 	print changed_board[i]
	board=[]
	board=deepcopy(changed_board)

	if check_solution(currentstate):
		isSolutionAvailable=1
		break
	# loop to check for 4 possible movements of robo
	for i in range(0,len(moves)):
		newx=currentstate[0][0]+moves[i][0]
		newy=currentstate[0][1]+moves[i][1]
		
		if(newx>=0 and newx<rowCount and newy>=0 and newy<columnCount):

			if(board[newx][newy]=='S' or board[newx][newy]==' '):
				# print 'robo in empty space or storage space'
				newstate=deepcopy(currentstate)
				newstate[0][0]=newx
				newstate[0][1]=newy
				newstate[-1].append(path[i])
				
				check_unique_state(newstate)
			
			else:
				if(board[newx][newy]=='O'):
					# print 'robo hitting wall'
					pass
				else:
					
					# print 'robo pushing block'
					for j in range(1,len(currentstate)-1):
						
						if newx==currentstate[j][0] and newy==currentstate[j][1]:
							# check if block can move or not
							if board[newx+moves[i][0]][newy+moves[i][1]]=='S' or board[newx+moves[i][0]][newy+moves[i][1]]==' ' :
								newstate=deepcopy(currentstate)
								newstate[0][0]=newx
								newstate[0][1]=newy
								newstate[j][0]=currentstate[j][0]+moves[i][0]
								newstate[j][1]=currentstate[j][1]+moves[i][1]
								newstate[-1].append(path[i])
							
								check_unique_state(newstate)
							break
# board has no solution if the queue is empty and goal state is still not found
if len(d)==0 or isSolutionAvailable==0:
	print 'Solution not available for the board'




			





























