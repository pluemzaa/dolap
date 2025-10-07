import math
def calculate_euclidean_distance():
   
    p_input = input("Enter coordinates of point P (p1, p2,..., qn): ")
    q_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")
    try:
        p = [float(coord) for coord in p_input.split(',')]
        q = [float(coord) for coord in q_input.split(',')]
        if len(p) != len(q):
            print("Error: Vectors must have the same size")
            return 
        sum_of_squares = sum((pi - qi) ** 2 for pi, qi in zip(p, q))
        distance = math.sqrt(sum_of_squares)
        print(f"Euclidean distance between point P and point Q: {distance:.2f}")
    except ValueError:
        print("Error: Invalid input. Please enter numbers separated by commas.")
calculate_euclidean_distance()