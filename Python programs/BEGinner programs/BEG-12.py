#ask for user's age
ageYears = int(input("How old are you?: "))

#since the age is years, we start converting by changing the years to days
ageDays = ageYears * 365.25

#age into hours...
ageHours = ageDays * 24

#...into minutes...
ageMinutes = ageHours * 60

#and finally to seconds
ageSeconds = ageMinutes * 60

print("Your age in seconds is:", ageSeconds)
