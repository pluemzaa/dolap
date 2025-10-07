a = input("Enter coordinates of point P (p1, p2,...,qn):")
a = a.split(",")
a = [int(x) for x in a]

b = input("Enter coordinates of point Q (q1, q2,..., qn):")
b = b.split(",")
b = [int(x) for x in b]

c = 0
if len(a) == len(b):
    for i in range(len(a)):
        c = c + (a[i]-b[i])**2
    c = c**0.5
    print(f"Euclidean distance between point P and point Q: {c:.2f}")
else:
    print("Error: Vectors must have the same size")