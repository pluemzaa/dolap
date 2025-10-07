p = input('Enter coordinates of point P (p1, p2,...,qn): ').split(',')
q = input('Enter coordinates of point Q (q1, q2,..., qn): ').split(',')

if len(p) != len(q):
    print('Error: Vectors must have the same size')
else:
    p = [int(x) for x in p]
    q = [int(x) for x in q]

    result = 0
    for i in range(len(p)):
        result += (p[i]-q[i])**2

    print('Euclidean distance between point P and point Q: %.2f' %result**0.5)