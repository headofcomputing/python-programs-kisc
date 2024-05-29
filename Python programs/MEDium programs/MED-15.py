#create string randomData
randomData = "WordFishMathBookTreeRockPlanStar"

#create string vowel to use in if statement
vowel = "aeiouAEIOU"

#create counters for vowels and consonants
vowelChar = 0
consoChar = 0

#for each character in randomData:
for i in randomData:

    #if the character is one of the characters in vowel, raise vowelChar by 1
    if(i in vowel):

        vowelChar += 1
    
    #else, raise consoChar by 1
    else:

        consoChar += 1
    

#print the results
print(vowelChar, "vowels present in randomData")
print(consoChar, "consonants present in randomData")


