# -----------------
# User Instructions
# 
# Write a strategy function, clueless, that ignores the state and
# chooses at random from the possible moves (it should either 
# return 'roll' or 'hold'). Take a look at the random library for 
# helpful functions.

import random

possible_moves = ['roll', 'hold']

def clueless(state):
    "A strategy that ignores the state and chooses at random from possible moves."
    # your code here
    choice = random.randint(0,1)
    return possible_moves[choice]


