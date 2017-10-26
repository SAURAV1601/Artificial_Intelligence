sudokuBoard=[]
row=[]
# This program is to solve sudoku puzzle using smart back tracking algorithm using the strategy of minimum remaining value(MRV) 

# This function prints the sudoku puzzle at given state
def printBoard(board):
	for i in range(0,9):
		print board[i]

# This function is to check if a number can be placed in a position or not. It returns true, if the number can be placed else false
def check(num,board,row,col):
	flag=0
	# Checks if the number exists in that column or row
	for i in range(0,9):
		if board[row][i]==num or board[i][col]==num:
			flag=1
	# Checks if the number exists in the 3*3 block or not
	row=row-row%3
	col=col-col%3
	for i in range(0,3):
		for j in range(0,3):
			if (i+row)<9 and (j+col)<9 and (i+row)>0 and (j+col)>0:
				if board[i+row][j+col]==num :
					flag=1
	# If number doesn't exist in row or column or block, then it returns true or else returns false 
	if flag==0:
		return True
	else:
		return False
# Main function to solve board using backtracking and MRV strategy
def solve(domains,board):
	minimum=15
	emptyflag=0
	zeroflag=1
	# checks if domains set of unfilled cells is empty or not, it is empty only when all cells are filled, so it returns true
	if domains==[]:
		return True
	#checks the domains of all unfilled cells and returns unfilled position with least domain length. 
	#That is a position which has less values to be filled in.
	for i in range(0,len(domains)):
		key=domains[i].keys()
		val=domains[i].get(key[0])
		domainLen=len(val)
		if domainLen<minimum and domainLen>0:
			minimum=domainLen
			position=key[0]
			array=val
			emptyflag=1
		# start backtracking, when a unfilled cell cannot have any number between 1 to 10
		if val==[]:
			return False
	#checks if there are any unfilled cells in puzzle
	if emptyflag==0:
		return True
	# Checking numbers in the given domain and fgoing forward for next unfilled cell
	for number in array:
		board[int(position[0])][int(position[1])]=number
		newDomains=[]
		#updating domains for each unfilled cell in puzzle
		for i in range(0,9):
			for j in range(0,9):
				if board[i][j]==0:
					cellDomain=[]
					for num in range(1,10):
						if check(num,board,i,j):
							cellDomain.append(num)
					newDomains.append({str(i)+str(j):cellDomain})
		#uncomment following line to see stages of solving each cell
		# printBoard(board)

		# recursive call to same function by filling the current cell
		if solve(newDomains,board):
			return True

		board[int(position[0])][int(position[1])]=0
		#uncomment following line to see stages of solving each cell when backtracked
		# printBoard(board)
	# Starts backtracing if no number in given domain can be placed in the given position
	return False

# Taking input sudoku puzzle
print "enter sudoku board"
for i in range(0,9):
	row=raw_input()
	sudokuBoard.append([])
	for j in range(0,9):
		sudokuBoard[-1].append(int(row[j]))
#uncomment following line to see the puzzle you entered
# print 'board you entered'
# printBoard(sudokuBoard)

#calculating domains for all unfilled cells in the puzzle
domains=[]
for i in range(0,9):
	for j in range(0,9):
		if sudokuBoard[i][j]==0:
			cellDomain=[]
			for num in range(1,10):
				if check(num,sudokuBoard,i,j):
					cellDomain.append(num)
			domains.append({str(i)+str(j):cellDomain})

# starts solving puzzle, if there is no solution. It goes to else condition
if solve(domains,sudokuBoard):
	print 'Solution is'
	printBoard(sudokuBoard)
else:
	print "no solution"

