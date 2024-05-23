#decide the rate of 3 items in a restaurant
burger = 10
spaghetti = 12
friedRice = 8

#ask for the number of each items the user wants
burgerOrder = int(input("How many burgers?: "))

spaghettiOrder = int(input("How many spaghettis?: "))

friedRiceOrder = int(input("How many fried rice?: "))

#Find the total of each items by multiplying the rate and the number of items
burgerTotal = burger * burgerOrder
spaghettiTotal = spaghetti * spaghettiOrder
friedRiceTotal = friedRice * friedRiceOrder

#Find the bill by adding all the total of each items
bill = burgerTotal + spaghettiTotal + friedRiceTotal

#Print the bill
print("You have ordered:")
print(burgerOrder, "burgers")
print(spaghettiOrder, "spaghettis")
print(friedRiceOrder, "fried rice")
print("Your total is:", bill)
