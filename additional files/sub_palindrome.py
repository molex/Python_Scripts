# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
import itertools

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    text = text.upper()
    for i,j,word in sub(text):
        #print i,j,word
        if valid(word):
            return i,j
   
def sub(text):
    nums = []
    for number in range(0,len(text)+1):
        nums.append(number)
    print nums
    for start,end in itertools.combinations_with_replacement(nums, 2):
        new_word = list(itertools.islice(text,start,end))
        new_word = "".join(new_word)
        print new_word
        yield start,end, new_word
               
def valid(word):
    return word == word[::-1]
         
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    #assert L('Racecar') == (0, 7)
    #assert L('RacecarX') == (0, 7)
    #assert L('Race carr') == (7, 9)
    #assert L('') == (0, 0)
    #assert L('something rac e car going') == (8,21)
    #assert L('xxxxx') == (0, 5)
    #assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()
#longest_subpalindrome_slice('text')

