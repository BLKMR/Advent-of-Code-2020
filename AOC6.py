## Advent of Code Day 6 Part 1 ##


with open('groups.txt', 'r') as datastr:
    data = datastr.read()
datalist = data.split('\n')



count = 0
splice = []
group = []
groups = []
totalsum = 0

for x in datalist:
    splice.extend(x)
    if x == '':
        groups.append(splice)
    else:
        groups.extend(splice)
    splice = []


key = list(map(chr, range(97, 123)))



def match_elements(a, b):
    match = []
    for i in a:
        if i in b:
            match.append(i)
    return match

    

for i in groups:
    for x in key:
        if i == x:
            group.append(x)                     
    if i == []:
        group = list(dict.fromkeys(group))
        yes = len(match_elements(key, group))
        totalsum += yes
        group = []

print(totalsum)
    
