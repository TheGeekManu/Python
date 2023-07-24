#Create a literal string
testString = "Hello, welcome to my world."

#Use the endswith function with no parameters
x = testString.endswith("my world.")
print(x)
print("\n")

#Use the endswith function with start and end parameters
x = testString.endswith("world", 20, 26)

print(x)
