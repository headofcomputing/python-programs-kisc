#create email_list
email_list = [
    "33jzbz8boz@demo.com",
    "prxfpjr8z0@sample.org",
    "10urskfvni@test.com",
    "18ecdupx6b@example.com",
    "5azjiac111@test.com",
    "ukvea90o99@demo.com",
    "f1n1nzwyn4@example.com",
    "umcj9bt4oy@demo.com",
    "i1l6rrb68y@demo.com",
    "bk2cv88whx@mail.net"
]

#create empty extractedList for output
extractedList = []

#for i in range of length of email_list:
for i in range(len(email_list)):

    #reset extract at the start of each extraction
    extract = ""

    #for j in range of the length of element in email_list:
    for j in range(len(email_list[i])):
        
        #if the character is @, break
        if(email_list[i][j] == "@"):

            break
        
        #else, extract each character
        else:

            extract = extract + email_list[i][j]

    #after extraction, append the extracted part to the list
    extractedList.append(extract)

#print extractedList
print(extractedList)
    
        