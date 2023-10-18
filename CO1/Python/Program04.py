import math

def calculate_sin(x, n):
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        result += term
    return result

# Input values
x = float(input("Enter the value of x in radians: "))
n = int(input("Enter the number of terms (n): "))

sin_x = calculate_sin(x, n)
print(f"sin({x}) using {n} terms is approximately {sin_x}")
