import math
while True:
    pn = input("Enter coordinates of point P (p1, p2,...,qn):")
    qn = input("Enter coordinates of point Q (q1, q2,..., qn):")
    p = [int(x) for x in pn.split(",")]
    q = [int(x) for x in qn.split(",")]


    if len(p) != len(q):
        print("Error: Vectors must have the same size")
    else:
        break
d = 0
for i in range(len(p)):
    d += (q[i] - p[i]) ** 2
distance = math.sqrt(d)
print(f"Euclidean distance between point P and point Q: {distance:.2f}")