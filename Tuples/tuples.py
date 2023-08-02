#A Tuple: collection which is ordered and unchangeable but allows duplicate members.

#Create a tuple with one item
age = (12,)
print(age)
print("\n")
print(type(age))
print("\n")

#Create tuples with multiple values
age = (6, 8,45,50)
boolean_values = ("True", "False")
time = ("7:00", "12:00", "6:00", "10:00")

#Use the tuple constructor
fish = tuple(("Shark","Dolphin","Whale","Tilapia"))

#Tuples are ordered and immutable
for x in age:
    print(x)

print("\n")

for x in boolean_values:
    print(x)

print("\n")

for x in time:
    print(x)

print("\n")

for x in fish:
    print(x)

print("\n")
print(type(age))
print(type(boolean_values))
print(type(time))
print(type(fish))
