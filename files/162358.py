import math
import sys

d = float()

p_append = []
q_append = []

p = (input("Enter coordinates of point P (p1, p2,...,qn): "))
q = (input("Enter coordinates of point Q (q1, q2,..., qn): "))



p = p.split(",")
p = [int(x) for x in p]
p_append.append(p)

q = q.split(",")
q = [int(y) for y in q]
q_append.append(q)


sum_squar_different = 0

if len(p) == len(q):
    n = len(p)

    for i in range(n):
        
        
        different = q[i] - p[i]
        squar_different = different ** 2
        sum_squar_different += squar_different 
        d = math.sqrt(sum_squar_different)


if len(p) != len(q):
    print("Error: Vectors must have the same size")
    sys.exit()

print(f"Euclidean distance between point P and point Q: {d:.2f}" )