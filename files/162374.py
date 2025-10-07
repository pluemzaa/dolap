Q = input("Enter coordinates of point Q (q1, q2,...,qn): ")
P = input("Enter coordinates of point P (p1, p2,...,qn): ")
#Q = [float(i.strip()) for i in Q.split(',')]
#P = [float(i.strip()) for i in P.split(',')]
if len(P) == len(Q):  # != แปลว่า "ไม่เท่ากัน"
    Q = [float(i.strip()) for i in Q.split(',')]
    P = [float(i.strip()) for i in P.split(',')]
    ans = 0
    for i in range(len(P)):
        d = P[i] - Q[i]
        ans += d ** 2
    total = (ans)**(1/2)
    print('Euclidean distance between point P and point Q:','%.2f'% total)
else:
    print("Error: Vectors must have the same size")