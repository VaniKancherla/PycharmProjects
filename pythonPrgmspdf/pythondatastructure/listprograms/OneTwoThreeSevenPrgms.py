numList = [4, 2, 12, 6, 8]

# sum of all the items in a list
sumOfItems = 0
for i in numList:
    sumOfItems += i
print(sumOfItems)

# multiplies all the items in a list
mulOfItems = 1
for m in numList:
    mulOfItems *= m
print(mulOfItems)

# get the smallest number from a list
numList.sort()
print(numList[0])

# Python program to clone or copy a list
copylist = numList.copy()
print(copylist)
