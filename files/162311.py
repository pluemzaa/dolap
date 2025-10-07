from math import sqrt
x = input('Enter coordinates of point P (p1, p2,...,qn):')
y = input('Enter coordinates of point Q (q1, q2,..., qn):')
x = x.split(',')
y = y.split(',')
if len(x) == len(y):
    
    for i in range(len(x)):
        x[i] = int(x[i])
        y[i] = int(y[i])
    d = 0   
    for i in range(len(x)):
        d += (x[i] - y[i]) ** 2

    distance = sqrt(d)
    print(f'Euclidean distance between point P and point Q: {distance:.2f}')
   
else:
     print('Error: Vectors must have the same size')