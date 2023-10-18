# Function to transpose a matrix
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2[0]):
        return None  # Matrix multiplication is not possible

    result = []
    transposed_matrix2 = transpose_matrix(matrix2)

    for row in matrix1:
        new_row = []
        for col in transposed_matrix2:
            dot_product = sum(a * b for a, b in zip(row, col))
            new_row.append(dot_product)
        result.append(new_row)

    return result

# Input matrix A
rows_A = int(input("Enter the number of rows for matrix A: "))
cols_A = int(input("Enter the number of columns for matrix A: "))

matrix_A = []
for i in range(rows_A):
    row = []
    for j in range(cols_A):
        element = float(input(f"Enter the element at position ({i + 1}, {j + 1}) of matrix A: "))
        row.append(element)
    matrix_A.append(row)

# Input matrix B
rows_B = int(input("Enter the number of rows for matrix B: "))
cols_B = int(input("Enter the number of columns for matrix B: "))

matrix_B = []
for i in range(rows_B):
    row = []
    for j in range(cols_B):
        element = float(input(f"Enter the element at position ({i + 1}, {j + 1}) of matrix B: "))
        row.append(element)
    matrix_B.append(row)

# Calculate the product of A and B^T
result = multiply_matrices(matrix_A, matrix_B)

# Display the result
if result:
    print("Result of A * B^T:")
    for row in result:
        print(row)
else:
    print("Matrix multiplication is not possible due to incompatible dimensions.")
