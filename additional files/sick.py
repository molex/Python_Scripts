# --------------
# user instructions
#
# write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# grading notes:
# 
# you will only be marked correct if your function runs 
# efficiently enough. we will be measuring efficency by counting
# the number of times you access each string. that count must be
# below a certain threshold to be marked correct.
# improved efficiency:
# write a function to generate all possible sub-words like [word,i,j]
# sort list according to length
# for each word, starting with the longest word,
# check if valid
import itertools

def longest_subpalindrome_slice(text):
    "return (i, j) such that text[i:j] is the longest palindrome in text."
    # your code here
    if text is '':
        return 0,0
    text = text.upper()

    generate_words(text)

def generate_words(text):
    nums = []
    word_list=[]
    for number in range(0,len(text)+1):
        nums.append(number)
    for start,end in list(itertools.combinations(nums, 2)):
        new_word = list(itertools.islice(text,start,end))
        new_word = "".join(new_word)
        word_list.append([new_word,start,end])
    valid(word_list)

def valid(word_list):
    valid_words = []
    for word in word_list:
        if word[0] == word[0][::-1]:
            valid_words.append([word[1],word[2]])
    longest(valid_words)

def longest(valid_words):
    test = max(valid_words, key=difference)
    #print tuple(test)
    return test

def difference(long_words):
    return long_words[1] - long_words[0]

                    
def test():
    l = longest_subpalindrome_slice
    #assert l('racecar') == (0, 7)
    #assert l('racecar') == (0, 7)
    ##assert l('racecarx') == (0, 7)
    #assert l('race carr') == (7, 9)
    #assert l('') == (0, 0)
    #assert l('something rac e car going') == (8,21)
    assert l('xxxxx') == (0, 5)
    assert l('mad am i ma dam.') == (0, 15)
    return 'tests pass'

#print test()
doh = longest_subpalindrome_slice('racecar')
print doh
