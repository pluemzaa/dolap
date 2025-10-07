d=0
p = (input("Enter coordinates of point P (p1, p2,...,qn): ")).split(',')
p = [int(i) for i in p]
q = (input("Enter coordinates of point Q (q1, q2,..., qn): ")).split(',')
q = [int(i) for i in q]
if len(p) != len(q) or len(q) != len(p):
    print("Error: Vectors must have the same size")
else:
    for i in range(len(p)) :
        d +=  (p[i]-q[i])**2
    d = d**0.5
    print(f'Euclidean distance between point P and point Q: {d:.2f}')