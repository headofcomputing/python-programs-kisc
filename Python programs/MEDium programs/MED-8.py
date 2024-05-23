#initialise counter for sum of even and odd numbers
evenSum = 0
oddSum = 0

#run for 100 times for numbers until 100
for i in range(1, 101):

    #if even - add i to evenSum. Else, add i to oddSum.
    if(i%2 == 0):

        evenSum = evenSum + i

    else:

        oddSum = oddSum + i

#print the sum of even and odd numbers
print("The sum of even numbers are:", evenSum)
print("The sum of odd numbers are:", oddSum)
