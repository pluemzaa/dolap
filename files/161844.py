P = input('Enter coordinates of point P (p1, p2,...,qn): ')
Q = input('Enter coordinates of point Q (q1, q2,..., qn):')
P = P.split(",")
Q = Q.split(",")
x = [float(t) for t in P]
y = [float(t) for t in Q]
i = 0
eu1 = 0
if len(P) == len(Q):
    while i < len(P):
        eu = (x[i] - y[i])**2
        i = i + 1
        eu1 = eu + eu1
    d = eu1 ** 0.5
    print(f'Euclidean distance between point P and point Q:{d:.2f}')
else:
    print('Error: Vectors must have the same size')