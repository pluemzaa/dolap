v1_str = input("Enter v1 (space-separated):")
v2_str = input("Enter v2 (space-separated):")
v1 = v1_str.split("")

r0 = v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]
print("Dot product:",r0)