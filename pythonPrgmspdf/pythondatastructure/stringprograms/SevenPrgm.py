# 7th prgm
items = input("Input comma separated sequence of words: ")
words = [word for word in items.split(",")]
# str = set(words)
# print(str)
# print(list(set(words)))
print(",".join(sorted(list(set(words)))))






















