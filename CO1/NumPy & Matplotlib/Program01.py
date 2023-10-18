import numpy as np
#from scipy import stats
#np_array=np.array([1,2,3,4,8,9,2,3])
np_array=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    element=int(input("enter element"))
    np_array.append(element)
                
print(np_array)
print(type(np_array))
print("mean",np.mean(np_array))
print("median",np.median(np_array))
#print("mode",stats.mode(np_array))
print("standard deviation",np.std(np_array))
