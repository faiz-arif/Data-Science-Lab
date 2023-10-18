class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"

    def add(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def subtract(self, other):
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def multiply(self, other):
        real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary_part = (self.real * other.imaginary) + (self.imaginary * other.real)
        return ComplexNumber(real_part, imaginary_part)

# Input complex numbers
real1 = float(input("Enter the real part of the first complex number: "))
imaginary1 = float(input("Enter the imaginary part of the first complex number: "))
real2 = float(input("Enter the real part of the second complex number: "))
imaginary2 = float(input("Enter the imaginary part of the second complex number: "))

# Create complex number objects
complex1 = ComplexNumber(real1, imaginary1)
complex2 = ComplexNumber(real2, imaginary2)

# Perform operations
sum_result = complex1.add(complex2)
diff_result = complex1.subtract(complex2)
product_result = complex1.multiply(complex2)

# Display results
print(f"Sum: {complex1} + {complex2} = {sum_result}")
print(f"Difference: {complex1} - {complex2} = {diff_result}")
print(f"Product: {complex1} * {complex2} = {product_result}")
