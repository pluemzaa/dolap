import math
w1 = input("Enter coordinates of point P (p1, p2,...,qn): ")
w2 = input("Enter coordinates of point Q (q1, q2,..., qn): ")
midtotal = 0
w1 = w1.split(',')
w2 = w2.split(',')
w1 = [int(x) for x in w1]
w2 = [int(x) for x in w2]
if len(w1) == len(w2):
    for i in range (len(w1)):
        total = (w1[i] - w2[i])**2
        midtotal += total
    alltotal = math.sqrt(midtotal)
    print(f"Euclidean distance between point P and point Q: {alltotal:.2f}")
else:
    print("Error: Vectors must have the same size")