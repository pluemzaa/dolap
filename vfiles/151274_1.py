v1_in = input("Enter v1:")
v1 = v1_in.split(' ')
v1[0] = int(v1[0])
v1[1] = int(v1[1])
v1[2] = int(v1[2])
v2_in = input("Enter v2:")
v2 = v2_in.split(' ')
v2[0] = int(v2[0])
v2[1] = int(v2[1])
v2[2] = int(v2[2])
r0 = v1[0]*v2[0]
r1 = v1[1]*v2[1]
r2 = v1[2]*v2[2]
s = r0+r1+r2
print ("Dot product:",s)