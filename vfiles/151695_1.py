v1_str = input("Enter v1 (space-separated):")
v2_str = input("Enter v2 (space-separated):")


v1 = [int(x) for x in v1_str.split()]
v2 = [int(x) for x in v2_str.split()]


dot_product = sum(x * y for x, y in zip(v1, v2))

print(f"Dot product:{dot_product}.")