#Create different types of set collections
university = {"University of California", "Oxford University", "MIT"}
decimalNumbers = {1, 5, 7, 9, 3}

#Duplicates are considered tobe one, they are not allowed
#One and True are the considered the same i.e. duplicates
booleanValues = {1, True, False, False}

#Use set constructor
nuclearFamily = set({"Father","Mother","Children"})

for x in university:
    print(x)

print("\n")

for x in decimalNumbers:
    print(x)

print("\n")

for x in booleanValues:
    print(x)

print("\n")

for x in nuclearFamily:
    print(x)

print("\n")

print(type(university))
print(type(decimalNumbers))
print(type(booleanValues))
print(type(nuclearFamily))

print("\n")

#Check the length of our set
print(len(nuclearFamily))
