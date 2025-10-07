p = input("Enter coordinates of point P (p1, p2,...,qn): ")
q = input("Enter coordinates of point Q (q1, q2,..., qn): ")
p = p.split(",")
q = q.split(",")
for i in range(len(q)):
    q[i]=float(q[i])
for w in range(len(p)):
    p[w]=float(p[w])
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    d=0
    d += (((q[i] - p[w])**2)**0.5)
    print(f"Euclidean distance between point P and point Q: {d:.2f}")