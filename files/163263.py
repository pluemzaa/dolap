import math
p_input = input("Enter coordinates of point P (p1, p2,...,qn): ")
p = [float(x) for x in p_input.split(",")]
q_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")
q = [float(x) for x in q_input.split(",")]
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    sum_sq = 0
    for i in range(len(p)):
        diff = p[i] - q[i]
        sum_sq += diff ** 2
    distance = math.sqrt(sum_sq)
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")