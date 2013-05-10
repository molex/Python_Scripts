# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    # #
    # Your code here.
    # #
    daysPrior = 0
    if year1 < 1900:
        daysPrior = getPriorDays(year1, month1, day1)
        year1 = 1900
        month1 = 1
        day1 = 1
        daysFirstYear = daysSinceBeginning(year1 - 1) + daysInThisYear(year1, month1, day1)
        daysLastYear = daysSinceBeginning(year2 - 1) + daysInThisYear(year2, month2, day2)
    else:
        daysFirstYear = daysSinceBeginning(year1 - 1) + daysInThisYear(year1, month1, day1)
        daysLastYear = daysSinceBeginning(year2 - 1) + daysInThisYear(year2, month2, day2)
    return (daysLastYear - daysFirstYear) + daysPrior
 
def daysSinceBeginning(year):
    days = 0
    while year >= 1900:
        days = days + daysInYear(year)
        year = year - 1
    return days
def getPriorDays(year, month, day):
    daysElapsed = daysInThisYear(year, month, day)
    days = 0
    day = 1
    month = 1
    while year < 1900:
        days = days + daysInYear(year)
        year = year + 1
    return days - daysElapsed
                
def daysInThisYear(year, month, day):
    days = day
    month = month - 1
    while month > 0:
        days = days + getNumDaysInMonth(month, year)
        month = month - 1
    return days      
                    
def getNumDaysInMonth(month, year):
    if(month == 4 or month == 6 or month == 9 or month == 11):
        return 30
    if(month == 2):
        if(isLeapYear(year)):
            return 29
        else:
            return 28
    else:
        return 31
def isLeapYear(year):
    if year % 400 == 0:
        return True
    if (year % 100 == 0):
        return False
    if year % 4 == 0:
        return True
    else:
       return False
def daysInYear(year):
    if year % 400 == 0:
        return 366
    if (year % 100 == 0):
        return 365
    if year % 4 == 0:
        return 366
    else:
        return 365    
    
result = daysBetweenDates(2012, 6, 29, 2013, 6, 29)
print result
# Test routine

def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                   ((2012, 1, 1, 2012, 3, 1), 60),
                   ((2011, 6, 30, 2012, 6, 30), 366),
                   ((2011, 1, 1, 2012, 8, 8), 585),
                   ((1900, 1, 1, 1999, 12, 31), 36523),
                   ((1898, 3, 1, 1999, 12, 31), 37193)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

