fises = input("Enter v1 (space-separated): ")
twos = input("Enter v2 (space-separated): ")
fist = fises.split(" ")
two = twos.split(" ")
fist[0] = int(fist[0])
fist[1] = int(fist[1])
fist[2] = int(fist[2])
two[0] = int(two[0])
two[1] = int(two[1])
two[2] = int(two[2])
r0 = fist[0]*two[0]
m0 =  fist[1]* two[1]
c0 = fist[2] * two[2]
p0 = r0 + m0
p1 = p0 + c0
print(f"Dot product: {p1}")