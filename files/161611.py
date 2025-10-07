P = input("Enter coordinates of point P (p1, p2,...,qn): ")
P = P.split(',')
P = [float(x) for x in P]

Q = input("Enter coordinates of point Q (q1, q2,..., qn): ")
Q = Q.split(',')
Q = [float(x) for x in Q]

D = 0

if len(P) != len(Q):
    print("Error: Vectors must have the same size")

for i in range(len(Q)):
    D += (P[i]-Q[i])**2
D = D**0.5

print("Euclidean distance between point P and point Q: %0.2f"%D)