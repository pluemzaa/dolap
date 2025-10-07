fises = input("Enter v1 (space-separated): ")
twos = input("Enter v2 (space-separated): ")

fist = fises.split(" ")
two = twos.split(" ")

fist[0] = int(fist[0])
fist[1] = int(fist[1])
fist[2] = int(fist[2])
# print(fist)

two[0] = int(two[0])
two[1] = int(two[1])
two[2] = int(two[2])
# print(two)

r0 = fist[0]*two[0]#1*4
# r1 = fist[1]*two[1]
# r2 = fist[2]*two[2]

# k0 = r0 + two[0]
# print(k0)
# k1 = k0 + two[2]
# k2 = r2 + two[2]
m0 =  fist[1]* two[1]#2*5

c0 = fist[2] * two[2]#3*6

p0 = r0 + m0
p1 = p0 + c0
# print(p0)
print(f"Dot product: {p1}")
# print(r0)
# print(l0)
# print(m0)
# print(c0)
# print(r2)