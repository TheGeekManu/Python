#Create a literal string
testString = "My friend is called Stållion Krughåz"

#Use the encode function without parameters.
#Note the default choice is UTF-8 when no encoding parameter is set.
print(testString.encode())
print("\n")

#Print encoded values under ASCII encoding with error parameters set
print(testString.encode(encoding="ascii",errors="backslashreplace"))
print("\n")
print(testString.encode(encoding="ascii",errors="ignore"))
print("\n")
print(testString.encode(encoding="ascii",errors="namereplace"))
print("\n")
print(testString.encode(encoding="ascii",errors="replace"))
print("\n")
print(testString.encode(encoding="ascii",errors="xmlcharrefreplace"))

