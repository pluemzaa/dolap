A = input("Enter coordinates of point P (p1, p2,...,qn): ")
B = input("Enter coordinates of point Q (q1, q2,..., qn): ")
A = A.split(",")
B = B.split(",")
Zum = 0

if len(A) != len(B):
      print("Error: Vectors must have the same size")
else:
      for i in range(len(A)):
            A[i] = int(A[i])

      for i in range(len(B)):
            B[i] = int(B[i])

      for i in range(len(A)):
            C = ((A[i]-B[i])**2)
            Zum += C
      print(f"Euclidean distance between point P and point Q: {Zum**0.5:.2f}")