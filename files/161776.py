p = input("Enter coordinates of point P (p1, p2,...,qn): ")
q = input("Enter coordinates of point Q (q1, q2,..., qn): ")

p = p.split(',')
p = [int(x) for x in p]
q = q.split(',')
q = [int(x) for x in q]

d = 0
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    for i in range(len(p)):
        d = d + (q[i] - p[i]) ** 2
    a = d ** 0.5
    print(f"Euclidean distance between point P and point Q: {a:.2f}")