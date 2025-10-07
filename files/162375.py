data = []
P_list = []
Q_list = []
P = input("Enter coordinates of point P (p1, p2,...,qn): ")
P_list = P.split(",")
P = [int(x) for x in P_list]
data.append(P)

Q = input("Enter coordinates of point Q (q1, q2,..., qn): ")
Q_list = Q.split(",")
Q = [int(x) for x in Q_list]
data.append(Q)

if len(data[0]) != len(data[1]):
    print("Error: Vectors must have the same size")
else:
    x_sq = 0
    for i in range(len(data[0])):
        diff = data[0][i] - data[1][i]
        x_sq = x_sq + diff ** 2
        distance = x_sq ** 0.5
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")