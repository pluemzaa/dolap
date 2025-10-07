input_p = input("Enter coordinates of point P (p1, p2,...,qn): ")
input_q = input("Enter coordinates of point Q (q1, q2,..., qn): ")
p = input_p.split(',')
q = input_q.split(',')
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:

# ตัวอย่างเช่น q = (30, 50, 60, 100), p = (20, 75, 50, 45)

# d = Sqrt( (30-20)**2 + (50-75)**2 +(60-50)**2 + (100-45)**2 )
    d = 0
    for i in range(len(p)):
        d += (float(q[i]) - float(p[i])) ** 2
    d = d ** 0.5
    print(f"Euclidean distance between point P and point Q: {d:.2f}")