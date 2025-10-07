import math
p_input = input("Enter coordinates of point P (p1, p2,...,qn): ")
p = p_input.split(',')
p = [float(x) for x in p]

q_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")
q = q_input.split(',')
q = [float(x) for x in q]
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else :
    d=0
    for i in range(len(p)):
        d  += (q[i]-p[i])**2
    d=math.sqrt(d)
    print(f"Euclidean distance between point P and point Q: {d:.2f}")