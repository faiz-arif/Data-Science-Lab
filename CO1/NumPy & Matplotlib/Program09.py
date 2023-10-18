import numpy as np
lower=int(input("enter a lower limit:"))
upper=int(input("enter a upper limit:"))
n=int((input("enter the size:")))
random_numbers = np.random.uniform(lower, upper, n)
print("Random Numbers from Uniform Distribution:",random_numbers)
