p = input("Enter coordinates of point P (p1, p2,...,qn): ")
q = input("Enter coordinates of point Q (q1, q2,..., qn): ")
p = p.split(",")
q = q.split(",")
x = [float(t) for t in p]
y = [float(t) for t in q]
i = 0
eu1 = 0

if len(p) == len(q):
    while i < len(p):
        eu = (x[i] - y[i]) ** 2
        i = i + 1
        eu1 = eu + eu1
    d = eu1 ** 0.5
    print(f"Euclidean distance between point P and point Q:{d:.2f}")
else:
    print("Error: Vectors must have the same size")