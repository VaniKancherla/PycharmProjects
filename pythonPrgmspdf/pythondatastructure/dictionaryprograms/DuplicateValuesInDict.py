samdict = {1: "a", 2: "b", 3: "c", 4: "d", 5:"a", 6: "c"}
dupvaluedict = {}
for key, value in samdict.items():
    dupvaluedict.setdefault(value, set()).add(key)

result = [key for key, values in dupvaluedict.items()
          if len(values) > 1]

# printing result
print("duplicate values", str(result))




