sudokuBoard=[]
row=[]
# This program is to solve sudoku puzzle using naive back tracking algorithm

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

# Main function to solve board using backtracking
def solve(board):
	i=0
	j=0
	emptyflag=0

	# Check if puzzle contains any zero's (unfilled cells), if all cells are filled it returns true
	# If there are unfilled cells, the position of first unfilled cell in order is chosen
	for row in range(9):
		for col in range(9):
			if(board[row][col]==0):
				i=row
				j=col
				emptyflag=1
	if emptyflag==0:
		return True

	# Checking numbers from 1 to 10, if any of the number cn be placed in the cell
	for number in range(1,10):
		if check(number,board,i,j):
			board[i][j]=number
			#uncomment folloeing line to see stages of solving each cell
			# printBoard(board)

			# recursive call to same function by filling the current cell
			if solve(board):
				return True		
			board[i][j]=0
			#uncomment following line to see stages of solving each cell when backtracked
			# printBoard(board)
	# Starts backtracing if no number from 1 to 10 can be placed in the given position 
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

# starts solving puzzle, if there is no solution. It goes to else condition
if solve(sudokuBoard):
	print 'Solution is'
	printBoard(sudokuBoard)
else:
	print "no solution"

