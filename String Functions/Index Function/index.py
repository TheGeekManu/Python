proverbial = "It is always good to share with those that lack."

#Index function without start and end parameters
indexCount = proverbial.index("share")
print(indexCount)
print('\n')

#Index function with start and end parameters
indexCount = proverbial.index("s", 20, 26)
print(indexCount)
