p = input('Enter coordinates of point P (p1, p2,...,qn): ')
q = input('Enter coordinates of point Q (q1, q2,..., qn): ')

p = p.split(',')
q = q.split(',')

p2 = []
q2 = []

for i in p:
    i = i.strip()
    if i != '':
        p2.append(float(i))
for i in q:
    i = i.strip()
    if i != '':
        q2.append(float(i))

if len(p2) != len(q2):
    print("Error: Vectors must have the same size")
    exit()

sum = 0
for i in range(len(p2)):
    d = p2[i] - q2[i]
    sum = sum + d*d

ans = sum ** 0.5
print("Euclidean distance between point P and point Q: %.2f" % ans)