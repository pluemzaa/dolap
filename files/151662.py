v1 = list(map(int, input("Enter v1 (space-separated): ").split()))
v2 = list(map(int, input("Enter v2 (space-separated): ").split()))

if len(v1) != 3 or len(v2) != 3:
    print("Error: Both vectors must have exactly 3 elements.")
else:
    dot_product = sum(x * y for x, y in zip(v1, v2))
    print("Dot product:", dot_product)