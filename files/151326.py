A = input("Enter v1 (space-separated): ")
B = input("Enter v2 (space-separated): ")
A1 = A.split(" ")
B1 = B.split(" ")

J = int(A1[0]) * int(B1[0]) + int(A1[1]) * int(B1[1]) + int(A1[2]) * int(B1[2])
print ("Dot product: ", J)