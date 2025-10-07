v1 = input("Enter v1 (space-separated):")
v1 = v1.split(' , ')
v1 = int(v1)

s = (v1[0],v1[1],v1[2])
print(s)

v2 = input("Enter v2 (space-separated):")
v2 = v2.split('  ')
v2 = int(v2)

w = (v2[0],v2[1],v3[2])
print(w)

a = (v1[0] * v2[0])
b = (v1[1] * v2[1])
c = (v1[2] * v2[2])

all = (a+b+c)
print(f"Dot Product:", {all})