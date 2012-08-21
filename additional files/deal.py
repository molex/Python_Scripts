# -----------
# User Instructions
# 
# Write a function, deal(numhands, n=5, deck), that 
# deals numhands hands with n cards each.
#

import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5):
    # Norvig's code
    # added parameter to deal, [r+s for r in '23456789TJQKA' for s in 'SHDC'] 
    # random.shuffle(deck)
    # return [deck[n*i:n*(i+1)] for i in range(numhands)]
    # Your code here.
    deck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 
    output = []
    random.shuffle(deck)
    for x in range(numhands):
        hand = []
        for y in range(n):
            hand.append(deck.pop())
        output.append(hand)
    return output
        
print deal(2,5)
