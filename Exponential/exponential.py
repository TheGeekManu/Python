import math

def exponential():
    """ This code provides exponential arithmetic functionality """

    base = float(input('Enter the base number: '))
    exponent = float(input('Enter the exponent number: '))
    print("You entered " + str(base) + " as the base number and " + str(exponent) + " as the exponent number.")

    try:
        result = base ** exponent
        print()
        print("The results of the exponent calculation of the base number " + str(base)+ " by an exponent value of " +str(exponent) + " is: " + str(result))

    except ValueError:
        print("Float Please.")

exponential()
