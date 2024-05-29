#initialise counter for while loop and number
primeCounter = 0
num = 2

#take input from user for n prime numbers
n = int(input("How many prime numbers do you wish to find?: "))

#run while loop for selected amount
while primeCounter < n:

    #set prime numbers to False
    prime = False

    #Check if the number is 2 or 3.
    if((num / 2 == 1) or (num / 3 == 1)):
            
        prime = True
    
    else:

        #if it is not 2 or 3, check if the number is prime by using similar code from MED-5
        for i in range(2, num//2):
            
            if(num%i == 0):

                prime = False
        
                break
            
            else:

                prime = True

    #if the prime number is True, raise the counter by 1
    if(prime == True):
        primeCounter += 1
        
        print(num)

    #Also raise the number by 1
    num += 1





            
        
