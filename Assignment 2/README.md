### Hill Climbing Algorithm
The implementation of Hill Climbing algorithm to find the minimum value of Ackley's function is file named hill_climb_search.py.

The initial position was chosen randomly and the next position is calculated with following equations:

    X' = (rand() – 0.5) * 0.1 + X
    Y' = (rand() – 0.5) * 0.1 + Y
    
Every new point is used to calculate ackley's value and checked with exsiting minimum value. The iteration is terminated when a minimum value is not found in last 100 iterations.

### Differential Evolution Algorithm
The implementation of Differential Evolution algorithm to find the minimum value of Ackley's function is file named differential_evolution.py.

Here, a population of 20 random points are selected initially and every new point is calculated by selecting 3 points from the population.
The mutation is as follows:

    New_position = a + Mutation_Factor * (b - c)  where a,b,c are 3 random different positions in given population

Every new point is used to calculate ackley's value and checked with exsiting minimum value. The iteration is terminated when a minimum value is not found in last 100 iterations.


#### Analysis

**Output of Hill Climbing Algorithm**

![Hill Climbing Algorithm](figure_1.jpeg)

In this algorithm, the minimum doesn't reach global minimum every time and it mostly terminates at a value of -20.

**Output of Hill Climbing Algorithm**

![Differential Evolution Algorithm](figure_2.jpeg)

In this algorithm, the minimum reaches global minimum almost every time with value -22.7 obtained at position (0,0). It is clear that it doesn't stop at local minima as it continously learning from previous values (that is, parent values).
