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
storage_coord=[]

def display_board():
	for i in range(0,rowCount):
		print board[i]

def check_solution(sol):
	
	storage_blockCount=0
	# for i in range(0,rowCount):
	# 	print empty_board[i]
	
	for i in range(1,len(sol)-1):
		# print sol[i]
		if(empty_board[sol[i][0]][sol[i][1]]=='S'):
			# print 'in storage'
			storage_blockCount+=1
		else:
			return 0
	if(storage_blockCount==countBlocks):
		print 'Solution found, Path to reach goal is  '
		print ', '.join(sol[-1])
		return 1;



def check_unique_state(state):
	
	new_state=deepcopy(state)
	new_state=new_state[:-1]
	
	if new_state not in uniquestate:
		
		uniquestate.append(new_state)
		d.append(state)


	
def man_distance(p1,p2):
	distance=abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
	return distance



# print "enter board"
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


# print 'your input board is '
# display_board()

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

		if board[i][j]=='S' or board[i][j]=='@' or board[i][j]=='#':
			storage_coord.append([i,j])

# print 'storagessss'
# print storage_coord

state.append([])

d=deque()

check_unique_state(state)

print 'Solution using A* Search'

while(len(d)>0):
	# print 'pop'

	currentstate=d.popleft()
	# print currentstate[-1]
	changed_board=deepcopy(empty_board)
	changed_board[currentstate[0][0]][currentstate[0][1]]='R'
	for i in range(1,len(currentstate)-1):
		changed_board[currentstate[i][0]][currentstate[i][1]]='B'
	# for i in range(0,rowCount):
	# 	print changed_board[i]
	board=[]
	board=deepcopy(changed_board)


	# print currentstate
	if check_solution(currentstate):
		isSolutionAvailable=1
		break
	for i in range(0,len(moves)):
		newx=currentstate[0][0]+moves[i][0]
		newy=currentstate[0][1]+moves[i][1]
		
		if(newx>=0 and newx<rowCount and newy>=0 and newy<columnCount):

			if(board[newx][newy]=='S' or board[newx][newy]==' '):
				# print 'in empty'
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
					# print board[newx][newy]
					# print 'blockk'
					for j in range(1,len(currentstate)-1):
						
						if newx==currentstate[j][0] and newy==currentstate[j][1]:
							if board[newx+moves[i][0]][newy+moves[i][1]]=='S' or board[newx+moves[i][0]][newy+moves[i][1]]==' ' :
								newstate=deepcopy(currentstate)
								newstate[0][0]=newx
								newstate[0][1]=newy
								newstate[j][0]=currentstate[j][0]+moves[i][0]
								newstate[j][1]=currentstate[j][1]+moves[i][1]
								newstate[-1].append(path[i])
								# print newstate
								check_unique_state(newstate)
							break
	
	distancearray=[]
	state_distance=100000
	for dstate in d:
		state_distance=0
		rb_min=100000
		for blockcount in range(1,len(dstate)-1):
			bs_min=100000
			
			for storagecount in range(0,len(storage_coord)):
				distance=man_distance(dstate[blockcount],storage_coord[storagecount])
				if distance<bs_min:
					bs_min=distance

			state_distance+=bs_min
			rb_dist=man_distance(dstate[0],dstate[blockcount])
			if rb_min>rb_dist:
				rb_min=rb_dist

		# dstate[-1].append([])


		state_distance+=rb_min

		state_distance+=len(dstate[-1])-1
		dstate[-1].append(state_distance)
		distancearray.append(state_distance)

	# print distancearray
	distancearray.sort()

	sorted_deque=deque()
	for dist in distancearray:
		# print len(d)
		for countdequestate in range(0,len(d)):
			if dist==d[countdequestate][-1][-1]:
				# print d[countdequestate]
				sorted_deque.append(d[countdequestate])
				d[countdequestate][-1][-1]=-1


	d=deepcopy(sorted_deque)


	for dstate in d:
		dstate[-1]=dstate[-1][:-1]

if len(d)==0 or isSolutionAvailable==0:
	print 'Solution not available for the board'




			





























