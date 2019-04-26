itrDic = ({1: "a", 2: "b", 3: "c", 4: "d"})
itrDic.__delitem__(4)
print(itrDic)
for d in itrDic.items():
    print(d)
for key, value in itrDic.items():
    print(key, value)


