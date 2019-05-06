
xmatrix = [[12, 7, 3],
           [4, 5, 6],
           [7, 8, 9]]
y = 9
print([[elem*y for elem in row] for row in xmatrix])

z = 2

for row in xmatrix:
    for val in row:
        val*z

print(xmatrix)

