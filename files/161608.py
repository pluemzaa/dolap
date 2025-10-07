import math
p = input("Enter coordinates of point P (p1, p2,...,qn): ")
q = input("Enter coordinates of point Q (q1, q2,..., qn): ")
p_list = p.split(",")
q_list = q.split(",")

if len(p_list) != len(q_list):
    print("Error: Vectors must have the same size")
else :
    p = []
    q = []
    for i in range(len(p_list)):
        p.append(float(p_list[i].strip()))
        q.append(float(q_list[i].strip()))
        
    sum_sq = 0
    for i in range(len(p)):
        diff = p[i] - q[i]
        sum_sq += diff**2
        
    distrane = math.sqrt(sum_sq)
    print(f"Euclidean distance between point P and point Q: {distrane:.2f}")