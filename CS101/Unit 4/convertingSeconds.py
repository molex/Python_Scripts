# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3

def convert_seconds(seconds):
    hours = 0
    minutes = 0
    while seconds >= 3600:
        hours += 1
        seconds = seconds - 3600
    while seconds >= 60:
        minutes += 1
        seconds = float(seconds - 60)
    if hours > 1 or hours == 0:
        strHours = str(hours) + " hours"
    else:
        strHours = str(hours) + " hour"
    if minutes > 1 or minutes == 0:
        strMinutes = str(minutes) + " minutes"
    else:
        strMinutes = str(minutes) + " minute"
    if(int(seconds) == seconds):
        seconds = int(seconds)
    if seconds > 1 or seconds == 0:
        strSeconds = str(seconds) + " seconds"
    else:
        strSeconds = str(seconds) + " second"
    
    return strHours + ", " + strMinutes + ", " + strSeconds
    


print convert_seconds(3661)
# >>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
# >>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
# >>> 2 hours, 1 minute, 1.7 seconds
print convert_seconds(3600)