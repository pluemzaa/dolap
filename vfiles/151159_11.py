a = input("Enter v1 (space-separated): ")
a = v1.split(" ")
a = int(v1[0])
a = int(v1[1])
a = int(v1[2])

b = input("Enter v2 (space-separated): ")
b = v2.split(" ")
b = int(v2[0])
b = int(v2[1])
b = int(v2[2])

dp = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
print("Dot product: ", dp)