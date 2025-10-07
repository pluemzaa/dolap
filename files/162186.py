a = input("Enter coordinates of point P (p1, p2,...,qn): ")
a = a.split(",")
b = input("Enter coordinates of point Q (q1, q2,..., qn): ")
b = b.split(",")

if len(a) != len(b):
    print("Error: Vectors must have the same size")
else:
    y = 0
    for i in range(len(a)):
        a[i] = int(a[i])
        b[i] = int(b[i])
        z = (b[i] - a[i])**2
        y += z
    print(f"Euclidean distance between point P and point Q: {y**0.5:.2f}")