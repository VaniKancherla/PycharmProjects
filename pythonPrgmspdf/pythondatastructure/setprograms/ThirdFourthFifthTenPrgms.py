alp_set = {"a", "b", "c", "d", "e", "f"}
alp_set.add(12)
alp_set.update({"g", "h"})
print(alp_set)

#to remove item(s) from set
alp_set.remove("e")
print("Remove item using remove method: ", alp_set)

#remove an item from a set if it is present in the set
alp_set.discard(165)
print("Remove item using discard method: ", alp_set)

popitem = alp_set.pop()
print(popitem)
print("Remove item using remove method: ", alp_set)

alp_set.clear()
print(alp_set)

del alp_set
print(alp_set) # this will raise an error because the set no longer exists


