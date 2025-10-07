p = input("Enter coordinates of point P (p1, p2,...,qn): ")
q = input("Enter coordinates of point Q (q1, q2,..., qn): ")
p = p.split(',')
q = q.split(',')
vec1 = [float(i) for i in p]
vec2 = [float(i) for i in q]
if len(p) == len(q) :
    sum = 0
    for i in range(len(vec1)) :
        sum += abs(vec1[i] - vec2[i])**2
    sum = sum**(1/2)
    print(f"Euclidean distance between point P and point Q: {sum : .2f}")
else :
    print("Error: Vectors must have the same size")