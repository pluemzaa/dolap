import math

try:
    i = input("Enter coordinates of point P (p1, p2,..., qn): ")
    u = input("Enter coordinates of point Q (q1, q2,..., qn): ")

    p_coords = [float(coord) for coord in i.split(',')]
    q_coords = [float(coord) for coord in u.split(',')]

    if len(p_coords) != len(q_coords):
        print("Error: Vectors must have the same size")
    else:
        sum_of_squares = 0
        for i in range(len(p_coords)):
            sum_of_squares += (q_coords[i] - p_coords[i]) ** 2

        distance = math.sqrt(sum_of_squares)
        print(f"Euclidean distance between point P and point Q: {distance:.2f}")

except ValueError:
    print("Error: Invalid input. Please enter numbers separated by commas.")