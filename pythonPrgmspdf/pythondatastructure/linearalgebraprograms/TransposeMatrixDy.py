M = 3
N = 1


def transpose(matrixA, B):
    for i in range(N):
        for j in range(M):
            B[i][j] = matrixA[j][i]

        # driver code


matrixA = [[1],
           [2],
           [3]]

# To store result
B = [[0 for x in range(M)] for y in range(N)]
print("B: ", B)

transpose(matrixA, B)

print("Result matrix is")
for i in range(N):
    for j in range(M):
        print(B[i][j], " ", end='')
    print()

