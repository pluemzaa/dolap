v1 = input("Enter v1 (space-separated): ")
v2 = input("Enter v2 (space-separated): ")
v1_sp = v1.split(' ')
v1_sp[0] = int(v1_sp[0])
v1_sp[1] = int(v1_sp[1])
v1_sp[2] = int(v1_sp[2])
v2_sp = v2.split(' ')
v2_sp[0] = int(v2_sp[0])
v2_sp[1] = int(v2_sp[1])
v2_sp[2] = int(v2_sp[2])
k1 = v1_sp[0]*v2_sp[0]
k2 = v1_sp[1]*v2_sp[1]
k3 = v1_sp[2]*v2_sp[2]
total = k1+k2+k3
print(f"Dot product: {total}")