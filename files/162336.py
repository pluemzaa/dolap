al = 0
p = input("Enter coordinates of point P (p1, p2,...,qn): ")
q  = input("Enter coordinates of point Q (q1, q2,..., qn): ")
p = p.split(",")
n = len(p)
for i in range(n):
    p[i]= int(p[i]) 
q = q.split(",")
m = len(q)
for i in range(m):
    q[i] = int(q[i])
if n == m : 
    for i in range(n):
        avg = (p[i] - q[i])**2
        i += 1
        al += avg
    al = al**0.5 
    print(f'Euclidean distance between point P and point Q: {al:.2f}')
else :
    print("Error: Vectors must have the same size")