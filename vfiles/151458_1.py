v1 = input("Enter v1 (space-separated):")
v2 = input("Enter v2 (space-separated):")
hex_num = v1.split(" ")
hex_num = v2.split(" ")

v1[0] = int(v1[0])
v2[0] = int(v2[0])

print(hex_num)

print(v1[0] * v2[0])