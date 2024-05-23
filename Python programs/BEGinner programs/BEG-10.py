#ask the user for the value of the initial velocity
u = int(input("What is the initial velocity?: "))

#ask the user for the value of the acceleration
a = int(input("What is the acceleration of the car?: "))

#ask the user for the time
t = int(input("What is the time?: "))

#Calculate the final velocity by using the formula v = u + at
v = u + (a * t)

#print the final velocity
print("The final velocity is:", v)
