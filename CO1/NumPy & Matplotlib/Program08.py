import numpy as np
row=int(input("enter the number of raws:"))
col=int(input("enter the number of columns:"))
matrix=np.empty((row,col))
for i in range(row):
    for j in range(col):
        value1=int(input(f"enter the value for element at row{i+1}:,column{j+1}:"))
        matrix[i,j]=value1
determinant=np.linalg.det(matrix)
if determinant !=0:
    inverse=np.linalg.inv(matrix)
    print("matrix:",matrix)
    print("determinant",determinant)
    print("inverse:",inverse)
else:
    print("the matrix is singular (not invertible and the determinat is zero")
