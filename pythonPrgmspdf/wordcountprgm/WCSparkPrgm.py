file = open("/home/admin1/PycharmProjects/pythonPrgmspdf/wordcountprgm/smallwordcountfile.tsv")

wordcount = {}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k, v in wordcount.items():
    print(k, v)



