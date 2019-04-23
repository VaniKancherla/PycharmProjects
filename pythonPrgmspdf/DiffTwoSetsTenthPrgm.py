"""colourSet1 = set(["White", "Black", "Red"])
colourSet2 = set(["Blue", "Green", "Red"])
diff_colourSet1 = colourSet1.difference(colourSet2)
print(diff_colourSet1)"""

colourSet1 = set(["White", "Black", "Red"])
colourSet2 = set(["Blue", "Green", "Red"])
newClrList = []
for value in colourSet1:
    if value not in colourSet2:
        newClrList.append(value)

print(newClrList)


