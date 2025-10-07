p = input("Enter coordinates of point P (p1, p2,...,qn): ")
p = p.split(",")

q = input("Enter coordinates of point Q (q1, q2,..., qn): ")
q = q.split(",")

if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    p = [float(x) for x in p]
    q = [float(x) for x in q]
    sum = 0
    for i in range(len(p)):
        sum += ((p[i] - q[i]) ** 2)
    sum_all = (sum ** 0.5)
    print(f"Euclidean distance between point P and point Q: {sum_all:.2f}")