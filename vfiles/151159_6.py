v_1 = input("Enter v1 (space-separated):")
v1 = v_1.split("-")
v1[0] = int(v1[0])
v1[1] = int(v1[1])
v1[2] = int(v1[2])
print(v1)

v_2 = input("Enter v2 (space-separated):")
v2 = v_2.split("-")
v2[0] = int(v2[0])
v2[1] = int(v2[1])
v2[2] = int(v2[2])
print(v2)

d0 = v1[0]*v2[0]
d1 = v1[1]*v2[1]
d2 = v1[2]*v2[2]

d = [d0,d1,d2]
print(d)
dp = d0+d1+d2
print("Dot product:", dp)