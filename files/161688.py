import math

def parse_vector(input_str):
    return [float(x.strip()) for x in input_str.split(",")]

p_input = input("Enter coordinates of point P (p1, p2,...,qn): ")
q_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")

try:
    p = parse_vector(p_input)
    q = parse_vector(q_input)

    if len(p) != len(q):
        print("Error: Vectors must have the same size")
    else:
        squared_diff_sum = 0
        for i in range(len(p)):
            squared_diff = (p[i] - q[i]) ** 2
            squared_diff_sum += squared_diff

        distance = math.sqrt(squared_diff_sum)
        print(f"Euclidean distance between point P and point Q: {distance:.2f}")

except ValueError:
    print("Error: Please enter valid numeric coordinates separated by commas.")