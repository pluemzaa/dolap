#3
vector0 = input("Enter coordinates of point P (p1, p2,...,qn):").split(",")
vector1 = input("Enter coordinates of point Q (q1, q2,..., qn): ").split(",")
vector0 = [int(i) for i in vector0]
vector1 = [int(i) for i in vector1]
s = 0 
if len(vector0) == len(vector1) :
    for i in range(len(vector0)):
        s += (vector0[i] - vector1[i])**2
    s = s**0.5
    print (f"Euclidean distance between point P and point Q: {s:.2f}")
else :
    print ("Error: Vectors must have the same size")