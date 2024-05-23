#get country, age and driving test results from user
uCountry = str(input("What country are you from?: "))
uAge = int(input("What is your age?: "))
udTest = str(input("What was the result of your driving test? Pass/Fail: "))

#set licenseGrant to False
licenseGrant = False

#check the test results first, since the license is not granted if the result is Fail.
if(udTest == "Pass" or udTest == "pass"):

    #if Pass, then check age.
    if(uAge >= 16):

        #if the age is met, then check for countries.
        if((uCountry == "Nepal" or uCountry == "nepal") or (uCountry == "Australia" or uCountry == "australia")):

            #if the conditions are all met, set licenseGrant to True.
            licenseGrant = True

    #repeat.
    if(uAge >= 17):

        if(uCountry == "UK" or uCountry == "uk"):

            licenseGrant = True

    if(uAge >= 18):

        if((uCountry == "USA" or uCountry == "usa") or (uCountry == "Korea" or uCountry == "korea")):

            licenseGrant = True

else:

    licenseGrant = False


#if licenseGrant is True, then print Granted. Else, print not Granted.
if(licenseGrant == True):

    print("Granted")

else:

    print("not Granted")


