v1_str = input("Enter v1 (space-separated): ")
v1 = v1_str.split()
v1_0 = int(v1[0])
v1_1 = int(v1[1])
v1_2 = int(v1[2])


v2_str = input("Enter v2 (space-separated): ")
v2 = v2_str.split()
v2_0 = int(v2[0])
v2_1 = int(v2[1])
v2_2 = int(v2[2])
dot_product = v1_0 * v2_0 + v1_1 * v2_1 + v1_2 * v2_2
print("Dot product:", dot_product)