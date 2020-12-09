import itertools
from collections import Counter

data = open('pwpolicy.txt', 'r')
datastring = data.read()
datalist = datastring.split()


keys = datalist[0::3]
letters = datalist[1::3]
pw = datalist[2::3]

letter = [elem.strip(':') for elem in letters]

valids = 0
invalids = 0
newkeys = []

for i in datalist[0::3]:
    a = i.split('-')
    res = [int(i) for i in a]
    newkeys.append(res)


for (a, b, c) in  zip(letter, pw, newkeys):
    count = Counter(b)
    print(a, b, c, int(count[a]))
    s = int(count[a])
    print(c[1])
    if s > c[1]:
        invalids = invalids + 1
        print("invalid")
    elif s < c[0]:
        invalid = invalids + 1
        print("invalid")
    else:
        valids = valids + 1
        print("valid")



print(valids)
    
 


        










    







