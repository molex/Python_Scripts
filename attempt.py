import itertools

def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    
    # Your code here
    best = []
    options = []
    black = ("2C 2S 3C 3S 4C 4S 5C 5S 6C 6S 7C 7S 8C 8S 9C 9S TC TS JC JS QC QS KC KS AC AS").split()
    red = ("2H 2D 3H 3D 4H 4D 5H 5D 6H 6D 7H 7D 8H 8D 9H 9D TH TD JH JD QH QD KH KD AH AD").split()
    if '?B' in hand and '?R' in hand:
        hand.remove('?B')
        hand.remove('?R')
        options = list(itertools.product(black,red))
        for combo in options:
            hand.append(combo[0])
            hand.append(combo[1])
            curr_hand = sorted(hand)
            if best_hand(curr_hand) > best:
                best = best_hand(curr_hand)
            hand.remove(combo[0])
            hand.remove(combo[1])
    elif '?B' in hand:
        hand.remove('?B')
        for card in black:
            hand.append(card)
            curr_hand = sorted(hand)
            if best_hand(curr_hand) > best:
                best = best_hand(curr_hand)
            hand.remove(card)
    elif '?R' in hand:
        hand.remove('?R')
        for card in red:
            hand.append(card)
            curr_hand = sorted(hand)
            if best_hand(curr_hand) > best:
                best = bes-hand(curr_hand)
            hand.remove(card)
   
    else:
        best = best_hand(hand)
        
    return sorted(best)

def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    
    # Your code here
    return max(itertools.combinations(hand,5), key=hand_rank)
     

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'

# ------------------
# Provided Functions
# 
# You may want to use some of the functions which
# you have already defined in the unit to write 
# your best_hand function.

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    """Return True if the ordered 
    ranks form a 5-card straight."""
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has 
    exactly n-of-a-kind of. Return None if there 
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """If there are two pair here, return the two 
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None 

print test_best_wild_hand()
#best_wild_hand("6C 7C 8C 9C TC 5C ?B".split())
