import numpy as np

# Function to calculate the Euclidean distance
def euclidean_distance(point1, point2):
    return np.linalg.norm(point1 - point2)

# Input coordinates of two points
try:
    x1 = float(input("Enter the x-coordinate of point 1: "))
    y1 = float(input("Enter the y-coordinate of point 1: "))
    x2 = float(input("Enter the x-coordinate of point 2: "))
    y2 = float(input("Enter the y-coordinate of point 2: "))

    point1 = np.array([x1, y1])
    point2 = np.array([x2, y2])

    distance = euclidean_distance(point1, point2)

    print(f"The Euclidean distance between point 1 and point 2 is: {distance:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for coordinates.")
