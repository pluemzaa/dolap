p = input("Enter coordinates of point P (p1, p2,...,qn): ")
q = input("Enter coordinates of point Q (q1, q2,..., qn): ")
q_list = q.split(',')
p_list = p.split(',')
q_list = [int(x) for x in q_list]
p_list = [int(x) for x in p_list]
totel = 0
if len(p_list) == len(q_list):

    for i in range(len(p_list)):
        pq = (p_list[i] - q_list[i])**2
        totel = totel + pq


    print(f"Euclidean distance between point P and point Q: {totel**(1/2):.2f}")
else:
    print("Error: Vectors must have the same size")