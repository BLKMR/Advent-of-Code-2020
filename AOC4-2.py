import re
import string


with open('credentials.txt', 'r') as datastring:
    data = datastring.read()
datalist = data.split('\n')


list1 = []
list2 = []
newdata = []
dataset = []
setofdata = []

count = 0
havecid = 0
valids = 0
invalid = 0

for x in datalist:
    a = x.split()
    list1.extend(a)
    list2 = datalist[-1].split()
    if x == '':
        newdata.append(list1)
        list1 = []
    if x == datalist[-1]:
        newdata.append(a)
    

## PART 2 CODE
#  TO CHECK OLDVALID PASSPORTS FOR REQUIRED FIELDS        

        
byr = 'byr:'
iyr = 'iyr:'
eyr = 'eyr:'
hgt = 'hgt:'
hcl = 'hcl:'
ecl = 'ecl:'
pid = 'pid:'
cid = 'cid:'


good = []
passports = 0


## Nest a for loop in newdata to check each element.
## If element is there, check all

for x in newdata:
    for s in x:      
        ## ADDS "BYR:" TO "GOOD" LIST IF VALID   

        if byr in s:
            s = (int(s[4:8]))
            if s in range(1919,2003):
                s = byr + str(s)
                good.append(s)

        ## ADDS "IYR:" TO "GOOD" LIST IF VALID

        elif iyr in s:
            s = (int(s[4:8]))
            if s in range(2009, 2021):
                s = iyr + str(s)
                good.append(s)



        ## ADDS "EYR:" TO "GOOD" LIST IF VALID        

        elif eyr in str(s):
            s=(int(s[4:8]))
            if s in range(2019, 2031):
                s = eyr + str(s)
                good.append(s)


        ## ADDS "HGT:" TO "GOOD" LIST IF VALID

        elif hgt in s:
            height = s.split('hgt:')
            h = height[1]
            if len(h) >= 4:
                if len(h) == 4 and 'in' in h:
                    numbr = h[:2]
                    if int(numbr) >= 59 <= 76:
                        good.append(s)
                if len(h) == 5 and 'cm' in h:
                    numbr = h[:3]
                    if int(numbr) >= 150 <= 193:
                        good.append(s)



        ## ADDS "HCL:" TO "GOOD" LIST IF VALID

        elif hcl in str(s):
            if s[4] == '#':
                for x in s[5:]:
                    if x.isdigit() and int(x) >= 0 <= 9:
                        count += 1
                    elif x.isalpha() and x in string.ascii_lowercase[0:6]:
                        count += 1
                if count >= 6:
                    good.append(s) 

                    count = 0


        ## ADDS "ECL:" TO "GOOD" LIST IF VALID

        elif ecl in str(s):
            colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            color = s[4:]
            if color in colors:
                good.append(s)


        ## ADDS "PID:" FIELD TO "GOOD" LIST IF VALID

        elif pid in str(s):
            if len(s[4:]) == 9:
                good.append(s)


    ## ADDS "CID:" TO "GOOD" LIST IF VALID

        elif cid in str(s):
            good.append(s)


    for t in good:
        if cid in t:
            good.remove(t)

    if len(good) == 7:
        passports += 1

    ## Clear the list to restart the loop
    ## to check new list is valid.

    good.clear()


print("Out of", len(newdata), "passports. There are", passports," are valid!")



        
    


     





        
                        

                    






            



