dict = {}
dict['john'] = [[],[]]
print dict
list = ['Bryant', 'Debra', 'Walter']
count = 0
for i in dict['john']:
        if count == 0:
            i.append(list)
            count = count + 1
        
print dict