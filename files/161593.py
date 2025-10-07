import math
p_input = input("Enter coordinates of point P (p1, p2,...,qn): ")
q_input = input("Enter coordinates of point Q (q1, q2,..., qn):")
p_list = p_input.split(',')
q_list = q_input.split(',')

if len(p_list) != len(q_list):
    print("Error: Vectors must have the same size")
else:
    p = []
    q = []
    for i in range(len(p_list)):
        p.append(float(p_list[i].strip()))
        q.append(float(q_list[i].strip()))

    sum = 0
    for i in range(len(p)):
        diff = p[i] - q[i]
        sum += diff**2

    d = math.sqrt(sum)
    print(f"Euclidean distance between point P and point Q: {d:.2f}")