v1_str = input("Enter v1 (space-separated):")
v1 = v1_str.split(' ')

v1[0] = int(v1[0])
v1[1] = int(v1[1])
v1[2] = int(v1[2])
print(v1)

v2 = [4,5,6]

r0 = v1[0] * v2[0]
r1 = v1[1] * v2[1]
r2 = v1[2] * v2[2]

r = [r0,r1,r2]
s = r0+r1+r2
print(r)
print(s)