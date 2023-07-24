#Create a literal tabbed(\t) string
tabbedString = "M\to\tr\tn\ti\tn\tg"

#Perform a print to see how our tabbed(\t) string looks like before issung the expandtabs() function.
print(tabbedString)

#Perform a print to see how our tabbed(\t) string looks like under different tab sizes.
print(tabbedString.expandtabs())
print(tabbedString.expandtabs(2))
print(tabbedString.expandtabs(4))
print(tabbedString.expandtabs(10))
