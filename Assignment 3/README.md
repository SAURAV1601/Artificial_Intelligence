## Sudoku Solver 

### Input and Execution of program

#### Sample Input:
000000006
700000500
350260010
810500000
060030070
000006048
030057081
008000007
200000000

To execute the program, use the following command:

    python sudoku.py 
    python mrv.py

Now enter the input and press enter, solution will be displayed.

The puzzle is solved in two methods namely Naive backtracking and Smart backtracking.

### Naive Backtracking
The basic backtracking method by going through each empty slot on the board and checking for all the values 1-9, if a particular number can be placed or not( If the other constraints don't allow it, I need to backtrack to the previous position where another number is checked for validity). I am going row-by-row in search of empty slots on the board. This is a naive method as it results in a lot of unnecessary branching.

### Smart Backtracking
