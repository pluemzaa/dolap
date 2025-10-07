import math
p_input = input("Enter coordinates of point P (p1, p2,...,qn): ")
q_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")

try:
    p = [float(x.strip()) for x in p_input.split(",")]
    q = [float(x.strip()) for x in q_input.split(",")]
except ValueError:
    print("Error: Please enter only numbers separated by commas")
    exit()
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    sum_sq = 0
    for pi, qi in zip(p, q):
        sum_sq += (qi - pi) ** 2
    distance = math.sqrt(sum_sq)
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")