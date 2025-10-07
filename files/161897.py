import math
pakin = input("Enter coordinates of point P (p1, p2,...,qn): ")
quin = input("Enter coordinates of point Q (q1, q2,..., qn): ")

p = [int(x.strip()) for x in pakin.split(',')]
q = [int(x.strip()) for x in quin.split(',')]

if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:

    sum_sq_diff = 0
    for i in range(len(p)):
        sum_sq_diff += (p[i] - q[i]) ** 2


    distance = math.sqrt(sum_sq_diff)


    print(f"Euclidean distance between point P and point Q: {distance:.2f}")