#get three numbers from user
a = int(input("Please input the first number: "))
b = int(input("Please input the second number: "))
c = int(input("Please input the third number: "))

#if b is greater than a...
if(a < b):          

    #check if c is larger than b
    if(b < c):                            
        print(c, "is the largest number") 

    else:
        print(b, "is the largest number")

#or if a is greater than b...
elif(a > b):

    #check if c is larger than a
    if (a < c):
        print(c, "is the largest number")

    else:
        print(a, "is the largest number")
