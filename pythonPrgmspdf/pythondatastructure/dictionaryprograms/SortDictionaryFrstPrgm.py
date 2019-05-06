mydictionary = { 12: "vani", 1: "sreenu", 6: "bunny"}
print("Ascending Order: ")
for key in sorted(mydictionary.keys()):
    print("%s: %s" % (key, mydictionary[key]))
print("Descending Order:")
for key in sorted(mydictionary.keys(), reverse=True):
    print("%s: %s" % (key, mydictionary[key]))
