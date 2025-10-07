v1 = input("Enter v1 (space-separated): ")
v1_1 = v1.split()
v1_2 = [int(v1_1[0]), int(v1_1[1]), int(v1_1[2])]

v2 = input("Enter v2 (space-separated): ")
v2_1 = v2.split()
v2_2 = [int(v2_1[0]), int(v2_1[1]), int(v2_1[2])]

dot_product = v1_2[0]*v2_2[0]+v1_2[1]*v2_2[1]+v1_2[2]*v2_2[2]
print(f"Dot product: {dot_product:.2f}")