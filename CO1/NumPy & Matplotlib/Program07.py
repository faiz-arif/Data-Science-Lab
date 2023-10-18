import numpy as np
row=int(input("enter the number of raws:"))
col=int(input("enter the number of columns:"))
array1=np.empty((row,col))
for i in range(row):
    for j in range(col):
        value1=int(input(f"enter the value for element at row{i+1}:,column{j+1}:"))
        array1[i,j]=value1
array2=np.empty((row,col))
for i in range(row):
    for j in range(col):
        value2=int(input(f"enter the value for element at row{i+1}:,column{j+1}:"))
        array2[i,j]=value2
sum=array1+array2
diff=array1-array2
prod=array1*array2
div=array1/array2
print("array1:",array1)
print("array2:",array2)
print("sum=",sum)
print("difference=",diff)
print("division=",div)
add=np.add(array1,array2)
print(add)

