#get input from user
a = int(input("Please input a number:"))
b = int(input("Please input another number:"))

#get mathematical functions from user
func = input("What do you wish to do -  add/mul/div/sub?: ")


#set result
result = 0

#add/mul/div/sub respectively, set result to the outcome and print the result
if(func == "add"):
    
    result = a + b
    print("The sum of the two numbers is:", result)
    

elif(func == "mul"):

    result = a * b
    print("The multiplied result of the two numbers is:", result)

elif(func == "div"):

    result = a / b
    print("The divided result of the two numbers is:", result)

elif(func == "sub"):

    result = a - b
    print("The subtracted result of the two numbers is:", result)

    