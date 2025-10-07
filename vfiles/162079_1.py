p_input = input("Enter coordinates of point P (p1, p2,...,qn): ")
q_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")
p = p_input.split(",")
q = q_input.split(",")
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    total = 0
    for i in range(len(p)):
        diff = float(q[i]) - float(p[i])
        total = total + diff * diff
    distance = total ** 0.5
    print("Euclidean distance between point P and point Q:%.2f" % distance)