import math
p = input("Enter coordinates of point P (p1, p2,...,qn):")
q = input("Enter coordinates of point Q (q1, q2,..., qn):")
P = p.split(",")
Q = q.split(",")
P = [float(x) for x in P]
Q = [float(x) for x in Q]
if len(P) != len(Q):
    print("Error: Vectors must have the same size")
else:
    total = 0
    for i in range(len(P)):
        diff = P[i] - Q[i]
        Sqrt = diff **2
        total += Sqrt
    d = math.sqrt(total)
    print(f"Euclidean distance between point P and point Q:{d:.2f}")