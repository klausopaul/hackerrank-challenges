import re

decoded_matrix = ""
matrix = []
matrix_row = []
regex = r"\b\W+\b"

# Sizing the matrix
first_multiple_input = input().rstrip().split()
nRows = int(first_multiple_input[0])
nCols = int(first_multiple_input[1])

# Populating the matrix
for i in range(nRows):
    l = input()
    for x in range(len(l)):
        matrix_row.append(l[x])

    matrix.append(matrix_row.copy())
    matrix_row.clear()

# Decode the matrix
for j in range(nCols):
    for i in range(nRows):
        decoded_matrix += matrix[i][j]

# Final decoded matrix
print(re.sub(regex, " ", decoded_matrix))