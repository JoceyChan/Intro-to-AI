#
# heuristic.py
#
# This Python script file provides two functions in support of minimax search
# using the expected value of game states. First, the file provides the
# function "expected_value_over_delays". This function takes as an argument
# a state of game play in which the current player has just selected an
# action. The function calculates the expected value of the state over all
# possible random results determining the amount of time before the
# Guardian changes gaze direction. This function calculates this value
# regardless of whose turn it is. The value of game states that result from
# different random outcomes is determined by calling "value". Second, the
# file provides a heuristic evaluation function for non-terminal game states.
# The heuristic value returned is between "max_payoff" (best for the
# computer player) and negative one times that value (best for the opponent).
# The heuristic function may be applied to any state of play. It uses
# features of the game state to predict the game payoff without performing
# any look-ahead search.
#
# This content is protected and may not be shared, uploaded, or distributed.
#
# PLACE ANY COMMENTS, INCLUDING ACKNOWLEDGMENTS, HERE
#
# PLACE YOUR NAME AND THE DATE HERE
# Jocelyn Chan 11/18/21


from parameters import *
from minimax import probability_of_time
from minimax import value


def expected_value_over_delays(state, ply):
    """Calculate the expected utility over all possible randomly selected
    Guardian delay times, ranging from 2 to 5 steps. Return this expected
    utility value."""
    val = 0.0
    #state is an obj of game class, ply is a set of user and computer
    # PLACE YOUR CODE HERE
    # Note that the value of "ply" must be passed along, without
    # modification, to any function calls that calculate the value 
    # of a state.
    for i in range(2, 5+1):
        state.time_remaining = i  # i is for each gaurdian delayed time
        val += probability_of_time(i) * value(state, ply)
    return val


def heuristic_value(state):
    """Return an estimate of the expected payoff for the given state of
    game play without performing any look-ahead search. This value must
    be between the maximum payoff value and the additive inverse of the
    maximum payoff."""
    val = 0.0
    # between -100 and 100
    # symetric: if comp player in lead and person is ex 5 away the other side then person is in lead now comp is 5 est of an 80
    # PLACE YOUR CODE HERE
    # if player is in high lead then it is a greater pay off // rank ordering mus be pretty symetric // dot import just attributes of states and parameters


    return val
