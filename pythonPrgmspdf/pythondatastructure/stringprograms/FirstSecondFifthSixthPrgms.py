# 1st prgm
str1 = "vani kancherla"
print(len(str1))

# 2nd prgm
str2 = "vani kancherla"
count = {}
for i in str2:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1
print("Count of all characters in ", str2, " is: ", str(count))

# 5th prgm
list_words = ["u", "kancherla", "abc", "mumbai", "vani"]
max1 = len(list_words[0])
temp = list_words[0]
for i in list_words:
    if len(i) > max1:
        max1 = len(i)
        temp = i
print("The length of the longest word in list_words: ", temp)

# 6th Prgm
struplw = input("Enter String: ")
print("lower case of the given string: ", struplw.lower())
print("upper case of the given string: ", struplw.upper())
