# 3rd prgm
str1 = "mumbai"


def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]
  return str1


print(change_char(str1))

# 4th prgm
str4 = ["abc", "read", "living", "do"]
finalstr = []
for i in str4:
  lenstr = len(i)
  if lenstr >= 3:
    if i[-3:] == 'ing':
      i += 'ly'
      finalstr.append(i)
    else:
      i += 'ing'
      finalstr.append(i)
  else:
    finalstr.append(i)

print(str(finalstr))
