def square(x):
    return x * x
print square(5)
def factorial(n):
    if n == 1:
        return n
    if n == 0:
        return 1
    return n * factorial(n-1)
print factorial(3)
