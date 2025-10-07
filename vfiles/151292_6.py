v1_str = int(input("Enter v1 (space-separated):")
v2_str = int(input("Enter v2 (space-separated):")
v1 = v1_str.split(" ")
v2 = v2_str.split(" ")


r0 = v1[0]* v2[0]
r1 = v1[1]* v2[1]
r2 = v1[2]* v2[2]

r = [r0,r1,r2]
s = r0+r1+r2
print("Dot product:",s,end=" " )