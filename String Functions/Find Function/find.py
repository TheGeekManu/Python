#Create a literal string
findString = "Hey, do you mind going out for lunch ."

#Function to output results.
def findResult():
    '''A value of -1 is returned when an item is not found'''
    
    if findValue==-1:
        print('No such letter or word was found')
        print('\n')
    else:
        print(findValue)
        print('\n')

#Find a letter or word without start and end parameters set.
findValue = findString.find("m")
findResult()


#Find a letter or word with the start and end parameters set.
findValue = findString.find("o", 5, 10)
findResult()

#Try to find a letter not in our string.
#You should get the "No such letter or word was found" reply from our findResult() function.
findValue = findString.find("z")
findResult()


