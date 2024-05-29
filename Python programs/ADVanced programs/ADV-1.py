

#create list teamA and teamB
teamA = ["Messi", "DiMaria", "Dybala", "Ronaldo"]
teamB = ["Rohit", "Anjan", "Rejin", "Anzal"]

#create temp
temp = None

#print teamA and teamB before conversion
print("teamA =",teamA,"\nteamB =", teamB)

#swap the values in each list using loop and temp
for i in range(0, 4):

    temp = teamA[i]

    teamA[i] = teamB[i]

    teamB[i] = temp

#print teamA and teamB after conversion
print("\nteamA =",teamA,"\nteamB =", teamB)


