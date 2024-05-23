#get string from user
sen = str(input("Please input a string: "))

#initialise counter for vowel
vowelCount = 0

#run for length of string
for i in range(0, len(sen)):
    
    #if it is a, e, i, o, or u, increase vowelCount by 1
    
    if((sen[i] == "a") or (sen[i] == "A")):

        vowelCount = vowelCount + 1

    elif((sen[i] == "e") or (sen[i] == "E")):

        vowelCount = vowelCount + 1

    elif((sen[i] == "i") or (sen[i] == "I")):

        vowelCount = vowelCount + 1

    elif((sen[i] == "o") or (sen[i] == "O")):

        vowelCount = vowelCount + 1

    elif((sen[i] == "u") or (sen[i] == "U")):

        vowelCount = vowelCount + 1

#print vowelCount
print("The string has", vowelCount, "vowels")
