p_input = input("Enter coordinates of point P (p1, p2,...,qn): ")
q_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")

p = [float(x.strip()) for x in p_input.split(',')]
q = [float(x.strip()) for x in q_input.split(',')]

if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    total = 0
    for i in range(len(p)):
        total += (p[i] - q[i]) ** 2

    distance = total ** 0.5
    print(f"Euclidean distance between point P and point Q: {distance:.2f}")