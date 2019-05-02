import numpy as np

chess_matrix = np.zeros((8, 8))
chess_matrix[0::2, 1::2] = 1
chess_matrix[1::2, 0::2] = 1
print(chess_matrix)


def checkboardpattern(n):
    print("Checkerboard pattern:")
    x = np.zeros((n, n), dtype=int)
    x[1::2, 0::2] = 1
    x[0::2, 1::2] = 1
    for i in range(n):
        for j in range(n):
            print(x[i][j], end=" ")
        print()


n = int(input("Enter value of n :"))
checkboardpattern(n)
