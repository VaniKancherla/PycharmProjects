m = int(input("ENTER MARTIX ROW SIZE m : "))
n = int(input("ENTER MARTIX COLUMN SIZE n : "))

# initializing matrix elements as 0
X = [[0] * n for j in range(m)]
Y = [[0] * n for j in range(m)]
result = [[0] * n for j in range(m)]

print("Entry for 1st Matrix")
# getting input to matrix X
for i in range(m):
    for j in range(n):
        print('entry in row: ', i + 1, ' column: ', j + 1)
        X[i][j] = int(input())

# printing first matrix X
print("FIRST MATRIX : ")
for i in range(m):
    for j in range(n):
        print(X[i][j], end=" ")
    print()

# getting input to matrix X
for i in range(m):
    for j in range(n):
        print('entry in row: ', i + 1, ' column: ', j + 1)
        Y[i][j] = int(input())

# printing second matrix Y
print("SECOND MATRIX : ")
for i in range(m):
    for j in range(n):
        print(Y[i][j], end=" ")
    print()

# adding X and Y to result
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

# displaying result
print("SUM OF MATRICES IS : ")
for i in range(m):
    for j in range(n):
        print(result[i][j], end=" ")
    print()

