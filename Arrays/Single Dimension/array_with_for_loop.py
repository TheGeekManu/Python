#Create Array.
Houses = ["Mansion","Bungalow","Apartment"]

#Append Function
Houses.append("Mud hut")

#Use a for loop to print out the array items.
for x in Houses:
    print(x)

#Calculate Array Length.
print(len(Houses))

#Remove array elements.
Houses.pop(0)

#Second Method
Houses.remove("Apartment")

#Extend the array
Houses.extend("Null")

#Use a for loop to print out the array items.
for x in Houses:
    print(x)

#Calculate Array Length.
print(len(Houses))
