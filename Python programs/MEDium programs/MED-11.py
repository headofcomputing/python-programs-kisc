#get percentage from user
score = int(input("Please input your percentage: "))

#print the appropriate grade corresponding to the score
if score >= 90:

    print("Your grade is A*")

elif score >= 80:

    print("Your grade is A")

elif score >= 70:

    print("Your grade is B")

elif score >= 60:

    print("Your grade is C")

elif score >= 50:

    print("Your grade is D")

elif score >= 40:

    print("Your grade is E")

elif score < 40:

    print("Your grade is F")

#if the input is anything else, print invalid input.
else:

    print("Invalid input")
