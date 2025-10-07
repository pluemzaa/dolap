import math

p_input = input("Enter coordinates of point P (p1, p2,...,pn): ")
q_input = input("Enter coordinates of point Q (q1, q2,...,qn): ")

p = [float(x) for x in p_input.split(',')]
q = [float(x) for x in q_input.split(',')]

if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    sum_squared = 0
    for i in range(len(p)):
        sum_squared += (p[i] - q[i]) ** 2
    distance = math.sqrt(sum_squared)

    print(f"Euclidean distance between point P and point Q: {distance:.2f}")