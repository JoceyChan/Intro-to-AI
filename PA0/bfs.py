#
# bfs.py
#
# This file provides a function implementing breadth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# YOUR COMMENTS INCLUDING CITATIONS
# TA Liza Oh Office Hours, Pseudocode for bfs and dfs(Artificial Intelligence, A modern approach), Python Documentation (docs.python.org/3/tutorial/)
# YOUR NAME - THE DATE
# Jocelyn Chan - October 4, 2021


from route import Node
from route import Frontier


def BFS(problem, repeat_check=False):
    """Perform breadth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    # Initialize the node with the starting location
    node = Node(problem.start)

    # If the start location is the goal then return node
    if problem.is_goal(node.loc):
        return node

    # Queue keeps track of unvisited nodes
    frontier = Frontier(node)

    # We keep track of the visited nodes
    visited_nodes = [problem.start]

    #We continue moving in the tree layers until all nodes visited
    while not frontier.is_empty():
        # pop the node child from the queue since it will be visited
        node = frontier.pop()
        # visit every neighbor of the current node
        # node.expand(problem) returns list reachable nodes of current node
        if problem.is_goal(node.loc):
            return node
        for node_child in node.expand(problem):
            # Get location of child
            s = node_child.loc
            # If child node location is goal return node
            # If not visited...
            if repeat_check:
                if s not in visited_nodes:
                    # Register node as visited node to avoid inf loop
                    visited_nodes.append(s)
                    # This to later check reachable nodes and keep traversing tree
                    frontier.add(node_child)
            else:
                frontier.add(node_child)
    # Return None if start cannot reach end
    return None
