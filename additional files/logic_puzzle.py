"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:
laptop - !Wilkes
droid - Wilkes
tablet
iphone

programmer - not Wilkes, is Hamming
writer - !Minsky,!monday
manager - !Knuth, !Tablet,is simon
designer - !Thursday,!Droid

Monday 
Tuesday - Iphone, or Tablet
WednesDay - laptop,not Wilkes
Thursday- !Designer
Friday- !Tablet

KNuth = Simon +1 and Manager +1















11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.




You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""
import itertools

def logic_puzzle():
    "Return a list of the names of the people, in the order they arrive."
    ## your code here; you are free to define additional functions if needed
    programmers = {1:'Hamming',2:'Knuth',3:'Minsky',4:'Simon',5:'Wilkes'}
    days = Monday,Tuesday,Wednesday,Thursday,Friday = [1,2,3,4,5]
    orderings = list(days)
    values =  next(list((Hamming,Knuth,Minsky,Simon,Wilkes))
                for(Hamming,Knuth,Minsky,Simon,Wilkes) in orderings
                for(Programmer,Writer,Manager,Designer,Nothing) in orderings
                for(Laptop,Droid,Tablet,Iphone,Empty) in orderings
                if Programmer is Hamming and Wilkes is Droid and Wednesday is Laptop and Programmer is not Wilkes and Writer is not Minsky and Knuth is not Manager and dayAfter(Knuth,Simon)and dayAfter(Knuth,Manager) 
                if Thursday is not Designer and Friday is not Tablet and Designer is not Droid and (Tuesday is Iphone or Tuesday is Droid) and Wilkes is not Laptop and Tablet is not Manager
                if Laptop is Writer and Wilkes is Monday
                )
    resultList = []
    for item in values:
        for x,y in programmers.iteritems():
            if x is item:
                resultList.append(y)

    return resultList
                



def dayAfter(f1,f2):
    return (f1 -f2)== 1

print logic_puzzle()
    
