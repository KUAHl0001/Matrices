import numpy as np

# A 3X3 Square Matrix
matrix_try = np.array(
    [1, 4, 5]
)
# print(f"{matrix_try}")

### Row Matrix Learn
row_matrix = np.array(
    [1, 2, 3]
)
print(f"Row Matrix:{row_matrix}")

print("__________________________________________________________________________")

### Column Matrix Learn
column_matrix = np.array([[3],
                          [5],
                          [8]])
print("Column Matrix: ")
# The Loop is not necessary we are just using the loop to make the output look preetier
for element in column_matrix:
    print((f"[{element[0]}]"))

print("__________________________________________________________________________")

### Diagonal Matrix Learn

diagonal_matrix = np.array([
    [5, 0, 0],
    [0, 3, 0],
    [0, 0, 9]
])

print("Diagonal matrix: ")
for row in diagonal_matrix:
    print(f"[{row[0]} {row[1]} {row[2]}]")

print("In a diagonal matrix all values are 0 except of the diagonal which starts from the top left "
      "and ends at the bottom right corner of that matrix")

print("__________________________________________________________________________")

## Diagonal Elements

print("Diagonal elements is any element(Number) on the main diagonal matrix in the above case "
      "the diagonal elements are: [5, 3, 9]")

print("__________________________________________________________________________")

### Trace of Matrix Learn

print("Trace of matrix is the sum of the elements on the main diagonal "
      "of the matrix, for a trace of matrix it is not necessary that for "
      "the matrix to be a diagonal matrix it can be any type of a square matrix"
      "but we only take the sum of the diagonal elements from the square matrix")

trace_of_diagonal_matrix = np.array([
    [5, 0, 0],
    [0, 5, 0],
    [0, 0, 9]
])
print("Trace of Diagonal Matrix: ")
for row in trace_of_diagonal_matrix:
    print(f"[{row[0]} {row[1]} {row[2]}]")

print(f"trace of Answer: [5 + 5 + 9] = {5 + 5 + 9}")

print("Trace of Square Matrix: ")
trace_of_square_matrix = np.array([
    [3, 7, 9],
    [4, 5, 7],
    [2, 9, 6]
])

for row in trace_of_square_matrix:
    print(f"[{row[0]} {row[1]} {row[2]}]")

print(f"trace of Answer: [3 + 5 + 6] = {3 + 5 + 6}")

print("__________________________________________________________________________")



