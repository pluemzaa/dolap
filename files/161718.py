p = input('Enter coordinates of point P (p1, p2,...,qn):').split(',')
q = input('Enter coordinates of point Q (q1, q2,..., qn):').split(',')
p = [ float(p[i]) for i in range(len(p))]
q = [ float(q[j]) for j in range(len(q))]
s = 0
if len(p) == len(q):
    for i in range(len(p)):
        s += ((q[i]-p[i])**2)
    d = s**0.5
    print(f'Euclidean distance between point P and point Q: {d:.2f}')
else:
    print('Error: Vectors must have the same size')