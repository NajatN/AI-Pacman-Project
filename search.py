# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # Get the starting state from the problem
    start = problem.getStartState()
    # Check if the starting state is already the goal state
    if problem.isGoalState(start):
        return []
    # Initialize the node as the starting state
    node = problem.getStartState()
    # Create an empty set to keep track of visited nodes
    visited = set()
    # Create a stack to store the nodes to be explored and the corresponding actions to reach them
    s = util.Stack()
    # Push the starting state and an empty list of actions to the stack
    s.push((start, []))
    # While the stack is not empty, pop a node and its corresponding actions from the stack
    while not s.isEmpty():
        node, actions = s.pop()
        # If the popped node is the goal state, return the actions required to reach it
        if problem.isGoalState(node):
            return actions
        # If the popped node has not been visited yet, add it to the visited set
        if node not in visited:
            visited.add(node)
            # Get the successors of the current node and push them to the stack with the corresponding actions
            successors=problem.getSuccessors(node)
            for x in successors:
                s.push((x[0], actions + [x[1]]))
    # If the stack becomes empty and no solution is found, return an empty list of actions
    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Get the starting state of the problem
    start = problem.getStartState()
    # If the starting state is already the goal state, return an empty list of actions
    if problem.isGoalState(start):
        return []
    # Set the current node to the starting state
    node = problem.getStartState()
    # Create an empty set to keep track of visited nodes
    visited = set()
    # Create an instance of the Queue data structure to hold the nodes to be processed
    q = util.Queue()
    # Add the starting node and an empty list of actions to the queue
    q.push((start, []))
    # Loop until the queue is empty
    while not q.isEmpty():
        # Pop the next node and its corresponding actions from the front of the queue
        node, actions = q.pop()
        # If the current node is the goal state, return the list of actions taken to reach it
        if problem.isGoalState(node):
            return actions
        # If the current node has not been visited yet, mark it as visited by adding it to the visited set
        if node not in visited:
            visited.add(node)
            # Get the successors of the current node and add them to the queue with the corresponding actions taken
            successors=problem.getSuccessors(node)
            for x in successors:
                q.push((x[0], actions + [x[1]]))
    # If no goal state is found, return an empty list of actions
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Get the starting state of the problem
    start = problem.getStartState()
    # If the starting state is already the goal state, return an empty list of actions
    if problem.isGoalState(start):
        return[]
    # Set the current node to the starting state
    node = problem.getStartState()
    # Create an empty set to keep track of visited nodes
    visited = set()
    # Create an instance of the PriorityQueue data structure to hold the nodes to be processed,
    # ordered by the cost to reach them
    pq = util.PriorityQueue()
    # Add the starting node and an empty list of actions to the queue with a priority of 0
    pq.push((start, []) ,0) 
    # Loop until the queue is empty
    while not pq.isEmpty():
        # Pop the node and its corresponding actions with the lowest cost from the front of the queue
        node, actions = pq.pop()
         # If the current node is the goal state, return the list of actions taken to reach it
        if problem.isGoalState(node):
            return actions
         # If the current node has not been visited yet, mark it as visited by adding it to the visited set
        if node not in visited:
            # Get the successors of the current node
            successors = problem.getSuccessors(node)
            # For each successor of the current node
            for x in successors:
                state = x[0]
                # If the successor has not been visited yet
                if state not in visited:
                    next = x[1]
                    # Compute the new cost of the actions taken to reach the successor
                    g = actions + [next]
                    # Add the successor and its corresponding actions to the queue with a priority based on the new cost
                    pq.push((state, actions + [next]), problem.getCostOfActions(g))
        # Mark the current node as visited
        visited.add(node)
    return actions
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Get the starting state from the problem
    start = problem.getStartState()
    # Check if the starting state is already the goal state
    if problem. isGoalState(start) :
        return []
    # Initialize the node as the starting state
    node = problem.getStartState()
    # Create an empty set to keep track of visited nodes
    visited = set()
    # Create a priority queue to store the nodes to be explored and the corresponding actions to reach them with their priority values
    pq = util.PriorityQueue()
    # Push the start node with an empty list of actions to the priority queue with its priority value calculated by the nullHeuristic
    pq.push((start, []), nullHeuristic(start, problem)) 
    # While the priority queue is not empty
    while not pq.isEmpty():
        # Pop the node with the highest priority value (the lowest f-value) and its corresponding actions from the priority queue
        node, actions = pq.pop()
        # If the current node is the goal state, return the list of actions that led to this goal state
        if problem.isGoalState(node):
            return actions
        # If the current node has not been visited before
        if node not in visited:
            # Get the successors of the current node and iterate over them
            successors = problem.getSuccessors(node)
            for x in successors:
                # Get the state and action that led to the successor node
                state = x[0]
                # If the node has not been visited before
                if state not in visited:
                    next = x[1]
                    # Calculate the cost of the actions taken so far and the heuristic value for the successor node
                    do = actions + [next]
                    f = problem.getCostOfActions (do) + heuristic(state, problem)
                    # Push the successor node and its corresponding actions to the priority queue with its priority value calculated by f
                    pq.push((state, actions + [next]), f)
        # Mark the current node as visited after exploring all its successors
        visited.add(node)
    return actions
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
