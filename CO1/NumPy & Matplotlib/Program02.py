import numpy as np
array=np.array([[2, 8, 9, 4],[9, 4, 9, 4],[4, 5, 9, 7],[2, 9, 4, 3]])
print(array)
print(array.shape)
print(array.size)
occurance=repr(array).count("9, 4")
print("occurance of [9,4]",occurance)
