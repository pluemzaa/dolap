import math

p_input = input("Enter coordinates of point P (p1, p2,...,qn): ")
q_input = input("Enter coordinates of point Q (q1, q2,..., qn): ")

p_str_list = p_input.split(",")
q_str_list = q_input.split(",")

if len(p_str_list) != len(q_str_list):
    print("Error: Vectors must have the same size")
else:
    p = []
    q = []
    for i in range(len(p_str_list)):
        p.append(int(p_str_list[i].strip()))
        q.append(int(q_str_list[i].strip()))
    
    sum_squares = 0
    for i in range(len(p)):
        diff = p[i] - q[i]
        diff_square = diff ** 2
        sum_squares += diff_square
    
    distance = math.sqrt(sum_squares)
    print("Euclidean distance between point P and point Q: %.2f" % distance)