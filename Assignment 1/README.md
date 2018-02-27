## Sokoban Game
[Sokoban](https://en.wikipedia.org/wiki/Sokoban) is a puzzle game where the player has to move boxes into storage locations with some obstacles in between. 

Play Game online [here](http://www.game-sokoban.com/).

### Input Format

O - Obstacle  
S - Storage  
B - Block  
R - Robot

"**@**" - Block in storage space  
"**#**" - Robot in storage space

## Compile and Execute
The puzzle is solved using 6 different algorithms namely breadth first serach, depth first search, manhattan distance, greedy and A* search.

There are 6 different inputs in this repo in txt format.

Execute the python program as shown below

    python sokoban_bfs.py <input1.txt >output.txt
  
## Heuristic
Greedy best first search and A* search are implemented using Manhattan distance between robot, blocks and the nearest storage spaces. 
In this the distance from blocks to storage spaces is only considered, along with distance from robot to blocks.

    f(n) = Manhattan_distance(robot-block) + Manhattan_distance(block-storage space)
    
## Analysis
* BFS always returns an optimal solution as it checks for the solution level by level but it is comparatively slow.
* DFS opens a node and searches among its children till it reaches a leaf node, sometimes it is fast but gives a longer path to reach solution.
* Greedy Best first considers heuristic to move faster towards the goal, but it doesn't always provide the best solution. It is comparatively fast.
* A* is a combination of both BFS and greedy, so its output is the optimal solution and is faster than BFS.
