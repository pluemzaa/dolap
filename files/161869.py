total = 0
P = input("Enter coordinates of point P (p1, p2,...,qn):").split(",")
Q = input("Enter coordinates of point Q (q1, q2,..., qn):").split(",")
P = [int(x) for x in P]
Q = [int(x) for x in Q]
if len(P) != len(Q):
    print("Error: Vectors must have the same size")
else: 
    for i in range(len(P)):
        total += (P[i]-Q[i])**2
    print("Euclidean distance between point P and point Q: %.2f" % total**0.5)