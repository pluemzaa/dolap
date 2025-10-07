from math import sqrt
P = input("Enter coordinates of point P (p1, p2,...,qn):")
P = P.split(',')
Q = input("Enter coordinates of point Q (q1, q2,..., qn):")
Q = Q.split(',')
if len(P) == len(Q):
    for i in range(len(P)):
        P[i] = int(P[i])
        Q[i] = int(Q[i])
    d = 0
    for i in range(len(P)):
        d += (P[i] - Q[i]) ** 2
    distance = sqrt(d)
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")
else:
    print("Error: Vectors must have the same size")