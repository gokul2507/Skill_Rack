R, C = map(int, input().split())
matrix1 = Matrix(R, C)
matrix2 = Matrix(R, C)
for row in range(R):
    currRow = list(map(int, input().split()))
    for col in range(C):
        matrix1.setValue(row, col, currRow[col])
for row in range(R):
    currRow = list(map(int, input().split()))
    for col in range(C):
        matrix2.setValue(row, col, currRow[col])
matrix3 = matrix1 + matrix2
print("Sum Matrix:")
for row in range(matrix3.R):
    for col in range(matrix3.C):
        print(matrix3.getValue(row, col), end=" ")
    print()
