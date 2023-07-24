import math

def division():
    """ This code provides float division arithmetic functionality """

    floatInputOne = float(input('Enter the first number: '))
    floatInputTwo = float(input('Enter the second number: '))
    print("You entered " + str(floatInputOne) + " and " + str(floatInputTwo))

    try:
        result = floatInputOne / floatInputTwo
        print()
        print("The results of the division of " + str(floatInputOne)+ " and " +str(floatInputTwo) + " is: " + str(result))

    except ValueError:
        print("Integers Please")

division()
