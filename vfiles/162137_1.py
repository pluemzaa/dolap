p = input('Enter coordinates of point P (p1, p2,...,qn): ')
p = p.split(',')
q = input('Enter coordinates of point Q (q1, q2,..., qn): ')
q = q.split(',')
p = [float(x) for x in p]
q = [float(x) for x in q]

if len(p) != len(q):
    print('Error: Vectors must have the same size')
else:
    r = 0
    for i in range(len(p)):
        d = 0
        diff = p[i] - q[i]
        r += diff * diff
    d = r **0.5
    print(f'Euclidean distance between point P and point Q: {d:.2f}')