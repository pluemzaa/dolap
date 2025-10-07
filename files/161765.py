p = input("Enter coordinates of point P (p1, p2,...,qn): ")
p = p.split(",")
p = [float(x) for x in p]

q = input("Enter coordinates of point Q (q1, q2,..., qn): ")
q = q.split(",")
q = [float(x) for x in q]

d = 0

if len(p) != len(q) :
    print ("Error: Vectors must have the same size")

for i in range(len(q)):
    d += (p[i]-q[i])**2
d = d**0.5

print (f"Euclidean distance between point P and point Q: {d:.2f}")