# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(l):
    long = ()
    current = ()
    for i in l:
       if not current and not long:
           current = (i,0)
           long = current
       if current[0] == i:
           current = (i,current[1] + 1)
       else:
           current = (i,1)
           
       if long[0] == current[0]:
        long = current
       else:
           if current[1] > long[1]:
               long = current
    if long:
        return long[0]
    else:
        return None
        





#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

