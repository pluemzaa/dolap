import math

p_input = input("Enter coordinates of point P (p1, p2,...,qn): ")
P = [float(x) for x in p_input.split(",")]

q_input = input("Enter coordinates of point Q (q1, q2,...,qn): ")
Q = [float(x) for x in q_input.split(",")]

if len(P) != len(Q):
    print("Error: Vectors must have the same size")
else:
    sum_sq = sum((Q[i] - P[i])**2 for i in range(len(P)))
    distance = math.sqrt(sum_sq)
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")