v1_str = input("Enter v1 (space-separated): ")
v1 = v1str.split(" ")
v1[0] = int(v1[0])
v2[1] = int(v1[1])
v3[2] = int(v1[2])

v2_str = input("Enter v2 (space-separated): ")
v2 = v2str.split(" ")
v2[0] = int(v2[0])
v2[1] = int(v2[1])
v2[2] = int(v2[2])
 dot_porduct = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]
print(f"Dot product: {dot_porduct }")-