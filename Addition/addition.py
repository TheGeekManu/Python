import math

digitOne = input('Enter the first number: ')
digitTwo = input('Enter the second number: ')

try:
    integerInputOne = int(digitOne)
    integerInputTwo = int(digitTwo)
    print("You entered " + digitOne + " and " + digitTwo)
    result = integerInputOne + integerInputTwo
    print()
    print("The result of " + str(integerInputOne) +" + " + str(integerInputTwo) + " is: " + str(result))

except ValueError:
    print("Integers Please")


