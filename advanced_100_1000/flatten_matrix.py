matrix = [
  [1, 2, 3], # 1st row
  [4, 5, 6], # 2nd row
  [7, 8, 9]  # 3rd row
]
matrix_nums = [num for row in matrix for num in row]
print(', '.join(map(str, matrix_nums)))