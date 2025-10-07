import math

def parse_input(input_str):
    return [float(x.strip()) for x in input_str.split(',')]

p_input = input("Enter coordinates of point P (p1, p2,...,qn): ")
q_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")

try:
    p = parse_input(p_input)
    q = parse_input(q_input)

    if len(p) != len(q):
        print("Error: Vectors must have the same size")
    else:
        sum_squared_diff = 0
        for i in range(len(p)):
            diff = p[i] - q[i]
            sum_squared_diff += diff ** 2

        distance = math.sqrt(sum_squared_diff)
        print(f"Euclidean distance between point P and point Q: {distance:.2f}")

except ValueError:
    print("Error: Please enter only numbers separated by commas.")