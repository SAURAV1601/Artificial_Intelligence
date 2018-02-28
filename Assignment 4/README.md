## Connect4 Game

### Compile and execution of the code:

* Execute this python file using the following command

      Python connect4.py
    
* The AI plays as ‘0’ and user plays as ‘X’.
* Once the file is executed, the current state of board is displayed .
* Now, it prompts for user input and user has to give an input from 1 to 7, corresponding in
which column user wants to play.
* The user needs to give an input from 1 to 7 and press enter.
* Now, the AI makes the move and again waits for user to make their move.
* This process repeats until any player wins or game is draw.

### Design and heuristic of the AI

* It comprises of many functions like win() - to check whether anyone has won or not, gameover() - check whether game is over or not, maximise() - returns the best move of ai
player, search() - searches the tree for best move and so on
* The heuristic i used for giving a value to state is as follows:

        alpha= number of 4 streaks*100000 + number of 3 streaks*100 + number of 2 streaks
    
  Where, number of 4 streaks is consecutive 4 symbols of same player in horizontal or vertical directions or diagonally and number of 3 streaks is consecutive 3 symbols of same player in horizontal or vertical directions or diagonally and number of 2 streaks is consecutive 2 symbols of same player in horizontal or vertical directions or diagonally.
* The state with highest alpha value is determined as best move for the AI player.
* Also, for every state the program checks the tree upto 4 levels below its level in the tree. That is 2-ply check meaning it explores states in tree for 2 moves of user and 2 moves of AI.
* If many number of moves results in states with similar heuristic value, then it chooses the last move.
