v1 = int(input("Enter v1 (space-separated): "))
v2 = int(input("Enter v2 (space-separated): "))
v1_sp = v1.split(' ')
v2_sp = v2.split(' ')
k1 = v1[0]*v2[0]
k2 = v1[1]*v2[1]
k3 = v1[2]*v2[2]
total = k1+k2+k3
print(f"Dot product: {total}")