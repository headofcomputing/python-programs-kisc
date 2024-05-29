#get list from ADV-7
extractedList = ['33jzbz8boz', 
                 'prxfpjr8z0', 
                 '10urskfvni', 
                 '18ecdupx6b', 
                 '5azjiac111', 
                 'ukvea90o99', 
                 'f1n1nzwyn4', 
                 'umcj9bt4oy', 
                 'i1l6rrb68y', 
                 'bk2cv88whx']

#get user's username from the user
username = str(input("Please type your username: "))

#for i in range of length of extractedList:
for i in range(len(extractedList)):

    #if username matches element, print yes.
    if(username == extractedList[i]):

        print("Your username is in the list!")

    #else, print no.
    else:

        print("Your username is not on the list.")


