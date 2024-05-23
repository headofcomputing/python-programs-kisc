#ask for the points each player scored in the red team
red1 = int(input("How many points did the red1 player score?: "))
red2 = int(input("How many points did the red2 player score?: "))
red3 = int(input("How many points did the red3 player score?: "))

#print "\n" to add a gap between each section of print
print("\n")

#ask for the points each player scored in the blue team
blue1 = int(input("How many points did the blue1 player score?: "))
blue2 = int(input("How many points did the blue2 player score?: "))
blue3 = int(input("How many points did the blue3 player score?: "))

#Calculate total points each team scored
redTotal = red1 + red2 + red3
blueTotal = blue1 + blue2 + blue3

#Find average by dividing total points by 3...
redAvg = redTotal / 3
blueAvg = blueTotal / 3

#... and find the difference by subtracting redAvg by blueAvg
redBlueDiff = redAvg - blueAvg

#same here - for a gap between
print("\n")

#print the average points of each team and the difference 
print("The average points of red team is:", redAvg)
print("The average points of blue team is:", blueAvg)
print("The difference in average points of red and blue is:", redBlueDiff)

