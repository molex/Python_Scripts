# Investigating adding and appending to lists

# If you run the following four lines of codes, what are list1 and list2?

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

list1 = list1 + [5]
list2.append(5)

# to check, you can print them out using the print statements below.

# print list1
# print list2

# What is the difference between these two pieces of code?

def proc(mylist):
    mylist = mylist + [6]
    print mylist

def proc2(mylist):
    mylist.append(6)
    print mylist
# mylist = [1, 2, 3]
# proc(mylist)
# proc2(mylist)
# print mylist
# Can you explain the results given by the four print statements below? Remove
# the hashes # and run the code to check.

# print list1
# proc(list1)
# print list1

# print list2
# proc2(list2)
# print list2

# Python has a special assignment syntax: +=.  Here is an example:

list3 = [1, 2, 3, 4]
list3 += [5]

# Does this behave like list1 = list1 + [5] or list2.append(5)? Write a
# procedure, proc3 similar to proc and proc2, but for +=. When you've done
# that check your conclusion using the print-procedure call-print code as
# above.

# What happens when you try:

# ist1 = list1 + [7, 8, 9]
# print list1
# list2.append([7, 8, 9])
# print list2
# list3 += [7, 8, 9]
# print list3
# When you've understood the difference between the three methods,
# write a procedure list_test which takes three lists as inputs. You should
# mutate the first input list to include 'a' as the last entry, mutate the
# second to include the entries 'a', 'b', 'c' and finally the last list should
# not be mutated but a copy should be returned with the additional entry 'w'.

def list_test(a, b, c):
    # Your code here
    new = []
    a.append('a')
    b += ['a', 'b', 'c']
    new = c
    new + ['w']
    return new



first_input = [1, 2, 3]
second_input = [4, 5, 6]
third_input = [7, 8, 9]

print list_test(first_input, second_input, third_input)
# >>> [7,8,9,'w']
print first_input
# >>> [1,2,3,'a']
print second_input
# >>> [4,5,6,'a','b','c']
print third_input
# >>> [7,8,9]

