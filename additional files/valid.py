import string, re
def valid(f):
    try:
        return not re.search(r'\b0[0-9]',f) and eval(f) is True 
    except ArithmeticError:
        return False

print valid('1+1==3')
