d = 0
s = 0 
P = input("Enter coordinates of point P (p1, p2,...,qn): ")
Q = input("Enter coordinates of point Q (q1, q2,..., qn): ")
P = P.split(",")
P = [int (x) for x in P]
Q = Q.split(",")
Q = [int (y) for y in Q]

if len(Q) == len(P):
    for i in range(len(P)):
        x = Q[i]
        y = P[i]
        d = (x-y)**2
        s += d
    d = s**0.5
    print(f'Euclidean distance between point P and point Q: {d:.2f}')
else:
    print('Error: Vectors must have the same size')