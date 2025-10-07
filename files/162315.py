n1 = input("Enter coordinates of point P (p1, p2,...,qn): ").split(',')
n2 = input("Enter coordinates of point Q (q1, q2,..., qn): ").split(',')
v1 = [int(x) for x in n1]
v2 = [int(x) for x in n2]
if len(v1)==len(v2):
    d = [(v1[i]-v2[i])**2 for i in range(len(v1))]
    s = sum(d)
    t = s**0.5
    print(f'Euclidean distance between point P and point Q: {t:.2f}')
else:
    print("Error: Vectors must have the same size")