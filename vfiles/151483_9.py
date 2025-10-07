v1_input = input("Enter v1 (space-separated): ")
v1_parts = v1_input.split()
v1_0 = int(v1_parts[0])
v1_1 = int(v1_parts[1])
v1_2 = int(v1_parts[2])


v2_input = input("Enter v2 (space-separated): ")
v2_parts = v2_input.split()
v2_0 = int(v2_parts[0])
v2_1 = int(v2_parts[1])
v2_2 = int(v2_parts[2])
dot_product = v1_0 * v2_0 + v1_1 * v2_1 + v1_2 * v2_2
print("Dot product:", dot_product)