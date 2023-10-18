import random

# Simulate rolling a fair six-sided die 1000 times
num_rolls = 1000
results = [random.randint(1, 6) for _ in range(num_rolls)]

# Count the occurrences of each number
count_1 = results.count(1)
count_2 = results.count(2)
count_3 = results.count(3)
count_4 = results.count(4)
count_5 = results.count(5)
count_6 = results.count(6)

# Display the results
print("Results of rolling a fair six-sided die 1000 times:")
print("Number 1:", count_1, "occurrences")
print("Number 2:", count_2, "occurrences")
print("Number 3:", count_3, "occurrences")
print("Number 4:", count_4, "occurrences")
print("Number 5:", count_5, "occurrences")
print("Number 6:", count_6, "occurrences")
