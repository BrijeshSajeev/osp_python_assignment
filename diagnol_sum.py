# Sum of diagonal elements in a matrix

def diagnol_sum(matrix):
  return sum(matrix[i][i] for i in range(len(matrix)))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagnol_sum(matrix)) # 15
