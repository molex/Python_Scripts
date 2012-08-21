import itertools
import time
def zebra_puzzle():
    "Return a tuple (Water,Zebra) indicating thier house numbers."
    houses = first,_,middle,_,_ = [1,2,3,4,5]
    orderings = list(itertools.permutations(houses)) #1
    return next ((Water, Zebra)
                 for (red, green, ivory,yellow,blue) in orderings
                 if imright(green, ivory)         #6
                 for (Englishman,Spaniard, Ukranian, Japanese, Norwegian) in orderings
                 if Englishman is red             #2
                 if Norwegian is first            #10
                 if nextto(Norwegian,blue)        #15
                 for (coffee, tea, milk, oj, Water) in orderings
                 if coffee is green               #4
                 if Ukranian is tea               #5
                 if milk is middle                #9
                 for (oldGold, kools, chesterfields, luckyStrike, parliments)in orderings
                 if kools is yellow               #8
                 if luckyStrike is oj             #13
                 if Japanese is parliments        #14
                 for (dog, snails, fox, horse, Zebra) in orderings
                 if Spaniard is dog               #3
                 if oldGold is snails             #7
                 if nextto(chesterfields,fox)     #11
                 if nextto(kools, horse)          #12
                 )

def imright(h1,h2):
    return h1-h2 == 1

def nextto(h1,h2):
    return abs(h1-h2)==1

def t():
    t0 = time.clock()
    zebra_puzzle()
    t1 = time.clock()
    return t1 -t0
print t()
