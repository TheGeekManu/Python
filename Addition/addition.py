import math

digitOne = input('Enter the first number: ')
digitTwo = input('Enter the second number: ')

try:
    floatInputOne = float(digitOne)
    floatInputTwo = float(digitTwo)
    print("You entered " + digitOne + " and " + digitTwo)
    result = floatInputOne + floatInputTwo
    print()
    print("The result of " + str(floatInputOne) +" + " + str(floatInputTwo) + " is: " + str(result))

except ValueError:
    print("Integers Please")


