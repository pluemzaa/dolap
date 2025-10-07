v1 = input("Enter v1 (space-separated): ").split()
v2 = input("Enter v2 (space-separated): ").split()
v1 = [int(x) for x in v1]
v2 = [int(x) for x in v2]
dot_product = sum(v1[i] * v2[i] for i in range(3))
print("Dot product:", dot_product)