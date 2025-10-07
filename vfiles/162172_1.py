import math


p_input = input("Enter coordinates of point P (p1, p2,...,pn): ")
p = []
for x in p_input.split(','):
    p.append(float(x.strip()))

q_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")
q = []
for x in q_input.split(','):
    q.append(float(x.strip()))


if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    
    sum_squared = 0
    for i in range(len(q)):
        qi = q[i]
        pi = p[i]
        sum_squared = sum_squared + (qi - pi) ** 2
    

    d = math.sqrt(sum_squared)
    

    print(f"Euclidean distance between point P and point Q: {d:.2f}")