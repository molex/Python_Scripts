# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n): 
    alpha = 'abcdefghijklmnopqrstuvwxyz'
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

def rotate(string, num):
    # Your code here
    newString = ''
    for char in string:
        if char != " ":
            newString += shift_n_letters(char, num)
        else:
            newString += char
    return newString
        
        

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???