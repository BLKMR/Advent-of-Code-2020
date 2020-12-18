## Advent of Code Day 5: Part 1
## Michael Blackmer 12/15/2020


with open('seating.txt', 'r') as datastring:
    data = datastring.read()
datalist = data.split('\n')


def split_front(a_list):
    half = len(a_list)//2
    return a_list[:half]

def split_back(a_list):
    half = len(a_list)//2
    return a_list[half:]

row = []
col = []
F = []
B = []
L = []
R = []
final = []
seatids = []


for line in datalist:
    row = line[:-3]
    col = line[7:]
    
    if line == '':
        break

    if line[0] == "F":
        F = range(0,63)
        scanned = line[1::]
        for x in scanned:
            if x == "F":
                fr = split_front(F)
                F = fr
            if x == "B":
                bk = split_back(F)
                F = bk
            elif x == "F":
                fr = split_front(F)
            elif x == "B":
                bk = split_back(F)
        answerrow = F[0]       
    
    if line[0] == "B":
        B = range(64,128)
        scanned2 = line[1::]
        for x in scanned2:
            if x == "F":
                fr = split_front(B)
                B = fr
            if x == "B":
                bk = split_back(B)
                B = bk
            elif x == "F":
                fr = split_front(B) 
            elif x == "B":
                bk = split_back(B)
        answerrow = B[0]


    if col[0] == "R":
        R = range(4,8)
        col2 = col[1::]
        for x in col2:
            if x == "R":
                rgt = split_back(R)
                R = rgt
            if x == "L":
                lft = split_front(R)
                R = lft
            elif x == "R":
                rgt = split_back(R)
            elif x == "L":
                lft = split_front(R)
        answer = R[0]


    if col[0] == "L":
        L = range(0,4)
        col3 = col[1::]
        for x in col3:
            if x == "R":
                rgt = split_back(L)
                L = rgt
            if x == "L":
                lft = split_front(L)
                L = lft
            elif x == "R":
                rgt = split_back(L)
            elif x == "L":
                lft = split_front(L)
        answer = L[0]

    
    seatids.append(answerrow * 8 + answer)
    final = max(seatids)

print(final)
    
