import numpy as np
matrix1=[[1,2],[4,5]]
matrix2=[[6,7],[9,8]]
rows_1 = len(matrix1)
cols_1 = len(matrix1[0])
rows_2 = len(matrix2)
cols_2 = len(matrix2[0])
if cols_1 != rows_2:
    raise ValueError(f"Cannot multiply: Number of columns in the first matrix ({cols_1}) must equal the number of rows in the second matrix ({rows_2}).")

result = np.zeros((rows_1, cols_2))
for i in range(rows_1):
    for j in range(cols_2):
        for k in range(cols_1):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
            
            
print(result)