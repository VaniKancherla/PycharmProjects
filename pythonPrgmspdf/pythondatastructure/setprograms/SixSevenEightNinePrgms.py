setA = {"a", "b", "c", "k", "v"}
setB = {"d", "e", "v", "k"}

#to create an intersection of sets
print("intersection of sets: ", setA & setB)

#create a union of sets
print("union of sets: ", setA | setB)

#create set difference
print("set difference setA - setB: ", setA - setB)
print("set difference setB - setA: ", setB - setA)

#create a symmetric difference
print("symmetric difference: ", setA.symmetric_difference(setB))
print("symmetric difference: ", setB ^ setB)





