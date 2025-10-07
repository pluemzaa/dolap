v1 = input("Enter v1 (space-separated): ")
v1 = v1.split(" ")
v1 = int(v1[0])
v1 = int(v1[1])
v1 = int(v1[2])

v2 = input("Enter v2 (space-separated): ")
v2 = v2.split(" ")
v2 = int(v2[0])
v2 = int(v2[1])
v2 = int(v2[2])

dp = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
print("Dot product: ", dp)