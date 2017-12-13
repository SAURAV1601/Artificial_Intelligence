# Connect 4 game using min max algorithm and alpha-beta pruning
#The Heuristic function used is as follows 
#number of 4 streaks*100000 + number of 3 streaks*100 + number of 2 streaks
# The algorithm searches for 4 levels of sub trees for the best possible state
from copy import deepcopy
import random
connectBoard=[]
winVal=4

# Function to print the current board
def printBoard(state):
	for i in range(5,-1,-1):
		for j in range(0,7):
			print state[i][j],'|',
		print '\n___________________________'
	print '1 | 2 | 3 | 4 | 5 | 6 | 7 | '

#Function to get empty position (row number) in a given column
def getEmptyPosRow(col,state):
	for i in range(6):
		if state[i][col]==' ':
			return i
	return -1
#functions returns if any one wins or the game is over
def win(state):
	if getVal('0',state,4)>=1:
		print 'computer wins'
		printBoard(state)
		return 0
	if getVal('X',state,4)>=1:
		print 'user wins'
		printBoard(state)
		return 0
	if gameOver(state):
		print 'game is draw'
		printBoard(state)
		return 0
	return 1
#function to check whether game is over or not
def gameOver(state):
	for i in range(0,6):
		for j in range(0,7):
			if state[i][j]==' ':
				return 0
	return 1
#check if the the player has any streak in horizontal or vertical or diagonal directions
#and returns sum of the number of streaks in all directions
#val is streak length
def getVal(sym,state,val):
	count=0
	for i in range(0,6):
		for j in range(0,7):
			if state[i][j]==sym:
				count+=verticalCheck(i,j,state,val)
				count+=horizontalCheck(i,j,state,val)
				count+=positiveDiagonalCheck(i,j,state,val)
				count+=negativeDiagonalCheck(i,j,state,val)
	return count

#checks for vertical streak
def verticalCheck(row,col,state,val):
	count=0
	for i in range(row,6):
		if state[i][col]==state[row][col]:
			count+=1
		else:
			break
	if count>=val:
		return 1
	else:
		return 0

#checks for horizontal streak
def horizontalCheck(row,col,state,val):
	count=0
	for i in range(col,7):
		if state[row][i]==state[row][col]:
			count+=1
		else:
			break
	if count>=val:
		return 1
	else:
		return 0
#checks for upper diagonal streak
def positiveDiagonalCheck(row,col,state,val):
	count=0
	j=col
	for i in range(row,6):
		if j>6:
			break
		elif state[i][j]==state[row][col]:
			count+=1
		else:
			break
		j+=1
	if count>=val:
		return 1
	else:
		return 0
#checks for lower diagonal streak
def negativeDiagonalCheck(row,col,state,val):
	count=0
	j=col
	for i in range(row,-1,-1):
		if j>6:
			break
		elif state[i][j]==state[row][col]:
			count+=1
		else:
			break
		j+=1
	if count>=val:
		return 1
	else:
		return 0

def Maximize(depth,sym,state):
	if sym=='X':
		opp='0'
	else:
		opp='X'
	legal_moves = {} 
	for col in range(7):
        # if column col is empty
		pos=getEmptyPosRow(col, state)
		if pos!=-1:
            # make the move and store it in legal moves
			temp=deepcopy(state)
			temp[pos][col]=sym
			# search the tree in next lower level
			x=search(depth-1, temp, opp)
			legal_moves[col] = x-(2*x)
    
	best_alpha = -99999999
	best_move = 0
	#check for highest alpha value, that is best move and return it
	moves = legal_moves.items()
	random.shuffle(list(moves))
	for move, alpha in moves:
		if alpha >= best_alpha:
			best_alpha = alpha
			best_move = move
    
	return best_move



def search(depth, state, sym):
    # searches all states from this level and returns best alpha value
	legal_moves = []
	for i in range(7):
        # if column i is empty
		pos=getEmptyPosRow(i, state)
		if pos!=-1:
            # make the move and store it in legal moves
			temp=deepcopy(state)
			temp[pos][i]=sym
			legal_moves.append(temp)
    
    # if the state is a terminal node or depth = 0 , return heuristic value
	if depth == 0 or len(legal_moves) == 0 or gameIsOver(state):
		return heuValue(state, sym)
    
    # selecting other player and seraching the tree for their moves
	if sym=='0':
		opp='X'
	else:
		opp='0'

	alpha = -99999999
	for child in legal_moves:
		x=search(depth-1, child, opp)
		alpha = max(alpha, x-(2*x))
	return alpha

#heuristic function which returns value of the state in the tree
def heuValue(state, sym):
	if sym == 'X':
		opp='0'
	else:
		opp='X'
    
	my_fours = getVal(sym,state, 4)
	my_threes = getVal(sym,state, 3)
	my_twos = getVal(sym,state, 2)
	opp_fours = getVal(opp,state, 4)
	if opp_fours > 0:
		return -100000
	else:
		return my_fours*100000 + my_threes*100 + my_twos

def gameIsOver(state):
	if getVal('X',state,4)>= 1:
		return True
	elif getVal('O',state,4) >= 1:
		return True
	else:
		return False


print "Connect 4 board is as follows"
#initialising the board
for i in range(0,6):
	connectBoard.append([])
	for j in range(0,7):
		connectBoard[-1].append(' ')
printBoard(connectBoard)
print 'Symbols - User: X, Computer: 0'
# start of main loop
while(win(connectBoard)==1):
	#taking user player input and updating state of board
	print '\nEnter column number in 1 to 7'
	colnum=int(raw_input())
	pos=getEmptyPosRow(colnum-1,connectBoard)
	connectBoard[pos][colnum-1]='X'
	print '\n\n\n\nUser played at (',6-pos,',',colnum,')'

	#checks whether user wins with their move. If they don't win, computer plays
	#if user wins, program is terminated
	if win(connectBoard)==1:
		compos= Maximize(4,'0',connectBoard)

		row=getEmptyPosRow(compos,connectBoard)
		connectBoard[row][compos]='0'
		print 'Computer played at (',6-row,',',compos,')\n'
		printBoard(connectBoard)
	else:
		break
