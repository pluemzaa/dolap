v1_str = input("Enter v1 (space-separated): ")
v2_str = input("Enter v2 (space-separated): ")

v1 = list(map(int, v1_str.split()))
v2 = list(map(int, v2_str.split()))

dot_product = sum(x*y for x, y in zip(v1, v2))

print("Dot product", dot_product)