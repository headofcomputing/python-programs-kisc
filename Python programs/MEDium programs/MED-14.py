#This method will come out frequently. Try to understand how the swap with temp variable works.

#create list with names of channels
names = ["MrBeast", "GothamChess", "National Geographic", "HISTORY", "Mark Rober"]

#create list with views
views = [86000000, 292000, 246000, 235000, 14000000]

#create a variable that will "temporarily" hold the value swapping
temp = None

#print each list before conversion
print("names =", names)
print("views =", views)

#swap each values:
for i in range(0, 5):

    #value in names[i] goes to temp
    temp = names[i]

    #then replace the value in names[i] to the value in views[i]
    names[i] = views[i]

    #and replace the value in views[i] to the value in temp.
    views[i] = temp

#print each list after conversion
print("\n\n")
print("names =", names)
print("views =", views)

