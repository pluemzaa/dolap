mport math 

p_input = input(”Enter coordinates of point P (p1, p2,...,qn): “)
q_input = input(”Enter coordinates of point Q (q1, q2,..., qn): “)

p = [float(x.strip()) for x in p_input.split(”,“) if x.strip() != ”“]
q = [float(x.strip()) for x in q_input.split(”,“) if x.strip() != ”“]

if len(p) != len(q):
    print(”Error: Vectors must have the same size“)
else:
    sum_sq = 0
    for i in range(len(p)):
        sum_sq += (q[i] - p[i]) **2

    distance = math.sqrt(sum_sq)
    print(”Euclidean distance between point P and point Q: %.2f“ % distance)