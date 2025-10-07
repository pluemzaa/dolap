v1 = input("Enter v1 (space-separated): ")
v2 = input("Enter v2 (space-separated): ")
v1_split = v1.split()
v2_split = v2.split()

a1 = int(v1_split[0])
a2 = int(v1_split[1])
a3 = int(v1_split[2])

b1 = int(v2_split[0])
b2 = int(v2_split[1])
b3 = int(v2_split[2])

result = a1  b1 + a2  b2 + a3 * b3
print("Dot product:", result)