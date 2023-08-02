person = {
  "name" : "Patrick Star",
  "age" : 30,
  "title" : "Professor",
}

car = {
  "brand": "Mercedes",
  "model": "E300",
  "colors": ["silver","black-tint"],
  "year": 2007
}

#Use the dict constructor
course = dict(name = "Programming", year = 2023, institution = "Carnegie Mellow")

#print all items in a dictionary
for x in person:
    print(x)

print("\n")

for x in car:
    print(x)

print("\n")

for x in course:
    print(x)

print("\n")

#Print individual dictionary items
print(person["name"])
print(car["model"])
print(course["year"])

print("\n")

#Check length of our dictionary
print(len(course))
print(len(car))
print(len(person))

print("\n")

print(type(person))
print(type(car))
print(type(course))
