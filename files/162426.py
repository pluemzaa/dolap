import math

p = list(map(float, input("Enter coordinates of point P (p1, p2,...,qn): ").split(",")))
q = list(map(float, input("Enter coordinates of point Q (q1, q2,..., qn): ").split(",")))

if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    total = 0
    for pi, qi in zip(p, q):
        total += (qi - pi) ** 2
    distance = math.sqrt(total)
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")