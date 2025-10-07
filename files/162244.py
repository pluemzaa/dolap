p = input("Enter coordinates of point P (p1, p2,...,qn): ").strip().split(",")
q = input("Enter coordinates of point Q (q1, q2,..., qn): ").strip().split(",")
if len(p) != len(q):
    print("Error: Vectors must have the same size")
else:
    try:
        total = 0
        
        for i in range(len(p)):
            pi = float(p[i].strip())
            qi = float(q[i].strip())
            
            for diff in [(qi - pi)]:
                total += diff ** 2
        distance = total ** 0.5
        print("Euclidean distance between point P and point Q:", format(distance, ".2f"))
    except ValueError:
        print("Error: Please enter valid numbers only")