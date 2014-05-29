# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.
alpha = 'abcdefghijklmnopqrstuvwxyz'
def shift_n_letters(letter, n):    
    num = alpha.find(letter)
    total = len(alpha)
    if(letter == alpha[0] and n < 0 ):
       letter = alpha[total -1]
       n = n + 1
       num = alpha.find(letter)
    if(letter == alpha[total -1] and n > 0 ):
        letter = alpha[0]
        n = n -1
        num = alpha.find(letter)
        
    if  num + n >= total:
        n = (num + n)  - total
        return shift_n_letters(alpha[0], n)
    elif  num + n < 0:
        n = num + n        
        return shift_n_letters(alpha[total -1], n+ 1)
    else:
        return alpha[alpha.find(letter)+n]
    



print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
print shift_n_letters('z', 1)
print shift_n_letters('a', -1)
print shift_n_letters('k', -12)
print shift_n_letters('z', 26)
