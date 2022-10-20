#
# astar.py
#
# This file provides a function implementing A* search for a route finding
# problem. Various search utilities from "route.py" are used in this function,
# including the classes RouteProblem, Node, and Frontier. Also, this function
# uses heuristic function objects defined in the "heuristic.py" file.
#
# YOUR COMMENTS INCLUDING CITATIONS
# Pseudocode provided by professor
# YOUR NAME - THE DATE
# Jocelyn Chan - October 18, 2021


from route import Node
from route import Frontier


def a_star_search(problem, h, repeat_check=False):
    """Perform A-Star search to solve the given route finding problem,
    returning a solution node in the search tree, corresponding to the goal
    location, if a solution is found. Only perform repeated state checking if
    the provided boolean argument is true."""

    # PLACE YOUR CODE HERE

    # Initialize the node with the starting location
    node = Node(problem.start, h_eval=h.h_cost(problem.start))

    # If the start location is the goal then return node
    if problem.is_goal(node.loc):
        return node

    # Initializing the frontier to contain node
    frontier = Frontier(node, sort_by='f')

    # Initializing the reached set to contain node
    visited_nodes = [problem.start]

    while not frontier.is_empty():
        # removing  node from frontier
        node = frontier.pop()

        if problem.is_goal(node.loc):
            return node

        for node_child in node.expand(problem, h):
            s = node_child.loc

            if repeat_check:
                if s in visited_nodes:
                    if s in frontier and s.value('f') < frontier[s]:
                        del frontier[s]
                        frontier.add(node_child)
                else:
                    frontier.add(node_child)
                    visited_nodes.append(s)
            else:
                frontier.add(node_child)
    return None
