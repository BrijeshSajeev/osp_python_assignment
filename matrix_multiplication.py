# Matrix multiplication
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0]))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
print(result)
