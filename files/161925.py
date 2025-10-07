import math

P = input("Enter coordinates of point P (p1, p2,...,qn): ").split(',')
Q = input("Enter coordinates of point Q (q1, q2,...,qn): ").split(',')
P = [int(x) for x in P]
Q = [int(x) for x in Q]

if len(P) != len(Q):
    print("Error: Vectors must have the same size")
else:
    sum_diff = 0
    for i in range(len(P)):
        diff = P[i] - Q[i]
        sum_diff += diff ** 2
    distance = math.sqrt(sum_diff)
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")