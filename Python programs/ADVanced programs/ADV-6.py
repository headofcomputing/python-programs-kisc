#set tuples for finding city with most or least wastes
most = ("",0)
least = ("",0)

#for the specified range:
for i in range(0, 3):

    #get city and amount of waste of the city
    city = str(input("Please name a city that produces waste: "))
    waste = int(input("How much waste do they produce? (In kg):"))

    #This is for initializing least[1].
    if(least[1] == 0):

        least = (city, waste)
    
    #if amount of waste is greater than most[1]'s value, change the tuple to that value
    if(waste > most[1]):

        most = (city, waste)
    
    #else if amount of waste is less than least[1]'s value, change the tuple to that value
    elif(waste < least[1]):

        least = (city, waste)

#print the city with the most or least amount of waste
print("\n")
print(most[0], "produces the largest amount of waste out of the three cities")
print(least[0], "produces the least amount of waste out of the three cities")

