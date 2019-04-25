# Python function that takes two lists and returns True if they have at least one common member
list1 = [1, 2, 3, 4]
list2 = [2, 4, 12, 6]


def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result


print(common_data(list1, list2))


def commonitem(list1, list2):
    l1 = set(list1)
    l2 = set(list2)
    if len(l1 & l2) > 0:
        return True
    else:
        return False


print(commonitem(list1, list2))


# 10th program

wordList = ["vani", "kancherla", "abc", "xyz", "mum", "vij", "us"]
indexes = [0, 5, 4]
for ele in sorted(indexes, reverse=True):
    del wordList[ele]
print(wordList)


def myfunc(wordList1):
    indexes = [0, 4, 5]
    for i in sorted(indexes, reverse=True):
            del wordList1[i]
    print(wordList1)


wordList1 = ["vani", "kancherla", "abc", "xyz", "mum", "vij", "us"]
myfunc(wordList1)


