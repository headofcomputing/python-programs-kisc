#import random module as r.
import random as r

#set rows and columns for a 2D Array.
rows, columns = 3, 3

#set counters for numbers divisible by 2 or 3.
div2 = 0
div3 = 0

#create a 2D Array. i creates columns, j creates rows of 2D Array.
randomArray = [[0 for i in range(columns)] for j in range(rows)]

#nested for to cycle each element in a 2D Array
for i in range(0, 3):

    for j in range(0, 3):

        #create a random number and set element to random number
        rnum = r.randint(0, 100)

        randomArray[i][j] = rnum
        
        #if rnum is divisible by 2 or 3, raise appropriate counter
        if(rnum%2 == 0):

            div2 += 1

        if(rnum%3 == 0):
            
            div3 += 1

#print array
print(randomArray)

#print counters
print(div2,"numbers are divisible by 2")
print(div3,"numbers are divisible by 3")


