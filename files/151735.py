v1 = input("Enter v1 (space-separated): ")
v2 = input("Enter v2 (space-separated): ")

v1 = v1.split(" ")
v1[0] = int (v1[0])
v1[1] = int (v1[1])
v1[2] = int (v1[2])

v2 = v2.split(" ")
v2[0] = int (v2[0])
v2[1] = int (v2[1])
v2[2] = int (v2[2])

dp1 = v1[0]*v2[0]
dp2 = v1[1]*v2[1]
dp3 = v1[2]*v2[2]
dp4 = dp1+dp2+dp3
print("Dot product:",dp4)