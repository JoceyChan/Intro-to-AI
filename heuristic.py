#
# heuristic.py
#
# This script defines a utility class that can be used as an implementation
# of a frontier state (location) evaluation function for use in route-finding
# heuristic search algorithms. When a HeuristicSearch object is created,
# initialization code can be executed to prepare for the use of the heuristic
# during search. In particular, a RouteProblem object is typically provided 
# when the HeuristicFunction is created, providing information potentially
# useful for initialization. The actual heuristic cost function, simply
# called "h_cost", takes a state (location) as an argument.
#
# YOUR COMMENTS INCLUDING CITATIONS
# TA Liza Oh Office Hours, Pseudocode provided by professor
# YOUR NAME - THE DATE
# Jocelyn Chan October 15, 2021


import route


class HeuristicFunction:
    """A heuristic function object contains the information needed to
    evaluate a state (location) in terms of its proximity to an optimal
    goal state."""

    def __init__(self, problem=None):
        self.problem = problem
        # PLACE ANY INITIALIZATION CODE HERE
        self.maxSpeed = 0
        for i in self.problem.map.locations():  # all locations
            for j in self.problem.actions(i): # looking at each locations and the roads coming out of that location
                endLoc = self.problem.map.get_result(i, j) # getting one end location
                timeCost = self.problem.action_cost(i, endLoc) # time-cost of one segment
                speed = self.problem.map.euclidean_distance(i, endLoc)/timeCost
                if speed > self.maxSpeed:
                    self.maxSpeed = speed




    def h_cost(self, loc=None):
        """An admissible heuristic function, estimating the cost from
        the specified location to the goal state of the problem."""
        # a heuristic value of zero is admissible but not informative
        value = 0.0
        if loc is None:
            return value
        else:
            # PLACE YOUR CODE FOR CALCULATING value OF loc HERE
            distance = self.problem.map.euclidean_distance(loc, self.problem.goal) # coordinates
            value = distance/self.maxSpeed

            return value

