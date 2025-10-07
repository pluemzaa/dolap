p = input("Enter coordinates of point P (p1, p2,...,qn): ")
q = input("Enter coordinates of point Q (q1, q2,..., qn): ")
p = p.split(",")
q = q.split(",")

if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    total = 0
    for i in range(len(p)):
        total += (float(q[i]) - float(p[i])) ** 2
    print("Euclidean distance between point P and point Q: %.2f" % (total ** 0.5))