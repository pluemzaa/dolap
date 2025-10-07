p = input("Enter coordinates of point P (p1, p2,...,qn): ")
p = [int(n) for n in p.split(",")]

q = input("Enter coordinates of point Q (q1, q2,..., qn): ")
q = [int(n) for n in q.split(",")]

d = 0

if len(p) == len(q):
    for i in range(len(p)):
        d += (p[i] - q[i]) ** 2

    print(f"Euclidean distance between point P and point Q: {d ** 0.5:.2f}")
else:
    print("Error: Vectors must have the same size")