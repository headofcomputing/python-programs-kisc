#set variables needed for the program
divBy7 = 0
notDiv7 = 0
total = 0

#since we need 13 inputs and compare each, it is best to do a for loop
for i in range(0, 13):
    
    #get number from user
    number = int(input("Please input a number: "))
    
    #if number is divisible by 7, print "Divisible" and raise divBy7 by 1. 
    if(number%7 == 0):
        
        print("Divisible")

        divBy7 += 1
    
    #Else, print "Not divisible" and raise notDiv7 by 1. 
    else:

        print("Not divisible")

        notDiv7 += 1

        #add the number to the total.
        total = total + number

#print the calculated values.
print("numbers were divisible by 7:", divBy7)
print("numbers were not divisible by 7:", notDiv7)
print("Total of numbers that were not divisible by 7:", total)
