v1 = ("Enter v1 (space-separated):")
v1 = int(v1)
v1 = v1.split(' , ')
v2 = ("Enter v2 (space-separated):")
v2 = int(v2)
v2 = v2.split(' , ')

c1 = (v1[0]*v2[0])
c2 = (v1[1]*v2[1])
c3 = (v1[2]*v2[2])

all = (c1+c2+c3)
print(f"Dot Product:" {all})