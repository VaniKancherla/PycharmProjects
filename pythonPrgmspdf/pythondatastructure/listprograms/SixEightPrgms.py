stringList = ["cbc", "afa", "bvkb", 12, 6, "cbc", 6]

# remove duplicates from a list
finalList = []
for lst in stringList:
    if lst not in finalList:
        finalList.append(lst)
# print(finalList)

# list of words that are longer than n from a given list of words
wordList = ["vani", "kancherla", "ab", "u", "abc"]
finalWordList = []
value = int(input("Enter the value: "))
for i in wordList:
    if len(i) > value:
        finalWordList.append(i)
print(finalWordList)
