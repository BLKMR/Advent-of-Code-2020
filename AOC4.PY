
data = open('credentials.txt', 'r')
datastring = data.read()
datalist = datastring.split('\n')

newdata = []
dataset = []

count = 0
havecid = 0
valids = 0
invalid = 0

for i in datalist:
    a = i.split(' ')
    for x in a:
        newdata.append(x)
        
for x in newdata:
    count += 1
    total = count - 1
    dataset.append(x)    
    if x == '':
        if total == 8:
            valids += 1
        if total == 7 and any("cid:" in s for s in dataset):
            invalid += 1
        elif total == 7:
            valids += 1
        count = 0
        dataset = []
        

print("valid", valids)
