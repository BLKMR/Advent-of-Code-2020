import itertools
from collections import Counter

data = open('pwpolicy.txt', 'r')
datastring = data.read()
datalist = datastring.split()


keys = datalist[0::3]
letters = datalist[1::3]
pw = datalist[2::3]
letter = [elem.strip(':') for elem in letters]

invalids = 0
newkeys = []

for i in datalist[0::3]:
    a = i.split('-')
    res = [int(i) for i in a]
    newkeys.append(res)


for (a, b, c) in  zip(letter, pw, newkeys):
    count = Counter(b)
    s = int(count[a])
    print(a, b, c)
    checkone = b[c[0]-1]
    checktwo = b[c[1]-1]
    if a==checkone and a==checktwo:
        invalids += 1
    if a!=checkone and a!=checktwo:
        invalids += 1
   
print(1000 - invalids)






    
 


        










    







