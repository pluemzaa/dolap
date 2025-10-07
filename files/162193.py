P_input = input('Enter coordinates of point P (p1, p2,...,qn): ')
P = P_input.split(',')
P = [float(x) for x in P]

Q_input = input('Enter coordinates of point Q (q1, q2,..., qn): ')
Q = Q_input.split(',')
Q = [float(x) for x in Q]


if len(P) != len(Q):
    print('Error: Vectors must have the same size')
    
else:
    sum_ = 0
    for i in range(len(P)):
        diff = P[i] - Q[i]
        sum_ += diff ** 2
        total = sum_**0.5
    print(f'Euclidean distance between point P and point Q: {total:.2f}')