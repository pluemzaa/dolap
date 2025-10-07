P = input("Enter coordinates of point P (p1, p2,...,qn): ")
Q = input("Enter coordinates of point Q (q1, q2,..., qn): ")
P = P.split(",")
Q = Q.split(",")
P = [float(x) for x in P]
Q = [float(x) for x in Q]

if len(P) != len(Q):
    print("Error: Vectors must have the same size")
else:
    ssd = 0
    for i in range(len(P)):
        diff = P[i] - Q[i]
        ssd += diff * diff
    dis = ssd ** 0.5
    print(f"Euclidean distance between point P and point Q: {dis:.2f}")