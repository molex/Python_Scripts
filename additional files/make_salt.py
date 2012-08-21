import random
import string

# implement the function make_salt() that returns a string of 5 random
# letters use python's random module.
# Note: The string package might be useful here.

def make_salt():
    ###Your code here
    #nums = [random.randint(97,123) for x in range(5)]
    #alpha = map(chr, nums)
    #return "".join(alpha)
    #salt = ""
    #for x in range(5):
    #    num = random.randint(1,52)
    #    char = string.ascii_letters[num:num + 1]
    #    salt = salt + char
    #return salt
    return ''.join(random.choice(string.letters) for x in xrange(5))
print make_salt()

