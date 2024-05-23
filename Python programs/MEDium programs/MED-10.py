#get citizenship, age and test status from the user
userCitizenship = str(input("What country is your citizenship from?: "))
userAge = int(input("What is your age?: "))
userTestStatus = str(input("Did you pass the Driving Test? T/F: "))

#set licence to False
licence = False

#if userCitizenship is Nepal, userAge is over 18, and userTestStatus is true...
if((userCitizenship == "Nepal") or (userCitizenship == "nepal")):

    if(userAge > 18):

        if((userTestStatus == "T") or (userTestStatus == "t")):

            #...set licence to True
            licence = True

#Else, set licence to False
else:

    licence = False

#if the licence is True, print qualified. Else, print not qualified.
if(licence == True):

    print("You are qualified of a driving licence!")

else:
    
    print("You are not qualified of a driving licence!")




            
