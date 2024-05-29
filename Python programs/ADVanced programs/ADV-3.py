#create a list of random numbers
randomNumbers=[5, 56, 29, 91, 56, 6, 100, 13, 47, 78, 78, 89, 57, 41, 45, 72, 24, 92, 50, 81]

#create temp for swapping
temp = None

#print the list before swap
print("list:", randomNumbers)

#perform swap. However, since we are swapping 1-2, 3-4, 5-6 and so on, make so that i increases by 2.
for i in range(0, len(randomNumbers) - 1, 2):

    temp = randomNumbers[i]

    randomNumbers[i] = randomNumbers[i + 1]

    randomNumbers[i + 1] = temp


#print changed list.
print("\nchanged list: ", randomNumbers)


