#Using named indexes:
name = "My name is {name}, I'm {age} years old".format(name = "Brian", age = 28)

#Using numbered indexes:
location = "I live in {0}, Mail me at {1}".format("Parklands, Australia.","seniorprogrammer@firemail.com")

#Formatted and empty placeholders:
hotel = "The price of coffee is {:.2f}$, I shall drink {} cups".format(2,4)

#Placeholder for separating values above 1000 with a comma.
car = "I bought a {price:,} dollar sports car".format(price = 5000000)

#Placeholder to return a hexadecimal value
hexadecimalAge = "My age in hexadecimal is {age:x} years old".format(age = 28)

#Placeholder to return a binary value
binaryAge = "My age in binary is {age:b} years old".format(age = 28)

#Placeholder to return an octal value
octalAge = "My age in octal is {age:o} years old".format(age = 28)

#Placeholder to center align a value
birds = "The island is home to over {:^8} species of birds.".format(36)

#Display formatted output to screen.
print(name)
print('\n')
print(location)
print('\n')
print(hotel)
print('\n')
print(car)
print('\n')
print(hexadecimalAge)
print('\n')
print(binaryAge)
print('\n')
print(octalAge)
print('\n')
print(hexadecimalAge)
print('\n')
print(birds)
