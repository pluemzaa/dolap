import math

try:
    i = input("Enter coordinates of point P (p1, p2,..., qn): ")
    u = input("Enter coordinates of point Q (q1, q2,..., qn): ")

    p = [float(c) for c in i.split(',')]
    q = [float(c) for c in u.split(',')]

    if len(p) != len(q):
        print("Error: Vectors must have the same size")
    else:
        s = 0
        for i in range(len(p)):
            s += (q[i] - p[i]) ** 2

        d = math.sqrt(s)
        print(f"Euclidean distance between point P and point Q: {d:.2f}")

except ValueError:
    print("Error: Invalid input. Please enter numbers separated by commas.")