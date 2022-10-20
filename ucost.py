#
# ucost.py
#
# This file provides a function implementing uniform cost search for a
# route finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# YOUR COMMENTS INCLUDING CITATIONS
# TA Liza Oh Office Hours, Pseudocode provided by professor
# YOUR NAME - THE DATE
# Jocelyn Chan October 15, 2021


from route import Node
from route import Frontier

# look at for A* search

def uniform_cost_search(problem, repeat_check=False):
    """Perform uniform cost search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE

    # Initialize the node with the starting location
    node = Node(problem.start)

    # If the start location is the goal then return node
    if problem.is_goal(node.loc):
        return node

    # Initializing the frontier to contain node
    frontier = Frontier(node, sort_by='g') # not sure if I have to add the g for this part

    # Initializing the reached set to contain node
    visited_nodes = [problem.start]

    while not frontier.is_empty():
        node = frontier.pop()

        if problem.is_goal(node.loc):
            return node

        for node_child in node.expand(problem):
            s = node_child.loc

            if repeat_check:
                if s in visited_nodes:
                    if s in frontier and s.value() < frontier[s]:
                        del frontier[s]
                        frontier.add(node_child)
                else:
                    frontier.add(node_child)
                    visited_nodes.append(s)
            else:
                frontier.add(node_child)

    return None
