p = [float(x) for x in input("Enter coordinates of point P (p1, p2,...,qn): ").split(",")]
q = [float(x) for x in input("Enter coordinates of point Q (q1, q2,..., qn):").split(",")]

if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    s = 0
    for i in range(len(p)):
        s += (q[i] - p[i]) ** 2
    print(f"Euclidean distance between point P and point Q: {s ** 0.5:.2f}")