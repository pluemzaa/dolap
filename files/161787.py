import math

p_str = input('Enter coordinates of point P (p1, p2,...,qn): ')
q_str = input('Enter coordinates of point Q (q1, q2,...,qn): ')

try:
    p_coords = [float(x) for x in p_str.split(',')]
    q_coords = [float(x) for x in q_str.split(',')]
except ValueError:
    print("Error: Invalid input. Please enter numbers separated by commas.")
else:
    if len(p_coords) != len(q_coords):
        print("Error: Vectors must have the same size")
    else:
        sum_sq_diff = 0
        
        for i in range(len(p_coords)):
            sum_sq_diff += (p_coords[i] - q_coords[i]) ** 2
        
        distance = math.sqrt(sum_sq_diff)
        
        print(f'Euclidean distance between point P and point Q: {distance:.2f}')