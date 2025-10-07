v = input("Enter coordinates of point P (p1, p2,...,qn): ")
b = input("Enter coordinates of point Q (q1, q2,..., qn): ")
v, b = v.split(","), b.split(",")
v = [int(i) for i in v]
b = [int(j) for j in b]
t = []

if len(v) == len(b):
    for i in range(len(v)):
        t.append((v[i] - b[i])**2)

    a = 0
    for j in t:
        a += j

    print(f"Euclidean distance between point P and point Q: {a**(1/2):.2f}")
else:
    print("Error: Vectors must have the same size")