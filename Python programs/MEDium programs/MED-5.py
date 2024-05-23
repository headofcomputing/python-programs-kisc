#get a number from the user
num = int(input("Please input a number: "))

#since we do not know if it is prime, we set it to False
prime = False                                       

#repeat for 2 -> half of num to use i in the equation
for i in range(2, num//2):                          

    if(num%i == 0):                                 

        break   #since it is divisible by a number, use break to go out of the loop                       

    #else, set prime to True
    else:                                            

        prime = True                                

#print the outcome
if(prime == True):                                  

    print(num, "is a prime number")


else:
    print(num, "is not a prime number")
