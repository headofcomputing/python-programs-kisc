#create list ages with ages of 20 people
ages=[70, 85, 54, 92, 22, 49, 22, 78, 41, 18, 20, 85, 90, 8, 89, 92, 41, 59, 82, 48]

#create variable for counting numbers that are even, odd, divisible by 5, over 50
evenNum = 0
oddNum = 0

div5 = 0
over50 = 0

#Also create variable for calculating sum of numbers that are even, odd, total, and average
sumEven = 0
sumOdd = 0

totalAge = 0
avgAge = 0

#for each value in ages, compare each if statement to raise appropriate counters and sum
for i in ages:

    if(i%2 == 0):
        
        evenNum += 1
        sumEven += i
    
    else:

        oddNum += 1
        sumOdd += i

    if(i%5 == 0):

        div5 += 1

    if(i > 50):

        over50 += 1

    totalAge += i

#calculate average age
avgAge = totalAge / len(ages)

#print all the values except totalAge
print(evenNum, "ages were even")
print(oddNum, "ages were odd")

print(div5, "ages were divisible by 5")
print(over50, "ages were over 50")

print("The total sum of even ages were:", sumEven)
print("The total sum of odd ages were:", sumOdd)

print("The average age of 20 people was:", avgAge)


