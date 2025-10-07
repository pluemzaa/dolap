print('Hello Python!')
v1_str = input("Enter v1 (space-separated): ")
v1 = [int(x) for x in v1_str.split()]
v2_str = input("Enter v2 (space-separated): ")
v2 = [int(x) for x in v2_str.split()]

dot_product_result = (v1[0] * v2[0]) + \
                     (v1[1] * v2[1]) + \
                     (v1[2] * v2[2])
print(f"Dot product: {dot_product_result}")