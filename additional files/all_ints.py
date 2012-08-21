# ------------
# User Instructions
#
# Define a function, all_ints(), that generates the 
# integers in the order 0, +1, -1, +2, -2, ...

def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1
    

def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    # Your code here.
    count = 0
    i = 0
    while True:
        if count == 0:
            yield 0
            count = count + 1
            i = i + 1
        elif count %2 == 0:
            yield -1 * i
            count = count + 1
            i = i+1
        else:
            yield i
            count = count +1
            
            
   
a = all_ints() 
for i in range (10):
    print next(a)
