x = input("Enter v1 (space-separated):")
v1 = x.split(" ")
v1[0] = int(v1[0])
v1[1] = int(v1[1])
v1[2] = int(v1[2])

a = input("Enter v2 (space-separated):")
v2 = a.split(" ")
v2[0] = int(v2[0])
v2[1] = int(v2[1])
v2[2] = int(v2[2])

r = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2] 
print(f"Dot product:{r}")