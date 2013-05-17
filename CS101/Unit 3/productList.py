# Define a procedure, product_list,
# takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(n):
    sum = 1
    for x in n:
        sum = sum * x
    return sum







print product_list([9])
# >>> 9

print product_list([1, 2, 3, 4])
# >>> 24

print product_list([])
# >>> 1
