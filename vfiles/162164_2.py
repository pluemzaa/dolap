import math

p = input("Enter coordinates of point P (p1, p2,...,qn): ")
q = input("Enter coordinates of point Q (q1, q2,..., qn): ")


p = [float(x) for x in p.split(',')]
q = [float(x) for x in q.split(',')]

if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    sum = 0
    for i in range(len(p)):
        diff = q[i] - p[i]
        sum += diff ** 2
    distance = math.sqrt(sum)
    
print(f"Euclidean distance between point P and point Q: {distance:.2f}")