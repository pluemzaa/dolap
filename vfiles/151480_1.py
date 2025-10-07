a = list(map(int, input("Enter v1 (space-separated): ").split()))
b = list(map(int, input("Enter v2 (space-separated): ").split()))

dot_product = sum(x * y for x, y in zip(a, b))
print("Dot product =", dot_product)