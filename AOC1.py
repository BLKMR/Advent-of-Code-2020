def read_integers():
    with open('expense.txt') as f:
        return [int(x) for x in f]



for i in read_integers():
    num1 = 2020 - i
    for b in read_integers():
        if b == num1:
            print(b*i)

#  The code below scans through my file 3 times and checking to see if each number through adds with the other numbers to meet 2020
                   
for num1 in read_integers():
    for num2 in read_integers():
        for num3 in read_integers():
            if (num1 + num2 + num3) == 2020:
                print(num1, num2, num3)
                found = (num1 * num2 * num3)
                print(found)
                break
            
            
            
             
 

