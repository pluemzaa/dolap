v1_input = input("Enter v1 (space-separated): ")
v2_input = input("Enter v2 (space-separated): ")

v1_parts = v1_input.split()
v2_parts = v2_input.split()

v1 = [int(v1_parts[0]), int(v1_parts[1]), int(v1_parts[2])]
v2 = [int(v2_parts[0]), int(v2_parts[1]), int(v2_parts[2])]

dot_product = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

print("Dot product:", dot_product)