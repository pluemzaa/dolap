d=0
p = (input("Enter coordinates of point P (p1, p2,...,qn): ")).split(',')
p = [int(i) for i in p]
q = (input("Enter coordinates of point P (p1, p2,...,qn): ")).split(',')
q = [int(i) for i in q]
if len(p) != len(q) :
    print("Error: Vectors must have the same size")
for i in range(len(p)) :
    d +=  ((p[i]-q[i])**2)**0.5
print(d)