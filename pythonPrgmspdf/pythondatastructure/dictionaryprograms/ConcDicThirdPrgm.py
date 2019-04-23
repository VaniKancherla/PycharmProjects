mydictionary = {12: "vani", 1: "sreenu", 6: "bunny"}
#print(mydictionary)

dictSecond = {25: 94, 30: 91}
#print(dictSecond)

dictthird = {18: 2, 3: 4}
#print(dictSecond)

dictionarystr = {"v": "abc", "a": "xyz", "b": "efg"}
#print(dictionarystr)

dic4 = {}
for d in (mydictionary, dictSecond, dictthird, dictionarystr):
    dic4.update(d)
print(dic4)
