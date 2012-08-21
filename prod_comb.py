import itertools

black = ("2C 2S 3C 3S 4C 4S 5C 5S 6C 6S 7C 7S 8C 8S 9C 9S TC TS JC JS QC QS KC KS AC AS").split()
red = ("2H 2D 3H 3D 4H 4D 5H 5D 6H 6D 7H 7D 8H 8D 9H 9D TH TD JH JD QH QD KH KD AH AD").split()


print list(itertools.product(black,red))
  
