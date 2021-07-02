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


def graphSearch(problem,fringe):
    # A closed set for keeping track of visited nodes in graph search
    closed = set()
    # Initialize fringe with start state and empty path
    # Each element in the fringe contains the node location and the path to the node from the start state
    fringe.push([problem.getStartState(),[]])

    while not fringe.isEmpty():
        # get highest priority node in fringe
        node,path = fringe.pop()
        # test if node is goal state
        if problem.isGoalState(node):
            return path
        # make sure node has not already been explored (assumes node type is hashable)
        if not node in closed:
            # add unexplored node to the closed set
            closed.add(node)
            # and push its children to the fringe
            for child_node in problem.getSuccessors(node):
                child_path = path.copy()
                child_path.append(child_node[1])
                fringe.push([child_node[0],child_path])
    return None


def depthFirstSearch(problem):
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

    # LIFO stack for DFS fringe
    fringe = util.Stack()
    return graphSearch(problem,fringe)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # FIFO queue for BFS fringe
    fringe = util.Queue()
    return graphSearch(problem,fringe)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # UCS cost function
    def cost_fn(item):
        return problem.getCostOfActions(item[1])

    # Priority queue for UCS fringe with cost function as priority metric
    fringe = util.PriorityQueueWithFunction(cost_fn)
    return  graphSearch(problem,fringe)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # A* priority function = cost + heuristic
    def aStar_fn(item):
        return problem.getCostOfActions(item[1]) + heuristic(item[0],problem)

    # Priority queue for A* fringe with priority function
    fringe = util.PriorityQueueWithFunction(aStar_fn)
    return graphSearch(problem,fringe)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
