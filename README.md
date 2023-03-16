# AI Pacman Project
Depth First Search Algorithm
----------------------------

Our implementation of the depth-first search algorithm takes a SearchProblem instance as input. The start state and an empty list of actions are used to initialize a node and a stack if the start state is not already the target state. The algorithm then moves into a loop that retrieves a node from the stack along with a list of actions and checks to see if the node is the goal state. If not, the node is added to a visited set, its successors are retrieved, a new tuple is created with each successor state and a list of actions that includes the action of the current successor, and the stack is then pushed. An empty list is returned if the loop ends prematurely, and no goal state is reached.

Breadth First Search Algorithm
-------------------------------

Our implementation of the breadth-first search algorithm takes a SearchProblem instance as input. The start state and an empty list of actions are used to setup a node and a queue if the start state is not already the target state. The algorithm then moves into a loop where it removes a node and a list of actions from the queue and determines if the node is in the goal state. If not, it adds the node to a visited set and gets its successors. A new tuple is then created with each successor state and a list of actions that contains the action of the current successor, and it is queuing up on the queue. An empty list is returned if the loop ends with no goal state being reached.

Uniform Cost Search Algorithm
-----------------------------

Our implementation of the uniform cost search algorithm takes a SearchProblem instance as input. It initializes a node with the start state and an empty set called "visited". Next, with a priority of 0, a priority queue is established with a tuple consisting of the start state and an empty list of activities. After that, the algorithm enters a loop where it dequeues a node and a set of actions from the priority queue and determines whether the node is in the goal state. If not, it finds its successors, builds a new tuple with each successor state and a list of actions that includes the action taken by the current successor, and enqueues the tuple into the priority queue with a priority equal to the cost of the activities required to get to the successor state. The lowest cost node is enlarged first due to the priority queue. An empty list is returned if the loop ends with no goal state being reached.

A* Search Algorithm
--------------------
In the A* algorithm, a version of the UCS, the search is directed toward the desired state using a heuristic function. The problem and heuristic function are inputs for the aStarSearch function. In accordance with their expected total costs, the nodes that will be extended are placed in a priority queue. A node's priority is calculated by adding the anticipated cost of the path from the node to the goal state and the cost of the path from the start state to the node. The method then expands the successors of the node with the lowest predicted cost until it reaches the goal state, or an empty priority queue, which means that all possible paths have been explored and the goal state has not been found. In this case, an empty list is returned because there are no actions that can lead to the goal state.

Search Algorithms on Open Maze (BFS, DFS, UCS, A*)
--------------------------------------------------

When running the four different search algorithms on the openMaze, A*, UCS, and BFS discovered paths with the same cost, however DFS discovered a path with a noticeably greater cost. The outcome can be linked to DFS's nature, which encourages exploration to the greatest depths before backtracking, whereas A*, UCS, and BFS prioritize exploring promising options first. This emphasizes how critical it is to choose the right search algorithm based on the nature and goals of the problem.

Finding All Corners
--------------------

In this problem, the constructor stores the initial position of the agent as well as the locations of the four corners and the maze's structure. The start state of the issue is returned by the getStartState method, together with Pacman's location and a tuple indicating whether he has visited each of the four corners. The isGoalState method determines if the state is one that Pacman has visited from all four directions, or a goal state. The getSuccessors method moves Pacman in one of four directions, looks to see if it encounters a wall, and updates the visited corners tuple if necessary to generate potential successor states. The getCostOfActions function figures out how much a series of actions will cost. As expected, this implementation using BFS expands just under 2000 nodes (1966 nodes) on medium corners maze.

Corners Problem Heuristic
-------------------------

The cornersHeuristic function is a heuristic function created for the CornersProblem, which tries to consume all of the dots in the maze's corners. The function takes a list of four Boolean values indicating visited corners and a state input containing Pacman's position to extract corner coordinates and maze layout from the input. The function then generates a to_visit list containing the coordinates of unexplored corners, computes the Manhattan distance between each corner on the to_visit list, and adds these distances to the heuristic list. As the calculated shortest path from the current state to a goal state, the function returns the maximum value in the heuristic list.

The implemented heuristic is admissible and consistent. The heuristic is admissible because it never overestimates the cost to reach the goal state. It is consistent because its estimated cost from one state to another plus the cost of reaching the next state is less than or equal to the estimated cost of reaching the goal state from the current state. 
The cost of the paths returned by both A* and UCS was found to be equal (106), which further supports the claim that the heuristic we implement is not inconsistent.
 
Eating All Dots
----------------
 
For the FoodSearchProblem, the foodHeuristic function determines an admissible and consistent heuristic. It checks whether there is any food left to consume before using the mazeDistance function to determine the greatest distance between the current location and any food dot that is still present. As a lower constraint on the shortest path to a desired state, the function returns the greatest distance. This heuristic function is admissible since it returns a value that is less than or equal to the actual cost of reaching the goal state. Additionally, it is consistent because the maximum distance is always an overestimate of the remaining cost to the goal state. We also tried to use Manhattan distance instead of maze distance, but we observed that using Manhattan distance expanded more nodes than the required optimal amount, so we decided to use the maze distance instead.

Suboptimal Search
------------------

The ClosestDotSearchAgent is a search agent that locates the nearest food dot to Pacman at each step using breadth-first search. To locate the nearest dot, it constructs an AnyFoodSearchProblem object, which is implemented in the problem's isGoalState function. 

This implementation is not ideal because it may not always be possible to discover the quickest route for consuming all the dots by repeatedly traveling to the nearest one. Here's a small example where repeatedly going to the closest dot does not result in finding the shortest path for eating all the dots: If we have a maze where there are two ways to get to the last food dot, each of which has a different number of dots, and the Pacman selects the closer option, it might end up taking more steps overall than it would have if it had initially taken the longer road. Let’s say the initial path is shorter and has just one food dot. The second path is longer and has four food dots. The ClosestDotSearchAgent will pick the quicker route to get to the first food dot. The, it must go back and take the longer route in order to get to the other four dots. As a result, the agent's total path length will be longer than it would have been if it had initially taken the longer route and ate all the dots at once.
