# 8th prgm
str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('s', 1)[0])
print(str1.rsplit('-', 1)[0])

# 10th Prgm
strcount = "can you can a can as a canner can can a can"
print(strcount.count("can"))
print(strcount.count('n'))
print(strcount.count("can", 0, 23))

# 10th prgm
string = input("Enter string:")
word = input("Enter word:")
a = []
count = 0
a = string.split(" ")
for i in range(0, len(a)):
    if word == a[i]:
        count = count+1
print("Count of the word is:")
print(count)

# 9th prgm
import textwrap
sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
print()
print(textwrap.fill(sample_text, width=50))
print()


