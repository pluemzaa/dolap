v1_str = input("Enter v1 (space-separated):")
v2_str = input("Enter v2 (space-separated):")
v1 = list(map(int, v1_str.split()))
v2 = list(map(int, v2_str.split()))


r0 = v1[0]*v2[0]
r1 = v1[1]*v2[1]
r2 = v1[2]*v2[2]

s = r0+r1+r2