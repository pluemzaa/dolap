q = input("Enter coordinates of point P (p1, p2,...,qn): ")
p = input("Enter coordinates of point Q (q1, q2,..., qn): ")
q = q.split(",")
p = p.split(",")
vector1 = [float(v) for v in q]
vector2 = [float(v) for v in p]
if len(vector1) != len(vector2):
    print("Error: Vectors must have the same size")
else:
    sum = 0 
    for i in range(len(q)): 
        sum = sum + (abs(vector1[i] - vector2[i]) ** 2)
        
    d = sum ** (1/2)
    print(f"Euclidean distance between point P and point Q: {d:.2f}")