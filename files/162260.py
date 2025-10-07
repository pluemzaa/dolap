p = input("Enter coordinates of point P (p1, p2,...,qn): ")
q = input("Enter coordinates of point Q (q1, q2,..., qn): ")
p = p.split(",")
q = q.split(",")
for i in range(len(q)):
    q[i]=int(q[i])
for i in range(len(p)):
    p[i]=int(p[i])
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    d=0
    for i in range(len(q)):
        d += (q[i] - p[i])**2
    d=d**0.5
    print(f"Euclidean distance between point P and point Q: {d:.2f}")