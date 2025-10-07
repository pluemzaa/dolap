q = input("Enter coordinates of point P (p1, p2,...,qn): ").split(",")
p = input("Enter coordinates of point Q (q1, q2,..., qn):").split(",")

q = [float(x) for x in q]
p = [float(x) for x in p]
if len(q) != len(p):
    print("Error: Vectors must have the same size")
else:
    sum_plus = 0
    for i in range(len(q)):
        diff = q[i] - p[i]
        sum_plus += diff ** 2    
    d = sum_plus ** 0.5          
    print(f"Euclidean distance between point P and point Q: {d:.2f}")