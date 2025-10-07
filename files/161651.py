import math

p = input("Enter coordinates of point P (p1, p2,...,qn): ")
p = p.split(',')
q = input("Enter coordinates of point Q (q1, q2,..., qn): ")
q = q.split(',')

p = [float(i) for i in p]
q = [float(i) for i in q]

if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    total = 0
    for i in range(len(p)):
        total += (q[i] - p[i]) ** 2
    distance = math.sqrt(total)
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")