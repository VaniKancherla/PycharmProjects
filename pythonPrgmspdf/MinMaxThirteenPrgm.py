def minmaxNums(data):
  maxNum = data[0]
  minNum = data[0]
  for num in data:
    if num > maxNum:
        maxNum = num
    elif num < minNum:
        minNum = num
  return maxNum, minNum


print(minmaxNums([5, 12, 16, 6, 11, 8, 1]))
