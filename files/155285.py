v1_str = input('Enter v1 (space-separated): ')
v = v1_str.split(" ")
v1 = int(v[0])
v2 = int(v[1])
v3 = int(v[2])

v2_str = input('Enter v1 (space-separated): ')
v4 = v2_str.split(" ")
v5 = int(v4[0])
v6 = int(v4[1])
v7 = int(v4[2])

r0 = v1[0]*v2[0]
r1 = v1[1]*v2[1]
r2 = v1[2]*v2[2]

s = r0+r1+r2

print("Dot product: ",s)